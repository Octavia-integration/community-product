# © 2021 Jeremy Van Driessche
# © 2021 Niboo SRL (https://www.niboo.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Product - Product collection",
    "category": "Product",
    "summary": "Add possibility to define collection on product",
    "website": "https://www.niboo.com/",
    "version": "14.0.1.0.0",
    "license": "Other proprietary",
    "description": """
- Allow to link product to a collection
    """,
    "author": "Niboo",
    "depends": ["product", "purchase"],
    "data": [
        "views/product_collection_views.xml",
        "views/product_template_views.xml",
        "security/ir.model.access.csv",
        "wizard/add_product_collection_wizard_views.xml",
    ],
    "installable": False,
    "application": False,
}
