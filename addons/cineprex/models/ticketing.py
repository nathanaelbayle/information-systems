# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexTicketing(models.Model):
    _name = 'cineprex.ticketing'

    name = fields.Char()
    price = fields.Float()
    filmshow_id = fields.Many2one(comodel_name='cineprex.filmshow')