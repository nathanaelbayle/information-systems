# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CineprexTariff(models.Model):
    _name = 'cineprex.tariff'
    _description = 'Les tarifs'

    name = fields.Char('Nom du tarif')
    age = fields.Integer('Âge')
    price = fields.Float('Prix')
    age_name = fields.Char(compute='_age_name_pc',string='Âge')
    ticket_ids = fields.One2many(comodel_name='cineprex.ticket', inverse_name='tariff_id', string='Tickets')

    @api.depends('age')
    def _age_name_pc(self):
        for record in self:
            record.age_name = str(record.age) + ' ans'