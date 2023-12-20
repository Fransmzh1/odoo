from odoo import fields, models


class EstatePropertyTag (models.Model):

    _name = 'estate.property.tag'
    _description = 'Table estate_property_tag'

    name = fields.Char(string='Tag Name', required=True)
