
from odoo import models, fields

class Client(models.Model):
    _name = 'realestate.client'
    _description = 'Real Estate Client'

    name = fields.Char(string='Client Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
