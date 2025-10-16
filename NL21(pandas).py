import pandas as p

rainfall = {
    '10 am': [12, 13, 4, 2, 6, 7, 3, 9, 2, 5],
    '12 pm': [3, 7, 3, 9, 6, 0, 2, 5, 8, 3], 
    '4 pm': [4, 6, 3, 7, 3, 9, 1, 3, 0, 4],
    '6 pm': [1, 5, 3, 7, 8, 5, 9, 5, 3, 7]
}

report = p.DataFrame(rainfall, index=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9', 'day10'])
print(report)