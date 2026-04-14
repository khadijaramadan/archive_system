from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from .models import CustomUser, Department, Position
from .forms import CustomUserForm, DepartmentForm, PositionForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator

# استيراد موديل المراسلات من التطبيق الثاني
from correspondence.models import Correspondence 

User = get_user_model()

# دالة تبديل المستخدم (للتجربة فقط)
def switch_user(request, username):
    try:
        user_to_switch = User.objects.get(username=username)
        login(request, user_to_switch)
        return redirect('home')
    except User.DoesNotExist:
        return redirect('home')

# --- التعديل المطلوب لصفحة لوحة التحكم ---
class HomeView(TemplateView):
    template_name = 'accounts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # استيراد الموديلات
        from correspondence.models import Correspondence, Referral
        from django.db.models import Q # استيراد Q للبحث المتقدم
        
        # جلب كلمة البحث من الرابط (للبحث التقليدي)
        search_query = self.request.GET.get('search')
        
        # 1. الإحصائيات العادية
        if self.request.user.is_superuser:
            records = Correspondence.objects.all()
        else:
            records = Correspondence.objects.filter(created_by=self.request.user)
        
        # --- إضافة منطق البحث في القائمة ---
        filtered_records = records
        if search_query:
            filtered_records = records.filter(
                Q(subject__icontains=search_query) | 
                Q(ref_number__icontains=search_query)
            )

        total = records.count()
        context['total_corr'] = total
        
        if total > 0:
            context['inbox_p'] = (records.filter(corr_type='INCOMING').count() / total) * 100
            context['outbox_p'] = (records.filter(corr_type='OUTGOING').count() / total) * 100
        else:
            context['inbox_p'] = context['outbox_p'] = 0

        context['total_inbox'] = records.filter(corr_type='INCOMING').count()
        context['total_outbox'] = records.filter(corr_type='OUTGOING').count()
        context['total_internal'] = records.filter(corr_type='INTERNAL').count()
        context['processing_corr'] = records.filter(status='PROCESSING').count()
        
        # ============================================================
        # التعديل: استبعاد الداخلي من كرت المؤرشفة حسب طلب المشرف
        # ============================================================
        context['completed_corr'] = records.filter(status='COMPLETED').exclude(corr_type='INTERNAL').count()
        
        context['draft_corr'] = records.filter(status='DRAFT').count()
        
        # عرض القائمة المفلترة (آخر 5 نتائج)
        context['latest_correspondences'] = filtered_records.order_by('-created_at')[:5]

        # ============================================================
        # التصليح المطلوب لظهور الإشعارات عند محمد
        # ============================================================
        # قمنا بحذف exclude(correspondence__status='DRAFT') 
        # لكي تظهر المعاملات التي أعادها المدير للموظف (لأنها تصبح مسودة)
        qs_unread = Referral.objects.filter(
            receiver_user=self.request.user, 
            is_read=False
        )

        context['unread_count'] = qs_unread.count()
        context['recent_notifications'] = qs_unread.order_by('-created_at')[:5]
        # ============================================================
        
        return context
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

    def form_valid(self, form):
        messages.success(self.request, "تمت إضافة المستخدم الجديد بنجاح!")
        return super().form_valid(form)

# تعديل بيانات مستخدم
class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'accounts/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        messages.success(self.request, "تم تحديث بيانات المستخدم بنجاح!")
        return super().form_valid(form)

# حذف مستخدم
class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def post(self, request, *args, **kwargs):
        messages.success(request, "تم حذف المستخدم من النظام بنجاح.")
        return super().post(request, *args, **kwargs)

# ================================================================================
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

# =============================================================
