# © 2021 Jeremy Van Driessche
# © 2021 Niboo SRL (https://www.niboo.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    collection_id = fields.Many2one("product.collection")


class ProductProduct(models.Model):
    _inherit = "product.product"

    collection_id = fields.Many2one(related="product_tmpl_id.collection_id")
