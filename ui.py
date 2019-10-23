import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QAction, QDialog, QFileDialog, QLabel
from PySide2.QtCore import QFile, QObject
from PySide2.QtGui import QIcon


class MainWindow(QMainWindow):
 
    def __init__(self, ui_file, parent=None):
        super(MainWindow, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
 
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.window.setWindowIcon(QIcon('ressources/icon.png'))

        # Variables
        self.current_cb = ""

        
        # Buttons
        self.btn_select_cb = self.window.findChild(QPushButton,
                                                 "buttonSelectCookbook")
        self.btn_select_cb.clicked.connect(self.select_cookbook)

        self.btn_load_cb = self.window.findChild(QPushButton,
                                                 "buttonLoadCookbook")
        self.btn_load_cb.clicked.connect(self.load_cookbook)

        self.btn_add_recipe = self.window.findChild(QPushButton,
                                                    "buttonAddRecipe")
        self.btn_add_recipe.clicked.connect(self.new_recipe)

        
        # Actions
        self.action_new_cb = self.window.findChild(QAction,
                                                   "actionNewCB")
        self.action_new_cb.triggered.connect(self.new_cookbook)

        self.action_select_cb = self.window.findChild(QAction,
                                                    "actionSelectCB")
        self.action_select_cb.triggered.connect(self.select_cookbook)

        self.action_create_dummy_CB = self.window.findChild(QAction,
                                                            "actionCreateDummyCB")
        self.action_create_dummy_CB.triggered.connect(self.create_dummy_cookbook)

        self.action_new_recipe = self.window.findChild(QAction,
                                                       "actionAddRecipe")
        self.action_new_recipe.triggered.connect(self.new_recipe)

        self.action_edit_recipe = self.window.findChild(QAction,
                                                        "actionEditRecipe")
        self.action_edit_recipe.triggered.connect(self.edit_recipe)
        self.action_remove_recipe = self.window.findChild(QAction,
                                                          "actionRemoveRecipe")
        self.action_remove_recipe.triggered.connect(self.remove_recipe)

        self.action_add_dummy_recipe = self.window.findChild(QAction,
                                                             "actionAddDummyRecipe")
        self.action_add_dummy_recipe.triggered.connect(self.add_dummy_recipe)
        
        self.action_about = self.window.findChild(QAction,
                                                  "actionAbout")
        self.action_about.triggered.connect(self.about)
        
        self.action_exit = self.window.findChild(QAction,
                                                 "actionExit")
        self.action_exit.triggered.connect(self.exit_app)

        # Displays
        self.lbl_current_cb = self.window.findChild(QLabel,
                                                    "labelCurrentCookBook")
        
        # show main window
        self.window.show()


    # Functionality
    def new_cookbook(self):
        pass

    def select_cookbook(self):
        fileName = QFileDialog.getOpenFileName(self, "Select Cookbook",
                                               "", "")[0]
        if not fileName == '':
            self.lbl_current_cb.setText(fileName)

    def load_cookbook(self):
        pass

    def create_dummy_cookbook(self):
        pass

    def new_recipe(self):
        pass

    def edit_recipe(self):
        pass

    def remove_recipe(self):
        pass

    def add_dummy_recipe(self):
        pass

    def about(self):
        about_dialog = AboutDialog(self)
        

    def exit_app(self):
        print("exit")
        self.window.close()


class AboutDialog(QDialog):
    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)
        ui_file = QFile("ui/about.ui")
        ui_file.open(QFile.ReadOnly)
        self.dialog = QUiLoader().load(ui_file)
        ui_file.close()
        self.dialog.show()
