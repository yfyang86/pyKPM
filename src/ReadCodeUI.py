# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Knowledge.ui'
#
# Created: Sun Mar 22 14:18:07 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog, wikipath):
        #wikipath = "D:/code/snip"
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(1200, 800)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeview = QtGui.QTreeView(self.gridLayoutWidget)
        self.treeview.setMaximumSize(QtCore.QSize(300, 600))
        self.treeview.setObjectName(_fromUtf8("Project Tree View."))
        self.gridLayout.addWidget(self.treeview, 1, 1, 1, 1)
        # TEXTEDIT
        self.textEdit = Qsci.QsciScintilla(self.gridLayoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(780, 763))
        self.textEdit.setMaximumSize(QtCore.QSize(780, 763))
        self.textEdit.setCaretLineVisible(True)
        self.textEdit.setCaretLineBackgroundColor(QtGui.QColor("#A9D0F5"))
        self.textEdit.setMarginWidth(0, 35)
        self.textEdit.setMarginLineNumbers(0, True)
        self.textEdit.setMarginsBackgroundColor(QtGui.QColor("#FE9A2E"))
        self.textEdit.setToolTip(_fromUtf8(""))
        self.textEdit.setWhatsThis(_fromUtf8(""))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setAutoCompletionThreshold(1)
        self.textEdit.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
        self.textEdit.setEdgeMode(Qsci.QsciScintilla.EDGE_LINE)
        self.textEdit.setEdgeColumn(106)
        self.textEdit.setEdgeColor(QtGui.QColor("#3399FF"))
        self.textEdit.setFolding(Qsci.QsciScintilla.BoxedTreeFoldStyle)
        self.textEdit.setBraceMatching(Qsci.QsciScintilla.SloppyBraceMatch)
        self.textEdit.setFoldMarginColors(QtGui.QColor("#40BCFF"),QtGui.QColor("#AEAEAE"))
        # Tree View
        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath(wikipath)
        self.treeview.setModel(self.model)
        self.treeview.setRootIndex(self.model.index(wikipath))
        self.treeview.clicked.connect(self.on_treeview_clicked)
        "DEMO"
        self.gridLayout.addWidget(self.textEdit, 0, 2, 2, 5)
        self.Statuslabel = QtGui.QLabel(self.gridLayoutWidget)
        self.Statuslabel.setObjectName(_fromUtf8("Statuslabel"))
        self.gridLayout.addWidget(self.Statuslabel, 2, 2, 1, 1)
        self.calendarWidget = QtGui.QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setMaximumSize(QtCore.QSize(300, 180))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.gridLayout.addWidget(self.calendarWidget, 0, 1, 1, 1)
        # set LIST: history
        self.listHistory = QtGui.QListWidget(Dialog)
        self.listHistory.setObjectName(_fromUtf8("listHistory"))
        self.gridLayout.addWidget(self.listHistory, 0,8,2,1)
        self.listHistory.setFixedSize(QtCore.QSize(200, 763))
        self.listHistory.addItem("File History List")
        self.listHistory.clicked.connect(self.on_listHist_clicked)
        # Set Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setLex(self, filename,filePath):
        u = filename.split(".")
        suffix = u[len(u)-1]
        if suffix in ["cpp", "c", "cu"]:
            self.lexer = Qsci.QsciLexerCPP()
        elif suffix == "py" or suffix == "pwc":
            self.lexer = Qsci.QsciLexerPython()
        elif suffix == "rb":
            self.lexer = Qsci.QsciLexerRuby()
        elif suffix == "cs":
            self.lexer = Qsci.QsciLexerCSharp()
        elif suffix == "css":
            self.lexer = Qsci.QsciLexerCSS()
        elif suffix == "r" or suffix == "R":
            self.lexer = Qsci.QsciLexerLua()
        elif suffix == "java" or suffix == "jwc":
            self.lexer = Qsci.QsciLexerJava()
        elif suffix == "html" or suffix == "htm":
            self.lexer = Qsci.QsciLexerHTML()
        elif suffix == "make" or suffix == "htm":
            self.lexer = Qsci.QsciLexerCMake()
        elif suffix in ["cmd", "sh", "bat"]:
            self.lexer = Qsci.QsciLexerBatch()
        elif suffix == "diff":
            self.lexer = Qsci.QsciLexerDiff()
        elif suffix in ["f", "f90"]:
            self.lexer = Qsci.QsciLexerFortran()
        elif suffix in ["m", "mat"]:
            self.lexer = Qsci.QsciLexerMatlab()
        elif suffix in ["pl", "PL"]:
            self.lexer = Qsci.QsciLexerPerl()
        elif suffix in ["tex", "toc", "cls", "sty"]:
            self.lexer = Qsci.QsciLexerTeX()
        elif suffix == "sql":
            self.lexer = Qsci.QsciLexerSQL()
        elif suffix in ["xml2", "xml"]:
            self.lexer = Qsci.QsciLexerXML()
        else:
            self.lexer = Qsci.QsciLexerProperties()
        self.api = Qsci.QsciAPIs(self.lexer)
        self.api.add("aLongString")
        self.api.add("aLongerString")
        self.api.add("aDifferentString")
        self.api.add("sOmethingElse")
        self.api.prepare()
        self.textEdit.setLexer(self.lexer)
        self.textEdit.setText(open(filePath).read())

        
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)
        self.listHistory.addItem(filePath)
        self.setLex(fileName,filePath)
        

    def on_listHist_clicked(self):
        filePath = str(self.listHistory.selectedItems()[0].text())
        self.setLex(filePath,filePath)
        if filePath != "File History List":
            self.textEdit.setText(open(filePath).read())

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Code Reader", "Code Reader", None))
        Dialog.setWindowIcon(QtGui.QIcon("code.ico"))
        self.Statuslabel.setText(_translate("Dialog", "Status: Development Version 0.0.1", None))

from PyQt4 import Qsci

# demo Exmample
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, "D:/code")
    Dialog.show()
    sys.exit(app.exec_())
