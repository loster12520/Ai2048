import random


def coding(number, times):
    res = []
    # 判断是否为负
    if number < 0:
        res.append(0)
        number = -number
    else:
        res.append(1)

    # 判断是否大于1
    if number > 1:
        res.append(1)
        number = 1 / number
    else:
        res.append(0)

    print(bin(int(number * (2 ** times)))[2:].zfill(times))
    print(bin(int(number * (2 ** times))))

    [res.append(int(bit)) for bit in bin(int(number * (2 ** times)))[2:].zfill(times)]

    return res


def uncoding(codingList, times):
    print(int("".join(str(c) for c in codingList[2:]), 2) / (2 ** times))
    return int("".join(str(c) for c in codingList[2:]), 2) / (2 ** times) * (-1 if codingList[0] == 0 else 1) ** (
        -1 if codingList[1] == 1 else 1)


if __name__ == "__main__":
    t = 32
    for _ in range(10):
        c = [0 if random.random() > 0.5 else 1 for _ in range(t + 2)]
        u = uncoding(c, t)
        print(f"{c} : {u}")

    # n = 10086
    # c = coding(n, t)
    # u = uncoding(c, t)
    # print(f"{n} {c} {u}")
