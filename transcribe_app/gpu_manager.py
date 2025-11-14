import torch
import os
from faster_whisper import WhisperModel
from .modules.logger import log_info, log_debug, log_error, log_endpoint_call, log_endpoint_error

from dotenv import load_dotenv

load_dotenv()

class GPUManager:

    def __init__(self):
        self.models = {}
        self.num_gpus = torch.cuda.device_count()
        self.model_name = os.getenv('MODEL') or 'large-v3'
        self.models_loaded = False  # Flag to indicate if models are loaded
        log_info(f"DEBUG: Number GPUs found: [{self.num_gpus}]\n")
    
    def get_gpus(self):
        self.gpus_names = {}
        for gpu_id in range (self.num_gpus):
            torch.cuda.set_device(gpu_id)
            self.gpus_names[str(gpu_id)] = torch.cuda.get_device_name(gpu_id)
            log_info(f"DEBUG: GPU Names: [{self.gpus_names} -- ID:[{gpu_id}]]\n")        
        return self.gpus_names
    

    def load_models(self):
        #os.environ["CUDA_VISIBLE_DEVICES"] = "1" # test para subir somente na gpu 1
        MODEL = os.getenv('MODEL') or 'large-v3' # 'tiny', 'base', 'small', 'medium', 'large', 'large-v2', 'large-v3'
        DEVICE = os.getenv('DEVICE') or 'cuda' # 'cpu' ou 'cuda'
        COMPUTE_TYPE = os.getenv('COMPUTE_TYPE') or 'float16'  # 'int8' para CPU, 'float16' para GPU
        log_info(f"DEBUG: Number of GPUs found: [{self.num_gpus}]\n")
        for gpu_id in range(self.num_gpus):
            log_info(f"DEBUG: Loading model on GPU id [{gpu_id}]\n")
            torch.cuda.set_device(gpu_id)
            model = WhisperModel(
                MODEL,
                device=DEVICE,
                compute_type=COMPUTE_TYPE  # 'int8' para CPU, 'float16' para GPU
            )
            self.models_loaded = model
            
            memory_used = torch.cuda.device_memory_used()
            giga_byte = 1024**3
            log_debug(f"Memória Alocada (GB): {memory_used / giga_byte:.2f} GB")
            self.models = {
                "model_name": self.model_name,
                "allocated_memory": f"{memory_used / giga_byte:.2f} GB",
            }
        log_info(f"DEBUG: End Loading model in GPU id [{gpu_id}]\n")

    def get_model_loaded(self, gpu_id=0):
        log_info(f"DEBUG: GPU id [{gpu_id}] >> Load Model Status: [{self.models_loaded}]\n")
        if not self.models_loaded:
            log_error("Models are not loaded yet. Please call load_models() first.", "")
            raise RuntimeError("Models are not loaded yet. Please call load_models() first.")
        return self.models_loaded

    def get_model(self, gpu_id=0):
        log_info(f"DEBUG: GPU id [{gpu_id}] >> Load Model Status: [{self.models_loaded}]\n")
        if not self.models_loaded:
            log_error("Models are not loaded yet. Please call load_models() first.", "")
            raise RuntimeError("Models are not loaded yet. Please call load_models() first.")
        return self.models

# Instância global para gerenciar os modelos
gpu_manager = GPUManager()
