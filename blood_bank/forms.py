from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach

from .models import BloodDonor


class BloodDonorForm(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = ['name', 'mobile', 'blood_group', 'address', 'photo', 'last_donated']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'আপনার নাম লিখুন'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'মোবাইল নাম্বার'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ঠিকানা লিখুন'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'last_donated': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ✅ Remove ----- and set custom placeholder
        self.fields['blood_group'].choices = [('', 'রক্তের গ্রুপ নির্বাচন করুন')] + list(self.fields['blood_group'].choices)








# class BloodDonorForm(forms.ModelForm):
#     class Meta:
#         model = BloodDonor
#         fields = ['name', 'mobile', 'blood_group', 'address', 'photo', 'last_donated']
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save'))
#         self.fields['blood_group'].empty_label = 'Select blood_group'




# from django import forms
# from .models import BloodDonor


# class BloodDonorForm(forms.ModelForm):
#     class Meta:
#         model = BloodDonor
#         fields = ['name', 'mobile', 'blood_group', 'address', 'photo', 'last_donated']

