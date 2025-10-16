import pandas as pd

rain = {
    'day1': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 10, 8, 4],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day2': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 10, 8, 13],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day3': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 10, 13, 14],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day4': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 10, 5, 0],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day5': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 9, 8, 4],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day6': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 3, 8, 4],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day7': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [13, 10, 8, 4],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day8': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 10, 4, 4],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day9': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 10, 8, 1],
        'measure': ["cm", "cm", "cm", "cm"]
    },
    'day10': {
        'timing': ["10'O clock", "12'O clock", "4'O clock", "6'O clock"],
        'rainfall': [12, 10, 0, 0],
        'measure': ["cm", "cm", "cm", "cm"]
    }
}
w1=pd.DataFrame(rain['day1'])
w2=pd.DataFrame(rain['day2'])
w3=pd.DataFrame(rain['day3'])
w4=pd.DataFrame(rain['day4'])
w5=pd.DataFrame(rain['day5'])
w6=pd.DataFrame(rain['day6'])
w7=pd.DataFrame(rain['day7'])
w8=pd.DataFrame(rain['day8'])
w9=pd.DataFrame(rain['day9'])
w10=pd.DataFrame(rain['day10'])
print("day 1:\n",w1,"\n","day 2:\n",w2,"\nday 3:\n",w3,"\n","\nday 4:\n",w4,"\nday 5:\n",w5,"\n","\nday 6:\n",w6,"\nday 7:\n",w7,"\n","\nday 8:\n",w8,"\nday 9:\n",w9,"\n","\nday 10:\n",w10)