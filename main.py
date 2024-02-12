import random
import pandas as pd
lst = ['robot'] * 10 #создаем новый список robot и умнажаем на 10 (тоесть создатся 10шт robot)
lst += ['human'] * 11 # таким же образом добовляем 11шт human
random.shuffle(lst)  #случайным образом переупорядочивает элементы в списке (он не создает новый список)
data = pd.DataFrame({'whoAmI':lst, 'robot':[i for i in lst], 'human':[i for i in lst]})# проходим по списку и записываем robot и human
data['robot']  = data['robot'].map({'robot': 1, 'human': 0}) #меняем их значения
data['human']  = data['human'].map({'robot': 0, 'human': 1})
print(data)





