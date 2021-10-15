# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexProvider(models.Model):
    _name = 'cineprex.cinema'

    nom = fields.Char()
    adresse = fields.Char()
    ville = fields.Char()
    code_postal = fields.Integer()
    movie_ids = fields.One2many(comodel_name='cineprex.movie', inverse_name='cinema_id')