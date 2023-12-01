import json
import os
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, created_at, updated_at, scheduled_time=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at
        self.scheduled_time = scheduled_time

class NoteManager:
    def __init__(self, notes_file='notes.json'):
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as file:
                notes_data = json.load(file)
                notes = [Note(**note_data) for note_data in notes_data]
                return notes
        else:
            return []

    def save_notes(self):
        notes_data = [{'note_id': note.note_id, 'title': note.title, 'body': note.body,
                       'created_at': note.created_at, 'updated_at': note.updated_at,
                       'scheduled_time': note.scheduled_time}
                      for note in self.notes]

        save_choice = input("Вы хотите сохранить изменения в файле? (1/2): ").lower()
        if save_choice == '1':
            with open(self.notes_file, 'w') as file:
                json.dump(notes_data, file, indent = 4)
            print("Изменения успешно сохранены.")
        
        elif save_choice == '2': 
            print("Изменения не сохранены.")
        else:
            print("Неверный выбор.")

    def create_note(self, title, body, scheduled_time=None):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note_id = len(self.notes) + 1
        new_note = Note(note_id, title, body, timestamp, timestamp, scheduled_time)
        self.notes.append(new_note)
        print(f'Заметка успешно создана..')

    def list_notes(self):
        print('\n' + '='*100)
        if not self.notes:
            print("Нет доступных заметок.")
        else:
            for note in self.notes:
                scheduled_info = f"Запланированное время: {note.scheduled_time}" if note.scheduled_time else ""
                print(f"{note.note_id}. {note.title} - Создано: {note.created_at}, Изменено: {note.updated_at}, {scheduled_info}")
        print('='*100 + '\n')

    def view_note(self, note_id):
        print('\n' + '='*100)
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note:
            scheduled_info = f"Запланированное время: {note.scheduled_time}" if note.scheduled_time else ""
            print(f"{note.title}\n{note.body}\nСоздано: {note.created_at}, Изменено: {note.updated_at}, {scheduled_info}")
        else:
            print("\nЗаметка не найдена.")
        print('='*100 + '\n')

    def edit_note(self, note_id, title, body, scheduled_time=None):
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note:
            note.title = title
            note.body = body
            note.scheduled_time = scheduled_time
            note.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("\nЗаметка успешно отредактирована.")
        else:
            print("\nЗаметка не найдена.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        print("\nЗаметка удалена.")

    def select_notes_by_date(self, start_date, end_date):
        sort_options = {'1': 'created_at', '2': 'updated_at', '3': 'scheduled_time'}
        print("Сортировать по...")
        print("1. По времени создания")
        print("2. По времени изменения")
        print("3. По запланированному времени")
        
        choice = input("Введите ваш выбор (1/2/3): ")

        if choice not in sort_options:
            print("Неверный выбор.")   
        else:
            sort_by = sort_options[choice]
        
        selected_notes = sorted(
            [note for note in self.notes if start_date <= note.created_at <= end_date],
            key=lambda note: getattr(note, sort_by)
        )
        print('\n' + '='*100)
        if not selected_notes:
            print("В указанном диапазоне заметки не найдены.")
        else:
            for note in selected_notes:
                scheduled_info = f", Запланированное время: {note.scheduled_time}" if note.scheduled_time else ""
                
                print(f"{note.note_id}. {note.title} - "
                      f"Создано: {note.created_at}, Обновлено: {note.updated_at}{scheduled_info}")
        print('='*100+'\n') 


if __name__ == "__main__":
    manager = NoteManager()

    while True:
        print("Меню:")
        print("1. Создать заметку")
        print("2. Список всех заметок")
        print("3. Просмотр заметки")
        print("4. Редактирование заметки")
        print("5. Удаление заметки")
        print("6. Сортировка заметок по...")
        print("7. Сохранение изменений и/или выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            scheduled_time = input("Введите запланированное время. Формат: YYYY-MM-DD (выбор можно пропустить, нажав Enter): ")
            manager.create_note(title, body, scheduled_time)
        
        elif choice == "2":
            manager.list_notes()
        
        elif choice == "3":
            note_id = int(input("Введите ID заметки: "))
            manager.view_note(note_id)
       
        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок: ")
            body = input("Введите новый текст: ")
            scheduled_time = input("Введите новое запланированное время. Формат: YYYY-MM-DD (выбор можно пропустить, нажав Enter): ")
            manager.edit_note(note_id, title, body, scheduled_time)
       
        elif choice == "5":
            note_id = int(input("Введите ID заметки для удаления: "))
            manager.delete_note(note_id)
      
        elif choice == "6":
            start_date = input("Введите начальную дату (Формат: YYYY-MM-DD): ")
            end_date = input("Введите конечную дату (Формат: YYYY-MM-DD): ")
            manager.select_notes_by_date(start_date, end_date)
       
        elif choice == "7":
            manager.save_notes()
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор.")