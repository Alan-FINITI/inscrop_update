from odoo import api, fields, models

class HrRecipe(models.Model):
    _inherit = "mrp.bom"

    x_calculated_producted_quantity = fields.Float(string="Nombre de productions possibles", digits=(10, 2), compute='_compute_calculated_productable_qty')

    @api.depends('product_id', 'bom_line_ids.product_id.qty_available',
                 'bom_line_ids.product_qty')
    def _compute_calculated_productable_qty(self):
        for record in self:
            minimal_quantity = float('inf')
            for line in record.bom_line_ids:
                if line.product_id and line.product_id.qty_available and line.product_qty != 0:
                    component_qty = line.product_id.qty_available / line.product_qty
                    if component_qty < minimal_quantity:
                        minimal_quantity = component_qty
            record.x_calculated_producted_quantity = minimal_quantity if minimal_quantity != float('inf') else 0.0
        return record.x_calculated_producted_quantity
