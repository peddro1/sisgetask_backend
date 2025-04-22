# FROM python:3.11-alpine3.18
# LABEL maintainer="agap.samuel@ime.eb.br"

# # Essa variável de ambiente é usada para controlar se o Python deve 
# # gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
# ENV PYTHONDONTWRITEBYTECODE 1

# # Define que a saída do Python será exibida imediatamente no console ou em 
# # outros dispositivos de saída, sem ser armazenada em buffer.
# # Em resumo, você verá os outputs do Python em tempo real.
# ENV PYTHONUNBUFFERED 1

# # Copia a pasta "sisgetask_back" e "scripts" para dentro do container.
# COPY sisgetask_back /sisgetask_back
# COPY scripts /scripts

# # Entra na pasta sisgetask_back no container
# WORKDIR /sisgetask_back

# # A porta 8000 estará disponível para conexões externas ao container
# # É a porta que vamos usar para o Django.
# EXPOSE 8000

# # RUN executa comandos em um shell dentro do container para construir a imagem. 
# # O resultado da execução do comando é armazenado no sistema de arquivos da 
# # imagem como uma nova camada.
# # Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# # imagem e torná-la mais eficiente.
# RUN python -m venv /venv && \
#   /venv/bin/pip install --upgrade pip && \
#   /venv/bin/pip install -r /sisgetask_back/requirements.txt && \
#   mkdir -p /data/web/static && \
#   mkdir -p /data/web/media && \
#   chown -R root:root /venv && \
#   chown -R root:root /data/web/static && \
#   chown -R root:root /data/web/media && \
#   chmod -R 755 /data/web/static && \
#   chmod -R 755 /data/web/media && \
#   chmod -R +x /scripts

# # Adiciona a pasta scripts e venv/bin 
# # no $PATH do container.
# ENV PATH="/scripts:/venv/bin:$PATH"

# # Muda o usuário para duser
# #USER duser

# # Executa o arquivo scripts/commands.sh
# CMD ["commands.sh"]

FROM python:3.9-alpine3.13

COPY ./requirements.txt /tmp/requirements.txt
COPY ./sisgetask_back /sisgetask_back
WORKDIR /sisgetask_back
EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  apk add --update --no-cache postgresql-client && \
  apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
  /venv/bin/pip install -r /tmp/requirements.txt && \
  rm -rf /tmp && \
  apk del .tmp-build-deps && \
  adduser \
    --disabled-password \
    --no-create-home \
    django-user
 

ENV PATH="/venv/bin:$PATH"
USER django-user