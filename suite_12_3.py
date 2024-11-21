import unittest
import tests_12_3

tests_runner = unittest.TestSuite()

tests_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tests_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))


tests_test_runner = unittest.TextTestRunner(verbosity=2)
tests_test_runner.run(tests_runner)
