from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    menu_name = models.CharField(max_length=255, default='default')

    def __str__(self):
        return self.title