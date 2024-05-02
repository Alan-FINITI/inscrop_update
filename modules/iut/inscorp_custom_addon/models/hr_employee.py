from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    x_comment = fields.Char(string="Comment", size=1000, required=False)

    employee_enrollment_date = fields.Datetime(string="Employee enrollment date", required=True)
    employee_duration_time = fields.Float(string="Employee duration time",)
    employee_end_date = fields.Datetime(string="Employee end date",  compute="_compute_end", inverse="_inverse_end", readonly=True)

    @api.depends('employee_enrollment_date', 'employee_duration_time')
    def _inverse_end(self):
        for record in self:
            if record.employee_end_date and record.employee_enrollment_date:
                duration = relativedelta(record.employee_end_date, record.employee_enrollment_date)
                record.employee_duration_time = duration.minutes/60 + duration.hours + duration.days*24 + duration.months*30*24 + duration.years*365*24
            else:
                record.employee_duration_time = 0.0

    def _compute_end(self):
        for record in self:
            if record.employee_enrollment_date and record.employee_duration_time:
                record.employee_end_date = record.employee_enrollment_date + timedelta(hours=record.employee_duration_time)
            else:
                record.employee_end_date = record.employee_enrollment_date

    @api.onchange('employee_duration_time')
    def onchange_employee(self):
        self._compute_end()

    @api.onchange('employee_enrollment_date')
    def onchange_employee(self):
        self._inverse_end()