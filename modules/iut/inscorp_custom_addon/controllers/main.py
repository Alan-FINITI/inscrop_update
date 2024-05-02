from odoo import http, _
from odoo.http import Controller, route, request
import logging


_logger = logging.getLogger(__name__)

class ProductController(http.Controller):

    @http.route(['/add_allergen'], type='json', auth='public')
    def add_allergen(self, product_id, allergen_id):
        if request.env.user.has_group('stock.group_stock_manager'):
            product = request.env['product.template'].browse(int(product_id))
            allergen = request.env['allergen_category.category'].browse(int(allergen_id))
            allergen.products_ids += product
            return True

    @http.route(['/delete_allergen', '/web/delete_allergen'], type='json', auth='public')
    def delete_allergen(self, product_id, allergen_id):
        if request.env.user.has_group('stock.group_stock_manager'):
            product = request.env['product.template'].browse(int(product_id))
            allergen = request.env['allergen_category.category'].browse(int(allergen_id))
            allergen.products_ids = allergen.products_ids.filtered(lambda p: p.id != int(product_id))
            _logger.info("product id : %s allergen id : %s", product_id, allergen_id)
            if product.get_missing_ids():
                return True
            else:
                return False

        #     return request.redirect('/shop/{}'.format(product_id) if product_id else '/shop')
        # else:
        #     return request.redirect('/shop/{}'.format(product_id) if product_id else '/shop')
