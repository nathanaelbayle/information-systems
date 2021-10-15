# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexSalle(models.Model):
    _name = 'cineprex.salle'

    numero = fields.Integer()
    nb_place = fields.Integer()

    salle_3D = fields.Boolean()
    dolby = fields.Boolean()

    cinema_id = fields.Many2one(comodel_name='cineprex.cinema')


        
