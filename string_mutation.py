def mutate_string(arr,position, character):
    print(arr)
    list1 = list(arr)
    list1[position]=str(character)
    str1 = ''.join(list1)
    return str1
    
s = mutate_string('Jaton',3,'i')
print(s)
