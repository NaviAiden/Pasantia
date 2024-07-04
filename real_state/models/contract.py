from odoo import models, fields

class Contract(models.Model):
    _name = 'realestate.contract'
    _description = 'Real Estate Contract'

    property_id = fields.Many2one('realestate.property', string='Property', required=True)
    client_id = fields.Many2one('realestate.client', string='Client', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date')
    price = fields.Float(string='Price', related='property_id.price')
