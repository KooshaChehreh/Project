from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Logical delete, base manager
    class Meta:
        abstract = True


# BaseManager :
class BaseManager(models.Manager):

    """ This class will set some queries on each model to get the deleted items
        , the activated/deactivated items ... of a model."""

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    # define method for access all queryset
    def get_archive(self):
        return super().get_queryset()

    # define method for access all active query
    def get_active_list(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    # define deleted item for easy access data
    def get_deleted_list(self):
        return super().get_queryset().filter(is_deleted=True)

    # define deactivate item
    def get_deactivate_list(self):
        return self.get_queryset().filter(is_active=False)
