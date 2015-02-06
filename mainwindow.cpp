#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionAbout_triggered()
{
    QMessageBox::about(this,
                       tr("About DIE"),
                       QString("DICOM Image Editor a.k.a. DIE\n\n" \
                               "by Helder Oliveira\n" \
                               "heldercro@gmail.com"));
}
