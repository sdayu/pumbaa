import unittest

from pyramid import testing
import configparser

class WelcomeViewTests(unittest.TestCase):
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
        from pumbaa.views.welcome import index
        import mongoengine as me
        request = testing.DummyRequest()
        result = index(request)
        
        self.assertIn('recent_topics', result, 'topics disappear in result')
        self.assertIsInstance(result['recent_topics'], me.queryset.queryset.QuerySet)
        self.assertGreaterEqual(len(result['recent_topics']), 0)
        
        

class WelcomeViewFunctionalTests(unittest.TestCase):
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
        response = self.testapp.get('/', status=200)

        self.assertTrue('Hello, pumbaa.CoE!' in response.text)