# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CineprexMovieTheater(models.Model):
    _name = 'cineprex.movie_theater'
    _description = 'Les cinémas'

    name = fields.Char("Nom du cinéma")
    room_ids = fields.One2many(comodel_name='cineprex.room', inverse_name='movie_theater_id',string='Salles')
    society_id = fields.Many2one(comodel_name='res.company',string="Société")

