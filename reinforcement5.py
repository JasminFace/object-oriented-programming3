digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
tag = ['isa', 'dalawa', 'tatlo', 'apat', 'lima', 'anim', 'pito', 'walo', 'siyam']

numbers = {}
for i in range(len(digits)):
    numbers[digits[i]] = {
        'english': en[i],
        'french': fr[i],
        'tagalog': tag[i]
    }

print(numbers)