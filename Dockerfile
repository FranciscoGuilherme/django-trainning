FROM python:3.9.6-alpine

# =============================================
# -----[Configuracoes de permissionamento]-----
# =============================================

RUN adduser -D python-user
USER python-user

# ==============================================
# -----[Definicao do diretorio de trabalho]-----
# ==============================================

WORKDIR /usr/src/app

# ===============================================
# -----[Definicao das variaveis de ambiente]-----
# ===============================================

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/home/python-user/.local/bin:${PATH}"

# =======================================
# -----[Instalacao das dependencias]-----
# =======================================

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY --chown=python-user:python-user requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

# ========================
# -----[Copy project]-----
# ========================

COPY --chown=python-user:python-user . .
