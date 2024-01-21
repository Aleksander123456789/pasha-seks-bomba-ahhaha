def test_a(a: int) -> bool:
    for x in range(1000):
        for y in range(1000):
            if (48 != y + 2*x) or (a < x) or (a < y):
                pass
            else:
                return False
    return True

for a in range(300,0,-1):
    try:
        for x in range(1000):
            for y in range(1000):
                if (48 != y + 2*x) or (a < x) or (a < y):
                    pass
                else:
                    raise ValueError("не подходит a")
    except ValueError:
        continue
    print(a)
    break            
