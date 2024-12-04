with open('24_open_kim2023.txt') as file:
    line = file.read()
    # line= "AAZZZZABZZZZZCBZZZZB"
        #   "**"
        #   "* *ZZZZ* *ZZZZZ* *ZZZZB"
          
    line = line.replace('A', '*').replace('B', '*').replace('C', '*')
    # line_1 = line.split('**')
    total = len(max(line.split('**'), key=len))
    print(total)