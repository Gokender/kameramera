import os
from difflib import get_close_matches

from .utils import load_conf

class Index:

    def __init__ (self, index_filepath=None):

        self.cameras = []
        
        if index_filepath is None:
            index_filepath = os.path.join('kameramera', 'data', 'index.yml')
        
        self._data = load_conf(index_filepath)

        for camera in self._data['cameras']:
            self.cameras.append(self.Camera(camera))

    class Camera:
        def __init__(self, dict_data):
            self._data = dict_data
            self.id = self._data['id']
            self.name = self._data['name']
            self.manufacturer = self._data['manufacturer']
            self.path = self._data['path']

        def __repr__(self) -> str:
            return str(self._data)

    def get_by_id(self, id) -> Camera:
        for camera in self.cameras:
            if camera.id.lower() == id.lower():
                return camera
        #print('Error no cameras found with {}'.format(id))
        return None

    def get_by_name(self, name) -> Camera:
        for camera in self.cameras:
            if camera.name.lower() == name.lower():
                return camera
        #print('Error no cameras found with {}'.format(name))
        return None

    def get_by_manufacturer(self, manufacturer) -> Camera:
        for camera in self.cameras:
            if camera.manufacturer == manufacturer:
                return camera
        #print('Error no cameras found with {}'.format(manufacturer))
        return None
    
    def get_closest_camera(self, name) -> list:

        print([camera.name.lower() for camera in self.cameras])
        closest = get_close_matches(name, 
                                    [camera.name for camera in self.cameras],
                                    cutoff=0.4)

        if closest:
            return [self.get_by_name(name) for name in closest]
        return []