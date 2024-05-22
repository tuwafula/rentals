// Copyright (c) 2024, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {},

	rate(frm) {
		frm.trigger("update_total_amount");
	},

	update_total_amount(frm) {
		total_d = 0;
		for (let item of frm.doc.items) {
			total_d += item.distance;
		}

		const amount = total_d * frm.doc.rate;
		frm.set_value("total_amount", amount);
	},
});

frappe.ui.form.on("Ride Booking Item", {
	refresh(frm) {},

	distance(frm, cdt, cdn) {
		frm.trigger("update_total_amount");
	},

	items_remove(frm) {
		frm.trigger("update_total_amount");
	},
});
