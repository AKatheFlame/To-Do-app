import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("DarkAmber")

label1=sg.Text("Select archive:")
input1=sg.Input()
button1=sg.FileBrowse("Choose",key="archive")

label2=sg.Text("Select destination folder:")
input2=sg.Input()
button2=sg.FolderBrowse("Choose",key="folder")

extract_button=sg.Button("Extract")
output_label=sg.Text(key="output",text_color='green')

window=sg.Window("Archive Extractor",
                 layout=[[label1,input1,button1],
                         [label2,input2,button2],
                         [extract_button],
                         [output_label]])

while True:
    event,values=window.read()
    filepath=values['archive']
    dest_dir=values['folder']
    extract_archive(filepath,dest_dir)
    window["output"].update(value="Extraction Completed")

window.close()