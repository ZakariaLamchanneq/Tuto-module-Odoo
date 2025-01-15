from odoo import models, fields, api

class GestionCommandes(models.Model):
    _name = 'gestion.commandes'
    _description = 'Gestion des Commandes'

    name = fields.Char(string='Nom de la commande', required=True)
    date_commande = fields.Datetime(
        string='Date de la commande',
        default=fields.Datetime.now
    )
    client_id = fields.Many2one(
        'res.partner',
        string='Client',
        required=True
    )
    total = fields.Float(string='Total', required=True)
    status = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Confirmée'),
        ('done', 'Livrée')
    ], string='Statut', default='draft')