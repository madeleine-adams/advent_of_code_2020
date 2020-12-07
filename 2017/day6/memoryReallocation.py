file = open('memoryReallocation_input.txt', 'r')
starting_input = file.readline()


def find_index_of_largest(number_array):
    index = 0
    largest = number_array[0]
    for x in range(1, len(number_array)):
        if number_array[x] > largest:
            largest = number_array[x]
            index = x
    return index


def reallocate(mem_banks, mem_index):
    blocks = mem_banks[mem_index]
    mem_banks[mem_index] = 0
    mem_index = (mem_index + 1) % len(mem_banks)
    while blocks > 0:
        mem_banks[mem_index] += 1
        blocks -= 1
        mem_index = (mem_index + 1) % len(mem_banks)
    return mem_banks


memory_banks = starting_input.split()
for i in range(len(memory_banks)):
    memory_banks[i] = int(memory_banks[i])

previous_allocs = set()
previous_allocs.add(memory_banks.__str__())

has_repeated = False
realloc_count = 0

while not has_repeated:
    index_to_realloc = find_index_of_largest(memory_banks)
    memory_banks = reallocate(memory_banks, index_to_realloc)
    realloc_count += 1
    if previous_allocs.__contains__(memory_banks.__str__()):
        has_repeated = True
    else:
        previous_allocs.add(memory_banks.__str__())
print(realloc_count)
