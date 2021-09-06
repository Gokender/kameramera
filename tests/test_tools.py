import unittest

from kameramera import tools

class Lightmeter(unittest.TestCase):
    
    def setUp(self):
        self.posometre = tools.Lightmeter(100, '1/1000', 3.5, 500)
    
    def tearDown(self):
        pass

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