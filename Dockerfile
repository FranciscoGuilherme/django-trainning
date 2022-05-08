FROM ubuntu:18.04

# ==============================================
# -----[Definicao do diretorio de trabalho]-----
# ==============================================

WORKDIR /usr/src/app

# ===============================================
# -----[Definicao das variaveis de ambiente]-----
# ===============================================

ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ==================================================
# -----[Instalacao das dependencias do projeto]-----
# ==================================================

COPY ./requirements.txt .
RUN apt-get update
RUN apt-get install \
    python3-pip \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev \
    -y
RUN pip3 install -r requirements.txt
RUN pip3 install -U setuptools

# =============================================
# -----[Copia do projeto para o container]-----
# =============================================

COPY . .
