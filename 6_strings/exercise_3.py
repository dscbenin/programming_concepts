def count_letters(strng, letter):
    count = 0
    for i in strng:
        if i == letter:
            count += 1
    return count

print(count_letters("cabana", "a"))