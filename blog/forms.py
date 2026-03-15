from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# import bleach

from .models import Blog, BlogCategory



# BlogCategory Form 
class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))



# Blog Form 
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.fields['category'].empty_label = 'Select Category'
        # self.fields['slug'].label = "URL Slug"
        # self.fields['slug'].widget.attrs['placeholder'] = "auto-generated or manually editable"


    # def clean_slug(self):
    #     slug = self.cleaned_data['slug']
    #     qs = Discipline.objects.filter(slug=slug)
    #     if self.instance.pk:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError("This slug is already taken.")
    #     return slug



