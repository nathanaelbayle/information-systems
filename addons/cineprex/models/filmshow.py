# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexFilmshow(models.Model):
    _name = 'cineprex.filmshow'

    date = fields.Datetime()
    room_id = fields.Many2one(comodel_name='cineprex.salle')
    movie_id = fields.Many2one(comodel_name='cineprex.movie')
    ticketing_ids = fields.One2many(comodel_name='cineprex.ticketing', inverse_name='filmshow_id')