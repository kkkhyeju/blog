from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('home2/', wordcount.views.home2, name='home2'),
    path('about/', wordcount.views.about, name='about'),
    path('count/', wordcount.views.count, name='count'),

    path('blog/', include('blog.urls')),

    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
]