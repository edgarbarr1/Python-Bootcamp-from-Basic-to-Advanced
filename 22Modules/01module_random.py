import secrets

fruit = ['apple', 'banana', 'cherry', 'straw berry']
res = secrets.SystemRandom().choice(fruit)
print(res)
res = secrets.SystemRandom().choice(fruit)
print(res)
res = secrets.SystemRandom().choice(fruit)
print(res)
