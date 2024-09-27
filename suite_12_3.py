import unittest
import TournamentTestCase
import RunnerTestCase

st = unittest.TestSuite()
st.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTestCase.TournamentTest))
st.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTestCase.RunnerTest))

RaT = unittest.TextTestRunner(verbosity=2)
RaT.run(st)
