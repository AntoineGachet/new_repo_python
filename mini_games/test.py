import random 
y_pos = random.randint(-800, 800)
x_pos = random.randint(2, 3)
if x_pos == 2:
    x_direction = -1
else:
    x_direction = 1
y_direction = y_pos  # y_pos/1000
for n in range(100):
    print(y_direction)
