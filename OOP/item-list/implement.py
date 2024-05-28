class Inventory:
    def __init__(self):
        self._items = []  # ใช้ _items เพื่อบ่งบอกว่าเป็น private attribute

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError(f"Item not found: {item}")

    def __len__(self):
        return len(self._items)

    # เพิ่มเติม method สำหรับ Read (อ่าน) และ Update (แก้ไข)
    def get_items(self):
        return self._items.copy()  # คืนค่าสำเนาเพื่อป้องกันการแก้ไขจากภายนอก

    def update_item(self, old_item, new_item):
        if old_item in self._items:
            index = self._items.index(old_item)
            self._items[index] = new_item
        else:
            raise ValueError(f"Item not found: {old_item}")
