from pymodbus.client.sync import ModbusTcpClient


class PowerHomePlus:
    def __init__(
            self,
            ip
    ):
        self.last_values = {}
        self.client = ModbusTcpClient(
            ip,
            port=502,
            timeout=10,
        )

    @staticmethod
    def decode_power(register):
        """decode power values"""
        offset = 16384
        return register - offset

    @staticmethod
    def decode_uint16(register):
        """decode uint16 values"""
        return register

    def get_values(self):
        """
        46: battery charge level
        47: battery power
        48: battery grid power
        """
        addresses = [46, 47, 48]

        decode_funktion = [
            self.decode_uint16,
            self.decode_power,
            self.decode_power
        ]

        results = []

        for i in range(len(addresses)):
            value = self.client.read_holding_registers(
                address=addresses[i],
                count=1,
                unit=64
            )
            if not value.isError():
                decoded_value = decode_funktion[i](
                    value.registers[0]
                )
                results.append(decoded_value)
            else:
                print(f"Error reading register {addresses[i]} from Sax Power Home Plus Battery")
                results.append(None)

        return results

    def close(self):
        self.client.close()