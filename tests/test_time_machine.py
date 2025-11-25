import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.time_machine import VirtualTimeMachine, TimeTravelType
from src.simple_time_machine import SimpleTimeMachine

class TestTimeMachine(unittest.TestCase):
    def setUp(self):
        self.machine = VirtualTimeMachine()
        self.simple_machine = SimpleTimeMachine()
    
    def test_past_travel(self):
        result = self.machine.execute_time_travel(1969, TimeTravelType.PAST)
        self.assertTrue(result['success'])
        self.assertEqual(result['current_year'], 1969)
    
    def test_future_travel(self):
        result = self.machine.execute_time_travel(2050, TimeTravelType.FUTURE)
        self.assertTrue(result['success'])
        self.assertEqual(result['current_year'], 2050)
    
    def test_simple_machine_travel(self):
        result = self.simple_machine.travel_to_year(1985)
        self.assertIn("successful", result)
        self.assertEqual(self.simple_machine.current_year, 1985)

if __name__ == '__main__':
    unittest.main()
