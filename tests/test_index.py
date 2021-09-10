import unittest

from kameramera import index

class Index(unittest.TestCase):
    
    def setUp(self):
        self.index = index.Index()

    def test_get_by_id(self):
        self.assertEqual(self.index.get_by_id('canon_ae1').id, 'canon_ae1')
    
    def test_get_by_name(self):
        self.assertEqual(self.index.get_by_name('Canon AE-1').id, 'canon_ae1')

    def test_get_by_manufacturer(self):
        self.assertEqual(self.index.get_by_manufacturer('Canon')[0].id, 
                         'canon_ae1')
    
    def test_get_closest_camera(self):
        self.assertEqual(self.index.get_closest_camera('ae-1')[0].id, 'canon_ae1')