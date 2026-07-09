from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach




from core.utils.number_converter import (
    bangla_to_english,
    english_to_bangla,
)

from core.forms import  BanglaDecimalField

from .models import Doctor

from .models import Hospital, Specialization, Doctor, DoctorSchedule






class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'


class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'



class DoctorForm(forms.ModelForm):
    # consultation_fee = BanglaDecimalField(max_digits=10, decimal_places=2)

    consultation_fee = BanglaDecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            # "placeholder": "৫৬০",
        }),
    )

    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            # 'hospitals': forms.CheckboxSelectMultiple,
            'specializations': forms.CheckboxSelectMultiple,
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.fields['department'].empty_label = 'Select Department'

        if self.instance.pk and self.instance.consultation_fee:

            self.initial["consultation_fee"] = english_to_bangla(
                self.instance.consultation_fee
            )







class DoctorScheduleForm(forms.ModelForm):
    class Meta:
        model = DoctorSchedule
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['doctor'].empty_label = 'Select Doctor'
        self.fields['day_of_week'].empty_label = 'Select Day'

