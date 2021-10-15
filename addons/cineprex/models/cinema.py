# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexCinema(models.Model):
    _name = 'cineprex.cinema'

    nom = fields.Char()
    adresse = fields.Char()
    ville = fields.Char()
    code_postal = fields.Integer()

    room_ids = fields.One2many(comodel_name='cineprex.room', inverse_name='cinema_id')

    # movie_ids = fields.One2many(comodel_name='cineprex.movie', inverse_name='cinema_id')