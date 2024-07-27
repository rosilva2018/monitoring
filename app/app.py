import logging
import time
import os
from logging_loki import LokiHandler

# Obter a URL do Loki a partir da variável de ambiente
loki_url = os.getenv('LOKI_URL', 'http://localhost:3100')  # Valor padrão para testes locais

# Configurar o manipulador Loki
loki_handler = LokiHandler(
    url=f"{loki_url}/loki/api/v1/push",
    tags={"application": "python-app"},
    version="1",
)

# Configurar o logger
logger = logging.getLogger("python-logger")
logger.setLevel(logging.INFO)
logger.addHandler(loki_handler)

if __name__ == "__main__":
    while True:
        logger.info("Log de exemplo enviado para o Loki!")
        time.sleep(5)
