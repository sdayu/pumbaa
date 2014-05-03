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

        from pumbaa.models import users
        #create user
        self.user = users.User()
        self.user.username = "korn"
        self.user.password = "korn"
        self.user.email = "korn@xx.com"
        self.user.display_name = "korn naja"
        self.user.last_name = "naja"
        self.user.first_name = "korn"
        self.user.save()

    def tearDown(self):
        testing.tearDown()
        self.user.delete()

    def test_index_get_recent_topics(self):
        from pumbaa.views.profile import index
        request = testing.DummyRequest()
        request.matchdict['profile_id'] = self.user.username
        result = index(request)
        
        self.assertIn('profile_id', result, 'profile name disappear in result')

        

class ProfileViewFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pumbaa import main
        
        cfg = configparser.ConfigParser()
        cfg.read('../../test.ini')
        
        settings = dict(cfg.items('app:main'))

        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

        from pumbaa.models import users
        #create user
        self.user = users.User()
        self.user.username = "korn"
        self.user.password = "korn"
        self.user.email = "korn@xx.com"
        self.user.display_name = "korn naja"
        self.user.last_name = "naja"
        self.user.first_name = "korn"
        self.user.save()

    def tearDown(self):
        testing.tearDown()
        self.user.delete()
        
    def test_get_welcome_msg(self):
        response = self.testapp.get('/profile/'+self.user.username, status=200)
        self.assertTrue('Profile Name' in response.text)