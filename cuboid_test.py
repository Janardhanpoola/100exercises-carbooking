import unittest
from cuboid import cuboid_volume
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(cuboid_volume(2),8)
        self.assertEqual(cuboid_volume("oakys"),3)
    