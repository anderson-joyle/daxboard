from django.db import models

# Create your models here.
class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Access(Common):
    resource = models.URLField(max_length=256, blank=False)
    tenant = models.CharField(max_length=50, blank=False)
    success = models.BooleanField(default=False)

    def __str__(self):
        return '{0} ({1}...)'.format(self.tenant, self.resource[:20])