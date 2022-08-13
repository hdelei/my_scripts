import os
import subprocess
import sys

task_number = input('Type task name/number: ')
tasks_dir = 'E:/pytask/tasks/'

path = os.path.join(tasks_dir, task_number)
file = task_number + '.txt'

task_created = False
try:
    os.mkdir(path)
    with open(os.path.join(path, file), 'w') as fp:
        pass
    task_created = True
except OSError as error:
    print(error)

if not task_created:
    sys.exit(1)

notepad = r'C:/Program Files (x86)/Notepad++/Notepad++.exe'
if not os.path.exists(notepad):
    notepad = 'Notepad.exe'

subprocess.Popen([notepad, os.path.join(path, file)])
