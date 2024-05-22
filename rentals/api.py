import frappe


@frappe.whitelist()
def get_emoji():
    return "💸"

def get_query_permission_conditions(user):
    return "name = 1"