# coding: utf-8
# ############################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://www.vauxoo.com>).
#    All Rights Reserved
# ############ Credits #######################################################
#    Coded by: Yanina Aular <yani@vauxoo.com>
#    Planified by: Moises Lopez <moises@vauxoo.com>
#    Audited by: Humberto Arocha <hbto@vauxoo.com>
# ############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ############################################################################
{
    "name": "Import Tax and Tariff",
    "version": "1.6",
    "summary": "Import Tax and Tariff",
    "depends": [
        "account_accountant",
        "stock"],
    "author": "Vauxoo",
    "website": "http://www.vauxoo.com/",
    "category": "Accounting",
    "data": [
        "view/import_tax_view.xml",
        "view/tariff_tariff_view.xml",
        "security/ir.model.access.csv"],
    "demo": [],
    "test": [],
    "active": False,
    "images": [],
    "installable": True,
    "application": True,
}
