grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Jhonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = tuple(students)
srt_stds = tuple(sorted(students_)) # srt_stds - сокращение от sorted_students
a = (sum(grades[0]))/5
b = (sum(grades[1]))/4
j = (sum(grades[2]))/4
k = (sum(grades[3]))/3
s = (sum(grades[4]))/5
report_card = dict()
report_card.update({srt_stds[0]:a, srt_stds[1]:b, srt_stds[2]:j, srt_stds[3]:k, srt_stds[4]:s})
print(report_card)
key = input('Введите имя ученика: ') #дополнительно решил ввести выдачу значений из словаря путем пользовательского ввода ключа
print(report_card.get(key))




