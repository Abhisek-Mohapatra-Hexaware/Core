
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('recipes/',recipes,name="recipes"),
    path('delete_recipe/<id>/',delete_recipe,name='delete_recipe'),
    path('update_recipe/<id>/',update_recipe,name='update_recipe'),
    path('login/',login_page,name="login_page"),
    path('register/',register_page,name="register_page"),
    path('logout/',logout_page,name="logout_page"),
    path('admin/', admin.site.urls),
    path('students/',get_students,name='get_students'),
    path('see_marks/<student_id>',see_marks,name='see_marks'),
    path('send_email/',send_email,name='send_email'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        documents_root=settings.MEDIA_ROOT)


urlpatterns+=staticfiles_urlpatterns()



