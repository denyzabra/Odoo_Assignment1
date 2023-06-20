from odoo import fields, models

class CustomRFQ(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.One2many('res.partner', 'rfq_id', string='Vendors')
    winning_bid_id = fields.Many2one('custom.bid', string='Winning Bid')
