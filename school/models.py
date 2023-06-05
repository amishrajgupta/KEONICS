from django.shortcuts import render,redirect,reverse,get_object_or_404
from datetime import timezone
from django.utils import timezone as django_timezone
from django.db import models
from django.contrib.auth.models import User
import razorpay
# Create your models here.

# razorpay_client = razorpay.Client(auth=('rzp_test_aLwq1HTCozbuy9', 'k1RXb3PPUf8uXoOHBVSLR2ID'))

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.CharField(max_length=20, default='created')
    def create_payment(request, order_id):
        order = Order.objects.get(id=order_id)
        if order.status == 'created':
            client = razorpay.Client(auth=('rzp_test_aLwq1HTCozbuy9', 'k1RXb3PPUf8uXoOHBVSLR2ID'))
            payment_data = {
                'amount': int(order.amount) * 100,
                'currency': 'INR',
                'receipt': str(order.id),
                'order_id': order.order_id,
                'notes': {
                    'name': order.name,
                    'email': order.email,
                }
            }
            response = client.order.create_payment(payment_data)

            return render(request, 'school/payment.html', {'order': order, 'response': response})

        return redirect('order_details', order_id=order.id)

    def __str__(self):
        return self.order_id

class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    email=models.EmailField(null=True)
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Others'),    
    )
    g_choices = models.CharField(max_length=20, choices=gender_choices,null=True)
    present_address=models.CharField(max_length=100,null=True)
    permanent_address=models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to='static/teacher_photos',null=True)
    state_choices=(
        ('andaman_nicobar_island','Andaman and Nicobar Island'),
        ('andhra_pradesh','Andhra Pradesh'),
        ('arunachal_pradesh','Arunachal Pradesh'),
        ('assam','Assam'),
        ('bihar','Bihar'),
        ('chandigarh','Chandigarh'),
        ('chhattisgarh','Chhattisgarh'),
        ('dadra_nagar_haveli','Dadra and Nagar Haveli'),
        ('daman_diu','Daman and Diu'),
        ('delhi','Delhi'),
        ('goa','Goa'),
        ('gujarat','Gujarat'),
        ('haryana','Haryana'),
        ('himachal_pradesh','Himachal Pradesh'),
        ('jammu_kashmir','Jammu and Kashmir'),
        ('jharkhand','Jharkhand'),
        ('karnataka','Karnataka'),
        ('kerala','Kerala'),
        ('lakshadweep','Lakshadweep'),
        ('madhya_pradesh','Madhya Pradesh'),
        ('maharashtra','Maharashtra'),
        ('manipur','Manipur'),
        ('meghalaya','Meghalaya'),
        ('mizoram','Mizoram'),
        ('nagaland','Nagaland'),
        ('odisha','Odisha'),
        ('puducherry','Puducherry'),
        ('punjab','Punjab'),
        ('rajasthan','Rajasthan'),
        ('sikkim','Sikkim'),
        ('tamil_nadu','Tamil Nadu'),
        ('telangana','Telangana'),
        ('tripura','Tripura'),
        ('uttar_pradesh','Uttar Pradesh'),
        ('uttarakhand','Uttarakhand'),
        ('west_bengal','West Bengal'),
    )
    state=models.CharField(max_length=40,choices=state_choices,null=True)
    district=models.CharField(max_length=40,null=True)  
    pin_code=models.CharField(max_length=40,null=True)  
    aadhar=models.FileField(upload_to='static/teacher_aadhar',null=True)
    degree=models.FileField(upload_to='static/teacher_degree',null=True)
    resume=models.FileField(upload_to='static/teacher_resume',null=True)
    course_choices=(('one','course1'),('two','course2'),('three','course3'),
('four','course4'),('five','course5'),('six','course6'),('seven','course7'),('eight','course8'),('nine','course9'),('ten','course10'))
    course=models.CharField(max_length=10,choices=course_choices,default='one')
    
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('one','course1'),('two','course2'),('three','course3'),
('four','course4'),('five','course5'),('six','course6'),('seven','course7'),('eight','course8'),('nine','course9'),('ten','course10')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    aadhaar=models.CharField(max_length=40,null=True)
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Others'),    
    )
    g_choices = models.CharField(max_length=20, choices=gender_choices,null=True)
    bgroup_choices = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    bg_choices = models.CharField(max_length=20, choices=bgroup_choices,null=True)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='static/franchise_photos',null=True)
    high_edu_quali_choices = (
        ('10th', '10th'),
        ('12th', '12th'),
        ('graduation', 'Graduation'),
        ('post_graduation', 'Post Graduation'),
        ('other', 'Other'),
    )
    high_edu_quali = models.CharField(max_length=20, choices=high_edu_quali_choices,null=True)
    occupation_choices = (
        ( 'govt_service', 'Govt. Service'),
        ('private_service', 'Private Service'),
        ('student', 'Student'),
        ('unemployed', 'Unemployed'),
        ('housewife', 'Housewife'),
    )
    occupation= models.CharField(max_length=20, choices=occupation_choices,null=True)
    category_choices=(
        ('general','General'),
        ('obc','OBC'),
        ('sc','SC'),
        ('st','ST'),
        ('minority','Minority'),
    )
    category= models.CharField(max_length=20, choices=category_choices,null=True)
    father_name=models.CharField(max_length=40,null=True)
    father_occupation=models.CharField(max_length=40,null=True)
    father_mobile=models.CharField(max_length=40,null=True)
    permanent_address=models.CharField(max_length=100,null=True)
    pin=models.CharField(max_length=40,null=True)
    district=models.CharField(max_length=40,null=True)
    state_choices=(
        ('andaman_nicobar_island','Andaman and Nicobar Island'),
        ('andhra_pradesh','Andhra Pradesh'),
        ('arunachal_pradesh','Arunachal Pradesh'),
        ('assam','Assam'),
        ('bihar','Bihar'),
        ('chandigarh','Chandigarh'),
        ('chhattisgarh','Chhattisgarh'),
        ('dadra_nagar_haveli','Dadra and Nagar Haveli'),
        ('daman_diu','Daman and Diu'),
        ('delhi','Delhi'),
        ('goa','Goa'),
        ('gujarat','Gujarat'),
        ('haryana','Haryana'),
        ('himachal_pradesh','Himachal Pradesh'),
        ('jammu_kashmir','Jammu and Kashmir'),
        ('jharkhand','Jharkhand'),
        ('karnataka','Karnataka'),
        ('kerala','Kerala'),
        ('lakshadweep','Lakshadweep'),
        ('madhya_pradesh','Madhya Pradesh'),
        ('maharashtra','Maharashtra'),
        ('manipur','Manipur'),
        ('meghalaya','Meghalaya'),
        ('mizoram','Mizoram'),
        ('nagaland','Nagaland'),
        ('odisha','Odisha'),
        ('puducherry','Puducherry'),
        ('punjab','Punjab'),
        ('rajasthan','Rajasthan'),
        ('sikkim','Sikkim'),
        ('tamil_nadu','Tamil Nadu'),
        ('telangana','Telangana'),
        ('tripura','Tripura'),
        ('uttar_pradesh','Uttar Pradesh'),
        ('uttarakhand','Uttarakhand'),
        ('west_bengal','West Bengal'),
    )
    state=models.CharField(max_length=40,choices=state_choices,null=True)
    aadhar = models.FileField(upload_to='static/aadhar/',null=True)
    has_aadhar = models.BooleanField(default=False)
    twel_marks = models.FileField(upload_to='static/12th_marks/',null=True)
    has_twel_marks = models.BooleanField(default=False)
    tenth_marks = models.FileField(upload_to='static/sslc_marks/',null=True)
    has_tenth_marks = models.BooleanField(default=False)
    degree= models.FileField(upload_to='static/degree/',null=True)
    has_degree = models.BooleanField(default=False)
    caste= models.FileField(upload_to='static/caste/',null=True)
    has_caste = models.BooleanField(default=False)
    others= models.FileField(upload_to='static/others/',null=True)
    has_others = models.BooleanField(default=False)
    ration= models.FileField(upload_to='static/ration/',null=True)
    has_ration = models.BooleanField(default=False)
    income= models.FileField(upload_to='static/income/',null=True)
    has_income = models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    
class FrenchiseExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    address=models.CharField(max_length=100,null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40,null=False)
    status=models.BooleanField(default=False)
    username=models.CharField(max_length=40)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=40)
    photo = models.ImageField(upload_to='static/franchise_photos',null=True)
    pin_code = models.CharField(max_length=40,null=True)
    state_choices=(
        ('andaman_nicobar_island','Andaman and Nicobar Island'),
        ('andhra_pradesh','Andhra Pradesh'),
        ('arunachal_pradesh','Arunachal Pradesh'),
        ('assam','Assam'),
        ('bihar','Bihar'),
        ('chandigarh','Chandigarh'),
        ('chhattisgarh','Chhattisgarh'),
        ('dadra_nagar_haveli','Dadra and Nagar Haveli'),
        ('daman_diu','Daman and Diu'),
        ('delhi','Delhi'),
        ('goa','Goa'),
        ('gujarat','Gujarat'),
        ('haryana','Haryana'),
        ('himachal_pradesh','Himachal Pradesh'),
        ('jammu_kashmir','Jammu and Kashmir'),
        ('jharkhand','Jharkhand'),
        ('karnataka','Karnataka'),
        ('kerala','Kerala'),
        ('lakshadweep','Lakshadweep'),
        ('madhya_pradesh','Madhya Pradesh'),
        ('maharashtra','Maharashtra'),
        ('manipur','Manipur'),
        ('meghalaya','Meghalaya'),
        ('mizoram','Mizoram'),
        ('nagaland','Nagaland'),
        ('odisha','Odisha'),
        ('puducherry','Puducherry'),
        ('punjab','Punjab'),
        ('rajasthan','Rajasthan'),
        ('sikkim','Sikkim'),
        ('tamil_nadu','Tamil Nadu'),
        ('telangana','Telangana'),
        ('tripura','Tripura'),
        ('uttar_pradesh','Uttar Pradesh'),
        ('uttarakhand','Uttarakhand'),
        ('west_bengal','West Bengal'),
    )
    state=models.CharField(max_length=40,choices=state_choices,null=True)
    district=models.CharField(max_length=40,null=True)
    city=models.CharField(max_length=40,null=True)
    # payment_id = models.CharField(max_length=100, null=True, blank=True)
    # def initiate_payment(self, amount):
    #     amount_in_paise = amount * 100  # Convert the amount to paise
    #     data = {
    #         'amount': amount_in_paise,
    #         'currency': 'INR',
    #         'payment_capture': '1',
    #     }

    #     payment = razorpay_client.order.create(data=data)
    #     self.payment_id = payment['id']
    #     self.save()
    #     return payment
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)

