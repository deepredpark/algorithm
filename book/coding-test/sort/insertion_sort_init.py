#My solution

cards = [7,5, 9, 0,3,1,6,2,4,8]

def insertion_sort(cards):

    for i in range(1,len(cards)):
        num = cards.pop(i)
        min_index = 0
        j = 0
        while j < i:
            if num <= cards[j]:
                break
            else:
                min_index += 1
            j += 1
        cards.insert(min_index, num)
    return cards

print(insertion_sort(cards))

#Dongbin Na
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
        print(array)
print(array)
