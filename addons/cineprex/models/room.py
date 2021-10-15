# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexRoom(models.Model):
    _name = 'cineprex.room'

    name = fields.Integer()
    seat = fields.Integer()
    threeDimension = fields.Boolean()
    airConditioner = fields.Boolean()
    filmshow_ids = fields.One2many(comodel_name='cineprex.filmshow', inverse_name='room_id')