from fractions import Fraction
from decimal import Decimal, ROUND_UP

import os

from . import utils
from .constants import FILM_SPEED

class Lightmeter:

    def __init__(self, conf_file=os.path.join('kameramera', 'camera.yaml'), **kwargs):
        """A lightmeter object

        Allows to manage a lightmeter object and to calculate for the 4 variables 
        the best value for a correct exposure. You can override any of these variables 
        present in the configuration file: shutter_speed, aperture, film_speed, 
        illuminance

        Args:
            conf_file (str): The filepath of the conf YAML file. 
                Defaults to 'kameramera/camera.yaml'

            **kwargs: Arbitrary keyword arguments.

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.

        """
        conf_data = utils.load_conf(conf_file)

        if 'shutter_speed' in kwargs:
            shutter_speed = kwargs['shutter_speed']
        else:
            shutter_speed = conf_data['camera']['shutter_speed']

        self.shutter_speed = float(Fraction(shutter_speed))
        self.shutter_speed_norm = self._shutter_speed

        if 'film_speed' in kwargs:
            film_speed = kwargs['film_speed']
        else:
            film_speed = conf_data['camera']['film_speed']

        self.film_speed = film_speed

        if 'aperture' in kwargs:
            aperture = kwargs['aperture']
        else:
            aperture = conf_data['camera']['aperture']

        self.aperture = aperture

        if 'illuminance' in kwargs:
            illuminance = kwargs['illuminance']
        else:
            illuminance = conf_data['scene']['illuminance']

        self.illuminance = illuminance

        self.incident_light_constant = conf_data['constant']['incident_light_constant']

    @property
    def shutter_speed_norm(self):
        return self._shutter_speed_norm

    @shutter_speed_norm.setter
    def shutter_speed_norm(self, value):
        if value > 1:
            self._shutter_speed_norm = str(round(value))
        else:
            self._shutter_speed_norm = '1/{}'.format(round(1/value))

    @property
    def shutter_speed(self):
        return self._shutter_speed

    @shutter_speed.setter
    def shutter_speed(self, shutter_speed):
        self._shutter_speed = float(Fraction(shutter_speed))
        self.shutter_speed_norm = self._shutter_speed

    @property
    def film_speed(self):
        return self._film_speed

    @film_speed.setter
    def film_speed(self, film_speed):
        self._film_speed = int(film_speed)
    
    @property
    def aperture(self):
        return self._aperture

    @aperture.setter
    def aperture(self, aperture):
        self._aperture = float(aperture)

    @property
    def illuminance(self):
        return self._illuminance

    @illuminance.setter
    def illuminance(self, illuminance):
        self._illuminance = int(illuminance)

    def get_shutter_speed(self):
        """Update the shutter speed from other variables
        """
        self.shutter_speed = (pow(self.aperture, 2) * self.incident_light_constant)/(self.illuminance * self.film_speed)
    
    def get_aperture(self):
        """Update the aperture from other variables
        """
        aperture_float = Decimal((self.illuminance * self.film_speed * self.shutter_speed)/(self.incident_light_constant)).sqrt()
        self.aperture = aperture_float.quantize(Decimal('0.1'), rounding=ROUND_UP)

    def get_film_speed(self):
        """Update the film speed from other variables
        """
        film_speed = (pow(self.aperture, 2) * self.incident_light_constant)/(self.shutter_speed * self.illuminance)
        self.film_speed = utils.get_closest_value(FILM_SPEED, film_speed)

    def get_illuminance(self):
        """Update the illuminance from other variables
        """
        self.illuminance = (pow(self.aperture, 2) * self.incident_light_constant)/(self.shutter_speed * self.film_speed)