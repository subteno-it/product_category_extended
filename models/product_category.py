# -*- coding: utf-8 -*-
##############################################################################
#
#    product_category_extended module for OpenERP, Add onchange on product category to fill sale and purchase taxes and uom on product
#    Copyright (C) 2011 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#    Copyright (C) 2015 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of product_category_extended
#
#    product_category_extended is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    product_category_extended is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    taxes_id = fields.Many2many(comodel_name='account.tax', string='Customer Taxes', domain=[('type_tax_use', '=', 'sale')])
    supplier_taxes_id = fields.Many2many(comodel_name='account.tax', string='Vendor Taxes', domain=[('type_tax_use', '=', 'purchase')])
    uom_id = fields.Many2one(comodel_name='product.uom', string='Default UoM', help='Default Unit of Measure')
    uom_po_id = fields.Many2one(comodel_name='product.uom', string='Purchase UoM', help='Unit of Measure for purchase')
    uos_id = fields.Many2one(comodel_name='product.uom', string='Unit of Sale', help='See product definition')
    uos_coef = fields.Float(string='UOM -> UOS coef', digits=(16, 4), help='See product definition')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
