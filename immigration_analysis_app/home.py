import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#config
st.set_page_config(layout="wide",
                   page_title="Immigration analysis app",
                   page_icon='🦆')


years=list(range(1980,2014))
cols_to_drop=['Type','Coverage','AREA','DEV','REG']
rename_dict={'OdName':'Country',
             'AreaName': 'Continent',
             'RegName':'Region',
             'DevName':'Status'}

@st.cache_data()

def load_data(path):
    df = pd.read_excel('Canada.xlsx', sheet_name=1, skiprows=20, skipfooter=2)
    df.drop(columns=cols_to_drop,inplace=True)
    df.rename(columns=rename_dict,inplace=True)
    df['Total']=df[years].sum(axis=1)   
    df.set_index('Country',inplace=True)
    return df

with st.spinner("Processing Immigration data...."):
    df=load_data('canada.xlsx')



st.image("https://prominentoverseas.com/wp-content/uploads/2022/04/canada-immigration_330195183.jpeg",use_column_width=True)
st.title("Immigration Analysis App")
total_immigration=df['Total'].sum()
st.subheader("Data Summary")
total_countries=df.shape[0]
duration='1980-2013'
c1,c2,c3,c4,c5,c6=st.columns(6)
c1.metric('Total countries',total_countries)
c2.metric('Years',duration)
c3.metric('Total immigration',total_immigration)

st.header("Imigration Visualisation")
fig=px.line(df,x=df.index,y='Total')
st.plotly_chart(fig, use_container_width=True)

top_countries=df.sort_values(by='Total',ascending=False).head(25)

c1,c2= st.columns([1,3])

limit =c2.slider("select number of countries",1,25,value=5)
countries=top_countries.index.tolist()[:limit]
countries_df=df.loc[countries,years].T
fig2=px.area(countries_df,x=countries_df.index,y=countries_df.columns)

c1.dataframe(top_countries)
c2.plotly_chart(fig2,use_container_width=True)


st.subheader("Trend comparison")
c1,c2=st.columns([1,3])
country_list=df.index.tolist()
countries=c2.multiselect("Select Countries",country_list)
if countries:
    countries_df=df.loc[countries,years].T
    fig3=px.line(
        countries_df,
        x=countries_df.index,
        y=countries_df.columns,
    )

    c2.plotly_chart(fig3, use_container_width=True)
    for country in countries:
        c1.info(f'{country}:{df.loc[country, "Total"]} Immigration')
    c2.plotly_chart(fig3,use_container_width=True)
    st.toast("your graph has been loaded",icon='❤️')