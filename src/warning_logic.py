from .models import Side,Zone,WarningLevel,WarningState
class BlindSpotWarning:
 def __init__(self,side,cfg):self.side=side;self.cfg=cfg;self.state=WarningState(side)
 def update(self,zone,approach,valid=True):
  if not valid:
   self.state=WarningState(self.side,WarningLevel.SENSOR_FAULT,True,False,'BSW_201' if self.side==Side.LEFT else 'BSW_202');return self.state
  target=Zone.LEFT if self.side==Side.LEFT else Zone.RIGHT
  if zone==target:
   self.state.detect_count+=1;self.state.clear_count=0
   if self.state.detect_count>=self.cfg.detect_samples:self.state.level=WarningLevel.APPROACHING if approach else WarningLevel.OCCUPIED;self.state.led_on=True;self.state.buzzer_on=approach;self.state.active_dtc=('BSW_103' if self.side==Side.LEFT else 'BSW_104') if approach else ('BSW_101' if self.side==Side.LEFT else 'BSW_102')
  else:
   self.state.detect_count=0;self.state.clear_count+=1
   if self.state.clear_count>=self.cfg.clear_samples:self.state=WarningState(self.side)
  return self.state
