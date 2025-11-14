import os
from django.apps import AppConfig
from .gpu_manager import gpu_manager
from .modules.logger import log_info


class TranscribeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transcribe_app'

    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            log_info("Inicializando API Transcribe Fast Whisper...\n")
            #log_info("Inicializando GPU Manager e carregando modelos...\n")
            #gpu_manager.load_models() # Descomentar para carregar modelos na inicialização