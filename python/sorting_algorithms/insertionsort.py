############################ VARIABLES ###############################

input = "16488966731210545555236"
array = list(map(int, input))
result = [array[0]]
array.pop(0)

############################ MAIN ####################################

for i in array:
    result.append(i)
    index = -1
    while result[index] < result[index-1]:
        result[index], result[index-1] = result[index-1], result[index]
        index -= 1
        if index == -abs(len(result)): break

print(result)