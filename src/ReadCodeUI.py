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
    def setupUi(self, Dialog):
        wikipath = "C:/data"
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(1200, 800)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeview = QtGui.QTreeView(self.gridLayoutWidget)
        self.treeview.setMaximumSize(QtCore.QSize(400, 1200))
        self.treeview.setObjectName(_fromUtf8("Project Tree View."))
        self.gridLayout.addWidget(self.treeview, 1, 1, 1, 1)
        # TEXTEDIT
        self.textEdit = Qsci.QsciScintilla(self.gridLayoutWidget)
        self.textEdit.setMinimumSize(QtCore.QSize(780, 750))
        self.textEdit.setMaximumSize(QtCore.QSize(780, 750))
        self.textEdit.setCaretLineVisible(True)
        self.textEdit.setCaretLineBackgroundColor(QtGui.QColor("#A9D0F5"))
        self.textEdit.setMarginWidth(0, 30)
        self.textEdit.setMarginLineNumbers(0, True)
        self.textEdit.setMarginsBackgroundColor(QtGui.QColor("#FE9A2E"))
        self.textEdit.setToolTip(_fromUtf8(""))
        self.textEdit.setWhatsThis(_fromUtf8(""))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setAutoCompletionThreshold(1)
        self.textEdit.setAutoCompletionSource(Qsci.QsciScintilla.AcsAPIs)
        # Tree View
        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath(wikipath)
        self.treeview.setModel(self.model)
        self.treeview.clicked.connect(self.on_treeview_clicked)
        "DEMO"
        self.gridLayout.addWidget(self.textEdit, 0, 2, 2, 5)
        self.Statuslabel = QtGui.QLabel(self.gridLayoutWidget)
        self.Statuslabel.setObjectName(_fromUtf8("Statuslabel"))
        self.gridLayout.addWidget(self.Statuslabel, 2, 2, 1, 1)
        self.calendarWidget = QtGui.QCalendarWidget(self.gridLayoutWidget)
        self.calendarWidget.setMaximumSize(QtCore.QSize(400, 200))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.gridLayout.addWidget(self.calendarWidget, 0, 1, 1, 1)
        # Set Dialog
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setLex(self, filename):
        u = filename.split(".")
        u = u[len(u)-1]
        return u

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeview_clicked(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())
        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)
        print filePath
        print fileName
        suffix = self.setLex(fileName)
        if suffix == "cpp":
            self.lexer = Qsci.QsciLexerCPP()
        elif suffix == "python":
            self.lexer = Qsci.QsciLexerPython()
        elif suffix == "rb":
            self.lexer = Qsci.QsciLexerRuby()
        elif suffix == "c":
            self.lexer = Qsci.QsciLexerCPP()
        elif suffix == "cs":
            self.lexer = Qsci.QsciLexerCSharp()
        elif suffix == "css":
            self.lexer = Qsci.QsciLexerCSS()
        elif suffix == "r" or suffix == "R":
            self.lexer = Qsci.QsciLexerRuby()
        elif suffix == "java" or suffix == "jwc":
            self.lexer = Qsci.QsciLexerJava()
        else:
            self.lexer = Qsci.QsciLexerBatch()
        self.api = Qsci.QsciAPIs(self.lexer)
        self.api.add("aLongString")
        self.api.add("aLongerString")
        self.api.add("aDifferentString")
        self.api.add("sOmethingElse")
        self.api.prepare()
        self.textEdit.setLexer(self.lexer)
        self.textEdit.setText(open(filePath).read())

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Statuslabel.setText(_translate("Dialog", "Status", None))

from PyQt4 import Qsci

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
