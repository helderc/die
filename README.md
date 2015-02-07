# DICOM Image Editor (DIE)

This software is a DICOM editor. *It doesn't permit you change the image inside a DICOM file*.

Some features, meant to be developed (so far) are:
- Clone DICOM header;
- Edit specific tags on header.


## Generating correct resource file
Just type:

`$ pyrcc4 -o mainwindow_qrc.py resource.qrc -py3`