class Trainer:
    NEXT_TRAINER_ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.NEXT_TRAINER_ID
        Trainer.NEXT_TRAINER_ID += 1

    @staticmethod
    def get_next_id():
        return Trainer.NEXT_TRAINER_ID

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
