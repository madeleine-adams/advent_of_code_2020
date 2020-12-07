file = open('aMazeOfTwistyTrampolinesAllAlike_input.txt', 'r')
lines = file.readlines()

instructions = [0] * len(lines)
for i in range(len(lines)):
    instructions[i] = int(lines[i].strip())

steps_taken = 0
current_index = 0

while 0 <= current_index < len(lines):
    i = current_index
    instruction = instructions[current_index]
    current_index += instruction
    if instructions[i] >= 3:
        instructions[i] -= 1
    else:
        instructions[i] += 1
    steps_taken += 1
print(steps_taken)
