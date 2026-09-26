from .models import Side,Zone
from .zone_classifier import classify
from .warning_logic import BlindSpotWarning
class BswSimulator:
 def __init__(self,cfg,objects=None):self.cfg=cfg;self.objects=list(objects or []);self.left=BlindSpotWarning(Side.LEFT,cfg);self.right=BlindSpotWarning(Side.RIGHT,cfg);self.time_s=0.0
 def step(self,dt=.2):
  self.time_s+=dt;la=ra=None;lf=rf=False
  for o in self.objects:
   x=o.observe(self.time_s,dt)
   if x is None: continue
   if not x.valid:
    if o.y_m<0:lf=True
    else:rf=True
    continue
   z=classify(x,self.cfg)
   if z==Zone.LEFT:la=x.relative_speed_mps>self.cfg.approach_speed_mps
   elif z==Zone.RIGHT:ra=x.relative_speed_mps>self.cfg.approach_speed_mps
  return self.left.update(Zone.LEFT if la is not None else Zone.CLEAR,bool(la),not lf),self.right.update(Zone.RIGHT if ra is not None else Zone.CLEAR,bool(ra),not rf)
 def run(self,duration,dt=.2):return [self.step(dt) for _ in range(int(duration/dt))]
