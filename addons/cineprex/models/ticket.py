# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexTicket(models.Model):
    _name = 'cineprex.ticket'

    name = fields.Char()
    price = fields.Float()
    filmshow_id = fields.Many2one(comodel_name='cineprex.seance')