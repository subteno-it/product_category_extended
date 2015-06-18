# -*- coding: utf-8 -*-
##############################################################################
#
#    product_category_extended module for OpenERP, Add onchange on product category to fill sale and purchase taxes and uom on product
#    Copyright (C) 2011 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
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

from openerp import models, fields, api


class product_category(models.Model):
    _inherit = 'product.category'

    sale_taxes_ids = fields.Many2many('account.tax', 'product_cat_tax_cust_rel', 'cat_id', 'tax_id', 'Sale Taxes',
                                      domain=[('parent_id', '=', False), ('type_tax_use', 'in', ['sale', 'all'])],
                                      help='Taxes applied on sale orders')
    purchase_taxes_ids = fields.Many2many('account.tax', 'product_cat_tax_supp_rel', 'cat_id', 'tax_id', 'Purchase Taxes',
                                          domain=[('parent_id', '=', False), ('type_tax_use', 'in', ['purchase', 'all'])],
                                          help='Taxes applied on purchase orders')
    uom_id = fields.Many2one('product.uom', 'Default UoM', help='Default Unit of Measure')
    uom_po_id = fields.Many2one('product.uom', 'Purchase UoM', help='Unit of Measure for purchase')
    uos_id = fields.Many2one('product.uom', 'Unit of Sale', help='See product definition')
    uos_coef = fields.Float('UOM -> UOS coef', digits=(16, 4), help='See product definition')


class product_product(models.Model):
    _inherit = 'product.product'

    @api.onchange('categ_id')
    def onchange_category(self):
        """
        When category changes, we search for taxes, UOM and product type
        """

        self.uom_id = False
        self.uom_po_id = False
        self.taxes_id = []
        self.supplier_taxes_id = []

        self.taxes_id = self.categ_id.sale_taxes_ids
        self.supplier_taxes_id = self.categ_id.purchase_taxes_ids
        self.uom_id = self.categ_id.uom_id
        self.uom_po_id = self.categ_id.uom_po_id
        self.uos_id = self.categ_id.uos_id
        self.uos_coef = self.categ_id.uos_coef


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
