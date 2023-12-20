from contextlib import nullcontext
from email.policy import default
from odoo import fields, models, api
from datetime import datetime


class EstateProperty (models.Model):

    _name = 'estate.property'
    _description = 'Table estate_property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    property_tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    date_availability = fields.Date(string='Available from', copy=False, default=datetime.today())
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer (string='Bedrooms', default=2)
    living_area = fields.Integer (string='Living Area (sqm)')
    facades = fields.Integer(string = 'Facades')
    garage = fields.Boolean(string = 'Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
                        string=('Garden Orientation'),
                        selection=[('North','North'), ('South','South'), ('East','East'), ('West','West')],
                        help="Arah matamu eh mata angin"
                        )
    state = fields.Selection(
                        string=('State'), required=True, 
                        selection=[('new','New'),
                                    ('received','Offered Received'),
                                    ('accepted','Offer Accepted'),
                                    ('sold','Sold'),
                                    ('canceled','Canceled')
                                ],
                        default='new',
                        copy=False
            )
    user_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    total_area = fields.Integer(compute="_compute_total")
    best_offer = fields.Float(string="Best Offer")
    active = fields.Boolean(string='Active', default=True)

    @api.depends('garden_area', 'living_area')
    def _compute_total(self):
        for record in self:
            record.total_area =  record.garden_area + record.living_area

    # @api.depends('offer_ids')
    # def _compute_best_offer(self):
    #     for record in self:
    #         record.best_offer = max( record.offer_ids.mapped('price') )