#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
#%%
#load the data as a pandas dataframe object
automobile = pd.read_csv('E:/Datasets/Automobile_data.csv')
automobile
#%%
# grouping based on 'company' 
company = automobile.groupby('company')
#%%
# how many records are there for BMW?
len(company.get_group('bmw'))
#%%
# each company's most expensive car
plt.style.use('fivethirtyeight')
company.price.max().plot(kind="barh")
plt.xlabel('price')
#%%
# rename column 'num-of-cylinders' to 'cylinders'
automobile.rename(columns={'num-of-cylinders':'cylinders'}, 
                  inplace=True)
#%%
# use a pie chart to find the proportions of number of cylinders
plt.style.use('ggplot')
automobile.cylinders.value_counts().plot(kind="pie",
                                         legend=True)
#%%
titanic = sns.load_dataset('titanic')
titanic
#%%
# load the titanic data
sns.countplot(x="deck",
              data=titanic)
#%%
# visualization using a pie chart
# replicate ggplot's style
plt.style.use('ggplot')
survived = titanic.survived.value_counts()
survived.plot(kind="pie",
              # show legend
              legend=True,
              # update labels
              labels=['Died', 'Survived'],
              # make one slide explode out
              explode=(0.10, 0),
              # add shadows
              shadow=True,
              colors=['green', 'orange'],
              autopct='%.2f',
              startangle=90)
#print(plt.figsize)
#%%
# adjusting the figure size
fig = plt.figure(figsize=(8, 8))
plt.pie(survived)