import unittest

from pyramid import testing

class TopicInfoViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
    
    def tearDown(self):
        testing.tearDown()

    def test_index_get_info(self):
        pass
