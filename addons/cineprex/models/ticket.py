# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexTicket(models.Model):
    _name = 'cineprex.ticket'
    _description = 'Ticket des séances'
    _rec_name = "valeur"

    valeur = fields.Char(compute='_valeur')
    seance_id = fields.Many2one(string="Séance", comodel_name='cineprex.seance')
    tarif_id = fields.Many2one(string="Tarif", comodel_name='cineprex.tarif' )
    prix = fields.Float(string='Prix du ticket', compute='_prix')

    @api.depends('tarif_id','seance_id','prix')
    def _prix(self):
        for record in self:
            prix = 0
            prix = prix + record.tarif_id.price
            if record.seance_id.salle_id.salle_3D:
                prix = prix + 5
            if record.seance_id.salle_id.dolby:
                prix = prix + 1.5
            record.prix = prix

    @api.depends('seance_id')
    def _valeur(self):
        for record in self:
            record.valeur = "Ticket pour " + record.seance_id.movie_id.nom + " programmé le " + str(record.seance_id.horaire)