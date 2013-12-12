'''
@Date: Tuesday, 10 December 2013 
@Author: Abrelrahman Moez (aka - Hydra)
@Script: ResistorCalc.py
@Description: Resistor Calculator
@Version: 1.0
'''
from PyQt4 import QtGui, QtCore
import sys
import webbrowser
#
class UI(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle('Resistor Calculator')
		# --------- Declaring Constants ---------- #		
		# Colors for digits
		self.digit_colors = {	'':'',
							'Black': 0,
							'Brown':1,
							'Red':2,
							'Orange':3,
							'Yellow':4,
							'Green':5,
							'Blue':6,
							'Violet':7,
							'Gray':8,
							'White':9}
		# Colors for multiplier
		self.multiplier_colors = {	'':'',
									'Black':float(1),
									'Brown':float(10),
									'Red':float(100),
									'Orange':float(1000),
									'Yellow':float(10000),
									'Green':float(100000),
									'Blue':float(1000000),
									'Violet':float(10000000),
									'Gold':float(0.1),
									'Silver':float(0.01),
									}
		# Colors for tolerance
		self.tolerance_colors = {	'':'',
									'Brown': float(0.01),
									'Red': float(0.02),
									'Green': float(0.05),
									'Blue': float(0.25),
									'Violet': float(0.001),
									'Silver': float(0.1),
									'Gold': float(0.05),
								}
		# Colors for Temperature Coefficeinet
		self.temp_coefficient_colors = {'':'',
										'Brown':'100 ppm',
										'Red':'50 ppm',
										'Orange': '15 ppm',
										'Yellow': '25 ppm'
										}
		# Establishing User Interface
		self.create_UI = self.Create_UI()
		self.resize(600,370)

	def Create_UI(self):
		# Resistor bands type
		self.bands_number = QtGui.QGroupBox('Bands number', self)
		self.bands_number.move(20,20)
		self.bands_number.resize(180,120)
		
		self.four_band = QtGui.QRadioButton('4-Band Resistor', self.bands_number)
		self.four_band.move(20,20)
		
		self.five_band = QtGui.QRadioButton('5-Band Resistor', self.bands_number)
		self.five_band.move(20,40)
		
		self.six_band = QtGui.QRadioButton('6-Band Resistor', self.bands_number)
		self.six_band.move(20,60)
		#
		self.four_band.clicked.connect(self.calc_four_bands)
		self.five_band.clicked.connect(self.calc_five_bands)
		self.six_band.clicked.connect(self.calc_six_bands)
		# ------------------------------------------------------- #
		self.colors_bands = QtGui.QGroupBox('Bands Color',self)
		self.colors_bands.move(220,20)
		self.colors_bands.resize(360,120)
		# Color #1
		self.color_1 = QtGui.QLabel('1st  Band:', self.colors_bands)
		self.color_1.move(20,20)
		self.colors_1 = QtGui.QComboBox(self.colors_bands)
		self.colors_1.move(80,20)
		# Color #2
		self.color_2 = QtGui.QLabel('2nd Band:', self.colors_bands)
		self.color_2.move(20,50)
		self.colors_2 = QtGui.QComboBox(self.colors_bands)
		self.colors_2.move(80,50)
		# Color #3
		self.color_3 = QtGui.QLabel('3rd Band:', self.colors_bands)
		self.color_3.move(20,80)
		self.colors_3 = QtGui.QComboBox(self.colors_bands)
		self.colors_3.move(80,80)
		# Color #4
		self.color_4 = QtGui.QLabel('Multiplier:', self.colors_bands)
		self.color_4.move(180,20)
		self.colors_4 = QtGui.QComboBox(self.colors_bands)
		self.colors_4.move(260,20)
		# Color #5
		self.color_5 = QtGui.QLabel('Tolerance:', self.colors_bands)
		self.color_5.move(180,50)
		self.colors_5 = QtGui.QComboBox(self.colors_bands)
		self.colors_5.move(260,50)
		# Color #6
		self.color_6 = QtGui.QLabel('Temp. Coeff.:', self.colors_bands)
		self.color_6.move(180,80)
		self.colors_6 = QtGui.QComboBox(self.colors_bands)
		self.colors_6.move(260,80)

		# Filling Digits Colors Lists #
		for x, y in self.digit_colors.items():
			self.colors_1.addItem(x)
			self.colors_2.addItem(x)
			self.colors_3.addItem(x)
		# Filling Multiplier Colors Lists
		for x, y in self.multiplier_colors.items():
			self.colors_4.addItem(x)	
		# Filling Tolerance Colors Lists
		for x, y in self.tolerance_colors.items():
			self.colors_5.addItem(x)
		# Filling Temperature Coefficient
		for x, y in self.temp_coefficient_colors.items():
			self.colors_6.addItem(x)

		# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- #

		self.calc_button = QtGui.QPushButton('Calculate!', self)
		self.calc_button.move(110,160)
		self.calc_button.resize(110,30)
		self.calc_button.clicked.connect(self.Calculate)

		self.documentation_button = QtGui.QPushButton('Documentation', self)
		self.documentation_button.move(240,160)
		self.documentation_button.resize(110,30)
		self.documentation_button.clicked.connect(self.doucmentation)

		self.contact_button = QtGui.QPushButton('Contact', self)
		self.contact_button.move(370,160)
		self.contact_button.resize(110,30)
		self.contact_button.clicked.connect(self.contact)
		
		# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- #
		# Result Groupbox
		self.result = QtGui.QGroupBox(self)
		self.result.move(50, 210)
		self.result.resize(500,150)
		self.result.setStyleSheet('QGroupBox {border-radius: 5px; background: #FFF7CB};')
		self.shadow = QtGui.QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(7)
		self.shadow.setOffset(1,1)
		self.shadow.setColor(QtGui.QColor(65, 65, 65, 210))
		self.result.setGraphicsEffect(self.shadow)
		# -----------------------
		self.resistance_label = QtGui.QLabel('<font color=red> <b> Resistance:', self.result)
		self.resistance_label.move(20,20)
		self.resistance_value = QtGui.QLineEdit(self.result)
		self.resistance_value.setReadOnly(True)
		self.resistance_value.move(150,20)
		self.resistance_value.resize(300,20)


		self.tolerance_label = QtGui.QLabel('<font color=red> <b> Tolerance:', self.result)
		self.tolerance_label.move(20,50)
		self.tolerance_value = QtGui.QLineEdit(self.result)
		self.tolerance_value.setReadOnly(True)
		self.tolerance_value.move(150,50)
		self.tolerance_value.resize(300,20)

		self.Rtolerance_label = QtGui.QLabel('<font color=red> <b> R. Tolerance:', self.result)
		self.Rtolerance_label.move(20,80)
		self.Rtolerance_value = QtGui.QLineEdit(self.result)
		self.Rtolerance_value.setReadOnly(True)
		self.Rtolerance_value.move(150,80)
		self.Rtolerance_value.resize(300,20)

		self.temp_coeff_label = QtGui.QLabel('<font color=red> <b> Temp. Coefficient:', self.result)
		self.temp_coeff_label.move(20,110)
		self.temp_coeff_value = QtGui.QLineEdit(self.result)
		self.temp_coeff_value.setReadOnly(True)
		self.temp_coeff_value.move(150,110)
		self.temp_coeff_value.resize(300,20)

	def calc_four_bands(self):
		self.colors_1.setEnabled(True)
		self.color_1.setEnabled(True)
		self.colors_2.setEnabled(True)
		self.color_2.setEnabled(True)
		
		self.colors_3.setEnabled(False)
		self.color_3.setEnabled(False)
		
		self.colors_4.setEnabled(True)
		self.color_4.setEnabled(True)
		
		self.colors_5.setEnabled(True)
		self.color_5.setEnabled(True)
		
		self.colors_6.setEnabled(False)
		self.color_6.setEnabled(False)

	def calc_five_bands(self):
		self.colors_1.setEnabled(True)
		self.color_1.setEnabled(True)

		self.colors_2.setEnabled(True)
		self.color_2.setEnabled(True)

		self.colors_3.setEnabled(True)
		self.color_3.setEnabled(True)

		self.colors_4.setEnabled(True)
		self.color_4.setEnabled(True)

		self.colors_5.setEnabled(True)
		self.color_5.setEnabled(True)

		self.colors_6.setEnabled(False)
		self.color_6.setEnabled(False)

	def calc_six_bands(self):
		self.colors_1.setEnabled(True)
		self.color_1.setEnabled(True)

		self.colors_2.setEnabled(True)
		self.color_2.setEnabled(True)

		self.colors_3.setEnabled(True)
		self.color_3.setEnabled(True)

		self.colors_4.setEnabled(True)
		self.color_4.setEnabled(True)

		self.colors_5.setEnabled(True)
		self.color_5.setEnabled(True)

		self.colors_6.setEnabled(True)
		self.color_6.setEnabled(True)

	def Calculate(self):
		try:
			if self.four_band.isChecked():
				first_color = str(self.colors_1.currentText())
				second_color = str(self.colors_2.currentText())
				third_color = str(self.colors_4.currentText())
				fourth_color = str(self.colors_5.currentText())
				# ----------------------------------------------
				digit_1 = str(self.digit_colors[first_color])
				digit_2 = str(self.digit_colors[second_color])
				multiplier = self.multiplier_colors[third_color]
				tolerance = self.tolerance_colors[fourth_color]
				# For maintenance 
				# print digit_1, digit_2, multiplier, tolerance
				# ----------------------------------------------
				append_digits = float(digit_1+digit_2)
				resisitance = append_digits*multiplier
				setResisitance = self.resistance_value.setText(str(resisitance)+' Ohms')
				setTolerance = self.tolerance_value.setText(str(tolerance))
				#
				tolerance_value = resisitance*tolerance
				r_plus_t = str(resisitance+tolerance_value)
				r_minus_t = str(resisitance-tolerance_value)
				setRTolerance = self.Rtolerance_value.setText(" ".join((r_plus_t,"Ohms","/",r_minus_t, "Ohms")))

			elif self.five_band.isChecked():
				first_color = str(self.colors_1.currentText())
				second_color = str(self.colors_2.currentText())
				third_color = str(self.colors_3.currentText())
				fourth_color = str(self.colors_4.currentText())
				fifth_color = str(self.colors_5.currentText())
				# ----------------------------------------------
				digit_1 = str(self.digit_colors[first_color])
				digit_2 = str(self.digit_colors[second_color])
				digit_3 = str(self.digit_colors[third_color])
				multiplier = self.multiplier_colors[fourth_color]
				tolerance = self.tolerance_colors[fifth_color]
				# For maintenance 
				# print digit_1, digit_2, digit_3, multiplier, tolerance 
				# ----------------------------------------------
				append_digits = float(digit_1+digit_2+digit_3)
				resisitance = append_digits*multiplier
				setResisitance = self.resistance_value.setText(str(resisitance)+' Ohms')
				setTolerance = self.tolerance_value.setText(str(tolerance))
				# ----------------------------------------------
			elif self.six_band.isChecked():
				first_color = str(self.colors_1.currentText())
				second_color = str(self.colors_2.currentText())
				third_color = str(self.colors_3.currentText())
				fourth_color = str(self.colors_4.currentText())
				fifth_color = str(self.colors_5.currentText())
				sixth_color = str(self.colors_6.currentText())
			
				# ----------------------------------------------
				digit_1 = str(self.digit_colors[first_color])
				digit_2 = str(self.digit_colors[second_color])
				digit_3 = str(self.digit_colors[third_color])
				multiplier = self.multiplier_colors[fourth_color]
				tolerance = self.tolerance_colors[fifth_color]
				# For maintenance 
				# print first_color, second_color, third_color, multiplier, tolerance, temp_coeff
				# ----------------------------------------------
				append_digits = float(digit_1+digit_2+digit_3)
				resisitance = append_digits*multiplier
				setResisitance = self.resistance_value.setText(str(resisitance)+' Ohms')
				setTolerance = self.tolerance_value.setText(str(tolerance))
				temp_coeff = str(self.temp_coefficient_colors[sixth_color])
				# ----------------------------------------------
				setTempCoeff = self.temp_coeff_value.setText(temp_coeff)
			else:
				msg_box = QtGui.QMessageBox.critical(self,  'Error',  'You forgot to choose bands number!',  QtGui.QMessageBox.Ok)
				return
			tolerance_value = resisitance*tolerance
			r_plus_t = str(resisitance+tolerance_value)
			r_minus_t = str(resisitance-tolerance_value)
			setRTolerance = self.Rtolerance_value.setText(" ".join((r_plus_t,"Ohms","/",r_minus_t, "Ohms")))
		except:
			msg_box = QtGui.QMessageBox.critical(self,  'Error',  'Wrong Inputs!',  QtGui.QMessageBox.Ok)

	def doucmentation(self):
		self.goDoc = Documentation()
		self.goDoc.show()
	def contact(self):
		self.goContact = Contact()
		self.goContact.show()
#
class Documentation(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.resize(400,480)
		#
		self.doc_handler = open('Documentation.html','r')
		self.data = self.doc_handler.read()
		self.doc_handler.close()
		#
		self.text_edit = QtGui.QTextEdit(self.data, self)
		self.text_edit.move(20,20)
		self.text_edit.resize(360,440)
		self.text_edit.setReadOnly(True)
		self.setWindowTitle('Documentation')
class Contact(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.resize(300,150)
		self.setWindowTitle('Contact')
		#
		self.contact_container = QtGui.QGroupBox(self)
		self.contact_container.move(20,20)
		self.contact_container.resize(260,110)
		#self.contact_container.setStyleSheet('QLabel{color: red;')		
		#
		self.twitter = QtGui.QLabel('<b>Follow: <a style="text-decoration: none" href="http://twitter.com/abdelrahmanmoez">Twitter</a>', self.contact_container)
		self.twitter.move(20,20)
		self.twitter.linkActivated.connect(self.twitterOpener)
		#
		self.facebook = QtGui.QLabel('<b>Like:   <a style="text-decoration: none" href="https://www.facebook.com/The.Hydra.Python.Programmer"> Facebook </a>', self.contact_container)
		self.facebook.move(20,40)
		self.facebook.linkActivated.connect(self.facebookOpener)
		#
		self.github = QtGui.QLabel('<b> Follow: <a style="text-decoration: none" href="https://github.com/Hydr4/"> Github </a>', self.contact_container)
		self.github.move(20,60)
		self.github.linkActivated.connect(self.githubOpener)
		#
		self.mail = QtGui.QLabel('<b> Email: <a style="text-decoration: none" href="mailto:abdelrahman.moez@gmail.com"> abdelrahman.moez@gmail.com </a><b>', self.contact_container)
		self.mail.move(20,80)
		self.mail.linkActivated.connect(self.mailOpener)
	def twitterOpener(self):
		webbrowser.open('http://twitter.com/abdelrahmanmoez')
	def facebookOpener(self):
		webbrowser.open('https://www.facebook.com/The.Hydra.Python.Programmer')
	def githubOpener(self):
		webbrowser.open('https://github.com/Hydr4/')
	def mailOpener(self):
		webbrowser.open('mailto:abdelrahman.moez@gmail.com')
		
def main():
	app = QtGui.QApplication(sys.argv)
	foo = UI()
	foo.show()
	sys.exit(app.exec_())
#
main()
