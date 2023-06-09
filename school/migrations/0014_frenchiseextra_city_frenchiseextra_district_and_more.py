# Generated by Django 4.2.1 on 2023-05-20 18:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20230510_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='frenchiseextra',
            name='city',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='frenchiseextra',
            name='district',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='frenchiseextra',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='frenchiseextra',
            name='photo',
            field=models.ImageField(null=True, upload_to='static/franchise_photos'),
        ),
        migrations.AddField(
            model_name='frenchiseextra',
            name='pin_code',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='frenchiseextra',
            name='state',
            field=models.CharField(choices=[('andaman_nicobar_island', 'Andaman and Nicobar Island'), ('andhra_pradesh', 'Andhra Pradesh'), ('arunachal_pradesh', 'Arunachal Pradesh'), ('assam', 'Assam'), ('bihar', 'Bihar'), ('chandigarh', 'Chandigarh'), ('chhattisgarh', 'Chhattisgarh'), ('dadra_nagar_haveli', 'Dadra and Nagar Haveli'), ('daman_diu', 'Daman and Diu'), ('delhi', 'Delhi'), ('goa', 'Goa'), ('gujarat', 'Gujarat'), ('haryana', 'Haryana'), ('himachal_pradesh', 'Himachal Pradesh'), ('jammu_kashmir', 'Jammu and Kashmir'), ('jharkhand', 'Jharkhand'), ('karnataka', 'Karnataka'), ('kerala', 'Kerala'), ('lakshadweep', 'Lakshadweep'), ('madhya_pradesh', 'Madhya Pradesh'), ('maharashtra', 'Maharashtra'), ('manipur', 'Manipur'), ('meghalaya', 'Meghalaya'), ('mizoram', 'Mizoram'), ('nagaland', 'Nagaland'), ('odisha', 'Odisha'), ('puducherry', 'Puducherry'), ('punjab', 'Punjab'), ('rajasthan', 'Rajasthan'), ('sikkim', 'Sikkim'), ('tamil_nadu', 'Tamil Nadu'), ('telangana', 'Telangana'), ('tripura', 'Tripura'), ('uttar_pradesh', 'Uttar Pradesh'), ('uttarakhand', 'Uttarakhand'), ('west_bengal', 'West Bengal')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='aadhaar',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='aadhar',
            field=models.FileField(null=True, upload_to='static/aadhar/'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='bg_choices',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='caste',
            field=models.FileField(null=True, upload_to='static/caste/'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='category',
            field=models.CharField(choices=[('general', 'General'), ('obc', 'OBC'), ('sc', 'SC'), ('st', 'ST'), ('minority', 'Minority')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='degree',
            field=models.FileField(null=True, upload_to='static/degree/'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='district',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='father_mobile',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='father_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='father_occupation',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='g_choices',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_aadhar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_caste',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_degree',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_others',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_ration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_tenth_marks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='has_twel_marks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='high_edu_quali',
            field=models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('graduation', 'Graduation'), ('post_graduation', 'Post Graduation'), ('other', 'Other')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='income',
            field=models.FileField(null=True, upload_to='static/income/'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='occupation',
            field=models.CharField(choices=[('govt_service', 'Govt. Service'), ('private_service', 'Private Service'), ('student', 'Student'), ('unemployed', 'Unemployed'), ('housewife', 'Housewife')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='others',
            field=models.FileField(null=True, upload_to='static/others/'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='permanent_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='photo',
            field=models.ImageField(null=True, upload_to='static/franchise_photos'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='pin',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='ration',
            field=models.FileField(null=True, upload_to='static/ration/'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='state',
            field=models.CharField(choices=[('andaman_nicobar_island', 'Andaman and Nicobar Island'), ('andhra_pradesh', 'Andhra Pradesh'), ('arunachal_pradesh', 'Arunachal Pradesh'), ('assam', 'Assam'), ('bihar', 'Bihar'), ('chandigarh', 'Chandigarh'), ('chhattisgarh', 'Chhattisgarh'), ('dadra_nagar_haveli', 'Dadra and Nagar Haveli'), ('daman_diu', 'Daman and Diu'), ('delhi', 'Delhi'), ('goa', 'Goa'), ('gujarat', 'Gujarat'), ('haryana', 'Haryana'), ('himachal_pradesh', 'Himachal Pradesh'), ('jammu_kashmir', 'Jammu and Kashmir'), ('jharkhand', 'Jharkhand'), ('karnataka', 'Karnataka'), ('kerala', 'Kerala'), ('lakshadweep', 'Lakshadweep'), ('madhya_pradesh', 'Madhya Pradesh'), ('maharashtra', 'Maharashtra'), ('manipur', 'Manipur'), ('meghalaya', 'Meghalaya'), ('mizoram', 'Mizoram'), ('nagaland', 'Nagaland'), ('odisha', 'Odisha'), ('puducherry', 'Puducherry'), ('punjab', 'Punjab'), ('rajasthan', 'Rajasthan'), ('sikkim', 'Sikkim'), ('tamil_nadu', 'Tamil Nadu'), ('telangana', 'Telangana'), ('tripura', 'Tripura'), ('uttar_pradesh', 'Uttar Pradesh'), ('uttarakhand', 'Uttarakhand'), ('west_bengal', 'West Bengal')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='tenth_marks',
            field=models.FileField(null=True, upload_to='static/sslc_marks/'),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='twel_marks',
            field=models.FileField(null=True, upload_to='static/12th_marks/'),
        ),
    ]
