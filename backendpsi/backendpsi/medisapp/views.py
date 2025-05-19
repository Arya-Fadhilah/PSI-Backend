from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.serializers import MCUrecordSerializer
from .models import MCURecord
from .models import Patient, MCURecord
from .forms import TambahForm

@login_required
def pasien(request):
    mypasien = Patient.objects.all()
    template = loader.get_template('medisapp/pasien.html')
    context = {
        'mypasien': mypasien,
    }
    return HttpResponse(template.render(context, request))


@login_required
def mcurecord(request):
    if request.method == "POST":
        id_pasien = request.POST.get('patient_id')
        patient = get_object_or_404(Patient, patient_id=id_pasien)
        mcu_records = MCURecord.objects.filter(patient=patient).order_by('-timestamp')

        if  request.POST.get('pk') != None:
            history_mcu= mcu_records.get(pk=request.POST.get('pk'))
        else:
            history_mcu = mcu_records.first()

        return render(request, 'medisapp/mcu_pasien.html', {
            'patient': patient,
            'mcu_records': mcu_records,
            'latest_mcu_record': history_mcu
        })
    
    return render(request, 'medisapp/pasien.html')


@login_required
def tambah(request):
    if request.method == 'POST':
        form = TambahForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('pasien')  # Redirect to a success page
    else:
        form = TambahForm()

    return render(request, 'medisapp/tambah.html', {'form': form})


def edit(request):
    if request.method == 'POST':
        id_pasien = request.POST.get('patient_id')
        patient = get_object_or_404(Patient, patient_id=id_pasien)
        form = TambahForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('pasien')  # Redirect to a success page
    else:
        form = TambahForm(instance=patient)

    return render(request, 'medisapp/edit.html', {'form': form,
                                                    'patient':patient})


def delete(request):
    if request.method == "POST":
        id_pasien = request.POST.get('patient_id')
        patient = get_object_or_404(Patient, patient_id=id_pasien)  # pastikan ini sesuai ID pasien
        patient.delete()
        return redirect('pasien')
    else:
        return HttpResponse(status=405, content="Method not allowed!")

@api_view(['POST'])
def update_sensor_data(request):
    if request.method == 'POST':
        serializer = MCUrecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response({'message': 'Sensor data updated successfully'}, status=200)
        return Response(serializer.errors, status=400)

