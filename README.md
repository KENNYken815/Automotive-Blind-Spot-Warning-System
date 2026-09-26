# Automotive Blind Spot Warning System

Completed host-runnable reference simulator for detecting vehicles approaching from rear-side blind spots and producing left/right visual and audible driver warnings.

> Educational/reference implementation. It does not claim validation with real radar, ultrasonic sensors, cameras, or a production vehicle ECU.

## Implemented
- Left/right blind-spot zone classification
- Virtual vehicle position and relative-speed model
- Approaching-vehicle detection
- Detection debounce and warning hysteresis
- Left/right LED and buzzer states
- Project-defined diagnostic codes
- Deterministic demonstration scenarios
- Automated unit tests

## Project structure
```text
src/                 core application logic
scenarios/           ready-to-run demonstration cases
tests/               automated verification
docs/                architecture and test notes
run_demo.py          main entry point
Makefile             convenience commands
README.md            project guide
```

## Reference geometry
- Longitudinal blind-spot window: -5 m to +5 m
- Lateral window: 0.5 m to 3.5 m
- Approach threshold: > 2.0 m/s
- Warning qualification: 2 consecutive samples
- Warning clear: 3 consecutive clear samples

These are project parameters, not OEM specifications.

## Run
```bash
python3 run_demo.py
python3 -m unittest discover -s tests -v
```

Or:
```bash
make run
make test
```

## Demonstration scenarios
1. Clear road
2. Left blind-spot vehicle
3. Right-side approaching vehicle

## Diagnostic codes
- `BSW_000` No active warning
- `BSW_101` Left blind-spot occupied
- `BSW_102` Right blind-spot occupied
- `BSW_103` Left-side approaching vehicle
- `BSW_104` Right-side approaching vehicle
- `BSW_201` Left sensor timeout
- `BSW_202` Right sensor timeout
- `BSW_203` Invalid sensor data

These are project-defined IDs, not OEM identifiers.

## Hardware path
The virtual object layer can later be replaced with radar/ultrasonic/camera-derived detections and the output layer mapped to MCU GPIO, LEDs, buzzers, or CAN. Real sensor behavior, timing, functional safety, and vehicle integration require dedicated validation.

## Safety
This is not a certified driver-assistance system and should not be relied upon as a real vehicle safety function.
