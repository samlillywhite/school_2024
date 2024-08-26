try:
    file_to_read = 'barney.txt'
    a = 10.7 / 0
    fin = open(file_to_read, 'r')
except FileNotFoundError:
    print('File not found', file_to_read)
except ZeroDivisionError:
    print('idiot')
