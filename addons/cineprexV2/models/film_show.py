# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class CineprexFilmshow(models.Model):
    _name = 'cineprex.film_show'
    _description = 'Les seances de cinéma'
    _rec_name = 'value'

    value = fields.Char(compute='_value_pc')
    start_date = fields.Datetime('Heure de début')
    end_date = fields.Datetime(compute='_end_date_pc', store=True, string="Heure de fin")
    full = fields.Boolean(compute='_full_pc', string="Complet")
    room_id = fields.Many2one(comodel_name='cineprex.room',string="Salle")
    movie_id = fields.Many2one(comodel_name='cineprex.movie',string="Film")
    tickets_ids = fields.One2many(comodel_name='cineprex.ticket', inverse_name='film_show_id', string='Tickets')

    @api.depends('start_date', 'room_id', 'movie_id')
    def _value_pc(self):
        for record in self:
            record.value = "Séance du "+ str(record.start_date) + " dans " + record.room_id.value + " pour  " + record.movie_id.name

    @api.depends('start_date', 'movie_id')
    def _end_date_pc(self):
        for record in self:
            record.end_date = record.start_date + datetime.timedelta(hours=record.movie_id.duration)

    @api.depends('tickets_ids','room_id')
    def _full_pc(self):
        for record in self:
            if len(record.tickets_ids) >= record.room_id.seat:
                record.full = True
            else:
                record.full = False

