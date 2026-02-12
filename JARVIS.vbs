Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Path ke Python 3.12
pythonPath = "C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe"
scriptFolder = objFSO.GetParentFolderName(WScript.ScriptFullName)
windowsScript = scriptFolder & "\jarvis_windows.py"
textScript = scriptFolder & "\jarvis_text.py"

' Coba Windows TTS dulu (lebih stable)
on error resume next
objShell.Run pythonPath & " """ & windowsScript & """", 1, False

' Jika error, coba pyttsx3
if err.number <> 0 then
    objShell.Run pythonPath & " """ & textScript & """", 1, False
end if

