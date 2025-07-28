from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EmployeeAsset(models.Model):
    _name = 'employee.asset'
    _description = 'Employee Asset'

    name = fields.Char(string="Asset Name", required=True)
    asset_type = fields.Selection([
        ('laptop', 'Laptop'),
        ('phone', 'Phone'),
        ('id_card', 'ID Card'),
        ('other', 'Other'),
    ], string="Asset Type", required=True)
    serial_number = fields.Char(string="Serial Number", required=True)
    purchase_date = fields.Date(string="Purchase Date")
    condition = fields.Selection([
        ('new', 'New'),
        ('good', 'Good'),
        ('repair', 'Needs Repair'),
        ('broken', 'Broken'),
    ], string="Condition", default="new")
    employee_id = fields.Many2one('hr.employee', string="Assigned Employee")
    assignment_date = fields.Date(string="Assignment Date")
    return_date = fields.Date(string="Return Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('assigned', 'Assigned'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
    ], string="Status", default='draft', tracking=True)

    _sql_constraints = [
        ('unique_serial_number', 'unique(serial_number)', 'Serial Number must be unique!')
    ]

    def action_assign(self):
        for record in self:
            if record.state == 'assigned':
                raise ValidationError(_("Asset is already assigned."))
            if not record.employee_id:
                raise ValidationError(_("Please assign an employee before assigning the asset."))
            record.state = 'assigned'
            record.assignment_date = fields.Date.today()

    def action_return(self):
        for record in self:
            record.state = 'returned'
            record.return_date = fields.Date.today()

    def action_mark_lost(self):
        for record in self:
            record.state = 'lost'
