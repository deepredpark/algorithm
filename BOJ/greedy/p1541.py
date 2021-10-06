calculation = input()

num_list = calculation.replace("+", "-").split("-")
num_list = list(map(int, num_list))
calc_list = []
for i in calculation:
    if not i.isdigit():
        calc_list.append(i)

for i in range(len(calc_list)):
    if calc_list[i] == "-":
        j = i
        while j < len(calc_list):
            calc_list[j] = "-"
            j += 1
        break

result = num_list[0]
for i in range(len(calc_list)):
    if calc_list[i] == "+":
        result += num_list[i+1]
    else:
        result -= num_list[i+1]

print(result)
