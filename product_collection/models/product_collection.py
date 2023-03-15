# © 2021 Jeremy Van Driessche
# © 2021 Niboo SRL (https://www.niboo.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models


class ProductCollection(models.Model):
    _name = "product.collection"
    _description = "Product Collection"

    name = fields.Char(required=True)
    description = fields.Text()
    product_ids = fields.One2many(
        comodel_name="product.template", inverse_name="collection_id", string="Products"
    )

    def open_add_product_wizard(self):
        """
        Open wizard to ease the add of products to the collection
        """
        self.ensure_one()
        wizard = self.env["add.product.collection.wizard"].create(
            {"collection_id": self.id, "product_ids": [(6, 0, self.product_ids.ids)]}
        )
        return {
            "name": _("Add product to collection"),
            "view_mode": "form",
            "res_model": "add.product.collection.wizard",
            "res_id": wizard.id,
            "target": "new",
            "type": "ir.actions.act_window",
            "context": dict(self.env.context, create=False),
        }
