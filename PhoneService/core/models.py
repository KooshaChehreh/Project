from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils import timezone


class BaseManager(models.Manager):
    """ This class will set some queries on each model to get the deleted items,
        the activated/deactivated items... of a model."""

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


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = BaseManager()

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Deleted Datetime",
        help_text="This is deleted datetime"
    )

    restored_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name='Restored Datetime',
        help_text='This is Restored Datetime'
    )

    is_deleted = models.BooleanField(
        default=False,
        editable=False,
        db_index=True,
        verbose_name="Deleted status",
        help_text="This is deleted status",
    )

    is_active = models.BooleanField(
        default=True,
        editable=False,
        verbose_name="Active status",
        help_text="This is active status",
    )

    def deleter(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save(using=using)

    def restore(self):
        self.restored_at = timezone.now()
        self.is_deleted = False
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()

# class UserCustomManager(UserManager):
#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields = {'is_staff': True, 'is_superuser': True, **extra_fields}
#         if not extra_fields['phone']:
#             raise ValueError("Phone number is needed, please enter your phone number.")
#         else:
#             username = extra_fields['phone']
#             user = self.create_user(username=username, **extra_fields)
#             return user
#
#     def create_user(self, username, email=None, password=None, **extra_fields):
#         extra_fields = {'is_staff': False, 'is_superuser': False, **extra_fields}
#         if not email:
#             user = self.create_user(username=username, **extra_fields)
#         else:
#             user = self.create_user(username=email, **extra_fields)
#         return user


# u = UserCustomManager()
# print(u.create_superuser('koosha'))
