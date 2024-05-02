from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class StockPicking (models.Model):
    _inherit = 'stock.picking'

    x_today_date = fields.Datetime(string="today date", compute="TodayDateCalcul", store=True)

    def TodayDateCalcul(self):
        for record in self:
            record.x_today_date = datetime.now();