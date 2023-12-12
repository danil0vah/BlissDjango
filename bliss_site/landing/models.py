from django.db import models

class ToursView(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=False)
    is_realised = models.BooleanField()
