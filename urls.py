from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('learner', views.Learn, name="learn"),
    path('instruct', views.Instruct, name="instructor"),
    path('course/', views.courses, name="Course"),
    path('cond/', views.terms, name="Cond"),
    path('Earn/', views.earnings, name="earn"),
    path('Enroll', views.enrol, name="Enroll"),
    path('Payments', views.pay, name="payment"),
    path('Thank You/', views.regdone, name="done"),
    path('wel_learn', views.welcome_learn, name="welcome_learn"),
    path('wel_earn', views.welcome_earn, name="welcome_earn"),
    path('completed',views.success, name="success"),
    path('staff/', views.staff, name="staff"),
    path('verify',views.verify,  name='verify'),
    path('approve', views.approve,  name="approve"),
    path('reject', views.reject, name="reject"),
    path('done1', views.done1, name="done1"),
    path('pair',views.paired, name="paired")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
