import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
def main():
	df = load_data()
	st.title('covid-19 country-wise tracking and comparison')
	countries = df.Country.unique()
	selected_countries = st.sidebar.multiselect('Select Countries to compare', countries)
	if selected_countries:
		subset_df = df[df.Country.isin(selected_countries)]
	else:
		subset_df = df[df.Country.isin(['India'])]
	fig1 = px.line(subset_df, x="Date", y="Confirmed", color='Country')
	fig2 = px.line(subset_df, x="Date", y="Recovered", color='Country')
	fig3 = px.line(subset_df, x="Date", y="Deaths", color='Country')
	st.header('Confirmed Cases')
	st.write(fig1)
	st.header('Recovered Cases')
	st.write(fig2)
	st.header('Deaths')
	st.write(fig3)
	st.markdown('''---''')
	st.markdown('Contributors')
	st.markdown('Supan Shah - https://github.com/Supan14')
	st.markdown('Harsh Thakkar - https://github.com/ht2631999')
	
@st.cache
def load_data():
	return pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
if __name__ == '__main__':
	main()
