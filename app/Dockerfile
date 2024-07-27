# Use a imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos para a imagem
COPY requirements.txt .

# Atualiza o pip para a versão mais recente
RUN pip install --upgrade pip

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo da aplicação para a imagem
COPY . .

# Define a variável de ambiente para a URL do Loki
ENV LOKI_URL=http://loki:3100

# Executa o script Python
CMD ["python", "app.py"]
