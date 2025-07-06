from django.contrib import admin
from . import models


@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    ordering = ("iso",)


@admin.register(models.TherapistProfile)
class TherapistProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    pass
