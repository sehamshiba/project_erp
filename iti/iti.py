from openerp.osv import orm, fields


class iti_students(orm.Model):
    def change_department(self, cr, uid, skills__ids, context=None):
        department = self.pool.get('iti.department').browse(cr, uid, skills__ids),

        return department

    _name = 'iti.student'
    grade = [('g', 'good'), ('vg', 'very good'), ('ex', 'exellent')]
    year = [('f', '2012'), ('s', '2013'), ('l', '2014')]
    state = [('applied', 'Applied'), ('accepted', 'Accepted')]

    def dep_domain(self, cr, uid, ids, grade, context=None):
        # g_ids = self.pool.get('iti.department').search(cr, uid, [('allowed', '=', True)])
        # vg_ids = self.pool.get('iti.department').search(cr, uid, [])
        # if grade == 'vg' or grade == 'ex':
        # domain_ids = vg_ids
        # else:
        # domain_ids = g_ids

        # return {'domain': {'department_id': [('id', 'in', domain_ids)]}}

        if grade == 'g':
            domain = [('allowed', '=', True)]
        else:
            domain = []
        return {
            'domain': {'department_id': domain}}

    def set_accepted(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'accepted'})

    _columns = {
        'img': fields.binary('image'),
        'name': fields.text('Name'),
        'age': fields.char('Age'),
        'salary': fields.float('Salary'),
        'faculty': fields.text('faculty'),
        'grade': fields.selection(grade, 'Grade'),
        'graduation year': fields.selection(year, 'gryear'),
        'info': fields.html('signature'),
        'accepted': fields.boolean('accept'),
        'department_id': fields.many2one('iti.department', string='department'),
        'skills__ids': fields.many2many('iti.skills', string='skills'),
        'state': fields.selection(state, 'status'),
    }


class iti_department(orm.Model):
    _name = 'iti.department'
    _columns = {
        'name': fields.char('Name'),
        'desc': fields.text('description'),
        'student_ids': fields.one2many('iti.student', 'department_id', string='students'),
        'allowed': fields.boolean(string='allowed'),
    }


class iti_skills(orm.Model):
    _name = 'iti.skills'
    _columns = {
        'name': fields.char('skills'),
        # 'departmentt__id': fields.many2one('iti.department', string='department'),
    }


# _inherit
class hr_extend(orm.Model):
    _inherit = 'hr.employee'
    _columns = {
        'emp_code': fields.char('Employee cod'),
    }


class iti_catagory(orm.Model):
    _name = 'iti.catagory'
    _columns = {
        'name': fields.char('Name'),
        'cat_id': fields.char('cat_id'),
        'desc': fields.text('description'),
    }
class iti_subcatagory(orm.Model):
    _name = 'iti.subcatagory'
    _columns = {
        'name': fields.char('Name'),
        'desc': fields.text('description'),
        'catagory_id': fields.many2one('iti.catagory', string='catagory'),
    }

class iti_subsubcatagory(orm.Model):
    _name = 'iti.subsubcatagory'
    _columns = {
        'name': fields.char('Name'),
        'desc': fields.text('description'),
        'subcatagory_id': fields.many2one('iti.subcatagory', string='subcatagory'),
    }

class iti_product(orm.Model):
    _name = 'iti.product'
    _columns = {
        'name': fields.char('Name'),
        'desc': fields.text('description'),
        'catagory_id': fields.many2one('iti.catagory', string='catagory'),
        'subcatagory_id': fields.many2one('iti.subcatagory', string='subcatagory'),
        'subsubcatagory_id': fields.many2one('iti.subsubcatagory', string='subsubcatagory'),
    }