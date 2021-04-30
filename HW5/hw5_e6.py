import re

lessons_dict = dict()
my_filename = r'e6_lessons.txt'
with open(my_filename, 'r') as lessons:
    while True:
        line = lessons.readline()
        if not line:
            break
        my_key = line.split()
        total_lessons = 0
        for key in my_key:
            key = re.sub('\(\w+\)', '', key)
            try:
                total_lessons += int(key)
            except ValueError:
                total_lessons += 0
        lessons_dict.update({re.sub('\:', '', my_key[0]): total_lessons})
print(lessons_dict)
