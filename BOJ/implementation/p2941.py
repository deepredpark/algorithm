word = input()
croatia_alpha =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(len(croatia_alpha)):
    word = word.replace(croatia_alpha[i], str(i))

print(len(word))
