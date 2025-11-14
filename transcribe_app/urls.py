from django.urls import path
from . import views

urlpatterns = [
    path('transcribe', views.transcribe_audio, name='transcribe_audio'),
    path('ping', views.ping, name='ping'),
    path('gpus', views.get_gpus, name='get_gpus'),
    path('load-models', views.load_models, name='load_models'),
    path('status-models', views.status_models, name='status_models')
]

