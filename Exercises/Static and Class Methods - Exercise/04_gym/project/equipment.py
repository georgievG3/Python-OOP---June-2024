class Equipment:
    NEXT_EQUIPMENT_ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.NEXT_EQUIPMENT_ID
        Equipment.NEXT_EQUIPMENT_ID += 1

    @staticmethod
    def get_next_id():
        return Equipment.NEXT_EQUIPMENT_ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
