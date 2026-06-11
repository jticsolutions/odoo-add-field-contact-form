{
    'name': 'Add Field Contact Form',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Añade un campo extra al formulario de contacto',
    'description': """
        Este módulo añade un campo personalizado al formulario de contacto del sitio web.
    """,
    'author': 'Tu Nombre',
    'website': 'https://github.com/tu-usuario/odoo-add-field-contact-form',
    'depends': ['website', 'website_form'],
    'data': [
        'views/contact_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
