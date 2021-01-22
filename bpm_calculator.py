#! python3
# bpm_calculator - Calculates bpm using tap temp in the console.


import time


# Display the program's instructions.
print('Press ENTER to begin, then continue pressing at your tempo to set the BPM.\nPress Ctrl-C to quit.')
input()         # Press Enter to begin
print('Started.')
startTime = time.time()
lastTime = startTime
time_deltas = []
presses = 0


# TODO: Start tracking the lap times.

try:
    while True:
        input()
        delta_time = (time.time() - lastTime)
        time_deltas.append(delta_time)
        if len(time_deltas) > 3:
            time_deltas.remove(time_deltas[0])
        total = 0
        for value in time_deltas:
            total += value
        bpm = round(60 / (total / len(time_deltas)))
        print(bpm)
        lastTime = time.time()

except KeyboardInterrupt:
    print('\nDone.')