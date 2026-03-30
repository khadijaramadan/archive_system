from django.db import models

from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    UNIT_TYPES = [
        ('office', 'مكتب'),
        ('admin', 'إدارة عامة'),
        ('section', 'قسم'),
    ]
    
    name = models.CharField(max_length=255, verbose_name="اسم الوحدة")
    code = models.CharField(max_length=20, unique=True, verbose_name="رمز الوحدة")
    unit_type = models.CharField(max_length=20, choices=UNIT_TYPES , default='section')
    level = models.PositiveIntegerField(default=3, verbose_name="المستوى الإداري")
    is_sovereign = models.BooleanField(default=False, verbose_name="وحدة سيادية/عابرة للمستويات")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_units')

    def __str__(self):
     return self.name
    class Meta:
        ordering = ['level', 'name']

class Position(models.Model):
    title = models.CharField(max_length=255, verbose_name="المسمى الوظيفي")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions', verbose_name="الإدارة")
    
    can_approve = models.BooleanField(default=False, verbose_name="يملك صلاحية الاعتماد")
    
    rank = models.PositiveIntegerField(default=3, verbose_name="الرتبة داخل الإدارة")

    class Meta:
        verbose_name = "المنصب"
        verbose_name_plural = "المناصب"
        ordering = ['department', 'rank']

    def __str__(self):
     return f"{self.title} - {self.department.name}"

class CustomUser(AbstractUser):

    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True, verbose_name="الإدارة")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المنصب الوظيفي")
    job_title = models.CharField(max_length=150, blank=True, verbose_name="المسمى الوظيفي")
    phone_number = models.CharField(max_length=15, blank=True, verbose_name="رقم الجوال")
    signature_image = models.ImageField(upload_to='signatures/', null=True, blank=True, verbose_name="التوقيع الرقمي")

    class Meta:
        verbose_name = "الموظف"
        verbose_name_plural = "الموظفين"
# Create your models here.
