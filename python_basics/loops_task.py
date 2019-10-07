import time

start_time = time.time()
num_of_iter = 0

while time.time() - start_time < 1:
    num_of_iter += 1


init_time = time.time()
last_time = time.time()

for i in range(num_of_iter):
    last_time = time.time()

time_for = last_time - init_time

print("For loop time is {}, while loop time is {}".format(time_for, 1))

assert 1 < time_for, "You are wrong"
