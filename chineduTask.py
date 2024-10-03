in_array = [2,4,6]
out_array = []
count = 1

for number in in_array:
    index = len(in_array) - count
    sum = in_array[index] + 1
    # print("logic: ",out_array.insert(index, sum))
    print(index)

    # out_array.insert(index, sum)
    # if sum < 10:
    #     count -= 1
    #     if count < 0:
    #         break
    #     for num in range(count, -1, -1):
    #         print(out_array.insert(num, in_array[index]))
    #         out_array.insert(num, in_array[index])

    count += 1

print(out_array)

