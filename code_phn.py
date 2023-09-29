import pandas as pd
#agrego linea de comentarios
df1 = pd.read_csv('input.csv',header=0)

df1.set_index('id', inplace=True)

df2 = pd.DataFrame([[1,5],[2,8],[3,14]], columns=['id','years'])

df2.set_index('id', inplace=True)


dfJoin = df1.join(df2, on='id', how='inner')

print(dfJoin)
print()
print(dfJoin.max())

i = dfJoin['years'].idxmax()

print()
print(i)

dfr = dfJoin.loc[i]

print()
print(dfr)

max = dfJoin['years'].max()

print(max)
print()
print()
#dfr2 = dfJoin[dfJoin['years']==max]

#print(dfJoin['years']==max)

print()
#print(dfr2)

dfr2 = dfJoin[dfJoin['years']==max]

print(dfr2)

dfr2.to_csv("output.csv", header=True)

