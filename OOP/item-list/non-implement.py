from collections import UserList

class Inventory(UserList):
    def add_item(self, item):
        self.data.append(item)  # ใช้ self.data แทน self._items

    def remove_item(self, item):
        try:
            self.data.remove(item)
        except ValueError:
            raise ValueError(f"Item not found: {item}")

    # เพิ่มเติม method สำหรับ Read (อ่าน) และ Update (แก้ไข)
    def get_items(self):
        return self.data.copy()  # คืนค่าสำเนาเพื่อป้องกันการแก้ไขจากภายนอก

    def update_item(self, old_item, new_item):
        try:
            index = self.data.index(old_item)
            self.data[index] = new_item
        except ValueError:
            raise ValueError(f"Item not found: {old_item}")
