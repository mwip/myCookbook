import sys
import os
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QAction, QDialog, QFileDialog, QLabel, QTableView, QStatusBar
from PySide2.QtCore import QFile, QObject, QStringListModel
from PySide2.QtGui import QIcon
from database import Database
from models import MainWindowTableModel


class MainWindow(QMainWindow):
 
    def __init__(self, ui_file, version, parent=None):
        super(MainWindow, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        self.version = version
        
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.window.setWindowIcon(QIcon('ressources/icon.png'))
        self.window.setWindowTitle('myCookbook')

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
        self.tbl_recipes = self.window.findChild(QTableView,
                                                 "tableRecipes")
        self.status = self.window.findChild(QStatusBar,
                                            "statusBar")

        # show main window
        self.window.show()
        
        # Connect table actions
        self.tbl_recipes.clicked.connect(self.tbl_clicked)
        self.tbl_recipes.doubleClicked.connect(self.tbl_dbl_clicked)
        


    # Functionality
    def new_cookbook(self):
        pass

    def select_cookbook(self):
        file_name = QFileDialog.getOpenFileName(self,
                                                     "Select Cookbook",
                                                     "", "")[0]
        self.current_cb = file_name
        if not file_name == '':
            self.lbl_current_cb.setText(file_name)
        if os.path.isfile(file_name):
            self.btn_load_cb.setEnabled(True)

    def load_cookbook(self):
        self.database = Database(self.current_cb)
        self.database.load_data_base()
        self.table_model = MainWindowTableModel(self.database.recipes)
        self.tbl_recipes.setModel(self.table_model)
        self.tbl_recipes.hideColumn(0)
        
        

    def create_dummy_cookbook(self):
        file_name = QFileDialog.getSaveFileName(self, "Create Dummy Cookbook",
                                               "", "")[0]
        print(file_name)
        if os.path.isfile(file_name):
            os.remove(file_name)
        db = Database(file_name)
        db.create_dummy_database()

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

    def tbl_clicked(self):
        pass
    
    def tbl_dbl_clicked(self):
        current_index = self.tbl_recipes.currentIndex()
        current_recipe_id = self.tbl_recipes.model().data(
            self.tbl_recipes.model().index(current_index.row(), 0))
        print("Load recipe: {}".format(current_recipe_id))
        self.show_recipe(current_recipe_id)

    def show_recipe(self, recipe_id):
        show_recipe_window = ShowRecipe(self, recipe_id)

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


class ShowRecipe(QMainWindow):
    def __init__(self, parent, recipe_id):
        self.recipe_id = recipe_id
        
        super(ShowRecipe, self).__init__(parent)
        ui_file = QFile("ui/showrecipe.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = QUiLoader().load(ui_file)
        ui_file.close()
        self.window.show()
