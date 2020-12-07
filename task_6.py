# Сдаюсь ~:-|

dict1 = {}
i = 0
with open('schedule.txt') as f:
   for line in f:
       name, lect, pract, lab = line.split(' ')
       print(line)
