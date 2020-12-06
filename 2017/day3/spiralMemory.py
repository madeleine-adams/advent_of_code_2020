import math
memory_index = 347991

# find which ring our index is in by taking the square root
square_root = math.ceil(math.sqrt(memory_index))
if square_root % 2 == 0:
    square_root += 1

square_index = math.floor(square_root / 2)
square = square_index ** 2

center_distance = square_index

edge_distance = 0
if square_root - 1 != 0:
    edge_distance = (memory_index-math.ceil(square_root/2)) % (square_root - 1)

print(center_distance + edge_distance)
