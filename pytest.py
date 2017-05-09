"""
Tests for HelloWorld program
"""

from hello import talk
import unittest

class TestHello(unittest.TestCase):
    def test_text_match(self):
        expected = "Hello world from Travis CI"
        self.assertEqual(expected, hello())

if __name__ == '__main__':
    unittest.main()
