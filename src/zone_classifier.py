import math
from .models import Zone
def classify(o,c):
 if not o.valid or not all(math.isfinite(v) for v in (o.x_m,o.y_m,o.relative_speed_mps)): return Zone.CLEAR
 if c.min_longitudinal_m<=o.x_m<=c.max_longitudinal_m and c.min_lateral_m<=abs(o.y_m)<=c.max_lateral_m:return Zone.LEFT if o.y_m<0 else Zone.RIGHT
 return Zone.CLEAR
