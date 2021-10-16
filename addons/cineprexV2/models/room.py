# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CineprexRoom(models.Model):
    _name = 'cineprex.room'
    _description = 'Les salles de cinéma'
    _rec_name = 'value'

    value = fields.Char(compute='_value_pc')
    name = fields.Char('Nom de la salle')
    seat = fields.Integer('Nombre de siège')
    threeDimension = fields.Boolean('3D')
    ice = fields.Boolean('Ice')
    dolby = fields.Boolean('Dolby')
    movie_theater_id = fields.Many2one(comodel_name='cineprex.movie_theater', string="Cinéma")
    film_show_ids = fields.One2many(comodel_name='cineprex.film_show', inverse_name='room_id', string='Séances')

    @api.depends('name', 'movie_theater_id')
    def _value_pc(self):
        for record in self:
            record.value = 'Cinéma: ' + record.movie_theater_id.name + ' - Salle: ' + record.name