# transcribe-faster-whisper-api

API para transcrição de áudio rápida utilizando o modelo Faster-Whisper.

## Descrição

Este projeto implementa uma API RESTful que permite transcrever arquivos de áudio de forma eficiente utilizando o modelo Whisper.
Ideal para automação de processos de transcrição, integração com sistemas ou criação de aplicações que exigem transcrição automática de áudio.

## Funcionalidades

- Envio de arquivos de áudio para transcrição
- Resposta rápida com resultado em texto
- Suporte a múltiplos formatos de áudio
- (Adicione outras funcionalidades específicas do seu projeto)

## Instalação

Clone este repositório:
```bash
git clone https://github.com/Rogertbs/transcribe-faster-whisper-api.git
```

Ative o ambiente virtual:
```bash
source venv/bin/activate
````

Instale as dependências:
```bash
# Exemplo usando Python
pip install -r requirements.txt
```
Configure o arquivo .env (cópia do .env-sample)

## Uso

Inicie o servidor:
```bash
python3 manage.py runserver 0.0.0.0:8000
```

Carrege o modelo (POST):
```bash 
http:127.0.0.1:8000/api/load-models
```
<img width="312" height="75" alt="image" src="https://github.com/user-attachments/assets/168b447c-5ac9-499d-8bd1-56cd21de30ad" />

Confirme se o modelo foi carregado (POST):
```bash 
http:127.0.0.1:8000/api/status-models
```
<img width="270" height="99" alt="image" src="https://github.com/user-attachments/assets/1f0b9be4-0931-4489-bede-4196aedda8d4" />


Envie um arquivo de áudio via requisição HTTP (POST) Body FormData(file) [audio: file]
```bash
http://localhost:8000/api/transcribe
```
<img width="529" height="284" alt="image" src="https://github.com/user-attachments/assets/d026933d-e2f7-4edf-a1f7-18050e0b8557" />

<img width="565" height="138" alt="image" src="https://github.com/user-attachments/assets/8e9c4843-cd94-4f05-b737-70a67f4706bd" />

Liste todas GPUs do servidor (GET) sem parâmetros
```bash
http://localhost:8000/api/gpus
```
<img width="319" height="120" alt="image" src="https://github.com/user-attachments/assets/d1ae3adb-899d-481a-b9ca-ab9b582bb7ac" />


## Tecnologias utilizadas

- Faster Whisper
- Python

## Contribuição

Contribuições são bem-vindas! Abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Desenvolvedor: Rogertbs  
GitHub: [github.com/Rogertbs](https://github.com/Rogertbs)
