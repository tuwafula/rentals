# Copyright (c) 2024, BWH and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestRideOrder(FrappeTestCase):
  
	def test_driver_set_name_and_phone_number_correctly(self):
		test_order = frappe.new_doc("Ride Order")
		test_order.customer_name = 'Morgan Tallburg'
		test_order.contact_number = '+254798356488'
		test_order.pickup_time = '2022-10-31 09:00:00'
		test_order.pickup_address = 'Moi International Airport'
		test_order.save()
		self.assertEqual(test_order.customer_name, "Morgan Tallburg")
		self.assertEqual(test_order.contact_number, "+254798356488")
  
  