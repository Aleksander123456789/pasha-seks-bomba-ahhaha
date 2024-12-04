with open('24_open_kim2021.txt', mode='r') as file:
    line = file.readline()
    
    # line.replace("XYYZ", "XYY YYZ")
    slices = line.split("XZZY")
    a = list()
    for slice in slices:
        a.append(len(slice))
    maximum = max(a)
    
    # maximum = max(len(slice) for slice in slices)    
    maximum = max(slices, key=len)
    print(len(maximum) + 6)
    print("index of max", slices.index(maximum))
    print(len(slices))
    
    
