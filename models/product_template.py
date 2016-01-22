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

from openerp.tools.translate import _
from openerp import models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.onchange('categ_id')
    def _onchange_categ_id(self):
        """
        When category changes, we search for taxes, UOM and product type
        """
        warn = False

        if not self.categ_id:
            self.categ_id = False
            self.uom_id = False
            self.uom_po_id = False
            self.taxes_id = []
            self.supplier_taxes_id = []
        else:
            # Search for the default value on this category
            if self.categ_id.taxes_id:
                self.taxes_id = self.categ_id.taxes_id
            if self.categ_id.supplier_taxes_id:
                self.supplier_taxes_id = self.categ_id.supplier_taxes_id
            if self.categ_id.uom_id:
                self.uom_id = self.categ_id.uom_id
            if self.categ_id.uom_po_id:
                self.uom_po_id = self.categ_id.uom_po_id
            if self.categ_id.uos_id:
                self.uos_id = self.categ_id.uos_id
                self.uos_coef = self.categ_id.uos_coef
            warn = {
                'title': _('Caution'),
                'message': _("""The product category has changed, thanks to control :
    * Sale and Purchase taxes
    * Unit sale and stock
    * The price with return unit"""),
            }
        return {'warning': warn}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
