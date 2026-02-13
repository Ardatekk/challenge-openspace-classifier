class Seat:

    #This class represents a seat.

    def __init__(self) -> None:
        #Initialize a seat.
        
        self.free = True
        self.occupant = ""

    def set_occupant(self, name: str) -> bool:
        #Assign someone to the seat.
        
        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False

    def remove_occupant(self) -> str:
        #Remove the person from the seat.

        person = self.occupant
        self.occupant = ""
        self.free = True
        return person

    def __str__(self) -> str:
        #Display the seat.

        if self.free:
            return "Free seat"
        return self.occupant


from typing import List

class Table:
    #A simple Table class that holds seats.

    def __init__(self, capacity: int = 4) -> None:
        #Initialize a table with a number of seats.

        self.capacity = capacity
        self.seats: List[Seat] = [Seat() for _ in range(capacity)]

    def has_free_spot(self) -> bool:
        #Check if the table has at least one free seat.
        
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name: str) -> bool:
        #Assign a person to the first free seat.
        
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self) -> int:
        #Count how many seats are still free.
        
        free_count = 0
        for seat in self.seats:
            if seat.free:
                free_count += 1
        return free_count

    def __str__(self) -> str:
        #Display the table with seat occupants.
        
        seat_strs = [str(seat) for seat in self.seats]
        return " | ".join(seat_strs)