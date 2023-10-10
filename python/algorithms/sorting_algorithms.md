### Insertionsort

![](working.png) 

### Ablauf

- [ ] declare an array (1) for the result
- [ ] convert the list with the input into an array (2)
- [ ] for each element in array (2) {
- [ ]     append element to array(1)
- [ ]     index = -1
- [ ] while the left neighbor is greater then the appended element {
- [ ]     swap them
- [ ]     index = index -1
- [ ]     if at the end of the array {break}
- [ ] }
- [ ] }

### Python Code

```python
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
```
