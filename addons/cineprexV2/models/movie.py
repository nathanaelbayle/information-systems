# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexMovie(models.Model):
    _name = 'cineprex.movie'
    _description = 'Les films'
    _rec_name = 'value'

    value = fields.Char(compute='_value_pc')
    name = fields.Char('Nom du film')
    filmmaker = fields.Char('Réalisateur')
    duration = fields.Float('Durée du film')
    reveal = fields.Date('Date de sortie')
    film_show_ids = fields.One2many(comodel_name='cineprex.film_show', inverse_name='movie_id', string='Séances')
    rental_id = fields.Many2one(comodel_name='cineprex.rental',string="Location")


    @api.depends('name', 'reveal', 'filmmaker')
    def _value_pc(self):
        for record in self:
            record.value = '"'+record.name+'"'+" sortie le "+str(record.reveal)+" réalisé par "+record.filmmaker