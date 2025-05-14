from django.db import models
from django.utils import timezone
from datetime import date


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    birth_date = models.DateField(verbose_name="Дата рождения")

    phone = models.CharField(max_length=15, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def age(self):
        return int((date.today() - self.birth_date).days / 365.25)


class Diagnosis(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование диагноза")

    def __str__(self):
        return self.name


class RehabilitationRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True, verbose_name="Диагноз")

    rehab_start = models.DateField(verbose_name="Дата начала реабилитации")
    rehab_end = models.DateField(verbose_name="Дата окончания реабилитации", null=True, blank=True)

    has_complications = models.BooleanField(default=False, verbose_name="Наличие осложнений")
    complication_details = models.TextField(blank=True, verbose_name="Подробности осложнений")

    notes = models.TextField(blank=True, verbose_name="Дополнительные заметки")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Реабилитация {self.patient} — {self.diagnosis}'
