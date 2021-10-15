# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexMovie(models.Model):
    _name = 'cineprex.movie'

    name = fields.Char()
    description = fields.Char()
    filmmaker = fields.Char()
    duration = fields.Integer()
    provider_id = fields.Many2one(comodel_name='cineprex.cinema')
    filmshow_ids = fields.One2many(comodel_name='cineprex.filmshow', inverse_name='movie_id')