import hashlib
import os
import shutil
import subprocess
import sys
from zipfile import ZipFile

NAME = 'brigadier'


def run(cmd):
    retcode = subprocess.call(cmd)
    if retcode:
        raise SystemExit("Command failure: %s exited %s." % (' '.join(cmd), retcode))


with open('VERSION', 'r') as fd:
    version = fd.read().strip()

name_versioned = NAME + '-' + version
dist_dir = os.path.join(os.getcwd(), 'dist')
build_dir = os.path.join(os.getcwd(), 'build')
exe_name = NAME + '.exe'
exe_path = os.path.join(dist_dir, exe_name)
zipfile_name = name_versioned + '.zip'

print("Building version %s..." % version)
run([
    sys.executable,
    '-m',
    'PyInstaller',
    '--clean',
    '--onefile',
    '--name',
    NAME,
    'brigadier',
])

print("Compressing to zip file...")
with ZipFile(zipfile_name, 'w') as packzip:
    packzip.write(exe_path, arcname=os.path.join(name_versioned, exe_name))

with open(zipfile_name, 'rb') as zipfd:
    sha1 = hashlib.sha1(zipfd.read()).hexdigest()

print("Cleaning up...")
if os.path.isdir(build_dir):
    shutil.rmtree(build_dir)

print("Built and archived to %s." % zipfile_name)
print("SHA1: %s" % sha1)
