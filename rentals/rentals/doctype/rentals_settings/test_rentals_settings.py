# Copyright (c) 2024, BWH and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestRentalsSettings(FrappeTestCase):
	
	def test_standard_rate_set(self):
		rate = frappe.new_doc("Rentals Settings")
		rate.standard_rate = 20
		rate.save()
		self.assertEqual(rate.standard_rate, 20)
