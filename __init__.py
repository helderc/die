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

# !/usr/bin/python
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
        for key in sorted(dcm_file.keys()):
            #print(key, '\t\t\t', dcm_file[key].value)
            #if (key != '(0019, 1061)' and key != '(0019, 1063)'):

            #node_id = parent + "." + hex(id(data_element))

            item_text = str(key) + ' --> '

            data_element = dcm_file[key]

            if isinstance(data_element.value, str):
                item_text = item_text + data_element.value
            if data_element.VR == "SQ":   # a sequence
                item_text2 = ''
                for i, dataset in enumerate(data_element.value):
                    sq_item_description = data_element.name.replace(" Sequence", "")  # XXX not i18n
                    item_text2.__add__("{0:s} {1:d}".format(sq_item_description, i + 1))

                item_text = item_text2

            #print(str(key) + ' --> ' + str(type(dcm_file[key].value)) + ': ' +  str(dcm_file[key].VR))

            item = QListWidgetItem(item_text)
            self.listWidgetLeft.addItem(item)

            #TODO: Create a model of QListView to insert each header line on it.

    """
    SLOTS
    """

    @pyqtSlot()
    def act_open_image(self):
        print(self.sender().objectName())

        a = self.sender().objectName()
        type(a)

        if self.sender().objectName() == 'btnOpenImageLeft':
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
