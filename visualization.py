import matplotlib.pyplot as plt
import seaborn as sns

data = [10, 15, 7, 18, 22]
labels = ['запрос 1', 'запрос 2','запрос 3','запрос 4','запрос 5']

plt.figure(figsize=(10, 5))
sns.barplot(x=labels, y=data)
plt.title("Статистика запросов к приложению")
plt.xlabel('Запросы')
plt.ylabel('Количество')
plt.savefig('requests_status.png')
plt.show()