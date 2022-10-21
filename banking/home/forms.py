from pyexpat import model
from django import forms
from . models import *
from django.urls import reverse_lazy


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = form_register
        fields = '__all__'
        
        widgets = {
           'DOB' : DateInput(),
           'district': forms.Select(attrs={'id': 'district', 'class': 'form-control'}),
           'branch': forms.Select(attrs={'id': 'branch', 'class': 'form-control',
                                              'branch-queries-url': reverse_lazy('ajax-load-branch')}),
        }
    def __init__(self, *args, **kwargs ):
        super(BookingForm,self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['DOB'].label = "Date of birth"
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')




       