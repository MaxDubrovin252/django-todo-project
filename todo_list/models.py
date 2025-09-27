from django.db import models

class Todo(models.Model):
    class Meta:
        verbose_name = "Todo Item"
        
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
