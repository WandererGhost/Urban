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


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        if cls.is_frozen:
            print('Тесты в этом кейсе заморожены')

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_walk(self):
        runner_1 = Runner('num_1')
        self.assertEqual(runner_1.distance, 0)
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, runner_1.speed*10)

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_run(self):
        runner_2 = Runner('num_2')
        self.assertEqual(runner_2.distance, 0)
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, runner_2.speed*10*2)

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_challenge(self):
        runner_3 = Runner('num_1')
        self.assertEqual(runner_3.distance, 0)
        runner_4 = Runner('num_3')
        self.assertEqual(runner_4.distance, 0)

        for i in range(10):
            runner_3.run()
            runner_4.walk()

        self.assertNotEqual(runner_3.distance, runner_4.distance)


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
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        if cls.is_frozen:
            print('Тесты в этом кейсе заморожены')
        else:
            cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Заморожено')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        if cls.is_frozen is False:
            for result in cls.all_results.values():
                print(result)

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_tour_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[1].values())[-1] == "Ник")

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_tour_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[2].values())[-1] == "Ник")

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_tour_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[3].values())[-1] == "Ник")

    @unittest.skip('Требовалось для предыдущего задания. Сейчас в принципе заморожен')
    def test_raise(self):
        tour = Tournament(3, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[4] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[4].values())[-1] == "Ник")
        # Ник оказывается на втором месте

    @unittest.skip('Требовалось для предыдущего задания. Сейчас в принципе заморожен')
    def test_change(self):
        tour = Tournament_change (3, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[5] = {place: participant.name for place, participant in tour.start().items()}
        self.assertTrue(list(self.all_results[5].values())[-1] == "Ник")


if __name__ == '__main__':
    unittest.main()
