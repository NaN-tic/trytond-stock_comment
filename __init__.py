#This file is part stock_comment module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .shipment import *
from .party import *


def register():
    Pool.register(
        ShipmentIn,
        ShipmentInReturn,
        ShipmentOut,
        ShipmentOutReturn,
        ShipmentInternal,
        Party,
        Address,
        module='stock_comment', type_='model')
