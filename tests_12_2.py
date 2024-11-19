import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


"""
Возможное исправление логической ошибки в классе Tounament
"""


class Tournament_change:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break  # Прерываем цикл, чтобы не продолжать итерацию по удаленному участнику

        return finishers



class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_tour_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[1].values())[-1] == "Ник")

    def test_tour_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[2].values())[-1] == "Ник")

    def test_tour_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[3].values())[-1] == "Ник")
        
    """
    Дополнительные тесты
    def test_raise(self):
        tour = Tournament(3, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[4] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[4].values())[-1] == "Ник")
        # Ник оказывается на втором месте

    def test_change(self):
        tour = Tournament_change (3, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[5] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[5].values())[-1] == "Ник")
    """




if __name__ == '__main__':
    unittest.main()
