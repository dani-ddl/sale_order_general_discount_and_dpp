
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.addons import decimal_precision as dp
from lxml import etree


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_dpp = fields.Float(
        digits=dp.get_precision('Discount'),
        string='Discount (%)',
    )

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super().onchange_partner_id()
        self.discount_dpp = self.partner_id.discount_dpp

        self.mapped('order_line').update({
            'discount3': self.discount_dpp,
        })
        return

    @api.onchange('discount_dpp')
    def onchange_general_discount(self):
        self.mapped('order_line').update({
            'discount3': self.discount_dpp,
        })
