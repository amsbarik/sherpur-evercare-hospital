
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


from .models import Appointment
from doctor.models import Doctor


# import bleach



# class AppointmentForm(forms.ModelForm):
#     schedule = forms.ChoiceField(choices=[], required=True)

#     class Meta:
#         model = Appointment
#         fields = [
#             'patient_name',
#             'patient_phone',
#             'patient_email',
#             'department',
#             'doctor',
#             'appointment_date',
#             'appointment_time',
#             'notes',
#         ]
#         widgets = {
#             'appointment_date': forms.DateInput(attrs={'type': 'date'}),
#             'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields['doctor'].queryset = Doctor.objects.none()

#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('patient_name', css_class='col-md-6'),
#                 Column('patient_phone', css_class='col-md-6'),
#             ),
#             Row(
#                 Column('patient_email', css_class='col-md-6'),
#                 Column('department', css_class='col-md-6'),
#             ),
#             Row(
#                 Column('doctor', css_class='col-md-6'),
#                 Column('schedule', css_class='col-md-6'),
#             ),
#             Row(
#                 Column('appointment_date', css_class='col-md-6'),
#                 Column('appointment_time', css_class='col-md-6'),
#             ),
#             'notes',
#             Submit('submit', 'Book Appointment')
#         )






# class AppointmentForm(forms.ModelForm):
#     schedule = forms.ChoiceField(choices=[], required=True)

#     class Meta:
#         model = Appointment
#         fields = [
#             'patient_name',
#             'patient_phone',
#             'patient_email',
#             'department',
#             'doctor',
#             'appointment_date',
#             'notes',
#         ]
#         widgets = {
#             'appointment_date': forms.DateInput(attrs={'type': 'date'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields['doctor'].queryset = Doctor.objects.none()

#         if 'department' in self.data:
#             try:
#                 department_id = int(self.data.get('department'))
#                 self.fields['doctor'].queryset = Doctor.objects.filter(
#                     department_id=department_id,
#                     is_available=True
#                 )
#             except (ValueError, TypeError):
#                 pass

#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('patient_name', css_class='col-md-6'),
#                 Column('patient_phone', css_class='col-md-6'),
#             ),
#             Row(
#                 Column('patient_email', css_class='col-md-6'),
#                 Column('department', css_class='col-md-6'),
#             ),
#             Row(
#                 Column('doctor', css_class='col-md-6'),
#                 Column('schedule', css_class='col-md-6'),
#             ),
#             'appointment_date',
#             'notes',
#             Submit('submit', 'Book Appointment')
#         )







# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column, Submit

# from .models import Appointment, Doctor, DoctorSchedule


# class AppointmentForm(forms.ModelForm):
#     schedule = forms.ChoiceField(
#         choices=[],
#         required=True,
#         label="Available Schedule"
#     )

#     class Meta:
#         model = Appointment
#         fields = [
#             'patient_name',
#             'patient_phone',
#             'patient_email',
#             'department',
#             'doctor',
#             'appointment_date',
#             'notes',
#         ]
#         widgets = {
#             'appointment_date': forms.DateInput(attrs={'type': 'date'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.fields['doctor'].queryset = Doctor.objects.none()
#         self.fields['schedule'].choices = [('', 'Select Schedule')]

#         department_id = self.data.get('department')
#         doctor_id = self.data.get('doctor')

#         if department_id:
#             self.fields['doctor'].queryset = Doctor.objects.filter(
#                 department_id=department_id,
#                 is_available=True
#             )

#         if doctor_id:
#             schedules = DoctorSchedule.objects.filter(doctor_id=doctor_id)

#             self.fields['schedule'].choices += [
#                 (
#                     schedule.id,
#                     f"{schedule.day_of_week}: {schedule.start_time} - {schedule.end_time}"
#                 )
#                 for schedule in schedules
#             ]

#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.layout = Layout(
#             Row(
#                 Column('patient_name', css_class='col-md-6'),
#                 Column('patient_phone', css_class='col-md-6'),
#             ),
#             Row(
#                 Column('patient_email', css_class='col-md-6'),
#                 Column('department', css_class='col-md-6'),
#             ),
#             Row(
#                 Column('doctor', css_class='col-md-6'),
#                 Column('schedule', css_class='col-md-6'),
#             ),
#             'appointment_date',
#             'notes',
#             Submit('submit', 'Book Appointment')
#         )


















