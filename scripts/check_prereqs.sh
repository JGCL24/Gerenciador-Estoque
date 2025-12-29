#!/usr/bin/env bash
set -e

echo "Checking prerequisites..."

if ! command -v python >/dev/null 2>&1; then
  echo "Python not found. Install Python 3.10+ from https://www.python.org/" >&2
  exit 2
fi
PYVER=$(python -c "import sys; print('.'.join(map(str, sys.version_info[:3])))")
echo "Python version: $PYVER"

if ! command -v node >/dev/null 2>&1; then
  echo "Node.js not found. Install Node.js (LTS >= 16) from https://nodejs.org/" >&2
  exit 2
fi
NODEV=$(node -v)
echo "Node: $NODEV"

if ! command -v npm >/dev/null 2>&1; then
  echo "npm not found. Install npm (comes with Node.js)." >&2
  exit 2
fi
NPmv=$(npm -v)
echo "npm: $NPmv"

echo "All required tools appear installed. Follow the README for the exact steps to set up backend and frontend."