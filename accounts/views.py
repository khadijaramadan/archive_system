from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib import messages  # استيراد مكتبة الرسائل
from .models import Department
from .forms import DepartmentForm
from .models import Position
from .forms import PositionForm


class HomeView(TemplateView):
    template_name = 'accounts/home.html'

# عرض قائمة المستخدمين
class UserListView(ListView):
    model = CustomUser
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'


# إدخال مستخدم جديد
class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'accounts/user_form.html'
    success_url = reverse_lazy('user_list')

    # إضافة رسالة نجاح بعد الحفظ
    def form_valid(self, form):
        messages.success(self.request, "تمت إضافة المستخدم الجديد بنجاح!")
        return super().form_valid(form)


# تعديل بيانات مستخدم
class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'accounts/user_form.html'
    success_url = reverse_lazy('user_list')

    # إضافة رسالة نجاح بعد التعديل
    def form_valid(self, form):
        messages.success(self.request, "تم تحديث بيانات المستخدم بنجاح!")
        return super().form_valid(form)


# حذف مستخدم
class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    # نستخدم دالة post لأنها هي اللي تتنفذ لما تضغطي على زر "نعم، احذف"
    def post(self, request, *args, **kwargs):
        messages.success(request, "تم حذف المستخدم من النظام بنجاح.")
        return super().post(request, *args, **kwargs)
#================================================================================
# 1. عرض قائمة الإدارات
class DepartmentListView(ListView):
    model = Department
    template_name = 'accounts/department_list.html'
    context_object_name = 'departments'

# 2. إضافة إدارة جديدة
class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'accounts/department_form.html'
    success_url = reverse_lazy('department_list')

    def form_valid(self, form):
        messages.success(self.request, "تمت إضافة الإدارة/الوحدة بنجاح!")
        return super().form_valid(form)

# 3. تعديل بيانات إدارة
class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'accounts/department_form.html'
    success_url = reverse_lazy('department_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث بيانات الإدارة بنجاح!")
        return super().form_valid(form)

# 4. حذف إدارة
class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'accounts/department_confirm_delete.html'
    success_url = reverse_lazy('department_list')

    def post(self, request, *args, **kwargs):
        messages.success(request, "تم حذف الإدارة من النظام بنجاح.")
        return super().post(request, *args, **kwargs)    
#=============================================================
# 1. عرض قائمة المناصب
class PositionListView(ListView):
    model = Position
    template_name = 'accounts/position_list.html'
    context_object_name = 'positions'

# 2. إضافة منصب جديد
class PositionCreateView(CreateView):
    model = Position
    form_class = PositionForm
    template_name = 'accounts/position_form.html'
    success_url = reverse_lazy('position_list')

    def form_valid(self, form):
        messages.success(self.request, "تمت إضافة المنصب الوظيفي بنجاح!")
        return super().form_valid(form)

# 3. تعديل منصب موجود
class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    template_name = 'accounts/position_form.html'
    success_url = reverse_lazy('position_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث بيانات المنصب بنجاح!")
        return super().form_valid(form)

# 4. حذف منصب
class PositionDeleteView(DeleteView):
    model = Position
    template_name = 'accounts/position_confirm_delete.html'
    success_url = reverse_lazy('position_list')

    def post(self, request, *args, **kwargs):
        messages.success(request, "تم حذف المنصب من النظام.")
        return super().post(request, *args, **kwargs)    