# -*- coding: utf-8 -*-
{
    'name': "cineprex",

    'summary': """
        Module de gestion de Cineprex""",

    'description': """
        Ce module permet la gestion de cineprex
    """,

    'author': "Marc-Alexis",
    'website': "https://www.univ-lr.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'demo/demo.xml',
        'views/cinema_view.xml',
        'views/movie_view.xml',
        'views/room_view.xml',
        'views/filmshow_view.xml',
        'views/ticketing_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
