with open('3-1input.txt') as f:
#with open('test.txt') as f:
    read_data = f.readlines()

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', '{', ']', '}', '\\', '|', '`', '~', ';', ':', '\'', '\"', ',', '<', '>', '?', '/']

#num_array = [{}] * len(read_data)
num_array = {}
symbol_loc = []
for x, line in enumerate(read_data):
    temp_num = ''
    found_num = False
    x_y = ''
    for y, char in enumerate(line):
        if char.isdigit():
            if found_num == False:
                x_y = '{xval},{yval},'.format(xval = x, yval = y)
            found_num = True
            temp_num += char
        else:
            if found_num == True:
                found_num = False
                x_y += '{yval}'.format(yval = y)
                num_array[x_y] = int(temp_num)
                #num_array[int(xval)].update({[z for z in range(int(yval), y)]})
                x_y = ''
                temp_num = ''
            if char in symbols:
                symbol_loc.append((x, y))
sum = 0
for sym in symbol_loc:
    del_list = []
    #search the pattern around it:
    for key in num_array.keys():
        key_arr = key.split(',')
        li = range(int(key_arr[1]), int(key_arr[2]))
        # left and right
        if (int(key_arr[0]) == sym[0]) and ((int(key_arr[1]) - sym[1] == 1) or (sym[1] - int(key_arr[2]) == 0)):
            print(num_array[key])
            sum += num_array[key]
            del_list.append(key)
        # up and down
        elif (sym[1] in li or (sym[1] - 1) in li or (sym[1] + 1) in li) and ((sym[0] - 1) == int(key_arr[0]) or (sym[0] + 1) == int(key_arr[0])):
            print(num_array[key])
            sum += num_array[key] 
            del_list.append(key)
    for key in del_list:
        del num_array[key]
print(sum)

