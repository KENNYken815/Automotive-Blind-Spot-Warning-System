def format_status(t,l,r):
 a=l.active_dtc!='BSW_000' or r.active_dtc!='BSW_000'
 return '\n'.join([f'Time: {t:.1f}s | SYSTEM WARNING: {"ON" if a else "OFF"}',f' LEFT : {l.level.value:<11} LED={"ON" if l.led_on else "OFF":<3} BUZZER={"ON" if l.buzzer_on else "OFF":<3} DTC={l.active_dtc}',f' RIGHT: {r.level.value:<11} LED={"ON" if r.led_on else "OFF":<3} BUZZER={"ON" if r.buzzer_on else "OFF":<3} DTC={r.active_dtc}'])
