#! python3
# бэкап папки с содержимым в zip

import os, zipfile, datetime, shutil, tkinter, sys
from tkinter import filedialog
from tkinter import messagebox

def backupToZip(folder):
    back = filedialog.askdirectory(title='Выберите папку, КУДА сохранить архив')
    if back:
        folder = os.path.abspath(folder)
        dateraw = datetime.datetime.now()
        date = dateraw.strftime('%Y-%m-%d_%H%M%S')
        zipFileName = os.path.basename(folder) + "_" + str(date)+".zip" #  составляем имя файла
        # создать zip
        print("Создается файл %s..." % (zipFileName))
        backupZip = zipfile.ZipFile(back+"\\"+zipFileName, "w")
        # обход дерева папки и сжатие файлов
        print(folder)
        for foldername, subfolders, filenames in os.walk(folder):
            print("Добавление файлов из папки %s..." % (foldername))
            # Добавить в zip текущую папку
            backupZip.write(foldername)
            # Добавить в zip все файлы из папки
            for filename in filenames:
                if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                    continue # don't backup the backup ZIP files
                backupZip.write(os.path.join(foldername, filename))  
        backupZip.close()
        #shutil.move(zipFileName, back)
        messagebox.showinfo("Результат", "Готово.")
    else:
        sys.exit()
root = tkinter.Tk()
root.withdraw()
# start = filedialog.askdirectory(parent=root,initialdir="/",title='Выберите папку, КОТОРУЮ нужно архивировать')
start = filedialog.askdirectory(title='Выберите папку, КОТОРУЮ нужно архивировать')
if start:
    backupToZip(start)
else:
    sys.exit()
