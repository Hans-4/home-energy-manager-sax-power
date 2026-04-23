# Energy Manager SAX

**Python package for reading from SAX devices**

## Supported devices

| Device                 | Verification             | Script             | Url                                                        |
|------------------------|--------------------------|--------------------|------------------------------------------------------------|
| Power Home Plus 7,7kWh | self tested              | power_home_plus.py | https://sax-power.net/produkte/sax-power-home-plus-7-7kwh/ |
| Power Home Plus 5,8kWh | should work / not tested | power_home_plus.py | https://sax-power.net/produkte/sax-power-home-5-8kwh/      |

## Installation

```bash
pip install home-energy-manager-sax_power
```

## Usage

```python
from sax_power.power_home_plus import PowerHomePlus

device = PowerHomePlus(ip="192.168.178.60")

level, power, grid_power = device.get_values()

print(level, power, grid_power)
```
