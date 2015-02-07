"""
   DICOM Image Editor (DIE)
   Copyright (C) 2015  Helder Oliveira

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

   You should have received a copy of the GNU General Public License along
   with this program; if not, write to the Free Software Foundation, Inc.,
   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 """

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
        self.connect(self.actionAboutQt, SIGNAL('triggered()'), self, SLOT('act_about_qt()'))
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
                          'DICOM Image Editor (DIE)',
                          '<p><font size=\"+4\">DICOM Image Editor</font></p>'
                          '<p>Software to edit headers of DICOM files!</p>'
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
