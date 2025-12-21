from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'djangoapp'

urlpatterns = [
    # ✅ Dealer proxy APIs
    path('dealers', views.get_dealers, name='get_dealers'),
    path('dealers/<str:state>', views.get_dealers_by_state, name='get_dealers_by_state'),
]

# ✅ Static & media (safe for lab)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
