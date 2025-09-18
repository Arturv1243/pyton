# Технические требования к заданию:
# Поиск слов в тексте
# Задание:
# • Дана книга в файле book.txt.
# • Напиши функцию word_count(filename), которая возвращает
# количество всех слов в книге.
# • Напиши функцию find_word(filename, word), которая
# возвращает,
# сколько раз встречается указанное слово (без учёта
# регистра).
# • Напиши функцию save_statistics(filename), которая создаёт
# файл
# stats.txt с результатами анализа (общее количество слов,
# топ-5 самых частых слов).
# Дополнительно: исключить стоп-слова (например: "и", "в",
# "на", "с").
import os

NOTES_DIR = 'notes'

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)


def create_note():
    title = input('Введите заголовок заметки: ').strip()
    filename = os.path.join(NOTES_DIR, f"{title}.txt")
    if os.path.exists(filename):
        print('Заметка с таким заголовком уже существует.')
        return
    print('Введите текст заметки. Для завершения введите пустую строку.')
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line)
    content = '\n'.join(lines)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Заметка сохранена.')


def list_notes():
    notes = os.listdir(NOTES_DIR)
    if not notes:
        print('Нет сохранённых заметок.')
        return
    print('Список заметок:')
    for note_file in notes:
        if note_file.endswith('.txt'):
            print(' - ' + note_file[:-4])  # выводим заголовок без расширения


def read_note():
    title = input('Введите заголовок заметки для чтения: ').strip()
    filename = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(filename):
        print('Заметка с таким заголовком не найдена.')
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f'Содержание заметки "{title}":')
    print(content)


def delete_note():
    title = input('Введите заголовок заметки для удаления: ').strip()
    filename = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(filename):
        print('Заметка с таким заголовком не найдена.')
        return
    os.remove(filename)
    print('Заметка удалена.')


def main():
    while True:
        print('\nВыберите действие:')
        print('1: Создать заметку')
        print('2: Просмотреть список заметок')
        print('3: Читать заметку')
        print('4: Удалить заметку')
        print('5: Выйти')
        choice = input('Ваш выбор: ').strip().lower()

        if choice == '1':
            create_note()
        elif choice == '2':
            list_notes()
        elif choice == '3':
            read_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print('Выход из программы.')
            break
        else:
            print('Некорректный ввод, попробуйте еще раз.')


if __name__ == '__main__':
    main()