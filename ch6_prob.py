import enum
import math
import random

import matplotlib.pyplot as plt

SQRT_TWO_PI = math.sqrt(2 * math.pi)


class Kid(enum.Enum):
    BOY = 0
    GIRL = 1


def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)


for _ in range(10000):
    younger, older = random_kid(), random_kid()
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

print("P(BOTH | OLDER):", both_girls / older_girl)
print("P(BOTH | EITHER):", both_girls / either_girl)


# Std normal -> Mu of 0, and std dev of 1
def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return math.exp(-((x - mu) ** 2) / 2 / sigma**2) / (SQRT_TWO_PI * sigma)


# uniform pdf...
# let's say you have 1000 values, and they each have an equal chance of being selected
# the value is 1/1000 = .001
# .001 * 1050 - 50 = 1 (entire area should sum up (integate) to 1)

xs = [x / 10 for x in range(-50, 50)]
# centered at 0, sigma of 1
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], "-", label="mu0,sigma=1")
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], "--", label="mu=0,sigma=2")
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ":", label="mu=0,sigma=0.5")
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], "-.", label="mu=-1,sigma=1")
plt.legend()
plt.title("Various normal distributions")
# plt.show()

plt.close()
plt.gca().clear()
plt.clf()


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], "-", label="mu=0,sigma=1")
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], "--", label="mu=0,sigma=2")
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ":", label="mu=0,sigma=0.5")
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], "-.", label="mu=-1,sigma=1")
plt.legend(loc=4)  # bottom right
plt.title("Various Normal cdfs")
plt.show()


# So then the inverse of the normal cdf (in goes the x, out comes probability), is in (prob) -> out (x that gives you that prob)
def inverse_normal_cdf(
    p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001
) -> float:
    """Find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0  # normal_cdf(-10) is (very close to) 0
    hi_z = 10.0  # normal_cdf(10)  is (very close to) 1
    mid_z = 0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # Consider the midpoint
        mid_p = normal_cdf(mid_z)  # and the cdf's value there
        if mid_p < p:
            low_z = mid_z  # Midpoint too low, search above it
        else:
            hi_z = mid_z  # Midpoint too high, search below it

    return mid_z


# def
