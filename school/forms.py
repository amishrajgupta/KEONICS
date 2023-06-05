from django import forms
from django.contrib.auth.models import User
from . import models
from tempus_dominus.widgets import DatePicker
from .models import Order

#for order
class OrderForm(forms.ModelForm):
    amount = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Amount'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = Order
        fields = ['amount', 'name', 'email']

#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

#for frenchise
class FrenchiseUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','password']

class FrenchiseExtraForm(forms.ModelForm):
    class Meta:
        model=models.FrenchiseExtra
        fields=['salary','address','mobile','status','email']

#for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['roll','cl','mobile','fee','status','aadhaar','g_choices','bg_choices','date_of_birth','photo','high_edu_quali','state','pin','occupation','category','father_name','father_occupation','father_mobile','permanent_address','district','aadhar','has_aadhar','twel_marks','has_twel_marks','tenth_marks','has_tenth_marks','degree','has_degree','caste','has_caste','others','has_others','ration','has_ration','income','has_income']
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker'}),
        }


#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','password']
class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['salary','mobile','status','email','g_choices','present_address','permanent_address','photo','district','state','pin_code','aadhar','degree','resume','course']




#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()




#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'



#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        # Here make some changes such as:
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

