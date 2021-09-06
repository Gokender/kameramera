from fractions import Fraction

class Lightmeter:

    def __init__(self, film_speed=None, shutter_speed=None, aperture=None, illuminance=None):

        self.shutter_speed = float(Fraction(shutter_speed))
        self.shutter_speed_norm = self._shutter_speed

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


    def get_shutter_speed(self):
        self.shutter_speed = (pow(self.aperture, 2) * self.incident_light_constant)/(self.illuminance * self.film_speed)