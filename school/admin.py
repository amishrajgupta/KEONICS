from django.contrib import admin
from .models import Attendance,StudentExtra,TeacherExtra,FrenchiseExtra,Notice
# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class FrenchiseExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(FrenchiseExtra, FrenchiseExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)
