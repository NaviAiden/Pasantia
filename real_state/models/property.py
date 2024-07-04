from odoo import models, fields
from datetime import datetime, timedelta

class Property(models.Model):
    _name = 'realestate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Property Name', required=True, default=" ")
    description = fields.Text(string='Description')
    rooms = fields.Integer(string='Number of Rooms', default=2, required=True)
    address = fields.Char(string='Address')
    price = fields.Float(string='Price')
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('commercial', 'Commercial'),
        ('duplex', 'duplex'),
    ], string='Property Type', default='house')
    disponibility_date = fields.Datetime(string='Date of Disponibility', copy=False, default=lambda self: fields.Datetime.now() + timedelta(days=90))
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    active = fields.Boolean(string="Active", default=True)
    
    state = fields.Selection([
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('under_repair', 'Under Repair'),
    ], string='Status', default='available')
    image_main = fields.Binary(string='Main Image')
    image_gallery = fields.Many2many('ir.attachment', string='Gallery Images')
    # Nuevo campo para ubicación
    location = fields.Char(string='Location')
    # Nuevo campo para poder hacer las comparaciones(nueva funcion)
    compare = fields.Boolean(string='Compare', default=True)


    #Para evitar que sigan marcados los campos despues de la comparacion se llama al metodo para limpiar los campos 
    def clear_compare(self):
        properties = self.search([('compare', '=', True)])
        properties.write({'compare': False})
