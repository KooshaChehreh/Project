from django.db import models
from django.contrib.auth.models import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #TODO: Logical delete, base manager
    class Meta:
        abstract = True


