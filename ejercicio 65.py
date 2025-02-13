#Ejercicio Tipos de Datos en Pandas 2
import pandas as pd 
data = {"nombre" : ['Ana', 'Luis' , 'Carlos'], "edad" : [30, 25, 40] }
df_empleados = pd.DataFrame(data)
edades = df_empleados.edad
print(edades)
print(type(edades))