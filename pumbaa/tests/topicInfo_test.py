import unittest

from pyramid import testing
import configparser

class TopicInfoTests(unittest.TestCase):
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

    def test_showTag_get_msg_TopicInfo(self):
        response = self.testapp.get('/', status=200)

        self.assertTrue('TopicInfo' in response.text)

    def test


if __name__ in "__main__":
    unittest.main()
