from src.config import BswConfig
from src.sensors import VirtualObject
from src.simulator import BswSimulator
def clear():return BswSimulator(BswConfig())
def left_vehicle():return BswSimulator(BswConfig(),[VirtualObject(1,-1,-2,0)])
def right_approaching():return BswSimulator(BswConfig(),[VirtualObject(2,-4,2,2.5)])
def left_sensor_fault():
 o=VirtualObject(3,-1,-2,0);o.invalid=True;return BswSimulator(BswConfig(),[o])
