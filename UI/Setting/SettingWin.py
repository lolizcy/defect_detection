# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingWin1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtGui import  QPalette, QColor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class SettingWin(QWidget):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(1293, 888)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Setting)
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Carmer_control = QtWidgets.QGroupBox(Setting)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Carmer_control.setFont(font)
        self.Carmer_control.setObjectName("Carmer_control")
        self.gridLayout = QtWidgets.QGridLayout(self.Carmer_control)
        self.gridLayout.setObjectName("gridLayout")
        self.carmer_one = QtWidgets.QCheckBox(self.Carmer_control)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.carmer_one.setFont(font)
        self.carmer_one.setObjectName("carmer_one")
        self.gridLayout.addWidget(self.carmer_one, 0, 0, 1, 1)
        self.carmer_two = QtWidgets.QCheckBox(self.Carmer_control)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.carmer_two.setFont(font)
        self.carmer_two.setObjectName("carmer_two")
        self.gridLayout.addWidget(self.carmer_two, 1, 0, 1, 1)
        self.carmer_three = QtWidgets.QCheckBox(self.Carmer_control)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.carmer_three.setFont(font)
        self.carmer_three.setObjectName("carmer_three")
        self.gridLayout.addWidget(self.carmer_three, 2, 0, 1, 1)
        self.carmer_four = QtWidgets.QCheckBox(self.Carmer_control)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.carmer_four.setFont(font)
        self.carmer_four.setObjectName("carmer_four")
        self.gridLayout.addWidget(self.carmer_four, 3, 0, 1, 1)
        self.carmer_all = QtWidgets.QCheckBox(self.Carmer_control)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.carmer_all.setFont(font)
        self.carmer_all.setObjectName("carmer_all")
        self.gridLayout.addWidget(self.carmer_all, 4, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.Carmer_control)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Acquisition_Control = QtWidgets.QGroupBox(Setting)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Acquisition_Control.setFont(font)
        self.Acquisition_Control.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Acquisition_Control.setObjectName("Acquisition_Control")
        self.layoutWidget = QtWidgets.QWidget(self.Acquisition_Control)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 26, 391, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fps_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fps_label.setFont(font)
        self.fps_label.setObjectName("fps_label")
        self.horizontalLayout.addWidget(self.fps_label)
        self.fps_value_label = QtWidgets.QLabel(self.layoutWidget)
        self.fps_value_label.setText("")
        self.fps_value_label.setObjectName("fps_value_label")
        self.horizontalLayout.addWidget(self.fps_value_label)
        self.verticalLayout.addWidget(self.Acquisition_Control)
        self.TrainSetting = QtWidgets.QGroupBox(Setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TrainSetting.setFont(font)
        self.TrainSetting.setObjectName("TrainSetting")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.TrainSetting)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.epoch_lineEdit = QtWidgets.QLineEdit(self.TrainSetting)
        self.epoch_lineEdit.setObjectName("epoch_lineEdit")
        self.gridLayout_4.addWidget(self.epoch_lineEdit, 0, 1, 1, 1)
        self.epoch_label = QtWidgets.QLabel(self.TrainSetting)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.epoch_label.setFont(font)
        self.epoch_label.setObjectName("epoch_label")
        self.gridLayout_4.addWidget(self.epoch_label, 0, 0, 1, 1)
        self.batch_size_label = QtWidgets.QLabel(self.TrainSetting)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.batch_size_label.setFont(font)
        self.batch_size_label.setObjectName("batch_size_label")
        self.gridLayout_4.addWidget(self.batch_size_label, 1, 0, 1, 1)
        self.train_model_label = QtWidgets.QLabel(self.TrainSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.train_model_label.sizePolicy().hasHeightForWidth())
        self.train_model_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.train_model_label.setFont(font)
        self.train_model_label.setObjectName("train_model_label")
        self.gridLayout_4.addWidget(self.train_model_label, 2, 0, 1, 1)
        self.semi_train = QtWidgets.QRadioButton(self.TrainSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semi_train.sizePolicy().hasHeightForWidth())
        self.semi_train.setSizePolicy(sizePolicy)
        self.semi_train.setMaximumSize(QtCore.QSize(150, 16777215))
        self.semi_train.setObjectName("semi_train")
        self.gridLayout_4.addWidget(self.semi_train, 2, 1, 1, 1)
        self.batch_size_lineEdit = QtWidgets.QLineEdit(self.TrainSetting)
        self.batch_size_lineEdit.setObjectName("batch_size_lineEdit")
        self.gridLayout_4.addWidget(self.batch_size_lineEdit, 1, 1, 1, 1)
        self.normal_train = QtWidgets.QRadioButton(self.TrainSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normal_train.sizePolicy().hasHeightForWidth())
        self.normal_train.setSizePolicy(sizePolicy)
        self.normal_train.setMaximumSize(QtCore.QSize(150, 16777215))
        self.normal_train.setObjectName("normal_train")
        self.gridLayout_4.addWidget(self.normal_train, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.TrainSetting)
        self.Skin_Setting = QtWidgets.QGroupBox(Setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Skin_Setting.setFont(font)
        self.Skin_Setting.setObjectName("Skin_Setting")
        self.bright_radioButton = QtWidgets.QRadioButton(self.Skin_Setting)
        self.bright_radioButton.setGeometry(QtCore.QRect(30, 40, 101, 20))
        self.bright_radioButton.setObjectName("bright_radioButton")
        self.dark_radioButton = QtWidgets.QRadioButton(self.Skin_Setting)
        self.dark_radioButton.setGeometry(QtCore.QRect(190, 40, 101, 20))
        self.dark_radioButton.setObjectName("dark_radioButton")
        self.verticalLayout.addWidget(self.Skin_Setting)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.Image_Format_Control = QtWidgets.QGroupBox(Setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_Format_Control.sizePolicy().hasHeightForWidth())
        self.Image_Format_Control.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Image_Format_Control.setFont(font)
        self.Image_Format_Control.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Image_Format_Control.setObjectName("Image_Format_Control")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Image_Format_Control)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.WidthMax_label = QtWidgets.QLabel(self.Image_Format_Control)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WidthMax_label.setFont(font)
        self.WidthMax_label.setObjectName("WidthMax_label")
        self.gridLayout_3.addWidget(self.WidthMax_label, 0, 0, 1, 1)
        self.WidthMax_value_label = QtWidgets.QLabel(self.Image_Format_Control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WidthMax_value_label.sizePolicy().hasHeightForWidth())
        self.WidthMax_value_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WidthMax_value_label.setFont(font)
        self.WidthMax_value_label.setText("")
        self.WidthMax_value_label.setObjectName("WidthMax_value_label")
        self.gridLayout_3.addWidget(self.WidthMax_value_label, 0, 1, 1, 1)
        self.HeightMax_label = QtWidgets.QLabel(self.Image_Format_Control)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HeightMax_label.setFont(font)
        self.HeightMax_label.setObjectName("HeightMax_label")
        self.gridLayout_3.addWidget(self.HeightMax_label, 1, 0, 1, 1)
        self.HeightMax_value_label = QtWidgets.QLabel(self.Image_Format_Control)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeightMax_value_label.sizePolicy().hasHeightForWidth())
        self.HeightMax_value_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HeightMax_value_label.setFont(font)
        self.HeightMax_value_label.setText("")
        self.HeightMax_value_label.setObjectName("HeightMax_value_label")
        self.gridLayout_3.addWidget(self.HeightMax_value_label, 1, 1, 1, 1)
        self.Width_label = QtWidgets.QLabel(self.Image_Format_Control)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Width_label.setFont(font)
        self.Width_label.setObjectName("Width_label")
        self.gridLayout_3.addWidget(self.Width_label, 2, 0, 1, 1)
        self.Width_spinBox = QtWidgets.QSpinBox(self.Image_Format_Control)
        self.Width_spinBox.setObjectName("Width_spinBox")
        self.gridLayout_3.addWidget(self.Width_spinBox, 2, 1, 1, 1)
        self.Height_label = QtWidgets.QLabel(self.Image_Format_Control)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Height_label.setFont(font)
        self.Height_label.setObjectName("Height_label")
        self.gridLayout_3.addWidget(self.Height_label, 3, 0, 1, 1)
        self.Height_spinBox = QtWidgets.QSpinBox(self.Image_Format_Control)
        self.Height_spinBox.setObjectName("Height_spinBox")
        self.gridLayout_3.addWidget(self.Height_spinBox, 3, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.Image_Format_Control)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.model_setting = QtWidgets.QGroupBox(Setting)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.model_setting.setFont(font)
        self.model_setting.setObjectName("model_setting")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.model_setting)
        self.gridLayout_2.setHorizontalSpacing(35)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.weights_label = QtWidgets.QLabel(self.model_setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weights_label.setFont(font)
        self.weights_label.setObjectName("weights_label")
        self.gridLayout_2.addWidget(self.weights_label, 0, 0, 1, 1)
        self.weights_lineEdit = QtWidgets.QLineEdit(self.model_setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weights_lineEdit.sizePolicy().hasHeightForWidth())
        self.weights_lineEdit.setSizePolicy(sizePolicy)
        self.weights_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.weights_lineEdit.setObjectName("weights_lineEdit")
        self.gridLayout_2.addWidget(self.weights_lineEdit, 0, 1, 1, 1)
        self.weights_upload = QtWidgets.QPushButton(self.model_setting)
        self.weights_upload.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weights_upload.setFont(font)
        self.weights_upload.setObjectName("weights_upload")
        self.gridLayout_2.addWidget(self.weights_upload, 0, 2, 1, 1)
        self.img_save_path_label = QtWidgets.QLabel(self.model_setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.img_save_path_label.setFont(font)
        self.img_save_path_label.setObjectName("img_save_path_label")
        self.gridLayout_2.addWidget(self.img_save_path_label, 1, 0, 1, 1)
        self.save_path_lineEdit = QtWidgets.QLineEdit(self.model_setting)
        self.save_path_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.save_path_lineEdit.setObjectName("save_path_lineEdit")
        self.gridLayout_2.addWidget(self.save_path_lineEdit, 1, 1, 1, 1)
        self.img_path_open = QtWidgets.QPushButton(self.model_setting)
        self.img_path_open.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.img_path_open.setFont(font)
        self.img_path_open.setObjectName("img_path_open")
        self.gridLayout_2.addWidget(self.img_path_open, 1, 2, 1, 1)
        self.cfg_label = QtWidgets.QLabel(self.model_setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cfg_label.setFont(font)
        self.cfg_label.setObjectName("cfg_label")
        self.gridLayout_2.addWidget(self.cfg_label, 2, 0, 1, 1)
        self.cfg_lineEdit = QtWidgets.QLineEdit(self.model_setting)
        self.cfg_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.cfg_lineEdit.setObjectName("cfg_lineEdit")
        self.gridLayout_2.addWidget(self.cfg_lineEdit, 2, 1, 1, 1)
        self.cfg_upload = QtWidgets.QPushButton(self.model_setting)
        self.cfg_upload.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cfg_upload.setFont(font)
        self.cfg_upload.setObjectName("cfg_upload")
        self.gridLayout_2.addWidget(self.cfg_upload, 2, 2, 1, 1)
        self.dataSet_label = QtWidgets.QLabel(self.model_setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dataSet_label.setFont(font)
        self.dataSet_label.setObjectName("dataSet_label")
        self.gridLayout_2.addWidget(self.dataSet_label, 3, 0, 1, 1)
        self.dataSet_lineEdit = QtWidgets.QLineEdit(self.model_setting)
        self.dataSet_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.dataSet_lineEdit.setObjectName("dataSet_lineEdit")
        self.gridLayout_2.addWidget(self.dataSet_lineEdit, 3, 1, 1, 1)
        self.dataSet_path_open = QtWidgets.QPushButton(self.model_setting)
        self.dataSet_path_open.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dataSet_path_open.setFont(font)
        self.dataSet_path_open.setObjectName("dataSet_path_open")
        self.gridLayout_2.addWidget(self.dataSet_path_open, 3, 2, 1, 1)
        self.model_save_label = QtWidgets.QLabel(self.model_setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.model_save_label.setFont(font)
        self.model_save_label.setObjectName("model_save_label")
        self.gridLayout_2.addWidget(self.model_save_label, 4, 0, 1, 1)
        self.model_save_lineEdit = QtWidgets.QLineEdit(self.model_setting)
        self.model_save_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.model_save_lineEdit.setObjectName("model_save_lineEdit")
        self.gridLayout_2.addWidget(self.model_save_lineEdit, 4, 1, 1, 1)


        self.model_save_path_open = QtWidgets.QPushButton(self.model_setting)
        self.model_save_path_open.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.model_save_path_open.setFont(font)
        self.model_save_path_open.setObjectName("model_save_path_open")
        self.gridLayout_2.addWidget(self.model_save_path_open, 4, 2, 1, 1)

        self.report_save_label = QtWidgets.QLabel(self.model_setting)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.report_save_label.setFont(font)
        self.report_save_label.setObjectName("report_save_label")
        self.gridLayout_2.addWidget(self.report_save_label, 5, 0, 1, 1)
        self.report_save_lineEdit = QtWidgets.QLineEdit(self.model_setting)
        self.report_save_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.report_save_lineEdit.setObjectName("report_save_lineEdit")
        self.gridLayout_2.addWidget(self.report_save_lineEdit, 5, 1, 1, 1)

        self.report_save_path_open = QtWidgets.QPushButton(self.model_setting)
        self.report_save_path_open.setMinimumSize(QtCore.QSize(0, 35))
        self.report_save_path_open.setFont(font)
        self.report_save_path_open.setObjectName("report_save_path_open")
        self.gridLayout_2.addWidget(self.report_save_path_open, 5, 2, 1, 1)




        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 7)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.verticalLayout_2.addWidget(self.model_setting)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.confirm = QtWidgets.QPushButton(Setting)
        self.confirm.setMinimumSize(QtCore.QSize(0, 40))
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_2.addWidget(self.confirm)
        self.cancel = QtWidgets.QPushButton(Setting)
        self.cancel.setMinimumSize(QtCore.QSize(0, 40))
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(Setting)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.Carmer_control.setTitle(_translate("Setting", "Carmer Control"))
        self.carmer_one.setText(_translate("Setting", "Carmer one"))
        self.carmer_two.setText(_translate("Setting", "Carmer two"))
        self.carmer_three.setText(_translate("Setting", "Carmer three"))
        self.carmer_four.setText(_translate("Setting", "Carmer four"))
        self.carmer_all.setText(_translate("Setting", "All"))
        self.Acquisition_Control.setTitle(_translate("Setting", "Acquisition Control"))
        self.fps_label.setText(_translate("Setting", "Acquisition Frame Rate(Fps):"))
        self.TrainSetting.setTitle(_translate("Setting", "Train Setting"))
        self.epoch_label.setText(_translate("Setting", "epochs:"))
        self.batch_size_label.setText(_translate("Setting", "batch-szie:"))
        self.train_model_label.setText(_translate("Setting", "train model:"))
        self.semi_train.setText(_translate("Setting", "semi-train"))
        self.normal_train.setText(_translate("Setting", "normal-train"))
        self.Skin_Setting.setTitle(_translate("Setting", "Skin Setting"))
        self.bright_radioButton.setText(_translate("Setting", "bright"))
        self.dark_radioButton.setText(_translate("Setting", "dark"))
        self.Image_Format_Control.setTitle(_translate("Setting", "Image Format Control"))
        self.WidthMax_label.setText(_translate("Setting", " WidthMax："))
        self.HeightMax_label.setText(_translate("Setting", " HeightMax："))
        self.Width_label.setText(_translate("Setting", " Width："))
        self.Height_label.setText(_translate("Setting", " Height:"))
        self.model_setting.setTitle(_translate("Setting", "Model Setting"))
        self.weights_label.setText(_translate("Setting", "import model weights:"))
        self.weights_upload.setText(_translate("Setting", "upload"))
        self.img_save_path_label.setText(_translate("Setting", "image save path:"))
        self.img_path_open.setText(_translate("Setting", "open"))
        self.cfg_label.setText(_translate("Setting", "import cfg:"))
        self.cfg_upload.setText(_translate("Setting", "upload"))
        self.dataSet_label.setText(_translate("Setting", "dataSet save path:"))
        self.dataSet_path_open.setText(_translate("Setting", "open"))
        self.model_save_label.setText(_translate("Setting", "model save path:"))
        self.model_save_path_open.setText(_translate("Setting", "open"))
        self.report_save_label.setText(_translate("Setting", "report save path:"))
        self.report_save_path_open.setText(_translate("Setting", "open"))
        self.confirm.setText(_translate("Setting", "确定"))
        self.cancel.setText(_translate("Setting", "取消"))
        pe = QPalette()
        Setting.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, QColor("#5A5A5A"))  # 设置背景色
        Setting.setPalette(pe)
        self.carmer_one.setStyleSheet("color: white")
        self.carmer_two.setStyleSheet("color: white")
        self.carmer_three.setStyleSheet("color: white")
        self.carmer_four.setStyleSheet("color: white")
        self.carmer_all.setStyleSheet("color: white")
        self.bright_radioButton.setStyleSheet("color: white;font-size:20px")
        self.dark_radioButton.setStyleSheet("color: white;font-size:20px")