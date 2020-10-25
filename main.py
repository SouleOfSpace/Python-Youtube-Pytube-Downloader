from main_window import Ui_Form
import progress_window
import downloader, utils

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import threading

import sys, os

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#Main Code
def setDirectori():
    '''Получаем путь к нужной директории'''
    try:
        dir_name = QFileDialog.getExistingDirectory()
        ui.lineEdit_2.setText(dir_name)
    except:
        return 0

def getDirectory():
    '''Возвращаем выбранный путь к директории, в которую хотим скачать файл'''
    path_dir = ui.lineEdit_2.text()
    return path_dir

def getRes():
    '''Возвращаем выбранное качество медиафайла'''
    index = ui.comboBox.currentIndex()
    res = ui.comboBox.itemText(index)[0:3]
    return res

def getURL():
    '''Получаем введенный URL'''
    URL = ui.lineEdit.text()
    return URL

def getSizeTubeFile(URL, res):
    '''Возвращаем полный размер медиафайла который пытаемся скачать'''
    size = downloader.getSizeTubeObject(URL, res)
    return size

def getSizeDownloadingFile():
    '''Возвращаем текущий размер файла, который скачиваем'''
    URL = getURL()
    res = getRes()
    filename = downloader.getTitleMediaFile(URL, res)
    path_directory = getDirectory()
    size_downloading_file_in_megabite = utils.getSizeFile(filename, path_directory)

    return size_downloading_file_in_megabite

def downloadFile():
    '''скачиваем видеофайл'''
    URL = getURL()
    res = getRes()
    path_directory = getDirectory()

    size_youtube_file_in_megabite = getSizeTubeFile(URL, res)

    downloader.main(URL, res, path_directory)
    progress_window.callDownloader(size_youtube_file_in_megabite)

ui.toolButton.clicked.connect(setDirectori)
ui.pushButton.clicked.connect(downloadFile)

Form.show()
sys.exit(app.exec_())
