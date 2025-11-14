import torch
from pydub import AudioSegment
from datetime import timedelta
import os, time, threading, multiprocessing
from threading import Thread
from .modules.logger import log_info, log_debug, log_error, log_endpoint_call, log_endpoint_error

from .gpu_manager import gpu_manager

class TranscribeAudioTask(Thread):

    def __ini__(self):
        log_info(f"Init TranscribeAudioTask\n")


    # def _transcribe_audio_task(self, audio_path):
    def _task_transcribe_audio(self, audio_path):
        log_info(f"DEBUG: Starting Transcribe Audio Task >> [{audio_path}]\n")
        # Selecionar a GPU menos utilizada # to do
        gpu_id = min(range(gpu_manager.num_gpus), key=lambda i: torch.cuda.memory_allocated(i))
        log_info(f"GPU Selected: [{gpu_id}]\n")       
        model = gpu_manager.get_model_loaded(gpu_id)
        log_info(f"DEBUG: Model: [{model}]")
        
        segments, info = model.transcribe(audio_path)
        log_info(f"DEBUG: result transcribe ??? \n [{segments}]") # remove to do

        full_transcription = []
        for segment in segments:
            full_transcription.append({
                "start": self._format_timestamp(segment.start),
                "end": self._format_timestamp(segment.end),
                "text": segment.text.strip()
            })
            
        response_data = {
            "segments": full_transcription,
            "language": info.language,
            "language_probability": info.language_probability,
            "duration_seconds": info.duration
        }

        os.remove(audio_path)

        return response_data
    
    def _format_timestamp(self, seconds: float) -> str:
        td = timedelta(seconds=seconds)
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"
