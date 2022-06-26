import streamlit as st
from views.about_app import about_app

# Add sidebar
st.sidebar.write('Bienvenido')

# Add a menu to sidebar
menu = ["Sobre la App", "", ""]
selected_option = st.sidebar.selectbox("Seleccione una opción", menu)

if selected_option == "Sobre la App":
    about_app()

###///////////////////////////////////
# '''
#     DEFINE VIEWS TO SHOW DATA
# '''
#//////////////////////////////////###