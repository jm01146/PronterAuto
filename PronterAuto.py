# imports for the project
import itertools
import time as t
import pywinauto
from pywinauto import mouse
from pywinauto.application import Application

# must be the printing time in seconds (round if have to)
time = 3600

# Connecting to Pronterface and Notepad after you manually boot it up (Don't hit start until you have you print running)
# run time warning is normal don't worry about it
app = Application(backend="uia").connect(title="Pronterface", timeout=100)
appDos = Application(backend="uia").connect(title="Untitled - Notepad", timeout=20)

# addressing what needs to be manipulated (don't mess with)
textEditor = app.Pronterface.child_window(auto_id="-31890", control_type='Edit').wrapper_object()
textEditorDos = appDos.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
sendButton = app.Pronterface.child_window(title="Send", auto_id="-31889", control_type="Button").wrapper_object()

# actual typing and send clicks repeated for a X amount of time(sleep function)
for _ in itertools.repeat(None, time):
    textEditor.type_keys("M114")
    sendButton.click_input()
    pywinauto.mouse.right_click(coords=(2080, 736))
    app.ContextMenu['Select All'].click_input()
    t.sleep(1)
    pywinauto.mouse.right_click(coords=(2080, 736))
    app.ContextMenu['Copy'].click_input()
    pywinauto.mouse.right_click(coords=(2763, 912))
    appDos.ContextMenu["Paste"].click_input()
    t.sleep(2)  # to make sure the program doesn't crash due to script overload

# don't need to use don't worry about it
# accessing control options for Pronterface
# app.Pronterface.print_control_identifiers()
