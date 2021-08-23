from unittest import TestCase

from version import A3DVersion


"""
80 00
80 01
00 01


In a3d 1 its always just 00 01
in a3d2 its package, nullmask, version
"""


class TestA3DVersion(TestCase):

    def setUp(self) -> None:
        self.version = A3DVersion()

    def test_read(self):
        self.assertIsNone(self.version.read())

    def test_write(self):
        self.fail()

    def test_from_file_path(self):
        self.fail()
