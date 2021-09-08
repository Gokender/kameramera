# kameramera

Library of useful tools for analog cameras (but also for more recent ones).

The goal of this project is to gather all useful information that can be found to help the photographer when using his camera.

The library is divided in several parts to manage different components.

## Cameras
### Body
TODO

### Lenses

## Films

TODO

## Tools
### Lightmeter

This tool is used to simulate a lightmeter. It is based on 4 variables : 
- the shutter speed
- the aperture
- film speed
- illuminance

It allows you to choose one of the optimal parameters according to the 3 others.

By default the program use a configuration file *'camera.yaml'* with simples values. You can choose your own config file.
```python
from kameramera import tools

posometre = tools.Lightmeter()
#posometre = tools.Lightmeter(conf_file='my_conf.yaml')

print(posometre.shutter_speed, posometre.shutter_speed_norm)
```
```shell
> 0.001 1/1000
```

```python
posometre.shutter_speed = 0.5
print(posometre.shutter_speed, posometre.shutter_speed_norm)
```
```shell
> 0.5 1/2
```

To find the best value for any of these variables (shutter speed, film speed, aperture and illuminance) :

```python
from kameramera import tools

posometre = tools.Lightmeter()
posometre.get_shutter_speed()
print(posometre.shutter_speed, posometre.shutter_speed_norm)
```
```shell
> 0.06125 1/16
```

You can also override any of the 4 attributes and have dict of all attributes:
```python
from kameramera import tools

posometre = tools.Lightmeter(shutter_speed='1/250', film_speed=400)
print(posometre.get_variables())
```
```shell
> {'shutter_speed': 0.004, 'shutter_speed_norm': '1/250', 'film_speed': 400, 'aperture': 3.5, 'illuminance': 500}
```