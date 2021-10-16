# -*- coding: utf-8 -*-
# from odoo import http


# class Cineprex(http.Controller):
#     @http.route('/cineprex/cineprex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cineprex/cineprex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cineprex.listing', {
#             'root': '/cineprex/cineprex',
#             'objects': http.request.env['cineprex.cineprex'].search([]),
#         })

#     @http.route('/cineprex/cineprex/objects/<model("cineprex.cineprex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cineprex.object', {
#             'object': obj
#         })
