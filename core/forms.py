from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach

from core.utils.number_converter import bangla_to_english

from .models import HeroOverview, FAQ, SiteSetting, Message




# custom form for translate number 
class BanglaDecimalField(forms.DecimalField):

    def to_python(self, value):

        value = bangla_to_english(value)

        return super().to_python(value)
    


class HeroOverviewForm(forms.ModelForm):
    class Meta:
        model = HeroOverview
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'


class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        # self.fields['category'].empty_label = 'Select Category'
