# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CineprexTicket(models.Model):
    _name = 'cineprex.ticket'
    _description = 'Ticket des séances'

    film_show_id = fields.Many2one(comodel_name='cineprex.film_show', string="Séance")
    tariff_id = fields.Many2one(comodel_name='cineprex.tariff', string="Tarif")
    price = fields.Float(compute='_price_pc',string='Prix du ticket')

    @api.depends('tariff_id','film_show_id','price')
    def _price_pc(self):
        for record in self:
            price = 0
            price = price + record.tariff_id.price
            if record.film_show_id.room_id.threeDimension:
                price = price + 5
            if record.film_show_id.room_id.ice:
                price = price + 2.5
            if record.film_show_id.room_id.dolby:
                price = price + 1.5
            record.price = price