from __future__ import unicode_literals
import frappe
from frappe import msgprint,throw, _
from erpnext.stock.doctype.quality_inspection_template.quality_inspection_template import get_template_details


@frappe.whitelist()
def get_item_specification_details(self):
	if not self.quality_inspection_template:
		self.quality_inspection_template = frappe.db.get_value('Item',
			self.item_code, 'quality_inspection_template')
	if not self.quality_inspection_template: return

	self.set('readings', [])
	parameters = get_template_details(self.quality_inspection_template)
	for d in parameters:
		child = self.append('readings', {})
		child.specification = d.specification
		child.test_method = d.test_method
		child.unit = d.unit
		child.result = d.result
		child.status = "Accepted"
		
@frappe.whitelist()
def test():
	return "test"

