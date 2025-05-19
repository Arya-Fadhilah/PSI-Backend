from django.db import models

# Model untuk Pasien
class Patient(models.Model):
    SEX = [
        (0,'Laki-laki'),
        (1,'Perempuan')
    ]
    nama_pasien = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.PositiveSmallIntegerField(choices=SEX)
    phone_number = models.CharField(max_length=15, help_text="nomor telpon indonesia")
    alamat = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.patient_id}: {self.nama_pasien}"

class MCURecord(models.Model):
    DEHIDRASI = [
        (0, 'Dehidrasi'),
        (1, 'Cukup'),
        (2, 'Baik')
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="mcu_records")
    timestamp = models.DateTimeField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    urine_color = models.PositiveSmallIntegerField(choices=DEHIDRASI)
    alcohol_level = models.DecimalField(max_digits=5, decimal_places=2)
    body_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.timestamp}: {self.patient_id}"



