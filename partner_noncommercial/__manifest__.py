# -*- coding: utf-8 -*-
# Copyright 2015-2018 Therp BV (https://therp.nl).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Partner Non Commercial',
    'version': '10.0.1.0.0',
    'author': 'Therp BV,Camptocamp,Odoo Community Association (OCA)',
    'website': 'https://github.com/oca/partner-contact',
    'complexity': 'normal',
    'category': 'Customer Relationship Management',
    'license': 'AGPL-3',
    'depends': [
        'sales_team',  # Contains address book configuration
    ],
    'data': [
        'views/menu.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
}
