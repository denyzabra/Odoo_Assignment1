from odoo import fields, models

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Requests'

    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity')
    purpose = fields.Text(string='Purpose')
    requested_by = fields.Many2one('res.users', string='Requested by')
