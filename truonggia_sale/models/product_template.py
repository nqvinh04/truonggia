from email.policy import default

from odoo import fields, models, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # packing_specifications = fields.Integer(string='Quy cách đóng thùng')
    packing_specifications = fields.Integer(string='Packing Specifications')
    unit_per_barrel = state = fields.Selection([
        ('package', 'Package'),
        ('box', 'Box'),
        ('cup', 'Cup'),
        ('shift', 'Shift'),
        ('shift', 'Shift'),
        ('handbag', 'Handbag')], string='Unit Per Barrel', default='package')
    truong_gia = fields.Boolean(string='Truong Gia', default=True)

