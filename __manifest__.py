{
    'name': 'Gestion des Commandes',
    'version': '1.0',
    'summary': 'Module de gestion des commandes client',
    'category': 'Sales',
    'author': 'Votre Nom',
    'website': 'http://votresite.com',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}