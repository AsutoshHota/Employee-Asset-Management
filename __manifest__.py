{
    'name': 'Employee Asset Management',
    'version': '16.0.1.0.0',  
    'category': 'Human Resources',
    'summary': 'Assign, Track, and Reclaim Assets for Employees',
    'author': 'Odoo', 
    'depends': ['hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/asset_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3', 
}
