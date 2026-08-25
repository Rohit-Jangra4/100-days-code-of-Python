# Question

import time

t = time.strftime('%H:%M:%S')
print("Current time:", t)

hour = int(input("Hour: "))

if hour >= 0 and hour < 12:
    print("Good morning Sir.")
elif hour >= 12 and hour < 17:
    print("Good afternoon Sir.")
elif hour >= 17 and hour <= 23:
    print("Good evening Sir.")
else:
    print("Invalid hour.")

    