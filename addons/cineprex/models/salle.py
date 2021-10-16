# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexSalle(models.Model):
    _name = 'cineprex.salle'
    _description = 'Salles de cinéma'
    _rec_name = 'valeur'

    valeur = fields.Char(compute='_valeur')
    numero = fields.Char()
    nb_place = fields.Integer("Nombre de places")
    salle_3D = fields.Boolean("Technologie 3D")
    dolby = fields.Boolean("Technologie Dolby")

    cinema_id = fields.Many2one(string = "Cinéma", comodel_name = "cineprex.cinema")

    seance_id = fields.One2many(string = "Séances", comodel_name='cineprex.seance', inverse_name='salle_id')
    
    @api.depends('numero', 'cinema_id')
    def _valeur(self):
        for record in self:
            record.valeur = record.cinema_id.nom + ' - Salle : ' + record.numero
