import os
import re
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
from pathlib import Path

def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


if __name__ == "__main__":
    gui_path = os.path.join(os.path.dirname(os.getcwd()),"GUI")
    views_path = os.path.join(gui_path, "Views")
    print(views_path)

    #
    for root, dirs, files in os.walk(views_path):
        path = root.split(os.sep)
        # print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            if re.compile("View.py").findall(file):
                print(len(path) * '---', file)
                replace(os.path.join(views_path,file), "QtGui, ", "")
    # replace('RuleEditorView.py', "QtGui, ", "")
    # replace('MainWindowView.py', "QtGui, ", "")