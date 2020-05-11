from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
""" us auth_views lib as login logout"""
from django.contrib.auth import views as auth_views
""" us CourseListView from courses"""
from courses.views import CourseListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('ecommerce/', include('ecommerce.urls')), # Include ecommerce app views. 

    path('mooc/accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('mooc/accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('mooc/course/', include('courses.urls')),
    path('mooc/', CourseListView.as_view(), name='course_list'),
    path('mooc/students/', include('students.urls')),
    path('mooc/api/', include('courses.api.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
