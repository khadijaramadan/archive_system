from django import forms
from .models import Department, Position, CustomUser

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code', 'unit_type', 'level', 'is_sovereign', 'parent']
        labels = {
            'name': 'اسم الوحدة',
            'code': 'رمز الوحدة',
            'unit_type': 'نوع الوحدة',
            'level': 'المستوى الإداري',
            'is_sovereign': 'وحدة سيادية',
            'parent': 'الوحدة التابعة لها',
        }


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title', 'department', 'can_approve', 'rank']
        labels = {
            'title': 'المسمى الوظيفي',
            'department': 'الإدارة',
            'can_approve': 'صلاحية الاعتماد',
            'rank': 'الرتبة داخل الإدارة',
        }


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'department', 'position', 'job_title', 'phone_number', 'signature_image']
        labels = {
            'username': 'اسم المستخدم',
            'email': 'البريد الإلكتروني',
            'department': 'الإدارة',
            'position': 'المنصب الوظيفي',
            'job_title': 'المسمى الوظيفي',
            'phone_number': 'رقم الجوال',
            'signature_image': 'التوقيع الرقمي',
        }

