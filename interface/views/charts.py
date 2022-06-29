import streamlit as st
from database.mongo_client import db_collection
import pandas as pd
import time

def charts():
    placeholder = st.empty()
    for seconds in range(100):

        with placeholder.container():

            col1, col2 = st.columns(2)

            data = db_collection.find()
            date, voltage, current = [], [], []

            print(data)

            for document in data:
                date.append(document['date'].strftime("%Y-%m-%d %H:%M:%S"))
                voltage.append(document['payload']['Fase1']['voltage'])
                current.append(document['payload']['Fase1']['current'])

            voltage_chart = pd.DataFrame({
                'date': date ,
                'voltage': voltage
            }).rename(columns={'date':'index'}).set_index('index')

            current_chart = pd.DataFrame({
                'date': date ,
                'current': current
            }).rename(columns={'date':'index'}).set_index('index')

            col1.line_chart(
                voltage_chart
            )

            col2.line_chart(
                current_chart
            )
        time.sleep(5)