import pandas as pd

df = pd.read_csv(r'C:\Users\Apara Maity\OneDrive\Desktop\titanic.csv')
df.info()

cols = ['Name', 'Ticket', 'Cabin']
df = df.drop(cols, axis=1)
#df = df.dropna()
#df.info()
dummies = []
cols = ['Pclass', 'Sex', 'Embarked']
for col in cols:
   dummies.append(pd.get_dummies(df[col]))
   titanic_dummies = pd.concat(dummies, axis=1)
df = pd.concat((df,titanic_dummies), axis=1)
df = df.drop(['Pclass', 'Sex', 'Embarked'], axis=1)
df.info()
df['Age'] = df['Age'].interpolate()
df.info()
print(df.head(50))


