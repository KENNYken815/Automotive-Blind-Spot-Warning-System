from scenarios.demo_scenarios import clear,left_vehicle,right_approaching,left_sensor_fault
from src.diagnostics import format_status

def main():
 for name,sim in [('CLEAR ROAD',clear()),('LEFT BLIND SPOT',left_vehicle()),('RIGHT APPROACHING',right_approaching()),('LEFT SENSOR FAULT',left_sensor_fault())]:
  print('\n'+'='*68+'\n'+name+'\n'+'='*68);s=sim.run(1.0)[-1];print(format_status(sim.time_s,*s))
if __name__=='__main__':main()
