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

RUN apt-get update
RUN apt-get install \
    build-essential \
    libssl-dev \
    python3-matplotlib \
    python3-sklearn \
    python3-pandas \
    python3-numpy \
    python3-scipy \
    python3-sympy \
    python3-nose \
    python3-pip \
    ipython3 \
    -y
RUN pip3 install -U Django

# =============================================
# -----[Copia do projeto para o container]-----
# =============================================

COPY . .
