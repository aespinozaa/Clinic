# -*- coding: utf-8 -*-
# Copyright 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Financial Risk',
    'summary': 'Manage partner risk',
    'version': '10.0.1.0.1',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'author': 'Tecnativa, Odoo Community Association (OCA)',
    'website': 'https://www.tecnativa.com',
    'depends': [
        'account',
    ],
    'data': [
        'data/partner_financial_risk_data.xml',
        'views/res_config_view.xml',
        'views/res_partner_view.xml',
        'wizard/partner_risk_exceeded_view.xml',
        'templates/assets.xml',
    ],
    'installable': True,
}
