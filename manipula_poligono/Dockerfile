FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONPATH=/workspace \
    DISPLAY=:99 \
    LIBGL_ALWAYS_SOFTWARE=1 \
    MESA_LOADER_DRIVER_OVERRIDE=llvmpipe \
    GALLIUM_DRIVER=llvmpipe

WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    freeglut3-dev \
    libgl1 \
    libgl1-mesa-dri \
    libglx-mesa0 \
    libglu1-mesa \
    novnc \
    openbox \
    websockify \
    x11-utils \
    x11vnc \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .
RUN chmod +x /workspace/scripts/entrypoint.sh

EXPOSE 6080 5900

CMD ["/workspace/scripts/entrypoint.sh"]
