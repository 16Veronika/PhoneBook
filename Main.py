import json
import easygui
if easygui.ccbox("Вы хотите начать? Continue - если да, Cancel - если нет.", "Пожалуйста выберете"):     # show a Continue/Cancel dialog
    pass  
else:
    sys.exit(0)
PHONEBOOK_FILE = "Contacs_list.json"
def load_phonebook():
    try:
        with open(PHONEBOOK_FILE, 'r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, 'w',encoding='utf-8') as file:
        json.dump(phonebook, file)

def view_contacts(phonebook):
    if not phonebook:
        print("Телефонный справочник пуст.")
    else:
        print("Телефонный справочник:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

def add_contact(phonebook, name, number):
    phonebook[name] = number
    save_phonebook(phonebook)
    print(f"Контакт '{name}' добавлен в телефонный справочник.")
    

def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
        print(f"Контакт '{name}' удален из телефонного справочника.")
    else:
        print(f"Контакт '{name}' не найден в телефонном справочнике.")

def search_contact(phonebook, name):
    if name in phonebook:
        print(f"Найден контакт '{name}': {phonebook[name]}")
    else:
        print(f"Контакт '{name}' не найден в телефонном справочнике.")

def edit_contact(phonebook, name, new_number):
    if name in phonebook:
        phonebook[name] = new_number
        save_phonebook(phonebook)
        print(f"Номер для контакта '{name}' изменен на '{new_number}'.")
    else:
        print(f"Контакт '{name}' не найден в телефонном справочнике.")

def import_contacts(phonebook, filename):
    try:
        with open(filename, 'r' ,encoding='utf-8') as file:
            data = json.load(file)
            phonebook.update(data)
            save_phonebook(phonebook)
            print(f"Контакты из файла '{filename}' импортированы в телефонный справочник.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

def main():
    phonebook = load_phonebook()

    while True:
        print("\nМеню:")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Найти контакт")
        print("5. Изменить номер контакта")
        print("6. Импортировать контакты из файла")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            view_contacts(phonebook)
        elif choice == "2":
            name = input("Введите имя контакта: ")
            number = input("Введите номер контакта: ")
            add_contact(phonebook, name, number)
        elif choice == "3":
            name = input("Введите имя контакта для удаления: ")
            delete_contact(phonebook, name)
        elif choice == "4":
            name = input("Введите имя контакта для поиска: ")
            search_contact(phonebook, name)
        elif choice == "5":
            name = input("Введите имя контакта для изменения номера: ")
            new_number = input("Введите новый номер: ")
            edit_contact(phonebook, name, new_number)
        elif choice == "6":
            filename = input("Введите имя файла для импорта контактов: ")
            import_contacts(phonebook, filename)
        elif choice == "7":
                result = easygui.buttonbox("Вы действительно хотите выйти?","Выход", choices=["Да", "Нет"])
                if result == "Да":
                    break
                elif result == "Нет":
                    continue
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()