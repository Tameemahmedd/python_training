class Flight:
    def __init__(self, id=None, airline='', source='', destination ='', duration=0.0, fare=0.0) -> None:
        self.id = id
        self.airline = airline
        self.source = source
        self.destination = destination
        self.duration = duration
        self.fare = fare

    def __str__(self) -> str:
        return f'{self.id}, {self.airline}, {self.source}, {self.destination}, {self.duration}, {self.fare}'

    def __repr__(self) -> str:
        return self.__str__()