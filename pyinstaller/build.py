from PyInstaller.__main__ import run

run([
    '--name=ttconv',
    '--onefile',
    '--clean',
    '--collect-all=ttconv',
    '--copy-metadata=ttconv',
    '-m',
    'ttconv.tt',
])
