from odoo import fields, models

class CustomRFQ(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many('res.partner', string='Vendors')

class CustomBid(models.Model):
    _name = 'custom.bid'
    _description = 'Bids received against an RFQ'

    rfq_id = fields.Many2one('purchase.order', string='RFQ')
    price = fields.Float(string='Price')
    quantity = fields.Float(string='Quantity')
    delivery_date = fields.Date(string='Delivery Date')

    status = fields.Selection([
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected'),
        ], string='Status', default='pending')
    is_winner = fields.Boolean(string='Winner')

