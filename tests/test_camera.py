import unittest

from kameramera import camera

class Camera(unittest.TestCase):

    def setUp(self):
        self.camera = camera.Camera(camera_id='canon_ae1')

    def test_general_manufacturer(self):
        self.assertEqual(self.camera.general.manufacturer, 'Canon')
    
    def test_general_name(self):
        self.assertEqual(self.camera.general.name, 'Canon AE-1')

    def test_general_type(self):
        self.assertEqual(self.camera.general.type, 'SLR')

    def test_general_format(self):
        self.assertEqual(self.camera.general.format, '24x35')
    
    def test_general_made_in(self):
        self.assertEqual(self.camera.general.made_in, 'Japan')
    
    def test_general_date(self):
        self.assertEqual(self.camera.general.date, '1976-1984')
    
    def test_general_body_construction(self):
        self.assertEqual(self.camera.general.body_construction, 'metal')

    def test_general_mount_threads(self):
        self.assertEqual(self.camera.general.mount_threads, '1/4"')

    def test_general_dimension(self):
        self.assertEqual(self.camera.general.dimension, '141x87x47.5 mm')

    def test_general_weight(self):
        self.assertEqual(self.camera.general.weight, '620g')

    def test_optics_lenses(self):
        self.assertEqual(self.camera.optics.lenses, 'interchangeable') 
    
    def test_optics_lenses_mount(self):
        self.assertEqual(self.camera.optics.lenses_mount, 'Canon FD')

    def test_sighting_type(self):
        self.assertEqual(self.camera.sighting.type, 'fixed eye-level pentaprism')
    
    def test_sighting_display(self):
        self.assertEqual(self.camera.sighting.display, False)

    def test_sighting_viewfinder_rangefinder(self):
        self.assertEqual(self.camera.sighting.viewfinder.rangefinder, 
                         ['split_image', 'microprism'])

    def test_sighting_viewfinder_aperture(self):
        self.assertEqual(self.camera.sighting.viewfinder.aperture, True)

    def test_sighting_viewfinder_exposure_indicator(self):
        self.assertEqual(self.camera.sighting.viewfinder.exposure_indicator, True)

    def test_sighting_viewfinder_flash_indicator(self):
        self.assertEqual(self.camera.sighting.viewfinder.flash_indicator, True)

    def test_focus_manual(self):
        self.assertEqual(self.camera.focus.manual, True)
    
    def test_focus_autofocus(self):
        self.assertEqual(self.camera.focus.autofocus, False)
    
    def test_focus_stabilization(self):
        self.assertEqual(self.camera.focus.stabilization, False)
    
    def test_focus_depth_of_field(self):
        self.assertEqual(self.camera.focus.depth_of_field, True)
    
    def test_shutter_type(self):
        self.assertEqual(self.camera.shutter.type, None)
    
    def test_shutter_shutter_speeds(self):
        self.assertEqual(self.camera.shutter.shutter_speeds, [
            '2',
            '1',
            '1/2',
            '1/4',
            '1/8',
            '1/15',
            '1/30',
            '1/60',
            '1/125',
            '1/250',
            '1/500',
            '1/1000'
        ])
    
    def test_shutter_pose(self):
        self.assertEqual(self.camera.shutter.pose, 'B')
    
    def test_shutter_self_timer(self):
        self.assertEqual(self.camera.shutter.self_timer, 10)

    def test_exposure_mode(self):
        self.assertEqual(self.camera.exposure.mode, ['M','S'])
    
    def test_exposure_correction(self):
        self.assertEqual(self.camera.exposure.correction, 1.5)
    
    def test_exposure_measure_type(self):
        self.assertEqual(self.camera.exposure.measure.type, 'TTL')
    
    def test_exposure_measure_light_sensor(self):
        self.assertEqual(self.camera.exposure.measure.light_sensor, 
                         'silicon photon cell')
    
    def test_exposure_measure_metering_mode(self):
        self.assertEqual(self.camera.exposure.measure.metering_mode, 
                         'center-weighted average metering')
    
    def test_exposure_measure_memory(self):
        self.assertEqual(self.camera.exposure.measure.memory, True)
    
    def test_film_format(self):
        self.assertEqual(self.camera.film.format, 135)
    
    def test_film_advance(self):
        self.assertEqual(self.camera.film.advance, 'manual')
    
    def test_film_frame_counter(self):
        self.assertEqual(self.camera.film.frame_counter, True)
    
    def test_film_film_speed(self):
        self.assertEqual(self.camera.film.film_speed, [
            25,
            32,
            40,
            50,
            64,
            80,
            100,
            125,
            160,
            200,
            250,
            320,
            400,
            500,
            640,
            800,
            1000,
            1250,
            1600,
            2000,
            2500,
            3200
        ])
    
    def test_flash_built_in(self):
        self.assertEqual(self.camera.flash.built_in, False)
    
    def test_flash_hot_shoe(self):
        self.assertEqual(self.camera.flash.hot_shoe, True)
    
    def test_flash_synchronization(self):
        self.assertEqual(self.camera.flash.synchronization, '1/60')

    def test_power_required(self):
        self.assertEqual(self.camera.power.required, True)

    def test_power_source_number(self):
        self.assertEqual(self.camera.power.source[0].number, 1) 
    
    def test_power_source_voltage(self):
        self.assertEqual(self.camera.power.source[0].voltage, 6) 
    
    def test_power_source_type(self):
        self.assertEqual(self.camera.power.source[0].type, [
            'alkaline-manganese',
            'silver oxyde',
            'lithium'
        ]) 