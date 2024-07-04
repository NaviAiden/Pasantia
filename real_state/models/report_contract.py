from odoo import models

class ReportContract(models.AbstractModel):
    _name = 'report.realestate.report_contract'
    _description = 'reporte de contratos'

    def get_report_values(self, docids, data=None):
        docs = self.env['realestate.contract'].browse(docids)
        return {
            'docs': docs,
        }
