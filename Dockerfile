# Usando uma imagem base baseada em Debian ou Ubuntu
FROM python:3.11-slim-bullseye

LABEL maintainer="thomasnicholaas@gmail.com"

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia a pasta "application" e "scripts" para dentro do container.
COPY application /application
COPY scripts /scripts

# Verifica se o arquivo commands.sh foi copiado
RUN ls -l /scripts

# Entra na pasta application no container
WORKDIR /application

# Expõe a porta 8000
EXPOSE 8000

# Instala dependências do sistema, cria usuário, configura permissões e instala dependências do Python em um único RUN
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc netcat && \ 
    rm -rf /var/lib/apt/lists/* && \
    useradd -m duser && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /application/requirements.txt && \
    chmod -R +x /scripts && \
    chown -R duser:duser /application && \
    mkdir -p /data/web/static /data/web/media && \
    chown -R duser:duser /data/web

# Adiciona a pasta scripts e venv/bin no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o script de inicialização
CMD ["commands.sh"]