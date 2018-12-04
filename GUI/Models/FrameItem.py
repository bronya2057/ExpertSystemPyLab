class FrameItem(object):
    def __init__(self, frame_name, slots={}, parent=None, slot_value="Frame"):
        self.parentItem = parent
        self.name = frame_name
        self.slots = slots
        self.slot_value = slot_value
        self.frame_items = []
        self.itemData = ["Frame Name", "Value", "Rel"]
        self.header_data = ["Frame hierarchy", "Value", "Relationship"]
        self.parse_slots()

    def parse_slots(self):
        if len(self.slots) > 0:
            for slot_name, slot_val in self.slots.items():
                if isinstance(slot_val,dict):
                    self.frame_items.append(FrameItem(slot_name, slot_val["slots"], self,slot_val))
                elif slot_name:
                    self.frame_items.append(FrameItem(slot_name, {}, self,slot_val))
                # FrameItem(slot, )

    def appendChild(self, item):
        # self.slots.update({name:item})
        self.frame_items.append(item)

    def insertChildren(self, position, count = 1):
        if position < 0 or position > len(self.frame_items):
            return False

        # for row in range(count):
            # data = [None for v in range(columns)]
        item = FrameItem("NewFrame", {}, self)
        self.frame_items.append(item)

        return True

    def child(self, row):
        return self.frame_items[row]

    def childCount(self):
        print("Node")
        print(self.name)
        print("ChildCount:")
        print(len(self.frame_items))
        return len(self.frame_items)

    def columnCount(self):
       return len(self.header_data)

    def data(self, column):
        try:
            if (column == 0):
                return self.name
            elif (column == 1):
                return self.slot_value
            elif (column == 2):
                return "TODO rel"
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        print("ROW: Node")
        print(self.name)
        print("parent:")
        print(self.parentItem.name)
        if self.parentItem:
            return self.parentItem.frame_items.index(self)

        return 0

    def header_data_val(self, column):
        try:
            return self.header_data[column]
        except IndexError:
            return None

    def set_name(self, name):
        self.name = name

    def remove_children_at(self, pos):
        if pos < len(self.frame_items):
            del self.frame_items[pos]
            print("GFW")

    def remove_parent(self):
        self.parentItem = None

    def childNumber(self):
        if self.parentItem != None:
            return self.parentItem.frame_items.index(self)
        return 0

    def removeChildren(self, position, count):
        if position < 0 or position + count > len(self.frame_items):
            return False

        for row in range(count):
            self.frame_items.pop(position)
        return True
