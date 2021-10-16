# -*- coding: utf-8 -*-
{
    'name': "cineprexV2",

    'summary': """
        Module de gestion de Cineprex""",

    'description': """
        Ce module permet la gestion de cineprex
    """,

    'author': "Marc-Alexis Azais, Bilal Belmoktar",
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
        'views/movie_theater_view.xml',
        'views/room_view.xml',
        'views/movie_view.xml',
        'views/film_show_view.xml',
        'views/ticket_view.xml',
        'views/tariff_view.xml',
        'views/society_view.xml',
        'views/rental_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
