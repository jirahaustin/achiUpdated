import re
import datetime
import sqlite3
import sys
from gui import *
from Custom_Widgets.Widgets import *
from database.database import *
from PySide2 import *
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QMainWindow, QApplication)
from PySide2.QtCharts import QtCharts

data = ["headache", "cold", "migrane", "vertigo"]

DIAGNOSIS_SECTION = 0
RECORDS_SECTION = 1
SUMMARY_SECTION = 2

TITLE_PAGE = 0
PROFILE_PAGE = 1
SYMPTOMS_PAGE = 2
INTERVIEW_PAGE = 3
VALIDATION_PAGE = 4
RESULT_PAGE = 5


class DataObject(Object):
    pass


def makeBulletList(arr):
    return ["● " + item for item in arr]


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.formData = DataObject()

        loadJsonStyle(self, self.ui)

        self.ui.leftMenuDiagnosisBtn.clicked.connect(
            lambda: self.ui.mainPages.setCurrentIndex(2))
        self.ui.leftMenuRecordsBtn.clicked.connect(
            lambda: self.ui.mainPages.setCurrentIndex(1))
        self.ui.leftMenuSummaryBtn.clicked.connect(
            lambda: self.ui.mainPages.setCurrentIndex(0))

        self.ui.dTakeBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(1))
        self.ui.pPExitBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(0))
        self.ui.pBottomNextBtn.clicked.connect(self.profileNext)
        # self.ui.pBottomNextBtn.clicked.connect(lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(2))
        self.ui.symPExitBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(1))
        # self.ui.symBottomNextBtn.clicked.connect(self.symptomsNext)
        self.ui.symBottomNextBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(3))
        self.ui.iPExitBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(2))
        self.ui.iBottomNextBtn.clicked.connect(self.interviewNext)
        # self.ui.iBottomNextBtn.clicked.connect(lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(4))
        self.ui.vPExitBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(3))
        self.ui.vBottomNextBtn.clicked.connect(self.validationNext)
        # self.ui.vBottomNextBtn.clicked.connect(lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(5))
        self.ui.resPExitBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(4))

        self.ui.recAuthSubmitBtn.clicked.connect(
            lambda: self.ui.recordsStackedWidget.setCurrentIndex(1))
        self.ui.recExitBtn1.clicked.connect(
            lambda: self.ui.recordsStackedWidget.setCurrentIndex(0))

        self.ui.sumAuthSubmitBtn.clicked.connect(
            lambda: self.ui.summaryStackedWidget.setCurrentIndex(1))
        self.ui.sumMainExitBtn.clicked.connect(
            lambda: self.ui.summaryStackedWidget.setCurrentIndex(0))

        self.ui.pUserDetailsBirthdateDateEdit.dateChanged.connect(
            self.renderAge)
        self.ui.symBodyComboBox.currentIndexChanged.connect(self.changePicture)

        self.ui.vTopEditBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(PROFILE_PAGE))
        self.ui.vMidEditBtn.clicked.connect(
            lambda: self.ui.diagnosisStackedWidget.setCurrentIndex(SYMPTOMS_PAGE))

        self.ui.resBottomSaveBtn.clicked.connect(self.saveResult)
        self.ui.resBottomCloseBtn.clicked.connect(self.closeResult)

    #     self.ui.symptomEntryContainer1.installEventFilter(self)
    # def eventFilter(self, obj, event):
    #     if obj == self.ui.symptomEntryContainer1 and event.type() == QtCore.QEvent.MouseButtonPress:
    #         print("clicked")
    #     return False
        self.ui.recSearchTable.setColumnWidth(0, 100)
        self.ui.recSearchTable.setColumnWidth(1, 100)
        self.ui.recSearchTable.setColumnWidth(1, 100)
        self.ui.recSearchTable.setColumnWidth(1, 100)
        self.ui.recSearchTable.setColumnWidth(1, 100)

        self.demographicPiechart()
        self.loadPatientsList()
        self.show()
    # def symptomsNext(self):
    #     # pass
    #     self.ui.verticalLayout_45.addWidget(QCheckBox("SomeText"))
    #     descLayout = QVBoxLayout()
    #     descLayout.setContentsMargins(20,0,0,0)
    #     lbl = QLabel("SomeOtherText")
    #     lbl.setMargin(30)
    #     descLayout.addWidget(lbl)
    #     self.ui.verticalLayout_45.insertLayout(descLayout)

    def closeResult(self):
        # insert clearing function
        self.ui.diagnosisStackedWidget.setCurrentIndex(TITLE_PAGE)

    def saveResult(self):
        # insert saving function
        # insert clearing function
        self.ui.diagnosisStackedWidget.setCurrentIndex(TITLE_PAGE)

    def validationNext(self):
        # function call for arr
        cause = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                 "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."]
        action = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                  "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"]
        prediction = "Urinary Track Infection (UTI)"
        confRating = "Very Likely"

        self.ui.resUserDetailsNameLabel.setText(
            self.formData.fname + " " + self.formData.mname + " " + self.formData.lname)
        self.ui.resUserDetailsBirthdateLabel.setText(
            self.formData.birthdate.strftime("%m/%d/%Y"))
        self.ui.resUserDetailsAgeLabel.setText(self.formData.age)
        self.ui.resUserDetailsSexLabel.setText(self.formData.sex)
        self.ui.resUserDetailsCivilLabel.setText(self.formData.civil)
        self.ui.resUserDetailsContactLabel.setText(
            self.formData.contact if self.formData.contact else "--Not Applicable--")
        self.ui.resUserDetailsAddressLabel.setText(
            self.formData.address if self.formData.address else "--Not Applicable--")

        self.ui.resResultPredictionLabel.setText(prediction)
        self.ui.resResultConfidenceLabel.setText(confRating)
        self.ui.resResultCauseListWidget.clear()
        self.ui.resResultCauseListWidget.addItems(makeBulletList(cause))
        self.ui.resResultActionListWidget.clear()
        self.ui.resResultActionListWidget.addItems(makeBulletList(action))

        self.ui.diagnosisStackedWidget.setCurrentIndex(RESULT_PAGE)

    def interviewNext(self):
        # function call for arr
        symptoms = ["headache", "cold", "fever", "malaise", "vertigo"]
        self.ui.vPatientDetailsNameLabel.setText(
            self.formData.fname + " " + self.formData.mname + " " + self.formData.lname)
        self.ui.vPatientDetailsBirthdateLabel.setText(
            self.formData.birthdate.strftime("%m/%d/%Y"))
        self.ui.vPatientDetailsAgeLabel.setText(self.formData.age)
        self.ui.vPatientDetailsSexLabel.setText(self.formData.sex)
        self.ui.vPatientDetailsCivilLabel.setText(self.formData.civil)
        self.ui.vPatientDetailsContactLabel.setText(
            self.formData.contact if self.formData.contact else "--Not Applicable--")
        self.ui.vPatientDetailsAddressLabel.setText(
            self.formData.address if self.formData.address else "--Not Applicable--")

        self.ui.vEmergencyNameLabel.setText(
            self.formData.emergencyName if self.formData.emergencyName else "--Not Applicable--")
        self.ui.vEmergencyRelationLabel.setText(
            self.formData.emergencyRelation if self.formData.emergencyRelation else "--Not Applicable--")
        self.ui.vEmergencyContactLabel.setText(
            self.formData.emergencyContact if self.formData.emergencyContact else "--Not Applicable--")

        self.ui.vSymptomsSymptomsListWidget.clear()
        self.ui.vSymptomsSymptomsListWidget.addItems(makeBulletList(symptoms))

        self.ui.diagnosisStackedWidget.setCurrentIndex(VALIDATION_PAGE)

    def renderAge(self):
        today = datetime.date.today()
        bday = self.ui.pUserDetailsBirthdateDateEdit.date().toPython()
        newAge = today.year - bday.year - \
            ((today.month, today.day) < (bday.month, bday.day))
        if newAge > 0:
            self.ui.pUserDetailsAgeLineEdit.setText(str(newAge))
        else:
            self.ui.pUserDetailsAgeLineEdit.setText("")

    def changePicture(self):
        selection = self.ui.symBodyComboBox.currentText()
        print(selection)
        location = f"images/Male{selection}.PNG"
        print(location)
        pixmap = QtGui.QPixmap(location)
        self.ui.symImage.setPixmap(pixmap)
        self.ui.symImage.setScaledContents(True)

    def checkName(self, name, errLabel, isRequired):
        if isRequired and not name:
            errLabel.setText("This field cannot be empty.")
        elif name and not re.search(r"^[a-z ,.'-]+$", name, re.IGNORECASE):
            errLabel.setText("Invalid name format.")
        else:
            errLabel.setText("")

    def checkDate(self, date, errLabel):
        today = datetime.datetime.today()
        if date.year > today.year or (date.year == today.year and date.month > today.month) or (date.year == today.year and date.month == today.month and date.day > today.day):
            errLabel.setText("Invalid date selected.")
        else:
            errLabel.setText("")

    def checkComboBox(self, cbValue, errLabel):
        if cbValue == "Select" or not cbValue:
            errLabel.setText("This field cannot be empty.")
        else:
            errLabel.setText("")

    def checkNumber(self, number, errLabel, isRequired):
        if isRequired and not number:
            errLabel.setText("This field cannot be empty.")
        elif number and not re.search(r"^\d{8}|(09|\+639)\d{9}", number):
            errLabel.setText("Invalid number format.")
        else:
            errLabel.setText("")

    def updateErrorSizePolicy(self, arr, targetWidget):
        sp = targetWidget.sizePolicy()
        withError = False
        for item in arr:
            if item.text():
                sp.setVerticalPolicy(QSizePolicy.Expanding)
                withError = True
                break
        else:
            sp.setVerticalPolicy(QSizePolicy.Ignored)
        targetWidget.setSizePolicy(sp)
        return withError

    def profileNext(self):
        topLine = [self.ui.lnameErrorLabel,
                   self.ui.fnameErrorLabel, self.ui.mnameErrorLabel]
        midLine = [self.ui.birthdateErrorLabel, self.ui.sexErrorLabel,
                   self.ui.civilErrorLabel, self.ui.contactErrorLabel]
        botLine = [self.ui.emergencyNameErrorLabel,
                   self.ui.emergencyContactErrorLabel]

        self.formData.lname = self.ui.pUserDetailsLnameLineEdit.text()
        self.formData.fname = self.ui.pUserDetailsFnameLineEdit.text()
        self.formData.mname = self.ui.pUserDetailsMnameLineEdit.text()

        self.formData.birthdate = self.ui.pUserDetailsBirthdateDateEdit.date().toPython()
        self.formData.age = self.ui.pUserDetailsAgeLineEdit.text()
        self.formData.sex = self.ui.pUserDetailsSexCb.currentText()
        self.formData.civil = self.ui.pUserDetailsCivilCb.currentText()
        self.formData.contact = self.ui.pUserDetailsContactLineEdit.text()
        self.formData.address = self.ui.pUserDetailsAddressTextEdit.toPlainText()

        self.formData.emergencyName = self.ui.emergencyNameLineEdit.text()
        self.formData.emergencyRelation = self.ui.emergencyRelationLineEdit.text()
        self.formData.emergencyContact = self.ui.emergencyContactLineEdit.text()

        # user details
        self.checkName(self.formData.lname, self.ui.lnameErrorLabel, True)
        self.checkName(self.formData.fname, self.ui.fnameErrorLabel, True)
        self.checkName(self.formData.mname, self.ui.mnameErrorLabel, True)
        self.checkDate(self.formData.birthdate, self.ui.birthdateErrorLabel)
        self.checkComboBox(self.formData.sex, self.ui.sexErrorLabel)
        self.checkComboBox(self.formData.civil, self.ui.civilErrorLabel)
        self.checkNumber(self.formData.contact,
                         self.ui.contactErrorLabel, False)

        # emergency contact
        self.checkName(self.formData.emergencyName,
                       self.ui.emergencyNameErrorLabel, False)
        self.checkNumber(self.formData.emergencyContact,
                         self.ui.emergencyContactErrorLabel, False)

        nameError = self.updateErrorSizePolicy(
            topLine, self.ui.pUserDetailsTopErrorContainer)
        detailError = self.updateErrorSizePolicy(
            midLine, self.ui.pUserDetailsMidErrorContainer)
        emergencyError = self.updateErrorSizePolicy(
            topLine, self.ui.pEmergencyErrorContainer)

        if not nameError and not detailError and not emergencyError:
            self.ui.diagnosisStackedWidget.setCurrentIndex(2)

    ###########################RECORDS################################
    def loadPatientsList(self):
        patients = [{'fname': 'Juan', 'lname': 'Dela Cruz', 'mname': 'Sebastian', 'bday': '2000-01-02', 'last_consultation': '2025-12-04'},
                    {'fname': 'Junel', 'lname': 'Batungbakal', 'mname': 'Dimagiba',
                        'bday': '2000-01-02', 'last_consultation': '2025-12-02'},
                    {'fname': 'Taylor', 'lname': 'Batungbakal', 'mname': 'Swift',
                        'bday': '2000-01-02', 'last_consultation': '2025-12-02'},
                    {'fname': 'Pedro', 'lname': 'Batungbakal', 'mname': 'Santos',
                        'bday': '2000-01-02', 'last_consultation': '2025-12-02'}
                    ]
        row = 0
        self.ui.recSearchTable.setRowCount(50)
        for patient in patients:
            self.ui.recSearchTable.setItem(
                row, 0, QTableWidgetItem(patient["fname"]))
        for patient in patients:
            self.ui.recSearchTable.setItem(
                row, 1, QTableWidgetItem(patient["lname"]))
        for patient in patients:
            self.ui.recSearchTable.setItem(
                row, 2, QTableWidgetItem(patient["mname"]))
        for patient in patients:
            self.ui.recSearchTable.setItem(
                row, 3, QTableWidgetItem(patient["bday"]))
        for patient in patients:
            self.ui.recSearchTable.setItem(
                row, 4, QTableWidgetItem(patient["last_consultation"]))
            row = row+1

        print(patients)

    def demographicPiechart(self):

        self.series = QtCharts.QPieSeries()
        self.series.append("Children", 80)
        self.series.append("Youth", 70)
        self.series.append("Adults", 50)
        self.series.append("Seniors", 40)

        # adding slice
        self.slice = QtCharts.QPieSlice()
        self.slice = self.series.slices()[2]
        self.slice.setExploded(True)
        self.slice.setLabelVisible(True)
        self.slice.setPen(QPen(Qt.darkGreen, 2))
        self.slice.setBrush(Qt.green)

        self.chart = QtCharts.QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart.setTitle("Pie Chart Example")

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.chartView.chart().setTheme(QtCharts.QChart.ChartThemeDark)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.chartView.sizePolicy().hasHeightForWidth())
        self.chartView.setSizePolicy(sizePolicy)
        self.chartView.setMinimumSize(QSize(0, 300))
        self.ui.sumMainGraph4Container.layout().addWidget(self.chartView)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
