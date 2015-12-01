# This file is part of the stock_comment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Company']
__metaclass__ = PoolMeta


class Company:
    __name__ = 'company.company'
    comment_shipment = fields.Text('Shipment Comment', translate=True)
