from django.contrib import admin

from models_demo.web.models import Employee, Department, Project, Vehicles, Category


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # CUSTOMIZATIONS:
    # make columns for each class attribute
    list_display = (
        'pk', 'id', 'first_name', 'last_name', 'department',
        'years_of_experience', 'age', 'start_date','own_vehicle_brand',
    )

    # ADD/Change page - group attr fields in separate sections for:
    fieldsets = (
        ('Personal Info',
         {'fields': ('first_name', 'last_name', 'age', 'start_date')}),

        ('Professional Info',
         {'fields': ('department', 'years_of_experience', 'own_vehicle_brand')},)
    )

    # make filter aside for the certain attribute/s -better look
    list_filter = ('years_of_experience', 'age',)

    # search field
    search_fields = ('last_name',)


@admin.register(Vehicles)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand',
                    'modification',
                    'year_of_production',
                    'horse_powers',
                    'is_hybrid', 'to_category',
                    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
