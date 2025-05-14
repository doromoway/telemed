from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient, Diagnosis, RehabilitationRecord
from .forms import PatientForm, DiagnosisForm, RehabilitationRecordForm



from django.shortcuts import render, redirect
from .models import Patient, Diagnosis, RehabilitationRecord
from .forms import PatientForm, DiagnosisForm, RehabilitationRecordForm


def dashboard_view(request):
    patients = Patient.objects.all()
    rehab_records = RehabilitationRecord.objects.select_related('patient', 'diagnosis')

    if request.method == 'POST':
        if 'first_name' in request.POST:  # добавление пациента
            patient_form = PatientForm(request.POST)
            if patient_form.is_valid():
                patient_form.save()
                return redirect('dashboard')
        elif 'name' in request.POST:  # добавление диагноза
            diagnosis_form = DiagnosisForm(request.POST)
            if diagnosis_form.is_valid():
                diagnosis_form.save()
                return redirect('dashboard')
        elif 'rehab_start' in request.POST:  # добавление записи реабилитации
            record_form = RehabilitationRecordForm(request.POST)
            if record_form.is_valid():
                record_form.save()
                return redirect('dashboard')
    else:
        patient_form = PatientForm()
        diagnosis_form = DiagnosisForm()
        record_form = RehabilitationRecordForm()

    return render(request, 'info_system/dashboard.html', {
        'patients': patients,
        'rehab_records': rehab_records,
        'PatientForm': patient_form,
        'DiagnosisForm': diagnosis_form,
        'RehabilitationRecordForm': record_form,
    })



def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пациент успешно добавлен')
        else:
            print("Ошибки формы пациента:", form.errors)
            messages.error(request, 'Ошибка при добавлении пациента')
    return redirect('dashboard')



def add_diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Диагноз успешно добавлен')
        else:
            messages.error(request, 'Ошибка при добавлении диагноза')
    return redirect('dashboard')



def add_rehabilitation_record(request):
    if request.method == 'POST':
        form = RehabilitationRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Реабилитационная запись добавлена')
        else:
            print("Ошибки формы реабилитации:", form.errors)
            messages.error(request, 'Ошибка при добавлении записи')
    return redirect('dashboard')



def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    rehab_records = RehabilitationRecord.objects.filter(patient=patient).select_related('diagnosis').order_by('-rehab_start')

    context = {
        'patient': patient,
        'rehab_records': rehab_records,
    }
    return render(request, 'info_system/patient_detail.html', context)
