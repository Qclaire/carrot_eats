from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    permissions = models.ManyToManyField('auth.Permission')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'role'
