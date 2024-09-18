class Patient:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def __str__(self):
        return f'id:{self.id}, Name:{self.name}'
    
    def __repr__(self):
        return self.__str__()
    