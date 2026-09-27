from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Zone(BaseModel):
    location = models.CharField(max_length=255)
    visitors = models.IntegerField(default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.location


class Visitors(BaseModel):
    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name='zone_visitors'
    )
    name = models.CharField(max_length=100)
    information = models.TextField()
    is_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name