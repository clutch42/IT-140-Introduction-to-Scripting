replace_dictionary = {}
replace_list = input().split()
replace_sentence = input().split()
for i in range(len(replace_list)):
    if i % 2 == 0:
        replace_dictionary.update({replace_list[i] : replace_list[i+1]})
for i in range(len(replace_sentence)):
    if replace_sentence[i] in replace_dictionary:
        replace_sentence[i] = replace_dictionary[replace_sentence[i]]
print(' '.join(replace_sentence))