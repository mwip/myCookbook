from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QColor


class MainWindowTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)

        # four empty lists
        self.recipe_ids = []
        self.recipe_names = []
        self.comments = []
        self.cuisines = []

        self.load_data(data)

        
    def load_data(self, data):
        for row in data:
            self.recipe_ids.append(row[0])
            self.recipe_names.append(row[1])
            self.comments.append(row[2])
            self.cuisines.append(row[-1])
            
        self.column_count = 4
        self.row_count = len(self.recipe_names)

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("ID", "Name", "Comment", "Cuisine")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            if column == 0:
                return self.recipe_ids[row]
            elif column == 1:
                return self.recipe_names[row]
            elif column == 2:
                return self.comments[row]
            elif column == 3:
                return self.cuisines[row]
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None
