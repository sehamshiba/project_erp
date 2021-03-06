from openerp.osv import orm, fields


# class iti_students(orm.Model):
# def change_department(self, cr, uid, skills__ids, context=None):
# department = self.pool.get('iti.department').browse(cr, uid, skills__ids),
#
# return department
#
# _name = 'iti.student'
# grade = [('g', 'good'), ('vg', 'very good'), ('ex', 'exellent')]
# year = [('f', '2012'), ('s', '2013'), ('l', '2014')]
# state = [('applied', 'Applied'), ('accepted', 'Accepted')]
#
# def dep_domain(self, cr, uid, ids, grade, context=None):
# # g_ids = self.pool.get('iti.department').search(cr, uid, [('allowed', '=', True)])
# # vg_ids = self.pool.get('iti.department').search(cr, uid, [])
# # if grade == 'vg' or grade == 'ex':
# # domain_ids = vg_ids
# # else:
# # domain_ids = g_ids
#
# # return {'domain': {'department_id': [('id', 'in', domain_ids)]}}
#
# if grade == 'g':
# domain = [('allowed', '=', True)]
# else:
# domain = []
# return {
# 'domain': {'department_id': domain}}
#
# def set_accepted(self, cr, uid, ids, context=None):
# return self.write(cr, uid, ids, {'state': 'accepted'})
#
# _columns = {
# 'img': fields.binary('image'),
# 'name': fields.text('Name'),
# 'age': fields.char('Age'),
# 'salary': fields.float('Salary'),
# 'faculty': fields.text('faculty'),
#         'grade': fields.selection(grade, 'Grade'),
#         'graduation year': fields.selection(year, 'gryear'),
#         'info': fields.html('signature'),
#         'accepted': fields.boolean('accept'),
#         'department_id': fields.many2one('iti.department', string='department'),
#         'skills__ids': fields.many2many('iti.skills', string='skills'),
#         'state': fields.selection(state, 'status'),
#     }
#
#
# class iti_department(orm.Model):
#     _name = 'iti.department'
#     _columns = {
#         'name': fields.char('Name'),
#         'desc': fields.text('description'),
#         'student_ids': fields.one2many('iti.student', 'department_id', string='students'),
#         'allowed': fields.boolean(string='allowed'),
#     }
#
#
# class iti_skills(orm.Model):
#     _name = 'iti.skills'
#     _columns = {
#         'name': fields.char('skills'),
#         # 'departmentt__id': fields.many2one('iti.department', string='department'),
#     }
#
#
# # _inherit
# class hr_extend(orm.Model):
#     _inherit = 'hr.employee'
#     _columns = {
#         'emp_code': fields.char('Employee cod'),
#     }
#

class iti_catagory(orm.Model):
    _name = 'iti.catagory'
    _columns = {
        'name': fields.char('Name'),
        'cat_id': fields.integer('cat_id', required=True),
        'desc': fields.text('description'),
    }


class iti_subcatagory(orm.Model):
    _name = 'iti.subcatagory'
    _columns = {
        'name': fields.char('Name'),
        'subcat_id': fields.integer('subcat_id', required=True),
        'desc': fields.text('description'),
        'catagory_id': fields.many2one('iti.catagory', string='catagory'),
    }


class iti_subsubcatagory(orm.Model):
    _name = 'iti.subsubcatagory'
    _columns = {
        'name': fields.char('Name'),
        'subsubcat_id': fields.integer('subsubcat_id', required=True),
        'desc': fields.text('description'),
        'subcatagory_id': fields.many2one('iti.subcatagory', string='subcatagory'),
    }


################ Warehouse############
class iti_warehouse(orm.Model):
    _name = "iti.warehouse"

    _columns = {
        'name': fields.char('Store Name', required=True),
        'address': fields.char("Address"),
        # 'product_ids':fields.one2many('iti.product', string="Products"),
        'keeper_id': fields.many2one('res.users', "Keeper"),
        'manager_id': fields.many2one('res.users', "Manager"),
        'super_manager_id': fields.many2one('res.users', "Super Manager",
                                            domain="[('id','=','ref('iti.group_iti_warehouse_supermanager')')]"),
        # 'super_manager_id': fields.many2one('res.users', "Super Manager", domain="[('id','=','ref('ourwarehouse.group_iti_warehouse_supermanager')')]"),
    }


# class iti_store(orm.Model):
#
#     _name = "iti.store"
#     _columns = {
#         'name': fields.char('Store Name', required=True),
#         'location': fields.char('Store Location', required=True),
#         'products_ids': fields.many2many('iti.product', string='Products'),
#         'employees_ids': fields.one2many('iti.employee', 'store_id', string='Employees'),
#         # 'keeper_id': fields.many2one('res.users', "Keeper"),
#         # 'manager_id': fields.many2one('res.users', "Manager"),
#         # 'super_manager_id': fields.many2one('res.users', "Super Manager", domain="[('id','=','ref('ourwarehouse.group_iti_warehouse_supermanager')')]"),
#
#     }

class iti_supplier(orm.Model):
    _name = "iti.supplier"
    _columns = {
        'name': fields.char('Supplier Name', required=True),
        'mail': fields.char('Supplier E_mail'),
        'mobile': fields.char('Supplier Mobile'),
        'address': fields.char('Supplier Address'),
        'products_ids': fields.many2many('iti.product', 'products_suppliers', string='products'),
    }


class iti_product(orm.Model):
    _name = 'iti.product'

    def _calc_code(self, cr, uid, ids, name, arg, context=None):
        result = {}
        ids = self.search(cr, uid, [])

        products = self.browse(cr, uid, ids, context)
        for product in products:
            #if (product.catagory_id and product.subcatagory_id and product.subsubcatagory_id):
            result[product.id] = str(product.code) + " " + str(product.catagory_id.cat_id) + " " + str(
                product.subcatagory_id.subcat_id) + " " + str(product.subsubcatagory_id.subsubcat_id)

        return result


    def check_keeper(self, cr, uid, ids, field_name, arg, context):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            keeper_id = product.warehouse_id.keeper_id.id
        res[product.id] = (keeper_id == uid)
        return res


    def set_accepted(self, cr, uid, ids, context=None):
        pass


    _columns = {
        'name': fields.char('Name'),
        'price': fields.float('Price'),
        'amount': fields.integer('Amount'),
        'productdate': fields.date('Productdate'),
        'expirdate': fields.date('Expirdate'),
        'code': fields.integer('Code', size=2, required=True),
        'net_code': fields.function(_calc_code, string='Reference', method=True, type='char', store=True),
        'desc': fields.text('description'),
        'catagory_id': fields.many2one('iti.catagory', string='catagory'),
        'subcatagory_id': fields.many2one('iti.subcatagory', string='subcatagory'),
        'suppliers_ids': fields.many2many('iti.supplier', string="Suppliers"),
        'subsubcatagory_id': fields.many2one('iti.subsubcatagory', string='subsubcatagory'),
        'status': fields.selection(string="Status", selection=[
            ("new", "New"),
            ('used', "Used"),
            ('damaged', 'Damaged'),
        ]),
        'state': fields.selection(string="State", default='new', selection=[
            ('new', 'New'),
            ('recieved', 'Recieved'),
            ('underReview', 'Under Review'),
            ('approved', 'Approved'),
            ('keeperConfirm', 'Keeper Confirm'),
            ('managerConfirm', 'Manager Confirm'),
            ('inStock', 'In Stock'),
        ], readonly=True),
        'warehouse_id': fields.many2one('iti.warehouse', string='Warehouse'),
        'is_keeper': fields.function(check_keeper, type='boolean', store=False),
    }


class iti_search(orm.Model):
    _name = 'iti.search'

    ch = [('name', 'Name'), ('code', 'Code')]
    _columns = {
        'search': fields.char(string='Search', size=100),
        'change': fields.selection(ch, string='Search By', size=100),
        'result': fields.text(string='Results', size=500)}


    def func1(self, cr, uid, ids, search, change, context=None):

        record = self.pool.get('iti.product').search(cr, uid, [(change, '=', search)])
        record = self.pool.get('iti.product').read(cr, uid, record)
        if record:
            v = {'result': 'Name:' + str(record[0]['name']) + ',Status:' + str(record[0]['status'])
                           + ',Code:' + str(record[0]['net_code'])
                           + ',Quantity:' + str(record[0]['amount']) + ',Price:' + str(record[0]['price'])
                           + ',Description:' + str(record[0]['desc'])}

        else:
            v = {'result': ''}
        return {'value': v}


    ###### functions#######



    def product_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'new'})
        return True


    def product_recieved(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'recieved'})
        return True


    def product_underReview(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'underReview'})
        return True


    def product_approved(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'approved'})
        return True


    def product_keeper_confirm(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'keeperConfirm'})
        return True


    def product_manager_confirm(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'managerConfirm'})
        return True


    def product_in_stock(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'inStock'})
        return True
