# использование %
print('В команде \"Мастера кода\" %(team1_num)s участников' % {'team1_num': 5})
print('В команде \"Волшебники данных\" %(team2_num)s участников' % {'team2_num': 6})
print('Итого сегодня в командах участников : %(team1_num)s и %(team2_num)s' % {'team1_num': 5, 'team2_num': 6})

# использование format()

print("Команда \"Волшебники данных\" решила  {score_2} задач".format(score_2=42))
print('\"Волшебники данных\" решили задачи за {team1_time}с !'.format(team1_time=18015.2))

# использование f-строка
score_1 = 40
score_2 = 42
chalenge_result = 'победа команды \"Мастера кода\"!'
task_total = score_1 + score_2
time_avg = 350.4

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы:{chalenge_result}')
print(f'Сегодня было решено {task_total} задач, в среднем {time_avg} секунды на задачу')


