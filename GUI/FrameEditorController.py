import os

from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog, QHeaderView, QSizePolicy

from GUI.Common import *
from GUI.Models.FrameTreeModel import FrameTreeModel
from GUI.Views.FrameEditorView import Ui_FrameEditor


class FrameEditorController(QDialog):
    def init_gui(self):

        # self.ui.listViewESThemes.clearSelection()
        # self.clear_answers_and_questions()
        self.ui.pbLoad.clicked.connect(self.on_pb_load_clicked)
        self.ui.pbAddChild.clicked.connect(self.on_pb_add_child_clicked)
        self.ui.pbRemoveObject.clicked.connect(self.on_pb_remove_item_clicked)
        self.ui.pbAddNode.clicked.connect(self.on_pb_add_node_clicked)
        self.ui.pbGraph.clicked.connect(self.draw_graph)
        self.ui.pbSave.clicked.connect(self.on_pb_save_clicked)

    def on_pb_load_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, open_file_dialog_desc, "../" + es_knowledge_base_str_token + "/" + frame_str_token,
                                                  open_file_dialog_label, options=options)
        if fileName:
            print(fileName)
            self.clear_all()
            self.frame_model = FrameTreeModel()
            self.frame_model.load_frame_file(fileName)
            self.ui.treeViewFrames.setModel(self.frame_model)
            self.ui.treeViewFrames.resizeColumnToContents(0)
            self.ui.treeViewFrames.setColumnWidth(0, 400)

    def on_pb_save_clicked(self):
        import json
        data = self.frame_model.get_json_ready_data()

        json_str = json.dumps(data, indent=2)
        print(json_str)

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, open_file_dialog_desc, "../" + es_knowledge_base_str_token + "/" + frame_str_token,
                                                  open_file_dialog_label, options=options)

        # file_name = self.ui.textEditThemeName.text()
        file_path = os.path.join(os.path.dirname(os.getcwd()), es_knowledge_base_str_token)
        full_file_path = os.path.join(file_path, file_name)
        print(full_file_path)

        try:
            with open(full_file_path, "w") as write_file:
                json.dump(data, write_file, indent=2)
        except OSError as e:
            FrameEditorController.prompt_error("Json cannot be saved")
        pass

    def on_pb_add_child_clicked(self):
        index = self.ui.treeViewFrames.currentIndex()
        self.frame_model.add_child_at(index)

    def on_pb_add_node_clicked(self):
        index = self.ui.treeViewFrames.currentIndex()
        self.frame_model.add_item_at(index)

    def on_pb_remove_item_clicked(self):
        index = self.ui.treeViewFrames.currentIndex()
        self.frame_model.remove_item_at(index)

    def clear_all(self):
        del self.frame_model

    def draw_graph(self):
        root_item = self.frame_model.rootItem

        for node in root_item.frame_items:
            print(node.name)

        root_frames = []
        self.frame_model.all_graph_frames.clear()
        self.frame_model.connected_subgraph_names.clear()
        for node in root_item.frame_items:
            root_frames.append(node.name)
            self.frame_model.construct_graph_frame(node)

        from graphviz import Digraph

        g = Digraph('G', filename='cluster.gv')
        g.attr(compound='true')
        # NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
        #       so that Graphviz recognizes it as a special cluster subgraph

        for node in self.frame_model.all_graph_frames:
            with g.subgraph(name="cluster_" + node.frame_name) as c:
                slot_full_description = ""
                if node.value == "Connect":
                    slot_full_description = node.name
                else:
                    slot_full_description = node.name + "_" + node.value

                c.node(slot_full_description)
                c.attr(style='filled')
                c.attr(color='lightgrey')
                c.node_attr.update(style='filled', color='white')
                # c.edges([('a0', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
                c.attr(label=node.frame_name)
                # g.edge(slot_full_description, 'b0', lhead="cluster_" + slot_full_description)

                if not node.frame_name == "Connect" and node.frame_name not in self.frame_model.connected_subgraph_names and node.frame_name not in root_frames:
                    g.edge(node.frame_name, slot_full_description, lhead="cluster_" + node.frame_name)
                    self.frame_model.connected_subgraph_names.append(node.frame_name)

        import os

        f = os.path.join(os.getcwd(), "cluster.gv.pdf")
        if os.path.exists(f):
            try:
                os.rename(f, f)
                print('Access on file "' + f + '" is available!')
                g.view()
            except OSError as e:
                print('Access-error on file "' + f + '"! \n' + str(e))
                FrameEditorController.prompt_error("File is used by another process", "File Open Fail")


        # import pydotplus
        # import matplotlib.pyplot as plt
        # import matplotlib.image as mpimg
        #
        # graph = pydotplus.Dot(graph_type='digraph')
        # node_a = pydotplus.Node("Node A", style="filled", fillcolor="red")
        # node_b = pydotplus.Node("Node B", style="filled", fillcolor="green")
        # node_c = pydotplus.Node("Node C", style="filled", fillcolor="#0000ff")
        # node_d = pydotplus.Node("Node D", style="filled", fillcolor="#976856")
        #
        # graph.add_node(node_a)
        # graph.add_node(node_b)
        # graph.add_node(node_c)
        # graph.add_node(node_d)
        #
        # graph.add_edge(pydotplus.Edge(node_a, node_b, label="Yes"))
        # graph.add_edge(pydotplus.Edge(node_a, node_c, label="No"))
        # graph.add_edge(pydotplus.Edge(node_b, node_c, label="No"))
        # graph.add_edge(pydotplus.Edge(node_c, node_d, label="Maybe"))
        #
        # graph.add_edge(
        #     pydotplus.Edge(node_d, node_a, label="and back we go again", labelfontcolor="#009933", fontsize="10.0",
        #                    color="blue"))
        #
        # graph.write_png('example2_graph.png')
        # img = mpimg.imread('example2_graph.png')
        # plt.imshow(img)
        # plt.show()

    @staticmethod
    def prompt_error(error_text, title_text="Frame Editor"):
        msg = QMessageBox()
        msg.setText(error_text)
        msg.setWindowTitle(title_text)
        retval = msg.exec_()

    def __init__(self):
        super(FrameEditorController, self).__init__()
        self.ui = Ui_FrameEditor()
        self.ui.setupUi(self)
        self.init_gui()
        self.show()
        self.frame_model = FrameTreeModel()



def init_frame_editor_gui():
    import sys
    app = QApplication(sys.argv)
    frame_editor = FrameEditorController()
    app.exec_()


if __name__ == "__main__":
    init_frame_editor_gui()
