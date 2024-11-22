import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s ||| %(levelname)s ||| %(message)s')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        if cls.is_frozen:
            print('Тесты в этом кейсе заморожены')

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_walk(self):
        try:
            runner_1 = Runner('num_1', speed=-9)
            self.assertEqual(runner_1.distance, 0)
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, runner_1.speed*10)
            logging.info('test_walk" выполнен успешно')
        except ValueError as veroor:
            logging.warning('Неверная скорость для Runner\n', exc_info=True)

        except TypeError as teroor:
            logging.warning('Неверный тип данных для объекта Runner\n', exc_info=True)

    @unittest.skipIf(is_frozen, 'Заморожено')
    def test_run(self):
        try:
            runner_2 = Runner(None)
            self.assertEqual(runner_2.distance, 0)
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, runner_2.speed*10*2)
            logging.info('test_run" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s ||| %(levelname)s ||| %(message)s')
    unittest.main()
