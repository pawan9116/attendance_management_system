from django.db import models

class Semester(models.Model):
	CHOICES = (
			(1, 'First'),
			(2, 'Second'),
			(3, 'Third'),
			(4, 'Fourth'),
			(5, 'Fifth'),
			(6, 'Sixth'),
			(7, 'Seventh'),
			(8, 'Eigth')
		)

	semester = models.IntegerField(default = 0, choices=CHOICES)

	def __str__(self):
		return str(self.semester)

class Department(models.Model):
	department = models.CharField(max_length=100)

	def __str__(self):
		return self.department