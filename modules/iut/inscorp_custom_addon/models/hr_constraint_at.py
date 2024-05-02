from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, timedelta



class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    @api.onchange('check_in', 'check_out')
    def _onchange_check_in_out(self):
        for attendance in self:
            if attendance.check_out and attendance.check_in:
                last_checkout = self.env['hr.attendance'].search([
                    ('employee_id', '=', attendance.employee_id.id),
                    ('check_out', '<', attendance.check_out),
                ], order='check_out desc', limit=1)
                if last_checkout and (attendance.check_out - last_checkout.check_out) < timedelta(minutes=30):
                    raise ValidationError("You cannot check in. Last check out was less than 30 minutes ago.")

                # Vérification de la durée maximale d'un shift
                shift_duration = attendance.check_out - attendance.check_in
                if shift_duration > timedelta(hours=4):
                    raise UserError("Maximum shift duration is 4 hours.")

                # Vérification de la durée minimale d'un shift
                try:
                    original_check_out = attendance.check_out  # Copie temporaire de check_out
                    if shift_duration < timedelta(hours=2):
                        attendance.sudo().check_out = False
                        raise ValidationError("Minimum shift duration is 2 hours.")
                except ValidationError as e:
                    attendance.sudo().check_out = original_check_out  # Restaurer la valeur d'origine
                    raise e  # Renvoyer l'exception

                # Vérification de la durée maximale de travail par jour
                today_attendances = self.env['hr.attendance'].search([
                    ('employee_id', '=', attendance.employee_id.id),
                    ('check_in', '>=', fields.Datetime.now().replace(hour=0, minute=0, second=0)),
                    ('check_out', '<=', fields.Datetime.now().replace(hour=23, minute=59, second=59)),
                ])
                total_duration = sum((att.check_out - att.check_in).total_seconds() / 3600 for att in
                                     today_attendances) + shift_duration.total_seconds() / 3600
                # Comparaison avec 8 heures
                if total_duration > 8:
                    raise ValidationError("Maximum work duration per day is 8 hours.")
