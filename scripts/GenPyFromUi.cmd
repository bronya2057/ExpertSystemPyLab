cd ..
cd GUI
cd Views
pyuic5 -x -o .\MainWindowView.py .\MainWindow.ui
pyuic5 -x -o .\RuleEditorView.py .\RuleEditor.ui
pyuic5 -x -o .\SemanticEditorView.py .\SemanticEditor.ui
pyuic5 -x -o .\FrameEditorView.py .\FrameEditor.ui

cd ..
cd ..
cd scripts
@echo off
rem Specify Sprint in the next format and you will get ICObjectTable, MainDeclDef, 
python .\RemoveGUIModule.py
popd
rem pause