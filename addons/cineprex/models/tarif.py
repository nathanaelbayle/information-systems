# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CineprexTarif(models.Model):
    _name = 'cineprex.tarif'
    _description = 'Les tarifs'
    _rec_name = "valeur"

    valeur = fields.Char(compute='_valeur')

    name = fields.Char('Nom du tarif')
    age = fields.Integer('Âge')
    price = fields.Integer('Prix')
    age_name = fields.Char(compute='_age_name_pc',string='Age')
    ticket_ids = fields.One2many(comodel_name='cineprex.ticket', inverse_name='tarif_id', string='Tickets')

    @api.depends('age')
    def _age_name_pc(self):
        for record in self:
            record.age_name = str(record.age) + ' ans'

    @api.depends('name', 'price')
    def _valeur(self):
        for record in self:
            record.valeur = "Tarif " + record.name + " - Prix : " + str(record.price) + "€"
