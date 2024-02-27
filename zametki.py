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

def read_note():
    if not os.path.exists("Notes"):
        print("Папки \"Notes\" не существует")
        return
    
    _title = input("Введите название заметки: ")
    if not os.path.exists(f"Notes/{_title}.json"):
        print("Заметки не найдена")
        return
    
    with open(f"Notes/{_title}.json", "r") as _note_file:
        for _line in _note_file:
            _split_line = _line.split(";")
            print(">>: " + _split_line[0])
            print("# : " + _split_line[1])
            break    

def edit_note():
    if not os.path.exists("Notes"):
        print("Папки \"Notes\" не существует")
        return
    
    _title = input("Введите название заметки: ")
    if not os.path.exists(f"Notes/{_title}.json"):
        print("Заметки не найдена")
        return

    with open(f"Notes/{_title}.json", "r") as _note_file:
        for _line in _note_file:
            _split_line = _line.split(";")
            print(">>: " + _split_line[0])
            print("# : " + _split_line[1])
            break
            
    _note = input("Введите новый текст заметки: ")
    
    with open(f"Notes/{_title}.json", "w") as _file:
        _file.write(_title)
        _file.write(";")
        _file.write(_note)
        
    print(f"Заметка {_title} отредактирована")

def delete_note():
    if not os.path.exists("Notes"):
        print("Папки \"Notes\" не существует")
        return
    
    _title = input("Введите название заметки: ")
    if not os.path.exists(f"Notes/{_title}.json"):
        print("Заметка не найдена")
        return
    
    os.remove(f"Notes/{_title}.json")
    print(f"Заметка {_title} удалена")    

while (True):
    print("Работа с заметками.")
    print("Выберите действие:")
    print("1 - Новая заметка")
    print("2 - Посмотреть заголовки заметок")
    print("3 - Прочесть заметку")
    print("4 - Редактировать заметку")
    print("5 - Удалить заметку")
    print("6 - Выход")
    _user_choice = input("Выберите опцию (1-6): ")
    
    if _user_choice == "1":
        create_note()
        print("Для продолжения нажмите Enter")
        input()
    elif _user_choice == "2":
        read_title_notes()
        print("Для продолжения нажмите Enter")
        input()
    elif _user_choice == "3":
        read_note()
        print("Для продолжения нажмите Enter")
        input()
    elif _user_choice == "4":
        edit_note()
        print("Для продолжения нажмите Enter")
        input()
    elif _user_choice == "5":
        delete_note()
        print("Для продолжения нажмите Enter")
        input()
    elif _user_choice == "6":
        break
    else:
        print("Неверный выбор. Введите заново.")