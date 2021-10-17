# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexSeance(models.Model):
    _name = 'cineprex.seance'
    _description = "Séances"
    _rec_name = "valeur"

    valeur = fields.Char(compute='_valeur')
    horaire = fields.Datetime()

    salle_id = fields.Many2one(comodel_name='cineprex.salle') 
    movie_id = fields.Many2one(comodel_name='cineprex.movie')

    @api.depends('horaire', 'movie_id')
    def _valeur(self):
        for record in self:
            record.valeur = "Séance du " + str(record.horaire)  + " pour le film " + record.movie_id.nom