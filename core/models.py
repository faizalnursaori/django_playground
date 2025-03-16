from django.db import models
from .utils import generate_id

class BaseModel(models.Model):
    id = models.CharField(primary_key=True, default=generate_id, editable=False, max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
        