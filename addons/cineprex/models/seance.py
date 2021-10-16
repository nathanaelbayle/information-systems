# -*- coding: utf-8 -*-

from odoo import models, fields

class CineprexSeance(models.Model):
    _name = 'cineprex.seance'
    
    horaire = fields.Datetime()

    salle_id = fields.Many2one(comodel_name='cineprex.salle') 
    movie_id = fields.Many2one(comodel_name='cineprex.movie')


    # ticketing_ids = fields.One2many(comodel_name='cineprex.ticket', inverse_name='seance_id')