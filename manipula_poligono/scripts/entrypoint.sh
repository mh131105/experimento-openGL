#!/usr/bin/env bash
set -euo pipefail

export DISPLAY="${DISPLAY:-:99}"
export LIBGL_ALWAYS_SOFTWARE="${LIBGL_ALWAYS_SOFTWARE:-1}"
export MESA_LOADER_DRIVER_OVERRIDE="${MESA_LOADER_DRIVER_OVERRIDE:-llvmpipe}"
export GALLIUM_DRIVER="${GALLIUM_DRIVER:-llvmpipe}"

cleanup() {
  kill 0 >/dev/null 2>&1 || true
}

trap cleanup EXIT

Xvfb "$DISPLAY" -screen 0 1280x720x24 -ac +extension GLX +render -noreset &

for _ in $(seq 1 20); do
  if xdpyinfo -display "$DISPLAY" >/dev/null 2>&1; then
    break
  fi
  sleep 0.5
done

openbox >/tmp/openbox.log 2>&1 &
x11vnc -display "$DISPLAY" -forever -shared -rfbport 5900 -nopw -quiet >/tmp/x11vnc.log 2>&1 &
websockify --web=/usr/share/novnc/ 6080 localhost:5900 >/tmp/websockify.log 2>&1 &

python -m app.main
