from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('app.urls'))
    path('base',views.base,name="base"),
    path('',views.home,name="home")
] +static(settings.MEDIA_URL,document_root =  settings.MEDIA_ROOT)
