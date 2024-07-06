from django.db import models

class Vacancy(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    employer_name = models.CharField(max_length=255)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title