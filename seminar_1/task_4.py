# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

crane = 60 # Журавли

team = crane / 3
men = team / 2
kate = team * 2

print(f'Петя и Сергей сделали по {int(men)} журавликов.\nКатя сделала {int(kate)} журавликов')