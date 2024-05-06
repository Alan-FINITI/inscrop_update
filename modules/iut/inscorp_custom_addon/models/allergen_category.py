from odoo import fields, models, api, _


class Category(models.Model):
    _name = "allergen_category.category"
    _description = "Table allergen category"
    _rec_name = "allergen"
    _display_name = "allergen"

    allergen = fields.Char("Allergen Category", size=100, required=False)
    products_ids = fields.Many2many(
        string="Product",
        comodel_name="product.template",
        inverse_name="allergen_category_ids"
    )

    def get_allergen_names(self):
        """
        :return:  a string with all allergen name with separator ','
        """
        string = ""
        for allergen_id in self:
            if allergen_id is not None:
                string += "{}".format(allergen_id.display_name)
                if len(self) > 1:
                    if allergen_id != self[-1]:
                        string += ", "
        return string
