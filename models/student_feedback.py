from odoo import models, api, fields

class StudentFeedback(models.Model):
    _name = "student.feedback"
    _description = "Student Feedback"
    student_name = fields.Char('Student Name')
    mobile = fields.Char('Mobile')
    counsellor = fields.Char('Student Counsellor')
    purpose = fields.Char('Purpose of Visit')
    rating = fields.Selection(selection=[('0','No rating'),('1','Extremely Disappointed'),('2','Unsatisfied'),('3','Informative'),('4','Satisfied'),('5','Very Satisfied')], string="Rating")
    message = fields.Text(string = "Message")