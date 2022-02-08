
from collections import defaultdict

cube_dict = defaultdict(lambda: [])


for i in range(10000):
    a = i ** 3
    a = [j for j in str(a)]
    a.sort(reverse = True)
    a = ''.join(a)
    a = int(a)

    cube_dict[a] += [i]

    if len(cube_dict[a]) == 5:
        print(cube_dict[a])
