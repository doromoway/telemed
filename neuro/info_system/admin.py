from django.contrib import admin
from .models import Patient, Diagnosis, RehabilitationRecord


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'gender', 'birth_date', 'age', 'phone', 'email', 'created_at')
    search_fields = ('last_name', 'first_name', 'email', 'phone')
    list_filter = ('gender', 'created_at')
    ordering = ('last_name',)

    readonly_fields = ('age', 'created_at')


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(RehabilitationRecord)
class RehabilitationRecordAdmin(admin.ModelAdmin):
    list_display = (
        'patient', 'diagnosis', 'rehab_start', 'rehab_end', 'has_complications', 'created_at'
    )
    list_filter = ('has_complications', 'rehab_start', 'rehab_end')
    search_fields = ('patient__last_name', 'diagnosis__name')
    autocomplete_fields = ('patient', 'diagnosis')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('patient', 'diagnosis', 'rehab_start', 'rehab_end')
        }),
        ('Осложнения', {
            'fields': ('has_complications', 'complication_details'),
            'classes': ('collapse',),
        }),
        ('Дополнительно', {
            'fields': ('notes', 'created_at'),
        }),
    )
