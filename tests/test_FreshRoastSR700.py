import unittest
from openroast.modules.roaster_libraries.FreshRoastSR700 import FreshRoastSR700

class TestFreshRoastSR700(unittest.TestCase):
    def setUp(self):
        self.FreshRoastSR700 = FreshRoastSR700()

    def test_creation(self):
        self.assertTrue(isinstance(self.FreshRoastSR700, FreshRoastSR700))


if __name__ == '__main__':
    unittest.main()
