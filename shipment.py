# This file is part stock_comment module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['ShipmentIn', 'ShipmentInReturn', 'ShipmentInternal', 'ShipmentOut',
    'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentIn:
    __name__ = 'stock.shipment.in'
    comment = fields.Text('Comment')


class ShipmentInReturn:
    __name__ = 'stock.shipment.in.return'
    comment = fields.Text('Comment')


class ShipmentInternal:
    __name__ = 'stock.shipment.internal'
    comment = fields.Text('Comment')


class ShipmentOut:
    __name__ = 'stock.shipment.out'
    comment = fields.Text('Comment')


class ShipmentOutReturn:
    __name__ = 'stock.shipment.out.return'
    comment = fields.Text('Comment')
