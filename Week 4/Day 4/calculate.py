def calculation(a: int, b: int) -> tuple[int, int]:
    add = a + b
    take = a - b
    return add, take


res = calculation(40, 10)
print(res)
