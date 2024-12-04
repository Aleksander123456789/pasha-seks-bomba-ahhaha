with open('24_aprobation2021.txt', mode='r') as file:
    main_line = file.read()
    main_line = main_line. \
        replace('G','*').\
        replace('W','*').\
        replace('P','*')
    line = main_line.split('*')
    maximum = len(max(line, key=len))
    print(maximum)

    
