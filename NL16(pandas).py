# Data frame
import pandas as m

a = {
    'name': ['M.LAKSHMI NARASIMHULU', 'M.HARIMITHESH'],
    'age': [19, 19],
    'department': ['CSE', 'AIDS']
}

b = m.DataFrame(a,index=[1,2])
print(b)