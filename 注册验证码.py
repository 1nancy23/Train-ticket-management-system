from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import random
import pymysql

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 460, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 360, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 90, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 56, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 56, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 140, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(234, 6, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(234, 6, 41))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 200, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(232, 9, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 9, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 250, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 7, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 7, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 300, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 13, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 13, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 410, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 11, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 11, 34))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 80, 241, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)


        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(220, 350, 161, 61))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.pushButton.clicked.connect(self.go_Log2)
        a = self.random_num()
        self.pushButton_3.setText(a)
        self.pushButton_3.clicked.connect(self.yzm)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.label_2.setVisible(False)
        self.label_3.setVisible(False)

        self.label.setVisible(False)     #手机号
        self.label_4.setVisible(False)   #密码
        self.label_5.setVisible(False)   #身份证
        self.label_6.setVisible(False)  #验证码

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.pushButton_2.setText(_translate("MainWindow", "返回"))
        self.label.setText(_translate("MainWindow", "当前手机号已存在"))
        self.label_2.setText(_translate("MainWindow", "当前用户名已存在"))
        self.label_3.setText(_translate("MainWindow", "请输入全部的信息"))
        self.label_4.setText(_translate("MainWindow", "密码不一致，请重新输入"))
        self.label_5.setText(_translate("MainWindow", "当身份证号已被绑定"))
        self.label_6.setText(_translate("MainWindow", "请重新输入验证码"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "请输入手机号"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入用户名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "再次输入确认密码"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "请输入身份证号"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "请输入验证码"))
        self.menu.setTitle(_translate("MainWindow", "账号注册"))

        #在进入注册界面时先生成一个随机验证码


    def yzm(self):
        b = self.random_num()
        self.pushButton_3.setText(b)

    def random_num(self):
        temp = ''
        check_num = 4   #验证码位数
        for i in range(check_num):  # check_num为需要循环的次数，也就是需要生成验证码的个数，默认为4
            choice = random.randint(1, 3)  # 生成1到3的随机数
            if choice  ==  1:  # 如果choice为1，则随机验证码的值为数字
                temp += random.choice('0123456789')
            elif choice  ==  2:  # 如果choice为2，则随机验证码的值为大写字母
                num = random.randint(65, 90)
                temp += chr(num)
            elif choice  ==  3:  # 如果choice为3，则随机验证码的值为小写字母
                num = random.randint(97, 122)
                temp += chr(num)
        return temp


    def go_Log2(self):

        conn = pymysql.connect(host='localhost',
                               port=3306,
                               user='root',
                               password='111111',
                               database='train',
                               charset='utf8')
        cursor = conn.cursor()
        success = 0     #用于确保全部注册信息都正确
        #每次点击确认出错后，下一次点击时先清空错误提示
        self.label.setVisible(False)     #手机号
        self.label_4.setVisible(False)   #密码
        self.label_5.setVisible(False)   #身份证
        self.label_6.setVisible(False)  #验证码

        tel = self.lineEdit_6.text()
        usr = self.lineEdit.text()
        pas1 = self.lineEdit_2.text()
        pas2 = self.lineEdit_3.text()
        ide = self.lineEdit_4.text()
        code = self.lineEdit_5.text()

        if tel != '' and usr != '' and pas1 != '' and pas2 != '' and ide != '' and code != '' :

            sql1 = "select * from 用户表 where 手机号 = '%s' " %(tel)
            cursor.execute(sql1)
            r = cursor.fetchall()
            lr = len(r)

            sql2 = "select * from 用户表 where 身份证号 = '%s' " %(ide)
            cursor.execute(sql2)
            r2 = cursor.fetchall()
            lr2 = len(r2)

            if lr != 0:
                self.label.setVisible(True)
                success = 1

            if lr2 != 0:
                self.label_5.setVisible(True)
                success = 1

            #获取当前的验证码的值
            c = self.pushButton_3.text()
            if code != c :
                #验证码输入错误时，自动刷新生成新的验证码
                self.yzm()
                self.label_6.setVisible(True)
                success = 1

            if pas1 != pas2 :
                self.label_4.setVisible(True)
                success = 1

            checkID = "select * from 身份表 where 姓名='%s' and 身份证号码='%s'" % (usr, ide)
            cursor.execute(checkID)
            if cursor.rowcount == 0:
                success = 1
                QMessageBox.critical(self, "身份信息错误", "请重新输入正确的身份信息")

            checkPhone = "select * from 手机号表 where 手机号码='%s'" % (tel)
            cursor.execute(checkPhone)
            if cursor.rowcount == 0:
                success = 1
                QMessageBox.critical(self, "手机号码错误", "请重新输入正确的手机号码信息")

            if success == 0:
                sql3 = "insert into 用户表 (手机号,密码,姓名,身份证号,余额) values ('%s','%s','%s','%s',0)" % (tel,pas1,usr,ide)
                cursor.execute(sql3)
                conn.commit() #提交数据
                QMessageBox.information(self, "注册", "注册成功！！！")
                self.pushButton_2.click()
        else:
            self.label_3.setVisible(True)
            QMessageBox.critical(self, "错误", "请输入完整信息！！！")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
