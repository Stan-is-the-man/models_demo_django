from datetime import date
from django.db import models
from django.urls import reverse

from models_demo.web.validators import validate_after_today, validate_over_18_years_old


# ABSTRACT CLASS:
#   1. Does not create a table
#   2. Can be inherited
class AuditInfoMixin(models.Model):
    # makes the class ABSTRACT
    class Meta:
        abstract = True

    # automatically set date/time on creation
    created_on = models.DateTimeField(
        auto_now_add=True,
    )  # this is optional

    # automatically set date/time on each save/update
    updated_on = models.DateTimeField(auto_now=True, )


# model for Foreign key to point to:
# SLUGS
class Department(models.Model):
    name = models.CharField(max_length=20)
    year_established = models.DateField

    # SLUGs - for SEO crawlers
    # slug = models.SlugField(
    #     unique=True,
    # )

    # How to be represented in admin site
    def __str__(self):
        return self.name

    # return a calculated(clickable) url for the object - make func, url and html
    def get_absolute_url(self):
        url = reverse('details department', kwargs={
            'pk': self.pk,
        })

        return url


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=20)
    code_name = models.CharField(
        max_length=20,
        unique=True,
    )
    deadline = models.DateField()

    # How to be represented in admin site
    def __str__(self):
        return self.name


# class Meta - verbose_name for any name you want in admin(or plurals)
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Power train"

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Vehicles(AuditInfoMixin, models.Model):
    brand = models.CharField(max_length=15)
    modification = models.CharField(max_length=15)
    # Validator
    year_of_production = models.DateField(null=True)
    horse_powers = models.PositiveIntegerField(null=True)
    is_hybrid = models.BooleanField(null=True)

    # FK to Category
    to_category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    def __str__(self):
        whole_name = self.brand + ' ' + self.modification
        return whole_name


class Employee(AuditInfoMixin, models.Model):
    # Gives extra information
    # It is default sorting, that can be override in views(9 row) by .order()
    class Meta:
        # sort age-asc, (-age) - desc IN ' '
        ordering = ('first_name', '-age',)

    first_name = models.CharField(max_length=40, )
    last_name = models.CharField(max_length=40, null=True)
    years_of_experience = models.PositiveIntegerField()
    review = models.TextField()

    # VALIDATORS - from validators.py
    start_date = models.DateField(
        null=True,
        validators=(validate_after_today,)
    )
    age = models.PositiveIntegerField(
        default=0,
        validators=(validate_over_18_years_old,)
    )

    # Foreign key many to one/one to many
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    own_vehicle_brand = models.ForeignKey(
        Vehicles,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # Foreign key many to many
    projects = models.ManyToManyField(
        Project,
        # to go through that table
        # through='EmployeeProject',
        # in '' so it can reach it, because the class(model) is after this statement
    )

    # The property method does not apply in the DB, use it just as a dynamic value
    # DO NOT CREATE Fields here- FKs !!!
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    # The property method does not apply in the DB, use it just as a dynamic value
    # DO NOT CREATE Fields here- FKs !!!
    @property
    def years_of_employment(self):
        return date.today() - self.start_date

    # Can be viewed in admin site
    # self.id = self.pk
    def __str__(self):
        return f"Employee ID:{self.pk} with name: {self.fullname}"


# FK one to one
class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True
    )


# # Model for FK many to many to go through:
class EmployeeProject(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT,
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
    )
    date_joined = models.DateField(
        auto_now_add=True,
    )
