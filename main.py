#### from https://www.blog.pythonlibrary.org/2018/05/30/loading-ui-files-in-qt-for-python/
import sys
from PySide2.QtWidgets import QApplication
from ui import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow('ui/mainwindow.ui')
    sys.exit(app.exec_())
