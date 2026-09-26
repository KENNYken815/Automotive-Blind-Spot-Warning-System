from .models import ObjectObservation
class VirtualObject:
 def __init__(self,object_id,x_m,y_m,relative_speed_mps=0.0): self.object_id=object_id;self.x_m=x_m;self.y_m=y_m;self.relative_speed_mps=relative_speed_mps;self.enabled=True;self.invalid=False
 def observe(self,timestamp_s,dt_s):
  if not self.enabled:return None
  self.x_m+=self.relative_speed_mps*dt_s
  if self.invalid:return ObjectObservation(timestamp_s,self.object_id,self.x_m,self.y_m,self.relative_speed_mps,False)
  return ObjectObservation(timestamp_s,self.object_id,self.x_m,self.y_m,self.relative_speed_mps,True)
