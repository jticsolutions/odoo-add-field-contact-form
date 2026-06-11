from odoo import models, fields

class ContactForm(models.Model):
    _inherit = 'website.form'

    # Ejemplo: campo extra (ajústalo según necesidad real)
    extra_field = fields.Char(string='Campo Extra', help="Campo personalizado añadido")
