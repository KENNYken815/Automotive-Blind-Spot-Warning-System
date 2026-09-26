import unittest
from src.config import BswConfig
from src.models import Side,Zone,WarningLevel,ObjectObservation
from src.zone_classifier import classify
from src.warning_logic import BlindSpotWarning
class TestBsw(unittest.TestCase):
 def test_zones(self):
  c=BswConfig();self.assertEqual(classify(ObjectObservation(0,1,-1,-2,0),c),Zone.LEFT);self.assertEqual(classify(ObjectObservation(0,2,1,2,0),c),Zone.RIGHT);self.assertEqual(classify(ObjectObservation(0,3,-10,2,0),c),Zone.CLEAR)
 def test_debounce(self):
  w=BlindSpotWarning(Side.LEFT,BswConfig());w.update(Zone.LEFT,False);self.assertEqual(w.state.level,WarningLevel.NONE);w.update(Zone.LEFT,False);self.assertEqual(w.state.level,WarningLevel.OCCUPIED)
 def test_approach(self):
  w=BlindSpotWarning(Side.RIGHT,BswConfig());w.update(Zone.RIGHT,True);w.update(Zone.RIGHT,True);self.assertEqual(w.state.level,WarningLevel.APPROACHING);self.assertTrue(w.state.buzzer_on)
 def test_sensor_fault(self):
  w=BlindSpotWarning(Side.LEFT,BswConfig());w.update(Zone.CLEAR,False,False);self.assertEqual(w.state.active_dtc,'BSW_201')
if __name__=='__main__':unittest.main()
