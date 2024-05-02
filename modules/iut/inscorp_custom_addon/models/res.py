from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_type = fields.Selection([
        ('vat1', 'VAT 1'),
        ('vat2', 'VAT 2'),
        ('vat3', 'VAT 3')
    ], string='VAT Type')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    partner_id = fields.Many2one('res.partner', string='Supplier')
    amount_total = fields.Float(string='Total Amount')
    show_validator_button = fields.Boolean(string="Show Validator Button", compute='_compute_show_validator_button',
                                           store=True)

    def button_validator(self):
        validated_state = 'purchase'
        self.write({'state': validated_state})
        self.show_validator_button = False
        return True

    @api.model
    def _check_order_total(self, partner_id):
        total_amount = sum(self.env['purchase.order'].search([('partner_id', '=', partner_id)]).mapped('amount_total'))
        if total_amount > 100000:
            return False
        return True

    def button_confirm(self):
        for order in self:
            if order.partner_id.vat_type == 'vat2':
                if not order._check_order_total(order.partner_id.id):
                    raise ValidationError(
                        _("Total order amount exceeds 100,000. Please review before confirming the order."))
        return super(PurchaseOrder, self).button_confirm()

    @api.depends('partner_id.vat_type')
    def _compute_show_validator_button(self):
        for order in self:
            order.show_validator_button = order.partner_id.vat_type == 'vat3'
