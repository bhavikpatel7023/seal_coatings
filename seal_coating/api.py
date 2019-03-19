from __future__ import unicode_literals
import frappe
from frappe import msgprint,throw, _
from erpnext.stock.doctype.quality_inspection_template.quality_inspection_template import get_template_details


@frappe.whitelist()
def get_item_specification_details(quality_inspection_template):
	parameters = frappe.get_doc("Quality Inspection Template",quality_inspection_template)
	return parameters.item_quality_inspection_parameter

		
@frappe.whitelist()
def test():
	return "test"

