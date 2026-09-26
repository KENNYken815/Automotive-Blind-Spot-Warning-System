from dataclasses import dataclass
from enum import Enum
class Side(str,Enum): LEFT='LEFT'; RIGHT='RIGHT'
class Zone(str,Enum): CLEAR='CLEAR'; LEFT='LEFT_BLIND_SPOT'; RIGHT='RIGHT_BLIND_SPOT'
class WarningLevel(str,Enum): NONE='NONE'; OCCUPIED='OCCUPIED'; APPROACHING='APPROACHING'; SENSOR_FAULT='SENSOR_FAULT'
@dataclass
class ObjectObservation: timestamp_s:float; object_id:int; x_m:float; y_m:float; relative_speed_mps:float; valid:bool=True
@dataclass
class WarningState: side:Side; level:WarningLevel=WarningLevel.NONE; led_on:bool=False; buzzer_on:bool=False; active_dtc:str='BSW_000'; detect_count:int=0; clear_count:int=0
