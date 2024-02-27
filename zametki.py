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

def read_title_notes():
    if not os.path.exists("Notes"):
        print("Папки \"Notes\" не существует")
        return
    
    _files = os.listdir("Notes")
    print("Список заметок:")
    for _file in _files:
        with open(f"Notes/{_file}", "r") as _note_file:
            for _line in _note_file:
                _split_line = _line.split(";")
                print(">>: " + _split_line[0])
                break
    
