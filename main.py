#### from https://www.blog.pythonlibrary.org/2018/05/30/loading-ui-files-in-qt-for-python/
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt, QCoreApplication
from ui import MainWindow

version = 0.0.0

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    form = MainWindow('ui/mainwindow.ui', version)
    sys.exit(app.exec_())
