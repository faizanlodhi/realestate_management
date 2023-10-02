from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"

    name = fields.Char(string="Type", required=True)
    offer_ids = fields.One2many(
        "estate.property.offer",
        "property_id",
        string="Offers",
        copy=False,
    )