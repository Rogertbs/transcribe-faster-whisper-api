from django.shortcuts import render
import os, requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .gpu_manager import gpu_manager
from .tasks import TranscribeAudioTask
from .modules.logger import log_info, log_debug, log_error, log_endpoint_call, log_endpoint_error


@csrf_exempt
def transcribe_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio']
        audio_path = default_storage.save('temp_audio.mp3', audio_file)
        full_audio_path = os.path.join(default_storage.location, audio_path)
        
        log_endpoint_call('transcribe_audio', {'audio': audio_file})

        task = TranscribeAudioTask()
        res = task._task_transcribe_audio(full_audio_path)
        return JsonResponse({'result': res})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def ping(request):
    print(f"DEBUG: [{request}]")
    return JsonResponse({'result': 'pong'})


@csrf_exempt
def get_gpus(request):
    if request.method == 'GET':
        try:
            gpu_manager.get_gpus()
            return JsonResponse({'status': 'success', 'gpu_names': gpu_manager.gpus_names})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def load_models(request):
    if request.method == 'POST':
        try:
            gpu_manager.load_models()
            return JsonResponse({'status': 'success', 'message': 'Models loaded successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


@csrf_exempt
def status_models(request):
    if request.method == 'POST':
        try:
            res = gpu_manager.get_model()
            print(f"DEBUG: Model Status >> [{res['model_name']}]\n")
            return JsonResponse({'status': 'success', 'Model name': res['model_name'], 'Allocated Memory': res['allocated_memory']})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
