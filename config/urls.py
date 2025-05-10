"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home, psychologists
from django.urls import path, include
from accounts import views as account_views
from accounts import views
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from accounts.views import psychologists_view


from config.sitemaps import StaticViewSitemap



sitemaps = {
    'static': StaticViewSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),

    # allauth: регистрация/логин/выход
    path('accounts/', include('allauth.urls')),

    # наши URL-ы для аккаунтов (profile, edit_profile и т.д.)
    path('accounts/', include('accounts.urls')),

    # главная и психологи
    path('', home, name='home'),
    path('psychologists/', psychologists, name='psychologists'),
    path('', account_views.home, name='home'),    # ✅ главная
    path('psychologists/', account_views.psychologists, name='psychologists'),
    # чат
    path('chat/', include('chat.urls')),
    path('', include('pages.urls')),
    path('psychology-tips/', views.psychology_tips, name='psychology_tips'),
    path('feedback/', views.feedback_view, name='feedback'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='sitemap'),
     path('psychologists/', psychologists_view, name='psychologists'),
     path('psychologists/', include('psychologists.urls')),
]

# медиа-файлы (аватары)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


