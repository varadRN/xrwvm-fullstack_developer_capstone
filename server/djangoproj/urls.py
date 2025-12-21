from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django proxy APIs (IMPORTANT)
    path('djangoapp/', include('djangoapp.urls')),

    # Frontend pages
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name='contact'),
    path('dealers/', TemplateView.as_view(template_name="index.html")),
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),



]

# Static & media handling
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
