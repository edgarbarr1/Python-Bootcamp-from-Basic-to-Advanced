import secrets


def flip_coin():
    rand = secrets.SystemRandom().random()
    if rand >= 0.5:
        return "Heads"
    else:
        return "Tails"


# function ovverriding
def flip_coin():
    if secrets.SystemRandom().random() >= 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(flip_coin())
print(flip_coin())
print(flip_coin())
print(flip_coin())
