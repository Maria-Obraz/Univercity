import PySimpleGUI as sg
import os
import docx2pdf
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image

def menu():
    layout = [
        [sg.Text('Выберите действие')],
        [sg.Listbox(['Сменить рабочий каталог',
                     'Преобразовать PDF в Docx',
                     'Преобразовать Doc, Docx в PDF',
                     'Сжать изображение',
                     'Удалить группу файлов',
                     'Выход'], size=(50, 6), key='options')],
        [sg.Button('OK'), sg.Button('Cancel')]
    ]

    window = sg.Window('File Converter', layout, element_justification='c')
    event, values = window.Read()

    if event == 'OK':
        option = values['options'][0]
        window.Close()
        return event, option
    else:
        window.Close()
        return event, None


def change_dir():
    layout = [
        [sg.Text('Укажите путь к каталогу')],
        [sg.Input(key='directory'), sg.FolderBrowse()],
        [sg.Button('OK'), sg.Button('Cancel')]
    ]

    window = sg.Window('Directory', layout)
    event, values = window.Read()

    window.Close()

    if event == 'OK':
        try:
            os.chdir(values['directory'])
        except:
            sg.Popup('Неверный путь')
            change_dir()
        return os.getcwd()

    return None


def find_files(dir, format):
    files = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            if format.__contains__(file.split('.')[-1]):
                files.append(file)

    return files


def choose_files(files):
    layout = [
        [sg.Text('Выберите файл для конвертации:')],
        [sg.Listbox(files, size=(60, 10), key='files')],
        [sg.Button('OK'), sg.Button('Cancel')]
    ]

    window = sg.Window('Choose files', layout)

    event, values = window.Read()
    window.Close()

    if event == 'OK':
        file = values['files'][0]
        if file:
            convert_file(file)


def convert_file(file):
    format_file = file.split('.')[-1]

    if format_file == 'pdf':
        new_file = file.replace(format_file, 'docx')

        try:
            parse(file, new_file)
        except:
            sg.Popup(f'Невозможно преобразовать файл {file} в формат pdf')

    elif format_file.lower() in ['jpg', 'jpeg', 'png']:
        compress_file(file)

    elif format_file.lower() in ['doc', 'docx']:
        try:
            new_file = file.replace(format_file, 'pdf')
            docx2pdf.convert(os.path.abspath(file), os.path.abspath(new_file))
        except:
            sg.Popup(f'Невозможно преобразовать файл {file} в формат pdf')

    else:
        sg.Popup(f'Неподдерживаемый формат файла: {format_file}')

def compress_file(file):
    image = Image.open(file)
    image.save(file, optimize=True, quality=50)

def delete_files(files, separator=';'):
    files = files.split(separator)
    for file in files:
        try:
            os.remove(os.path.abspath(file))
        except:
            sg.Popup(f'Невозможно удалить файл: {file}')

if __name__ == '__main__':
    while True:
        event, option = menu()
        if event == 'OK':

            if option == 'Сменить рабочий каталог':
                change_dir()
            elif option == 'Преобразовать PDF в Docx':
                format = 'pdf'
                files = find_files(os.getcwd(), format)
                if len(files) == 0:
                    sg.Popup('Файлы для конвертации не найдены')
                else:
                    choose_files(files)
            elif option == 'Преобразовать Doc, Docx в PDF':
                format = ['doc', 'docx']
                files = find_files(os.getcwd(), format)
                if len(files) == 0:
                    sg.Popup('Файлы для конвертации не найдены')
                else:
                    choose_files(files)
            elif option == 'Сжать изображение':
                format = ['jpg', 'jpeg', 'png']
                files = find_files(os.getcwd(), format)
                if len(files) == 0:
                    sg.Popup('Изображения для сжатия не найдены')
                else:
                    choose_files(files)
            elif option == 'Удалить группу файлов':
                files = sg.PopupGetFile('Выберите файлы для удаления', multiple_files=True)
                if files is not None:
                    delete_files(files)
            else:
                break
        else:
            break