{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage Real Estate properties, clients and contracts',
    'description': """
        Real Estate Management module for Odoo 15.
    """,
    'author': 'Alvaro Melgarejo',
    'website': 'http://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/compare_views.xml',
        'views/client_views.xml',
        'views/contract_views.xml',
        'data/property_data.xml',
        'data/client_data.xml',
        'data/contract_data.xml',
    ],
    'installable': True,
    'application': True,
}
