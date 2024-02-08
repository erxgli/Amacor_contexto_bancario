def change_col_name(df):
    #ESTA FUNCION CAMBIA EL NOMBRE DE LA COLUMNA DE LA BASE DE DATOS
    #CREAMOS UNA LISTA VACIA PARA DESPUÉS ALMACENAR LOS NOMBRES ACTUALIZADOS DE LAS COLUMNAS
    lista_nombres = []
    for i in range(len(df.columns)):
        # CREAMOS UN BUCLE PARA QUE EL USUARIO INTRODUZCA LOS NUEVOS NOMBRES DE LAS COLUMNAS
        lista_nombres.append(input(f"Introduce el nombre de la columna {i+1}: "))
    #SUSTITUCION DE LOS ANTIGUOS NOMBRES DE LAS COLUMNAS POR LOS ACTUALIZADOS (ANTERIORMENTE GUARDADOS EN LA LISTA)    
    df.columns = lista_nombres
    return df

def drop_columns(df,lista_columnas):
    #ESTA FUNCION ELIMINA LAS COLUMNAS DE LA BASE DE DATOS:
    df = df.drop(columns=[lista_columnas])
    return df

def outliers(var):
    #ESTA FUNCION MUESTRA LOS OUTLIERS DE LA BASE DE DATOS
    q1=var.quantile(0.25)
    q3=var.quantile(0.75)
    riq=q3-q1
    sup=q3+1.5*(riq)
    inf=q1-1.5*(riq)
    outl=(var>sup) | (var<inf)
    return outl

def drop_outliers(df,lista_columnas_numericas):
    #ESTA FUNCION ELIMINA LOS OUTLIERS DE LA BASE DE DATOS.
    #ANTES DE UTILIZAR ESTA FUNCIÓN ES RECOMENDABLE UTILIZAR LA FUNCIÓN "ident_cat_num"
    for i in df.loc[:,lista_columnas_numericas]:
            df=df[~outliers(df[i])]
            return df


def val_duplicated(df):
    #ESTA FUNCIÓN MUESTRA LOS VALORES DUPLICADOS DE LA BASE DE DATOS
    import pandas as pd 
    return print(f"[+] Hay {df.val_duplicated().sum()} valores duplicados")



def drop_val_duplicated(df):
    # ESTA FUNCION ELIMINA LOS VALORES DUPLICADOS DE LA BASE DE DATOS
    import pandas as pd
    df = df.drop_duplicates()
    print(f"[+] Los valores duplicados han sido eliminados")
    return df


def val_nuls(df):
    #ESTA FUNCION MUESTRA LOS VALORES NULOS DE LA BASE DE DATOS
    import pandas as pd
    return print(f"[+] Hay {df.isnull().sum().sum()} valores nulos")

def drop_val_nuls(df):
    # ESTA FUNCION ELIMINA LOS VALORES NULOS DE LA BASE DE DATOS
    import pandas as pd
    df = df.dropna()
    print(f"[+] Los valores nulos han sido eliminados")
    return df

def ident_cat_num(df): 
    # ESTA FUNCION IDENTIFICA SI LOS DATOS SON DE TIPO NUMERICO O CATEGORICO
    import pandas as pd
    #CREAMOS UNA LISTA PARA DESPUÉS ALMACENAR LOS NOMBRES DE LAS COLUMNAS QUE SEAN NUMERICAS
    list_numericas = [] 
    #CREAMOS UNA LISTA PARA DESPUÉS ALMACENAR LOS NOMBRES DE LAS COLUMNAS QUE SEAN CATEGORICAS
    list_categoricas = []
    #RECORREMOS LAS COLUMNAS DE LA BASE DE DATOS
    for i in df.columns: 
        #IDENTIFICAMOS SI LOS DATOS QUE CONTIENE LA COLUMNA SON NUMERICOS
        if pd.api.types.is_numeric_dtype(df[i])== True:
            #ALMACENAMOS LOS NOMBRES DE LAS COLUMNAS QUE SEAN NUM
            list_numericas.append(i)
        else:
            #SINO LOS ALMACENAMOS LOS NOMBRES DE LAS COLUMNAS QUE SEAN CATEGORICAS
            list_categoricas.append(i)
    return list_numericas,list_categoricas


import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def apply_onehot_encoding(df, categorical_columns):

    # Copia del DataFrame original
    df_copy = df.copy()

    # Instancio el OneHotEncoder
    onehot = OneHotEncoder()

    # Aplico el OneHot a las columnas categóricas y guardo el resultado en 'encoded_data'
    encoded_data = onehot.fit_transform(df[categorical_columns])

    # Convierto 'encoded_data' en un DataFrame y lo llamo 'encoded_df'
    encoded_df = pd.DataFrame(encoded_data.toarray(), columns=onehot.get_feature_names_out(categorical_columns))

    # Reseteo el índice de los dos DataFrames antes de concatenarlos
    df_copy.reset_index(drop=True, inplace=True)
    encoded_df.reset_index(drop=True, inplace=True)

    # Concateno los dos DataFrames
    df_encoded = pd.concat([df_copy, encoded_df], axis=1)

    # Elimino las columnas originales categóricas
    df_encoded.drop(columns=categorical_columns, inplace=True)

    return df_encoded



def onehot_encoder_test(df,columns):
    #ESTA FUNCION SE ENCARGA DE HACER ONEHOT A LAS COLUMNAS QUE NECESITEMOS
    #ESTE ONEHOT ES PARA HACER "TEST" DE LOS DATOS
    #IMPORTAMOS LAS LIBRERIAS NECESARIAS
    import pandas as pd 
    import sklearn 
    from sklearn.preprocessing import OneHotEncoder
    onehot = OneHotEncoder()
    aux = onehot.transform(df[[columns]])
    encoded_df = pd.DataFrame(aux.toarray(),columns= onehot.get_feature_names_out([columns]))
    df.reset_index(drop=True,inplace=True)
    encoded_df.reset_index(drop=True,inplace=True)
    df = pd.concat([df,encoded_df],axis=1)
    df.drop(columns=[columns],inplace=True)
    return df