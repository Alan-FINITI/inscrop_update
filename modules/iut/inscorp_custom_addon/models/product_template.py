from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    allergen_category_ids = fields.Many2many(
        string="Allergen Category",
        comodel_name="allergen_category.category",
        inverse_name="products_ids",

    )
    allergen_info = fields.Text(
        string="Allergen Information",
        compute='_compute_allergen_info'
    )

    @api.depends('bom_ids', 'bom_ids.bom_line_ids', 'bom_ids.bom_line_ids.product_id')
    def _compute_allergen_info(self):
        for record in self:
            allergens = []
            for bom in record.bom_ids:
                for line in bom.bom_line_ids:
                    if line.product_id.allergen_category_ids:
                        for allergen_category in line.product_id.allergen_category_ids:
                            allergens.append(allergen_category.allergen)
            record.allergen_info = ", ".join(allergens) if allergens else _("No allergens present")

    def get_allergen_ids(self):
        allergen_ids = self.env['allergen_category.category']
        for record in self:
            allergen_ids += allergen_ids.search([('products_ids', '=', record.id)])
        return allergen_ids

    def get_missing_ids(self):
        missing_allergen_ids = self.env['allergen_category.category']
        for record in self:
            missing_allergen_ids += missing_allergen_ids.search([('products_ids', '!=', record.id)])
        return missing_allergen_ids


    def open_wizard(self):
        return {
            'name': 'Add Allergen Categories',
            'type': 'ir.actions.act_window',
            'res_model': 'product.allergen.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_ids': [(6, 0, self.ids)]  # Pass selected product IDs to wizard
            },
        }
