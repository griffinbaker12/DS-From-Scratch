class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            self.current -= 1
            return self.current
        raise StopIteration


# Cool that Python doesn't require us to manually handle the indices to get the items here because
# the object takes care of it itself
for number in Countdown(5):
    print(f"{number:3d}")

print(f"{5 * "-"}")

cd_iter = iter(Countdown(5))
for _ in range(5):
    print(f"{next(cd_iter):3d}")
