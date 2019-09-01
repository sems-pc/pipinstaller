# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pip-gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import webbrowser
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 166)
        MainWindow.setMinimumSize(QtCore.QSize(503, 166))
        MainWindow.setMaximumSize(QtCore.QSize(503, 166))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 131))
        self.tabWidget.setObjectName("tabWidget")
        self.install = QtWidgets.QWidget()
        self.install.setObjectName("install")
        self.label = QtWidgets.QLabel(self.install)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.package_name = QtWidgets.QPlainTextEdit(self.install)
        self.package_name.setGeometry(QtCore.QRect(100, 20, 271, 31))
        self.package_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.package_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.package_name.setObjectName("package_name")
        self.install_button = QtWidgets.QPushButton(self.install)
        self.install_button.setGeometry(QtCore.QRect(380, 30, 80, 24))
        self.install_button.setObjectName("install_button")
        self.tabWidget.addTab(self.install, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.mirror = QtWidgets.QPlainTextEdit(self.tab_2)
        self.mirror.setGeometry(QtCore.QRect(100, 10, 271, 31))
        self.mirror.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mirror.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mirror.setObjectName("mirror")
        self.ustc = QtWidgets.QPushButton(self.tab_2)
        self.ustc.setGeometry(QtCore.QRect(220, 60, 80, 24))
        self.ustc.setObjectName("ustc")
        self.save_mirror = QtWidgets.QPushButton(self.tab_2)
        self.save_mirror.setGeometry(QtCore.QRect(380, 20, 80, 24))
        self.save_mirror.setObjectName("save_mirror")
        self.tuna = QtWidgets.QPushButton(self.tab_2)
        self.tuna.setGeometry(QtCore.QRect(130, 60, 80, 24))
        self.tuna.setObjectName("tuna")
        self.custom = QtWidgets.QPushButton(self.tab_2)
        self.custom.setGeometry(QtCore.QRect(310, 60, 80, 24))
        self.custom.setObjectName("custom")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.douban = QtWidgets.QPushButton(self.tab_2)
        self.douban.setGeometry(QtCore.QRect(40, 60, 80, 24))
        self.douban.setObjectName("douban")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.timeout = QtWidgets.QSpinBox(self.tab)
        self.timeout.setGeometry(QtCore.QRect(170, 40, 71, 24))
        self.timeout.setMaximum(600)
        self.timeout.setObjectName("timeout")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.savetimeout = QtWidgets.QPushButton(self.tab)
        self.savetimeout.setGeometry(QtCore.QRect(260, 40, 80, 24))
        self.savetimeout.setObjectName("savetimeout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.github = QtWidgets.QPushButton(self.tab_3)
        self.github.setGeometry(QtCore.QRect(10, 60, 80, 24))
        self.github.setObjectName("github")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.github.clicked.connect(lambda: github())
        self.install_button.clicked.connect(lambda: install_package())
        self.savetimeout.clicked.connect(lambda: set_timeout())
        self.tuna.clicked.connect(lambda: set_tuna())
        self.ustc.clicked.connect(lambda: set_ustc())
        self.douban.clicked.connect(lambda: set_douban())
        self.custom.clicked.connect(lambda: set_custom())
        self.save_mirror.clicked.connect(lambda: save_mirror())

        def save_mirror():
            mirror_url = self.mirror.toPlainText()
            cmd = "pip config set global.index-url %s" % mirror_url
            r = os.popen(cmd)
            info = r.readlines()
            for line in info:  # 按行遍历
                lines = line.strip('\r\n')
                # print(lines)
                if "Writing to" in lines:
                    self.statusbar.showMessage("Success!")

        def set_custom():
            self.mirror.setPlainText("")

        def set_ustc():
            self.mirror.setPlainText("https://pypi.mirrors.ustc.edu.cn/simple/")

        def set_douban():
            self.mirror.setPlainText("https://pypi.douban.com/simple/")

        def set_tuna():
            self.mirror.setPlainText("https://pypi.tuna.tsinghua.edu.cn/simple")

        def install_package():
            self.statusbar.showMessage("Installing......")
            # print(timeout)
            if timeout == 0:
                cmd = "pip3 install %s" % self.package_name.toPlainText()
            else:
                cmd = "pip3 install %s --timeout=%s" % (self.package_name.toPlainText(), timeout)
            r = os.popen(cmd)  # 执行该命令
            info = r.readlines()
            for line in info:  # 按行遍历
                lines = line.strip('\r\n')
                print(lines)
                if "Successfully installed" in lines:
                    self.statusbar.showMessage("Success!")
                elif "Requirement already satisfied" in lines:
                    self.statusbar.showMessage("Requirement already satisfied!")
                else:
                    self.statusbar.showMessage("Failed!")

        def github():
            webbrowser.open('https://github.com/Chrithon/pipinstaller')

        def set_timeout():
            global timeout
            timeout = self.timeout.value()
            # print(timeout)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Package"))
        self.install_button.setText(_translate("MainWindow", "install"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.install), _translate("MainWindow", "Install"))
        self.ustc.setText(_translate("MainWindow", "USTC"))
        self.save_mirror.setText(_translate("MainWindow", "OK"))
        self.tuna.setText(_translate("MainWindow", "Tuna"))
        self.custom.setText(_translate("MainWindow", "Custom"))
        self.label_2.setText(_translate("MainWindow", "Mirror"))
        self.douban.setText(_translate("MainWindow", "Douban"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mirror Setting"))
        self.label_3.setText(_translate("MainWindow", "Timeout"))
        self.savetimeout.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Timeout Settings"))
        self.label_4.setText(_translate("MainWindow", "Pip Installer v1.0"))
        self.github.setText(_translate("MainWindow", "Github"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "About"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PipInstaller", "PipInstaller"))
        self.label.setText(_translate("MainWindow", "Package"))
        self.install_button.setText(_translate("MainWindow", "install"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.install), _translate("MainWindow", "Install"))
        self.ustc.setText(_translate("MainWindow", "USTC"))
        self.save_mirror.setText(_translate("MainWindow", "OK"))
        self.tuna.setText(_translate("MainWindow", "Tuna"))
        self.custom.setText(_translate("MainWindow", "Custom"))
        self.label_2.setText(_translate("MainWindow", "Mirror"))
        self.douban.setText(_translate("MainWindow", "Douban"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Mirror Setting"))
        self.label_3.setText(_translate("MainWindow", "Timeout"))
        self.savetimeout.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Timeout Settings"))
        self.label_4.setText(_translate("MainWindow", "Pip Installer v1.0 "))
        self.github.setText(_translate("MainWindow", "Github"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "About"))


if __name__ == "__main__":
    timeout = 0
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
