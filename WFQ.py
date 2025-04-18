#1 Get array
from collections import deque
from numpy.ma.core import append

input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen", \
                 "E Mike", "E Joe", "P Dee", "E Vicky", "E George",\
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
                 "P Dee", "S Bill", "S Chase", "E Price", "P Dee",\
                 "E Sue"]

#make queues
Premium = deque()
Standard = deque()
Economy = deque()
#Add to queues
for i in input_packets:
    if i[0] == "E":
        Economy.append(i)
    if i[0] == "S":
        Standard.append(i)
    if i[0] == "P":
        Premium.append(i)
print(Premium)
print(Standard)
print(Economy)

#Pop queues
while Premium or Standard or Economy:
    # Dequeue from Premium queue (3 times)
    if Premium:
        print(Premium.popleft())
    if Premium:
        print(Premium.popleft())
    if Premium:
        print(Premium.popleft())
    # Dequeue from Standard queue (2 times)
    if Standard:
        print(Standard.popleft())
    if Standard:
        print(Standard.popleft())
    # Dequeue from Economy queue (1 time)
    if Economy:
        print(Economy.popleft())