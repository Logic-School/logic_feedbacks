from odoo import models, api, fields

class StudentFeedback(models.Model):
    _name = "student.feedback"
    _description = "Student Feedback"
    def _compute_name(self):
            for record in self:
                zeroes = "0"*(5 - len(str(record.id)))
                record.name = "FD"+zeroes+str(record.id)
    name = fields.Char(string="Name",compute="_compute_name")

    student_name = fields.Char('Student Name')
    mobile = fields.Char('Mobile')
    counsellor = fields.Many2one('hr.employee',string='Student Counsellor')
    purpose = fields.Char('Purpose of Visit')
    rating = fields.Selection(selection=[('0','No rating'),('1','Extremely Disappointed'),('2','Unsatisfied'),('3','Informative'),('4','Satisfied'),('5','Very Satisfied')], string="Rating")
    message = fields.Text(string = "Message")