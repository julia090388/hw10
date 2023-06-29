# Задание 44 В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

import = pandas, seaborn, random
     

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pandas.DataFrame({'whoAmI': lst})
data.head(20)


data.loc[data['whoAmI'] == 'robot', ['i_am_robot', 'i_am_human']] = [1, 0]
data.loc[data['whoAmI'] == 'human', ['i_am_human', 'i_am_robot']] = [1, 0]
data.head(n=20)
     


seaborn.heatmap(data[['i_am_robot', 'i_am_human']])
     
