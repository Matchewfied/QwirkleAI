import numpy as np


def sample_partition_points(N: int, D: int):
    final = sample_points(N // D, np.pi)
    for i in range(1, D):
        inter = sample_points(N // D, np.pi) + i * np.pi
        final = np.concatenate((inter, final))

    final = final / D
    assert(final.size == N)
    return final




def sample_points(N: int, scale: int):
    return scale * np.random.rand(N)

def inner_sin_cos(points):
    s = np.sin(points)
    c = np.cos(points)
    return np.dot(s, c) / points.size

"""idx = 10
while idx < 1000001:
    #p = sample_points(idx, np.pi)
    p = sample_partition_points(idx, 10)
    val = inner_sin_cos(p)
    print(f"Dot product with {idx} points: {val}")
    idx *= 10"""

def digit_sum(n):
    d_sum = 0
    while n > 0:
        d_sum += (n % 10)
        n //= 10
    return d_sum

off_lst_1 = []
off_lst_2 = []
for i in range(10000000):
    if i % 9 == 0 and digit_sum(i) % 9 != 0:
        off_lst_1.append(i)
    elif digit_sum(i) % 9 == 0 and i % 9 != 0:
        off_lst_2.append(i)

print("Off Lst 1", off_lst_1)
print("Off Lst 2", off_lst_2)
