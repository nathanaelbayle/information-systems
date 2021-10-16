# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexRental(models.Model):
    _name = 'cineprex.rental'
    _description = 'Les locations'
    _rec_name = 'value'

    value = fields.Char(compute='_value_pc')
    start = fields.Date("Début de la location")
    end = fields.Date("Fin de la location")
    price = fields.Float("Prix par jour")
    total_price = fields.Float(compute="_total_price_pc",string="Prix total de la location")
    provider_id = fields.Many2one(comodel_name='res.company',string="Fournisseur")
    movie_ids = fields.One2many(comodel_name='cineprex.movie', inverse_name='rental_id', string='Films')
    movie_html = fields.Html(compute='_movie_pc', string="Liste des films")

    @api.depends('start', 'end', 'provider_id')
    def _value_pc(self):
        for record in self:
            record.value = 'Location du ' + str(record.start) + ' au ' + str(record.end) + ' par ' + record.provider_id.name

    @api.depends('start', 'end', 'price')
    def _total_price_pc(self):
        for record in self:
            record.total_price = (record.end - record.start).days * record.price
    
    @api.depends('movie_ids')
    def _movie_pc(self):
        for record in self:
            html = '<ul>'
            for movie in record.movie_ids:
                html = html + "<li>" + movie.value + "</li>"
            html = html + "</ul>"
            record.movie_html = html