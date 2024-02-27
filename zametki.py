import os

def create_note():
    _title = input("Введите название заметки: ")
    _note = input("Введите текст заметки: ")
    
    if not os.path.exists("Notes"):
        os.mkdir("Notes")
    
    _file_name = f"Notes/{_title}.json"
    
    with open(_file_name, "w") as _file:
        _file.write(_title)
        _file.write(";")
        _file.write(_note)
    
    print(f"Заметка {_title} успешно создана!")
    
