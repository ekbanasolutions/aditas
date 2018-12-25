from django.conf.urls import url
from . import settings
urlpatterns = [
    url(r'^$', settings.Settings.as_view(), name='settings')
]