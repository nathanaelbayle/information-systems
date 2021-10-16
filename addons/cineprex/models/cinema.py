# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexCinema(models.Model):
    _name = 'cineprex.cinema'
    _description = "Liste des Cinéma"
    _rec_name = "valeur"

    valeur = fields.Char(compute='_valeur')

    nom = fields.Char("Nom")
    adresse = fields.Char("Adresse")
    ville = fields.Char("Ville")
    code_postal = fields.Integer("Code Postal")

    room_ids = fields.One2many(string="Salles", comodel_name='cineprex.salle', inverse_name='cinema_id')
    
    @api.depends('nom')
    def _valeur(self):
        for record in self:
            record.valeur = record.nom