from .models import Side,Zone
from .zone_classifier import classify
from .warning_logic import BlindSpotWarning
class BswSimulator:
 def __init__(self,cfg,objects=None):self.cfg=cfg;self.objects=list(objects or []);self.left=BlindSpotWarning(Side.LEFT,cfg);self.right=BlindSpotWarning(Side.RIGHT,cfg);self.time_s=0.0
 def step(self,dt=.2):
  self.time_s+=dt;la=ra=None;lf=rf=False
  for obj in self.objects:
   obs=obj.observe(self.time_s,dt)
   if obs is None:
    if obj.y_m<0:lf=True
    else:rf=True
    continue
   if not obs.valid:
    if obj.y_m<0:lf=True
    else:rf=True
    continue
   zone=classify(obs,self.cfg)
   if zone==Zone.LEFT:la=obs.relative_speed_mps>self.cfg.approach_speed_mps
   elif zone==Zone.RIGHT:ra=obs.relative_speed_mps>self.cfg.approach_speed_mps
  return self.left.update(Zone.LEFT if la is not None else Zone.CLEAR,bool(la),not lf),self.right.update(Zone.RIGHT if ra is not None else Zone.CLEAR,bool(ra),not rf)
 def run(self,duration,dt=.2):return [self.step(dt) for _ in range(int(duration/dt))]
