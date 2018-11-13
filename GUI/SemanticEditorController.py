from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QGraphicsScene, QGraphicsEllipseItem, QGraphicsItem

from GUI.Common import INVALID_INDEX
from GUI.CustomElements.ConnectibleEllipse import ConnectibleEllipse
from GUI.Models.Helpers.SemanticData import SemanticData
from GUI.Models.SemanticInputTableModel import SemanticInputTableModel
from GUI.Models.SemanticObjectListModel import SemanticObjectListModel
from GUI.Models.SemanticOutputTableModel import SemanticOutputTableModel
from GUI.Views.SemanticEditorView import Ui_SemanticEditor


class SemanticEditorController(QDialog):
    def __init__(self):
        super(SemanticEditorController, self).__init__()
        self.ui = Ui_SemanticEditor()
        self.ui.setupUi(self)
        # self.graphic_scene = QGraphicsScene(self)
        # self.graphic_ellipse = QGraphicsEllipseItem()
        #
        # self.ui.graphicsView.setScene(self.graphic_scene)
        #
        # self.brush = QBrush(Qt.red)
        # self.pen = QPen(Qt.black)
        # self.pen.setWidth(6)
        #
        # self.graphic_ellipse = self.graphic_scene.addEllipse(10,10,100,100,self.pen, self.brush)
        # self.graphic_ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        #
        # self.myEllipse = ConnectibleEllipse()
        # self.graphic_scene.addItem(self.myEllipse)
        #
        self.semantic_object_model = SemanticObjectListModel(self)
        self.in_model = SemanticInputTableModel(self)
        self.out_model = SemanticOutputTableModel(self)
        self.init_gui()

        self.show()

    def init_gui(self):
        self.ui.pbAddInput.clicked.connect(self.on_pb_add_input_clicked)
        self.ui.pbAddOutput.clicked.connect(self.on_pb_add_output_clicked)
        self.ui.pbAddObject.clicked.connect(self.on_pb_add_object_clicked)

        self.ui.pbRemoveInput.clicked.connect(self.on_pb_remove_input_clicked)
        self.ui.pbRemoveOutput.clicked.connect(self.on_pb_remove_output_clicked)
        self.ui.pbRemoveObject.clicked.connect(self.on_pb_remove_object_clicked)

        self.ui.listViewObjects.clicked.connect(self.request_in_out_data)
        self.ui.listViewObjects.clearSelection()

        # self.ui.listViewObjects.clicked.connect(self.in_model.request_input_for_selected)
        # self.ui.listViewObjects.clicked.connect(self.out_model.request_output_for_selected)
        self.ui.tableViewInput.clicked.connect(self.on_table_view_input_clicked)
        self.ui.tableViewOutput.clicked.connect(self.on_table_view_output_clicked)

        self.ui.listViewObjects.setModel(self.semantic_object_model)
        self.ui.tableViewInput.setModel(self.in_model)
        self.ui.tableViewOutput.setModel(self.out_model)

        # TESt
        self.ui.pushButton.clicked.connect(self.on_TEST_clicked)
    def on_pb_add_input_clicked(self):
        if -1 < SemanticData.selected_semantic_object_index:
            self.in_model.insert_new_input()

    def on_pb_add_output_clicked(self):
        if -1 < SemanticData.selected_semantic_object_index:
            self.out_model.insert_new_input()

    def on_pb_add_object_clicked(self):
        self.semantic_object_model.add_semantic_object()

    def on_pb_remove_input_clicked(self):
        row = self.ui.tableViewInput.currentIndex().row()
        self.in_model.remove_input_at(row)

    def on_pb_remove_output_clicked(self):
        row = self.ui.tableViewOutput.currentIndex().row()
        self.out_model.remove_output_at(row)

    def on_pb_remove_object_clicked(self):
        row = self.ui.listViewObjects.currentIndex().row()
        self.semantic_object_model.remove_semantic_object(row)

    def on_list_view_objects_clicked(self):
        row = self.ui.listViewObjects.currentIndex().row()
        if self.ui.listViewObjects.currentIndex().row() > INVALID_INDEX:
            SemanticData.set_selected_index = row
            # Request input and output
        print(row)

    def request_in_out_data(self):
        selected_object_index = self.ui.listViewObjects.currentIndex().row()
        self.in_model.clear_all_inputs()
        self.out_model.clear_all_inputs()
        self.semantic_object_model.set_selected_object(selected_object_index)
        self.in_model.request_input_for_selected()
        self.out_model.request_output_for_selected()


    def on_table_view_input_clicked(self):
        print("clicked")

    def on_table_view_output_clicked(self):
        print("clicked")

    def on_TEST_clicked(self):
        all_nodes = SemanticData.semantic_nodes

        import warnings
        import matplotlib.cbook
        warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

        import networkx as nx
        import matplotlib.pyplot as plt


        options = {
            'node_color': 'White',
            'node_size': 500,
            'width': 3,
        }

        G = nx.Graph()
        # G.add_node('Berea')
        # G.add_edge(5,100)

        # for node in all_nodes:
        #     node_name = node.name
        #     G.add_node(node_name)
        #     for index, node_input in enumerate(node.in_objects):
        #         G.add_node(node_input)
        #         G.add_edge(node_input, node_name, weight = node.in_interactions[index])
        #         print(node_input)
        #         print(node.in_interactions[index])
        #
        # pos = nx.random_layout(G)

        # i = "MyNode"
        # G.add_node(i, pos=(1, 1))
        # G.add_node(2, pos=(2, 2))
        # G.add_node(3, pos=(1, 0))
        # G.add_edge(i, 2, weight=0.5)
        # G.add_edge(i, 3, weight="has")
        # pos = nx.get_node_attributes(G, 'pos')
        # pos = nx.random_layout(G)
        # nx.draw(G, pos, with_labels=True, font_weight='bold', **options)
        # labels = nx.get_edge_attributes(G, 'weight')
        # nx.draw_networkx_edge_labels(G, pos, with_labels=True, edge_labels=labels)
        # plt.savefig("Plot.png")
        #
        # img = mpimg.imread('Plot.png')
        # plt.imshow(img)
        # plt.show()

    def paintEvent(self, *args, **kwargs):
        pass

    @staticmethod
    def prompt_error(error_text):
        msg = QMessageBox()
        msg.setText(error_text)
        retval = msg.exec_()

def init_semantic_editor_gui():
    import sys
    app = QApplication(sys.argv)
    rule_editor = SemanticEditorController()
    app.exec_()


if __name__ == "__main__":
    init_semantic_editor_gui()
