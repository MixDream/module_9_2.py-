first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
all_strings= first_strings+second_strings
first_result = [len(x) for x in first_strings if len(x)>5]
second_result = []
for x1 in first_strings:
    for x2 in second_strings:
        if len(x1) == len(x2):
            second_result.append((x1, x2))
third_result={x: len(x) for x in all_strings if len(x) % 2 == 0}
print(first_result)
print(second_result)
print(third_result)
