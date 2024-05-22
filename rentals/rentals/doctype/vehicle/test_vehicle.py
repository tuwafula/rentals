# Copyright (c) 2024, BWH and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestVehicle(FrappeTestCase):

	def test_set_title_correctly_set(self):
		test_vehicle = frappe.new_doc("Vehicle")
		test_vehicle.make = "Adudi"
		test_vehicle.model = "TTrs"
		test_vehicle.year = "2022"
		test_vehicle.color = 'Blue'
		test_vehicle.insurance_expiry = "2024-05-31"
		test_vehicle.save()
		self.assertEqual(test_vehicle.title, "Adudi TTrs, 2022")
