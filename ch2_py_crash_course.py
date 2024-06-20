list1 = list(range(1, 4))
list2 = ["a", "b", "c"]

pairs = [pair for pair in zip(list1, list2)]
print(pairs)

# This is the same as...
l, n = zip(*pairs)
print(l, n)

# Doing
l2, n2 = zip(("a", 1), ("b", 2), ("c", 3))
print(l2, n2)


def magic(*args, **kwargs):
    print("unnamed", args)
    print("named", kwargs)


magic(1, 2, 3, name="joe")

# Very useful for higher-order fns to accept arbitrary amount of arguments
