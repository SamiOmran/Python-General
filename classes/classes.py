"""Model for aircraft flights"""
from pprint import pprint as pp

class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError('No airline code in {0}'.format(number))
        if not number[:2].isupper():
            raise ValueError('Invalid airline code {0}'.format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError('Invalid route number {0}'.format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[2:]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat for a passenger.

        Args: a seat designater designator such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]


def main():
    # aircraft1 = Aircraft("G-EUPT", "Airbus A319", 22, 6)
    # print(aircraft1.seating_plan())
    flight = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", 22, 6))
    pp(flight._seating)

if __name__ == '__main__':
    main()
