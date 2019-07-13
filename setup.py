import os
import subprocess
import sys

if __name__ == '__main__':
    build_resources_command = [
        'pyside2-rcc',
        'res/resources.qrc',
        '-o', 'timechart/resources.py'
    ]

    subprocess.run(build_resources_command)

    command = [
        'pyinstaller',
        './main.py',
        '--name', 'timechart',
        '--icon', 'res/img/icon.ico',
        '--add-data', f'res/img/icon.png{os.pathsep}share/icons/',
        '--add-data', f'res/snap/timechart.desktop{os.pathsep}share/application/',
        '--window',
        '-y',
    ]

    if sys.platform == 'linux':
        command += [
            '--hidden-import', 'timechart.core.linux',
        ]
    elif sys.platform == 'win32':
        command += [
            '--hidden-import', 'timechart.core.win32',
        ]

    subprocess.run(command)
