import os

from .utils import load_conf

class General:
    def __init__(self, dict_data):
        self._data = dict_data
        self.manufacturer = self._data['manufacturer']
        self.name = self._data['name']
        self.type = self._data['type']
        self.format = self._data['format']
        self.made_in = self._data['made_in']
        self.date = self._data['date']
        self.body_construction = self._data['body_construction']
        self.mount_threads = self._data['mount_threads']
        self.dimension = self._data['dimension']
        self.weight = self._data['weight']

    def __repr__(self):
        return str(self._data)


class Optics:
    def __init__(self, dict_data):
        self._data = dict_data
        self.lenses = self._data['lenses']
        self.lenses_mount = self._data['lenses_mount']

    def __repr__(self):
        return str(self._data)


class Sighting:
    def __init__(self, dict_data):
        self._data = dict_data
        self.type = self._data['type']
        self.display = self._data['display']
        self.viewfinder = self.Viewfinder(self._data['viewfinder'])
    
    def __repr__(self):
        return str(self._data)

    class Viewfinder:
        def __init__(self, dict_data):
            self._data = dict_data
            self.rangefinder = self._data['rangefinder']
            self.aperture = self._data['aperture']
            self.exposure_indicator = self._data['exposure_indicator']
            self.flash_indicator = self._data['flash_indicator']
        
        def __repr__(self):
            return str(self._data)



class Focus:
    def __init__(self, dict_data):
        self._data = dict_data
        self.manual = self._data['manual']
        self.autofocus = self._data['autofocus']
        self.stabilization = self._data['stabilization']
        self.depth_of_field = self._data['depth_of_field']
    
    def __repr__(self):
        return str(self._data)

class Shutter:
    def __init__(self, dict_data):
        self._data = dict_data
        self.type = self._data['type']
        self.shutter_speeds = self._data['shutter_speeds']
        self.pose = self._data['pose']
        self.self_timer = self._data['self_timer']
    
    def __repr__(self):
        return str(self._data)

class Exposure: 
    def __init__(self, dict_data):
        self._data = dict_data  
        self.mode = self._data['mode']
        self.correction = self._data['correction']
        self.measure = self.Measure(self._data['measure'])
    
    def __repr__(self):
        return str(self._data)

    class Measure:
        def __init__(self, dict_data):
            self._data = dict_data  
            self.type = self._data['type']
            self.light_sensor = self._data['light_sensor']
            self.metering_mode = self._data['metering_mode']
            self.memory = self._data['memory']
        
        def __repr__(self):
            return str(self._data)
  
class Film:
    def __init__(self, dict_data):
        self._data = dict_data
        self.format = self._data['format']
        self.advance = self._data['advance']
        self.frame_counter = self._data['frame_counter']
        self.film_speed = self._data['film_speed']

    def __repr__(self):
        return str(self._data)

class Flash:
    def __init__(self, dict_data):
        self._data = dict_data
        self.built_in = self._data['built_in']
        self.hot_shoe = self._data['hot_shoe']
        self.synchronization = self._data['synchronization']
    
    def __repr__(self):
        return str(self._data)

class Power:
    def __init__(self, dict_data):
        self._data = dict_data
        self.source = []
        self.required = self._data['required']

        for source in self._data['source']:
            #print(source)
            self.source.append(self.Source(source))
        
    def __repr__(self):
        return str(self._data)

    class Source:
        def __init__(self, dict_data):
            self._data = dict_data
            self.number = self._data['number']
            self.voltage = self._data['voltage']
            self.type = self._data['type']
        
        def __repr__(self):
            return str(self._data)
        

class Camera:

    def __init__(self, camera_id=None, search=None):
        
        if camera_id is None and search is None:
            #raise ERROR
            print('Error no values')
            return
 
        if camera_id is not None:
            camera_file = '{}.yml'.format(camera_id)
            self._data = load_conf(os.path.join('kameramera',
                                                'data',
                                                'camera',
                                                camera_file))

        self.general = General(self._data['general'])
        self.optics = Optics(self._data['optics'])
        self.sighting = Sighting(self._data['sighting'])
        self.focus = Focus(self._data['focus'])
        self.shutter = Shutter(self._data['shutter'])
        self.exposure = Exposure(self._data['exposure'])
        self.film = Film(self._data['film'])
        self.flash = Flash(self._data['flash'])
        self.power = Power(self._data['power'])