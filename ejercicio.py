from abc import ABC, abstractmethod


class Game:
    def __init__(self):
        self.frames = [NormalFrame() for _ in range(9)] + [TenthFrame()]

    def ingresar_puntaje(self):
        pass

    def calcular_score(self):
        puntaje_total = 0
        frame_index = 0

        for _ in range(10):
            frame = self.frames[frame_index]  # se obtiene el frame en donde evaluamos el puntaje

            if frame.is_strike():  # si es strike
                puntaje_total = self.strike(frame_index)
                frame_index += 1
            elif frame.is_spare():
                puntaje_total = self.spare(frame_index)
                frame_index += 1
            else:
                puntaje_total += frame.score()
                frame_index += 1

        return puntaje_total

    def strike(self, frame_index):
        next_frame = self.frames[frame_index + 1]    # Calcular el strike actual y de paso verificar si hay 2 strikes
        # seguidos
        if next_frame.is_strike():
            next_next_frame = self.frames[frame_index + 2]
            return 20 + next_next_frame.rolls[0]
        return 10 + next_frame.score()

    def spare(self, frame_index):
        next_frame = self.frames[frame_index + 1]
        if next_frame.is_spare():
            return 10 + next_frame.score()


class Frame(ABC):
    def __init__(self):
        self.rolls = []  # registro de las tiradas que realiza un jugador en un frame específico

    @abstractmethod
    def add_roll(self, pins: int):
        pass

    @abstractmethod
    def score(self) -> int:
        pass

    def is_spare(self) -> bool:
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def is_strike(self) -> bool:
        return len(self.rolls) == 1 and self.rolls[0] == 10


class NormalFrame(Frame):
    def add_roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        return sum(self.rolls)


class TenthFrame(Frame):
    def add_roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        return sum(self.rolls)


class Roll:

    def __init__(self, pins: int):
        self.pins: int = pins


game = Game()
tiradas = [5, 3, 3, 7, 10, 0, 6, 1, 9, 10, 10, 2, 5, 0, 0, 5, 5, 10]
game.ingresar_puntaje()
puntaje_final = game.calcular_score()
print("Puntaje final:", puntaje_final)
