__author__ = 'Helder'

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

# module to read the .ui file
from PyQt4.uic import *


class Main(QMainWindow):
    """
    MainWindow class
    """
    # Janela principal
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        loadUi('mainwindow.ui', self)

        # image's file name
        self.arqImg = None

        # conectando os sinais aos slots
        # self.connect(self.actionAboutQt, SIGNAL('triggered()'), self, SLOT('act_about_qt()'))
        self.connect(self.actionAbout, SIGNAL('triggered()'), self, SLOT('act_about()'))


    def open_image(self):
        self.arqImg = QFileDialog.getOpenFileName(None,
                                                  'Open image', 'Image',
                                                  'Image (*.tif *.tiff *.bmp'
                                                  '*.jpg *.jpeg *.gif *.png);;'
                                                  'All files (*)')

    '''
    SLOTS
    '''

    @pyqtSlot()
    def act_open_image(self):
        self.open_image()

    @pyqtSlot()
    def act_about(self):
        QMessageBox.about(self,
                          'DICOM Image Editor',
                          '<p><font size=\"+4\">DICOM Image Editor</font><br><br>'
                          'Software to edit headers of DICOM files!</p>'
                          '<p><a href=\"http://helderc.github.io\">'
                          'http://helderc.github.io</a></p>')

    @pyqtSlot()
    def act_about_qt(self):
        QMessageBox.aboutQt(self, 'About Qt...')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    DIEWindow = Main()
    DIEWindow.setWindowTitle('DICOM Image Editor')
    DIEWindow.show()
    sys.exit(app.exec_())
