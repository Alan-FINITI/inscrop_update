from odoo import models, fields, api

class ProductAllergenWizard(models.TransientModel):
    _name = 'product.allergen.wizard'

    product_ids = fields.Many2many(
        comodel_name='product.template',
        string='Products',
        inverse_name="allergen_category_ids",
    )
    allergen_ids = fields.Many2many(
        string="Allergen Category",
        comodel_name="allergen_category.category",
        inverse_name="products_ids",
    )

    @api.model
    def default_get(self, fields):
        defaults = super(ProductAllergenWizard, self).default_get(fields)
        product_ids = self._context.get('default_product_ids')
        if product_ids:
            defaults['product_ids'] = product_ids
        return defaults

    def add_product_allergen(self):
        for record in self:
            for allergen in record.allergen_ids:
                allergen.products_ids += record.product_ids




