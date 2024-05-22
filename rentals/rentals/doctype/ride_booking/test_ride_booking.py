# Copyright (c) 2024, BWH and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestRideBooking(FrappeTestCase):

	def setUp(self):
		self.ride_order = frappe.get_doc({
                'doctype': 'Ride Order',
                'customer_name': 'Morgan Tallburg',
                'contact_number': '+254798356488',
                'pickup_time': '2024-05-31 09:00:00',
                'pickup_address': 'Moi International Airport'
            }).insert()
  
		self.driver = frappe.get_doc({
                'doctype': 'Driver',
                'first_name': 'Wayne',
                'license_number': 'JHK9322',
            }).insert()


		self.ride_booking = frappe.get_doc({
            'doctype': 'Ride Booking',
            'order': self.ride_order.name,
            'driver': self.driver.name,
            'rate': 20,
            'items': [
                {
                    'doctype': 'Ride Booking Item',
                    'source': 'A',
                    'destination': 'B',
                    'distance': 20
                },
                {
                    'doctype': 'Ride Booking Item',
                    'source': 'B',
                    'destination': 'C',
                    'distance': 40
                },
            ]
        }).insert()


	def tearDown(self):
		frappe.delete_doc('Ride Booking', self.ride_booking.name)
		frappe.delete_doc('Ride Order', self.ride_order.name)

	def test_total_amount_set_correctly(self):
		# self.assertEqual(self.ride_booking., 'Morgan Tallburg')
		total_distance = 0
		trips = self.ride_booking.items

		for trip in trips:
			total_distance += trip.distance

		total_cost = self.ride_booking.rate * total_distance
		self.assertEqual(self.ride_booking.total_amount, 1200)