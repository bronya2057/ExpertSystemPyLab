pyuic5 -x -o .\MainWindowView.py .\MainWindow.ui
pyuic5 -x -o .\RuleEditorView.py .\RuleEditor.ui

@echo off
rem Specify Sprint in the next format and you will get ICObjectTable, MainDeclDef, 
python .\RemoveGUIModule.py
popd
rem pause