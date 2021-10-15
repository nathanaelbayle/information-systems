# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexRoom(models.Model):
    _name = 'cineprex.room'

    numero = fields.Integer()
    nb_place = fields.Integer()

    salle_3D = fields.Boolean()
    dolby = fields.Boolean()

    cinema_id = fields.Many2one(comodel_name='cineprex.cinema')
    
    # filmshow_ids = fields.One2many(comodel_name='cineprex.filmshow', inverse_name='room_id')
