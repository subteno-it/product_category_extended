# -*- coding: utf-8 -*-
##############################################################################
#
#    product_tax_category module for OpenERP
#    Copyright (C) 2009 SYLEAM (<http://www.syleam.fr>) Christophe CHAUVET
#
#    This file is a part of product_tax_category
#
#    product_tax_category is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    product_tax_category is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv
from osv import fields

class product_category(osv.osv):
    _inherit = 'product.category'

    _columns = {
        'sale_taxes_ids': fields.many2many('account.tax', 'product_cat_tax_cust_rel',
            'cat_id', 'tax_id', 'Sales Taxes',
            domain=[('parent_id','=',False),('type_tax_use','in',['sale','all'])]),
        'purchase_taxes_ids': fields.many2many('account.tax', 'product_cat_tax_supp_rel',
            'cat_id', 'tax_id', 'Purchase Taxes',
            domain=[('parent_id', '=', False),('type_tax_use','in',['purchase','all'])]),
    }

product_category()

class product_product(osv.osv):
    _inherit = 'product.product'

    def onchange_category(self, cr, uid, ids, category, context=None):
        """
        When category change, we search:
        * Taxes (sale and purchase)
        * UOM
        * Product Type
        """
        if not context: context = {}
        res = {}

        if not category:
            res['categ_id'] = res['uom_id'] = res['uom_po_id'] = False
            res['supplier_taxes_id'] = []
            res['taxes_id'] = []
        else:
            res['categ_id'] =  category


        print 'Categ_id: %d' % category

        return {'value': res}

product_product()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
