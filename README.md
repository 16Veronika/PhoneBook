# Телефонный справочник
## ***Это простое консольное приложение с минимальным интерфейсом пользователя, предназначенное для управления телефонным справочником через командную строку.***

### Описание задачи.
Сделать консольное приложение Телефонный справочник с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.

## Структура приложения

### ***Импорт библиотек:***
```sh
import json
```
- Импортирует модуль json для работы с данными в формате JSON.

```sh
import easygui
```
- Импортирует модуль easygui, который предоставляет простые интерфейсы для создания диалоговых окон.

### ***Функции для работы с телефонным справочником:***
```sh
load_phonebook()
```
- Загружает телефонный справочник из файла JSON.
```sh
save_phonebook(phonebook)
```
- Сохраняет телефонный справочник в файл JSON.
```sh
view_contacts(phonebook) 
```
- Выводит на экран все контакты из телефонного справочника.
```sh
add_contact(phonebook, name, number)
```
- Добавляет новый контакт в телефонный справочник.
```sh
delete_contact(phonebook, name)
```
- Удаляет контакт из телефонного справочника.
```sh
search_contact(phonebook, name)
```
- Ищет контакт в телефонном справочнике по имени.
```sh
edit_contact(phonebook, name, new_number)
```
- Изменяет номер существующего контакта.

```sh
import_contacts(phonebook, filename) 
```
- Импортирует контакты из указанного файла в телефонный справочник.

### ***Основная функция main():***

Запускает основной цикл приложения.

Отображает меню для пользователя и обрабатывает выбор действия.

В зависимости от выбора пользователя вызывает соответствующие функции для работы с телефонным справочником.

Для выхода из приложения предоставляет пользователю возможность подтвердить свой выбор с помощью диалогового окна.
