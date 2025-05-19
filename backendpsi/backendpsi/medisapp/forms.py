# forms.py
from django import forms
from .models import Patient

BIRTH_YEAR_CHOICES = [y for y in range(1980, 2026)]


class TambahForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            'nama_pasien' : forms.TextInput(),
            'date_of_birth' : forms.SelectDateWidget(
                years=BIRTH_YEAR_CHOICES),
            'sex': forms.RadioSelect(attrs={
                 'class' : 'radio-group'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': "Example: 08XX XXXX XXXX"
            }),
            'alamat' : forms.TextInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the empty "-----" choice
        allowed_values = [0, 1]
        self.fields['sex'].choices = [
            choice for choice in self.fields['sex'].choices if choice[0] in allowed_values
        ]
    