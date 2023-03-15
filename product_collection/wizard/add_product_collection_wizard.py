# © 2021 Jeremy Van Driessche
# © 2021 Niboo SRL (https://www.niboo.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class AddProductCollectionWizard(models.TransientModel):
    _name = "add.product.collection.wizard"

    collection_id = fields.Many2one("product.collection")
    product_ids = fields.Many2many("product.template")

    def save(self):
        self.ensure_one()
        self.collection_id.write({"product_ids": [(6, 0, self.product_ids.ids)]})
