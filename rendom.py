import random

for i in range(3):
    print(random.randint(10, 20))
members = ['Allan', 'Jerald', 'Danton', 'Clinton']
leader = random.choice(members)
print(leader)