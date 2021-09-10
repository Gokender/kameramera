# kameramera

Library of useful informations for cameras, lenses and film.

![canon_ae1](https://upload.wikimedia.org/wikipedia/commons/b/b9/Wikicommons_canon_ae-1_program_canon_rrt877.jpg)
*Canon Ae-1 Program analog camera with 50mm Canon f/1.8 Lens. (CC-Zero)*

The goal of this project is to gather all useful information that can be found to help the photographer when using his camera.

The library is divided in several parts to manage different components.

## Index

Kameramera uses YAML files to manage the data of different cameras. The purpose of the index is to be able to search for a reference among all the data.

To use it :

```python
from kameramera import index

index = index.Index()

print(index.get_by_name('Canon AE-1'))
```
```shell
> {'id': 'canon_ae1', 'manufacturer': 'Canon', 'name': 'Canon AE-1', 'path': 'kameramera\\data\\camera\\canon_ae1.yml'}
```

You can access as an object : 

```python
print(index.get_by_name('Canon AE-1').id)
```
```shell
> canon_ae1
```

You can also search by manufacturer or id : 

```python
index.get_by_id('canon_ae1')
index.get_by_manufacturer('Canon') #return a list of Camera
```

If you don't have the exact name of the camera, you can get a list of camera by closest name :

```python
print(index.get_closest_camera('AE-1'))
```
```shell
> [{'id': 'canon_ae1', 'manufacturer': 'Canon', 'name': 'Canon AE-1', 'path': 'kameramera\\data\\camera\\canon_ae1.yml'}]
```

## Cameras

Cameras informations are divided in two parts : body and lenses. Each part corresponds to a different data file, located in the respective directories "kameramera/camera" and "kameramera/lenses

### Body

Camera body informations are split in 9 parts : general, optics, sighting, focus, shutter, exposure, film, flash, power.

#### General

Here, you'll find general informations about the camera such as : name, manufacturer, date, type of camera

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.general.manufacturer 
>> 'Canon'

camera.general.name
>> 'Canon AE-1'

camera.general.type
>> 'SLR'

camera.general.format
>> '24x35'
    
camera.general.made_in
>> 'Japan'
    
camera.general.date
>> '1976-1984'
    
camera.general.body_construction
>> metal

camera.general.mount_threads
>> '1/4"'

camera.general.dimension
>> '141x87x47.5 mm'

camera.general.weight
>> '620g'
```

#### Optics

Basics informations about lenses (if builtin for examples)

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.optics.lenses 
>> 'interchangeable'
    
camera.optics.lenses_mount
>> 'Canon FD'
```

#### Sighting

Everything related to viewfinder and display :

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.sighting.type
>> 'fixed eye-level pentapris'

camera.sighting.display
>> False

camera.sighting.viewfinder.rangefinder
>> True

camera.sighting.viewfinder.exposure_indicator
>> True

camera.sighting.viewfinder.test_sighting_viewfinder_flash_indicator
>> True
```

#### Focus

How the focus works on the camera :

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.focus.manual
>> True

camera.focus.autofocus
>> False

camera.focus.stabilization
>> False

camera.focus.depth_of_field
>> True
```

#### Shutter

Informations about the shutter.

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.shutter.type
>> None

camera.shutter.shutter_speeds
>> ['2', '1', '1/2', '1/4', '1/8', '1/15', '1/30', '1/60', '1/125', '1/250', '1/500', '1/1000']

camera.shutter.pose
>> 'B'

camera.shutter.self_timer
>> 10
```

#### Exposure

In this part you can access to differents exposure informations.

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.exposure.mode
>> ['M','S']

camera.exposure.correction
>> 1.5

camera.exposure.measure.type
>> 'TTL'

camera.exposure.measure.light_sensor
>> 'silicon photon cell'

camera.exposure.measure.metering_mode
>> 'center-weighted average metering'

camera.exposure.measure.memory
>> True
```

#### Film

If it's an analog camera you can access some informations about film

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.film.format
>> 135

camera.film.advance
>> 'manual'

camera.film.frame_counter
>> True

camera.film.film_speed
>> [25, 32, 40, 50, 64, 80, 100, 125, 160, 200, 250, 320, 400, 500, 640, 800, 1000, 1250, 1600, 2000, 2500, 3200]
```

#### Flash

Basics informations about flash

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.flash.built_in
>> False

camera.flash.hot_shoe
>> True

camera.flash.synchronization
>> '1/60'
```

#### Power

And lastly informations about power supply

```python
from kameramera import camera

camera = camera.Camera(camera_id='canon_ae1')

camera.power.required
>> True

camera.power.source[0].number
>> 1

camera.power.source[0].voltage
>> '1/60'

camera.power.source[0].type
>> ['alkaline-manganese', 'silver oxyde', 'lithium']
```

### Lenses

TODO

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