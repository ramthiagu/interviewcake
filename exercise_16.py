#!/usr/bin/env python

import unittest
class CakeThief:

    def get_max_cake_value(self,cake, capacity):
      cake_weight = cake[0]
      cake_value = cake[1]
      max_number_of_bags = capacity / cake_weight
      return max_number_of_bags * cake_value


class TestCakeThief(unittest.TestCase):
    def setUp(self):
	self.cake_theif = CakeThief()
	self.cakes = [(7,160), (3,90), (2,15)]
	self.capacity = 20

    def test_get_max_cake_value(self):
	self.assertEquals(self.cake_theif.get_max_cake_value(self.cakes[0], self.capacity), 320)
	self.assertEquals(self.cake_theif.get_max_cake_value(self.cakes[1], self.capacity), 540)
	self.assertEquals(self.cake_theif.get_max_cake_value(self.cakes[2], self.capacity), 150)