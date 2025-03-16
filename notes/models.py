from django.db import models
from core.models import BaseModel
# Create your models here.
class Notes(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    