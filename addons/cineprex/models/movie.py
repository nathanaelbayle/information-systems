# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexMovie(models.Model):
    _name = "cineprex.movie"
    _description = "Les films"
    _rec_name = "valeur"

    valeur = fields.Char(compute='_valeur')
    nom = fields.Char("Titre")
    realisateur = fields.Char("Réalisateur")
    date_sortie = fields.Date("Date de Sortie")
    duree = fields.Integer("Durée")
    description = fields.Char("Description")

    seance_id = fields.Many2one(string="", comodel_name='cineprex.seance', inverse_name='movie_id')

    @api.depends('nom', 'date_sortie', 'realisateur')
    def _valeur(self):
        for record in self:
            record.valeur = '"' + record.nom + '"' + " sortie le " + str(record.date_sortie) + " réalisé par " + record.realisateur