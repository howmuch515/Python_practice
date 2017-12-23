from subprocess import run
import os

if os.name == 'nt':
    run('calc.exe')
else:
    run('ls')
