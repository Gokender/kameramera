import unittest

from kameramera import tools

class Lightmeter(unittest.TestCase):
    
    def setUp(self):
        self.posometre = tools.Lightmeter()
    
    def test_shutter_speed_float(self):
        self.posometre.shutter_speed = 0.5
        self.assertEqual(self.posometre.shutter_speed, 0.5)

    def test_shutter_speed_ratio(self):
        self.posometre.shutter_speed = '1/2'
        self.assertEqual(self.posometre.shutter_speed, 0.5)

    def test_shutter_speed_norm_float(self):
        self.posometre.shutter_speed = 0.5
        self.assertEqual(self.posometre.shutter_speed_norm, '1/2')
    
    def test_shutter_speed_norm_int(self):
        self.posometre.shutter_speed = 2
        self.assertEqual(self.posometre.shutter_speed_norm, '2')

    def test_film_speed(self):
        self.posometre.film_speed = 400
        self.assertEqual(self.posometre.film_speed, 400)

    def test_aperture(self):
        self.posometre.aperture = 5.6
        self.assertEqual(self.posometre.aperture, 5.6) 
    
    def test_illuminance(self):
        self.posometre.illuminance = 10000
        self.assertEqual(self.posometre.illuminance, 10000)

    def test_get_shutter_speed(self):
        self.posometre.get_shutter_speed()
        self.assertEqual(self.posometre.shutter_speed, 0.06125)

    def test_get_aperture(self):
        self.posometre.get_aperture()
        self.assertEqual(self.posometre.aperture, 0.5)

    def test_get_film_speed(self):
        self.posometre.get_film_speed()
        self.assertEqual(self.posometre.film_speed, 6400)

    def test_get_illuminance(self):
        self.posometre.get_illuminance()
        self.assertEqual(self.posometre.illuminance, 30625)

    def test_get_variables(self):
        variables = {'shutter_speed': 0.001, 'shutter_speed_norm': '1/1000', 'film_speed': 100, 'aperture': 3.5, 'illuminance': 500}
        self.assertEqual(self.posometre.get_variables(), variables)