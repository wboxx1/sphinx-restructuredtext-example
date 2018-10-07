# -*- coding: utf-8 -*-

import unittest
from .foobar import hello_world, reverse

class TestFoobar(unittest.TestCase):
    def test_helloworld(self):
        self.assertEqual(hello_world(),"Hello World!")

    def test_reverse(self):
        self.assertEqual(reverse("Hello World!"), "!dlroW olleH")
        
if __name__ == '__main__':
    unittest.main()