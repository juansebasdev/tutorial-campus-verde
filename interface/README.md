# Visualización de Datos

Hasta este punto, ya tenemos un cliente que permite recibir datos a través del protocolo MQTT. Y otro cliente para la base datos, que se encarga del almacenamiento de datos en la base de datos.

Ahora, nos encargaremos de la presentación de los datos de una manera organizada y más entendible. Para ello, utilizaremos un framework que nos permite realizarlo de manera rápida y sencilla.

## Streamlit
![streamlit](https://eclecticaboutdata.com/wp-content/uploads/2021/10/DataVisualizationLibraries_HEADERIMAGE_1.png)


https://streamlit.io/

Es un framework open-source que facilita la implementación de interfaces de visualización para la presentación de datos. 

### Tres principios simples

+ Adopta la simplicidad de la secuencia de programación de Python
+ Añadir widgets es tan sencillo como de declarar una variable.
+ Despliegue instantáneo.

### Instalar Streamlit

```bash
pip install streamlit
```

Un vistazo rápido

```bash
streamlit hello
```

### Documentación Streamlit API Reference

https://docs.streamlit.io/

### Correr aplicación

```bash
streamlit run <app_name>
```

### Setup a menu

```python
# Add sidebar
st.sidebar.write('Bienvenido')

# Add a menu to sidebar
menu = ("op1", "op2", "op3")
selected_option = st.sidebar.selectbox("Seleccione una opción", menu, index=0)

# Change view
if selected_option == "op1":
    ...
elif selected_option == "op2":
    ...
elif selected_option == "op3":
    ...
```