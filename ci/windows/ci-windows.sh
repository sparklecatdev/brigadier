#!/bin/bash

set -eux -o pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd )"
python=python

$python -V
$python -m pip install -r "${script_dir}/requirements.txt"
$python -m pip freeze

$python -m PyInstaller \
    --clean \
    --onefile \
    brigadier
