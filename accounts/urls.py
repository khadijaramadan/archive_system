from django.urls import path
# استيرادات المستخدمين
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView, HomeView
)

# استيرادات الإدارات
from .views import (
    DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView
)

from .views import (
    PositionListView, PositionCreateView, PositionUpdateView, PositionDeleteView
)

urlpatterns = [
    # عرض قائمة المستخدمين
    path('users/', UserListView.as_view(), name='user_list'),

    # إدخال مستخدم جديد
    path('users/create/', UserCreateView.as_view(), name='user_create'),

    # تعديل مستخدم موجود (باستخدام الـ pk)
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),

    # حذف مستخدم موجود (باستخدام الـ pk)
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    path('', HomeView.as_view(), name='home'),  # الصفحة الرئيسية للتطبيق
    
    # مسارات الإدارات
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),

    # مسارات إدارة المناصب
    path('positions/', PositionListView.as_view(), name='position_list'),
    path('positions/create/', PositionCreateView.as_view(), name='position_create'),
    path('positions/<int:pk>/update/', PositionUpdateView.as_view(), name='position_update'),
    path('positions/<int:pk>/delete/', PositionDeleteView.as_view(), name='position_delete'),
]