#!/usr/bin/env bash
# One-time setup for the lesson video pipeline on the ThinkCentre. No sudo needed.
# It shares its Python venv, Kokoro voice and Whisper weights with loop-geterdone.'s videos.
#   bash video/setup.sh
set -euo pipefail
cd "$(dirname "$0")"
CACHE="${VIDEO_CACHE:-$HOME/.cache/loop-reels}"
KOKORO_DIR="${KOKORO_DIR:-$HOME/.cache/alchemist-lab-tts}"

# Python: Kokoro (voice), faster-whisper (captions), a static FFmpeg build (imageio-ffmpeg).
mkdir -p "$CACHE"
[ -x "$CACHE/venv/bin/python" ] || uv venv -q "$CACHE/venv" --python 3.12
VIRTUAL_ENV="$CACHE/venv" uv pip install -q kokoro-onnx==0.6.1 soundfile numpy faster-whisper imageio-ffmpeg pillow
FF="$("$CACHE/venv/bin/python" -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())')"
command -v ffmpeg >/dev/null || { mkdir -p "$HOME/.local/bin"; ln -sf "$FF" "$HOME/.local/bin/ffmpeg"; }

# Kokoro model: the same files the pixelbattle.me games use. Fetch them only if missing.
if [ ! -f "$KOKORO_DIR/kokoro-v1.0.onnx" ]; then
  mkdir -p "$KOKORO_DIR"
  base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
  curl -fL -o "$KOKORO_DIR/kokoro-v1.0.onnx" "$base/kokoro-v1.0.onnx"
  curl -fL -o "$KOKORO_DIR/voices-v1.0.bin" "$base/voices-v1.0.bin"
fi

# Whisper weights (small.en) into the cache.
"$CACHE/venv/bin/python" -c "from faster_whisper import WhisperModel; WhisperModel('${VIDEO_WHISPER:-small.en}', device='cpu', compute_type='int8', download_root='$CACHE/whisper')"

# Node: Remotion + its headless Chrome, Playwright for page captures.
npm install --no-audit --no-fund
npx remotion browser ensure

echo "video ready: $CACHE/venv/bin/python video/make_video.py <course>/<lesson>"
