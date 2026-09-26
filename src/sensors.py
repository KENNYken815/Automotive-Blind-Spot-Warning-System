from .models import ObjectObservation
class VirtualObject:
 def __init__(self,oid,x,y,v=0.0): self.object_id=oid;self.x_m=x;self.y_m=y;self.relative_speed_mps=v;self.enabled=True;self.invalid=False
 def observe(self,t,dt):
  if not self.enabled:return None
  self.x_m+=self.relative_speed_mps*dt
  return ObjectObservation(t,self.object_id,self.x_m,self.y_m,self.relative_speed_mps,not self.invalid)
