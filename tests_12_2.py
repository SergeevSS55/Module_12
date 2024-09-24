import unittest
import runner_and_tournament as RaT


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = RaT.Runner("Усэйн", speed=10)
        self.runner2 = RaT.Runner("Андрей", speed=9)
        self.runner3 = RaT.Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            result = {place: runner.name for place, runner in value.items()}
            print(f"{result}")

    def test_tournament1(self):
        tournament1 = RaT.Tournament(90, self.runner1, self.runner3)
        self.all_results['Tournament1'] = tournament1.start()
        self.assertTrue(self.all_results['Tournament1'][max(self.all_results['Tournament1'].keys())] == "Ник")

    def test_tournament2(self):
        tournament2 = RaT.Tournament(90, self.runner2, self.runner3)
        self.all_results['Tournament2'] = tournament2.start()
        self.assertTrue(self.all_results['Tournament2'][max(self.all_results['Tournament2'].keys())] == "Ник")

    def test_tournament3(self):
        tournament3 = RaT.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results['Tournament3'] = tournament3.start()
        self.assertTrue(self.all_results['Tournament3'][max(self.all_results['Tournament3'].keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
