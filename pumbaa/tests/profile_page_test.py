import unittest

from pyramid import testing
import configparser

class ProfileViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        
        cfg = configparser.ConfigParser()
        cfg.read('../../test.ini')
        settings = dict(cfg.items('app:main'))

        from pumbaa import models
        models.initial(settings)

    def tearDown(self):
        testing.tearDown()

    def test_index_get_recent_topics(self):
        from pumbaa.views.profile import index
        request = testing.DummyRequest()
        result = index(request)
        
        self.assertIn('profile_name', result, 'profile name disappear in result')
        

class ProfileViewFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pumbaa import main
        
        cfg = configparser.ConfigParser()
        cfg.read('../../test.ini')
        
        settings = dict(cfg.items('app:main'))

        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        testing.tearDown()
        
    def test_get_welcome_msg(self):
        response = self.testapp.get('/profile/zero', status=200)

        self.assertTrue('Profile Name' in response.text)