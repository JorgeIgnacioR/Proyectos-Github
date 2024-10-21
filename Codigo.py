import pandas as pd
url='https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df=pd.read_csv(url)
#ver primeras 5 filas
print(df.head(10))
#sacar info del data frame
print(df.info())


#EMPEZAMOS CON LA LIMPIEZA DE DATOS


#verificamos si hay valores nulos
print(df.isnull().sum())
#eliminar filas con valores nulos
df=df.dropna().reset_index(drop=True)
#verificar si hay duplicados
print(df.duplicated().sum())
#eliminar duplicados
df=df.drop_duplicates() 
print(df)

#conversion de tipos de datos
df['Age']=df['Age'].astype(int)
#creacion de nueva columna para saber los familiares que habia con el.
df['Tamano familia']=df['SibSp']+ df['Parch']
#ordenar data frame
df_sorted=df.sort_values(by='Age').reset_index(drop=True) #ordenamos edad de menor a mayor y nos conviene reinicar el index porque sino queda desordenado
print(df_sorted)

#SACAMOS VALORES ESTADISTICOS

#calculamos media de la edad
print(df['Age'].mean())
#valor de ticket maximo pagado
print(df['Fare'].max())


#VISUALIZACION DE DATOS
#import matplotlib.pyplot as plt
#df['Age'].hist(bins=30)
#plt.xlabel('Age')
#plt.ylabel('Count')
#plt.show() #nos muestra un grafico que representa la cantidad de personas con las distintas edades.


#CREACION DE RESUMEN DE DATOS
#summary=df.describe()
#summary.to_csv('summary.csv')       

#CATEGORIZAMOS LA EDAD
def cateforize_age(age):
    if age<18:
        return 'Nino'
    elif age<60:
        return 'Adulto'
    else:
        return 'Anciano'
    
df['Categoria edad']=df['Age'].apply(cateforize_age)
print(df)

#MOSTRAR SOBREVIVIENTES
survived_df=df[df['Survived'] == 1].reset_index(drop=True) #le estamos diciendo que marque todos donde la columna surviver=1
print(survived_df)


#CALCULAMOS MEDIA DE LA EDAD SEGUN LA CLASE EN QUE VIAJABAN
mean_age_by_class=df.groupby('Pclass')['Age'].mean()
print(mean_age_by_class)

#SACAMOS POR SEXO Y CLASES LA MEDIA DE LOS TICKETS PAGADOS
pivot_table=df.pivot_table(index='Sex',columns='Pclass',values='Fare',aggfunc='mean')
print(pivot_table)