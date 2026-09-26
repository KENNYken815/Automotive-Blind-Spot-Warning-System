from dataclasses import dataclass
@dataclass(frozen=True)
class BswConfig:
    max_lateral_m: float=3.5
    min_lateral_m: float=0.5
    min_longitudinal_m: float=-5.0
    max_longitudinal_m: float=5.0
    approach_speed_mps: float=2.0
    detect_samples: int=2
    clear_samples: int=3
