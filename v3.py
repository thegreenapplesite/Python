import sys
from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow
from PyQt5  import QtCore
from PyQt5.QtGui import QIcon,QTextCursor
from mycalc import Ui_calc #Mod1
import sys

class MainWindow(QMainWindow):

	def __init__(self,va1):
		super(MainWindow, self).__init__()
		self.ui = Ui_calc()
		self.ui.setupUi(self)
		self.va1=va1

		self.inputNumber=[self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine]
		self.other=[self.sum,self.deduct,self.multiply,self.divide,self.correctme,self.equal,self.addpoint,self.cancelme]

		for x in range(0,10):
			self.ui.btn[x].clicked.connect(self.inputNumber[x])
			self.ui.btn[x].setStyleSheet(open('/home/piemex/Documents/Python/GUI/Calc Project/mystylesheet.css').read())

		for x in range(0,8):
			self.ui.o[x].clicked.connect(self.other[x])
			self.ui.o[x].setStyleSheet(open('/home/piemex/Documents/Python/GUI/Calc Project/mystylesheet.css').read())


		self.ui.ponoff.clicked.connect(lambda:self.close())
		self.ui.ponoff.setStyleSheet(open('/home/piemex/Documents/Python/GUI/Calc Project/mystylesheet.css').read())
		self.ui.screen.setStyleSheet(open('/home/piemex/Documents/Python/GUI/Calc Project/mystylesheet.css').read())


		self.show()

	def keyPressEvent(self,e):
		if e.key()==QtCore.Qt.Key_0:
			self.zero();
		elif e.key()==QtCore.Qt.Key_1:
			self.one();
		elif e.key()==QtCore.Qt.Key_2:
			self.two();
		elif e.key()==QtCore.Qt.Key_3:
			self.three();
		elif e.key()==QtCore.Qt.Key_4:
			self.four();
		elif e.key()==QtCore.Qt.Key_5:
			self.five();
		elif e.key()==QtCore.Qt.Key_6:
			self.six();
		elif e.key()==QtCore.Qt.Key_7:
			self.seven();
		elif e.key()==QtCore.Qt.Key_8:
			self.eight();
		elif e.key()==QtCore.Qt.Key_9:
			self.nine();
		elif e.key()==QtCore.Qt.Key_Plus:
			self.sum();
		elif e.key()==QtCore.Qt.Key_Minus:
			self.deduct();
		elif e.key()==QtCore.Qt.Key_Asterisk:
			self.multiply();
		elif e.key()==QtCore.Qt.Key_Slash:
			self.divide();
		elif ( (e.key()==QtCore.Qt.Key_Equal) or (e.key()==QtCore.Qt.Key_Enter) ):
			self.equal();
		elif e.key()==QtCore.Qt.Key_Delete:
			self.cancelme();
		elif e.key()==QtCore.Qt.Key_Escape:
			sys.exit()
		else:
			print("Key not mapped")



	def addpoint(self):
		self.va1=self.va1+"."
		self.screenme(self.va1)



	def cancelme(self):
		self.va1=""
		self.ui.screen.clear()


	def correctme(self):
		x=self.va1
		x=x[0:len(x)-1]
		self.ui.screen.clear()
		self.va1=x
		self.ui.screen.setPlainText(self.va1)


	def findme(self):
		x=self.ui.screen.toPlainText();
		y=x.find("=")
		if y>-1:
			self.va1=""
			self.ui.screen.clear()

	def sum(self):
		self.va1= self.va1 + "+"
		self.screenme(self.va1)


	def multiply(self):
		self.va1= self.va1 + "*"
		self.screenme(self.va1)


	def divide(self):
		self.va1= self.va1 + "/"
		self.screenme(self.va1)



	def deduct(self):
		self.va1= self.va1 + "-"
		self.screenme(self.va1)


	def equal(self):
		result = 0
		result = eval(self.va1)
		self.ui.screen.moveCursor(QTextCursor.End)
		self.ui.screen.insertPlainText("=" + str(result))
		self.ui.screen.moveCursor(QTextCursor.End)



	def screenme(self,onevalue):
		self.ui.screen.setPlainText(onevalue);


	def zero(self):
		self.findme()
		self.va1= self.va1 + "0"
		self.screenme(self.va1)


	def one(self):
		self.findme()
		self.va1= self.va1 + "1"
		self.screenme(self.va1)


	def two(self):
		self.findme()
		self.va1= self.va1 + "2"
		self.screenme(self.va1)

	def three(self):
		self.findme()
		self.va1= self.va1 + "3"
		self.screenme(self.va1)


	def four(self):
		self.findme()
		self.va1= self.va1 + "4"
		self.screenme(self.va1)


	def five(self):
		self.findme()
		self.va1= self.va1 + "5"
		self.screenme(self.va1)


	def six(self):
		self.findme()
		self.va1= self.va1 + "6"
		self.screenme(self.va1)


	def seven(self):
		self.findme()
		self.va1= self.va1 + "7"
		self.screenme(self.va1)


	def eight(self):
		self.findme()
		self.va1= self.va1 + "8"
		self.screenme(self.va1)


	def nine(self):
		self.findme()
		self.va1= self.va1 + "9"
		self.screenme(self.va1)




app = QApplication(sys.argv)
w = MainWindow("")
w.show()
sys.exit(app.exec_())


