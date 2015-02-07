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
import dicom

from PyQt4.QtGui import *
from PyQt4.QtCore import *

# module to read the .ui file
from PyQt4.uic import *

# loading resource file
import mainwindow_qrc


class Main(QMainWindow):
    """
    MainWindow class
    """
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        loadUi('mainwindow.ui', self)

        # connecting signals to slots
        self.connect(self.btnOpenImageLeft, SIGNAL('clicked()'),
                     self, SLOT('act_open_image()'))
        self.connect(self.btnOpenImageRight, SIGNAL('clicked()'),
                     self, SLOT('act_open_image()'))
        self.connect(self.actionAboutQt, SIGNAL('triggered()'),
                     self, SLOT('act_about_qt()'))
        self.connect(self.actionAbout, SIGNAL('triggered()'),
                     self, SLOT('act_about()'))

    def open_image(self, side):
        dcm_filename = QFileDialog.getOpenFileName(None,
                                                   'Open image', 'image',
                                                   'DICOM (*.dcm *.dicom);;'
                                                   'All files (*)')
        dcm = dicom.read_file(dcm_filename)
        self.parse_dicom_header(dcm, side)


    def parse_dicom_header(self, dcm_file, side):
        for n, line in enumerate(dcm_file):
            print(n, line)

    """
    SLOTS
    """

    @pyqtSlot()
    def act_open_image(self):
        print(self.sender().objectName())

        if self.sender() == 'btnOpenImageLeft':
            print('LEFT Side')
            self.open_image('left')
        else:
            print('RIGTH Side')
            self.open_image('right')

    @pyqtSlot()
    def act_about(self):
        QMessageBox.about(self,
                          'DICOM Image Editor (DIE)',
                          '<p><font size="+4">DICOM Image Editor</font></p>'
                          '<p>Software to edit headers of DICOM files!</p>'
                          '<p><a href="http://helderc.github.io">'
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
