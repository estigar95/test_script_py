#Ejercicio Tipos de Datos en Pandas 1
import pandas as pd 
data = {"nombre" : ['Ana', 'Luis' , 'Carlos'], "edad" : [30, 25, 40] }
df_empleados = pd.DataFrame(data)
print(df_empleados)