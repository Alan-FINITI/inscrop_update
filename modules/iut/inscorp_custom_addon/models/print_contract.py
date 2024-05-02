from odoo import models, api

class Contract(models.Model):
    _inherit = 'hr.contract'

    def print_contract(self):
        # Code pour générer le rapport PDF du contrat
        # Vous pouvez utiliser ReportLab ou d'autres bibliothèques pour générer le PDF
        # Puis, renvoyez le contenu du rapport PDF
        return self.env.ref('inscorp_custom_addon.report_contract_template').report_action(self)