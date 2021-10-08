#My solution

cards = [7,5,9,0,3,1,6,2,4,8]

def select_sort(cards):

    for i in range(len(cards)-1):
        min_index = i
        for j in range(i+1,len(cards)):
            if cards[min_index] > cards[j]:
                min_index = j
        cards[i], cards[min_index] = cards[min_index], cards[i]
    return cards

print(select_sort(cards))

#Dongbin Na
#시간복잡도 N + (N-1) + ... + 2 = O(N ** 2)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
