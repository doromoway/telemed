from django import forms
from .models import Patient, Diagnosis, RehabilitationRecord


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'phone', 'email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['name']


class RehabilitationRecordForm(forms.ModelForm):
    class Meta:
        model = RehabilitationRecord
        fields = [
            'patient', 'diagnosis', 'rehab_start', 'rehab_end',
            'has_complications', 'complication_details', 'notes'
        ]
        widgets = {
            'rehab_start': forms.DateInput(attrs={'type': 'date'}),
            'rehab_end': forms.DateInput(attrs={'type': 'date'}),
            'complication_details': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Делаем поле подробностей обязательным, если есть осложнения
        self.fields['complication_details'].required = False

    def clean(self):
        cleaned_data = super().clean()
        has_complications = cleaned_data.get('has_complications')
        details = cleaned_data.get('complication_details')

        if has_complications and not details:
            self.add_error('complication_details', "Укажите подробности осложнений, если они есть.")
