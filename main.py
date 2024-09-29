import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Function to load the CSS from the external file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the external CSS file
load_css("style.css")

#Function to set back ground image
def set_bg_hack_url():
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://unsplash.com/photos/a-black-background-with-a-blue-abstract-design-OfdOEdGYiuk");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack_url()


with open('rf_model.pkl', 'rb') as file:
    model_loaded = pickle.load(file)  
    


df=pd.read_csv('car_price_prediction.csv')

st.title('Car Price Pridiction')
st.write('This is a simple car price prediction app')



# Create two columns for input fields
col1, col2 = st.columns([1, 1])
st.write("")

with col1:
    levy = st.number_input('Enter Levy:')
    manufacturer = st.selectbox('Enter Manufacturer:', df['Manufacturer'].value_counts().head(5).index.unique())
    model = st.selectbox('Enter Model:', df['Model'].value_counts().head(5).index.unique())
    category = st.selectbox('Enter Category:', df['Category'].value_counts().head(5).index.unique())
    leather = st.selectbox('Do you want leather interior:', df['Leather interior'].unique())
    fuel_type = st.selectbox('Fuel Type:', df['Fuel type'].unique())
    engine_volume = st.number_input('Enter Engine Volume:')
    year = st.number_input('Enter Year Manufactured:', min_value=1940, max_value=2024)
    
with col2:
    milage = st.number_input('Enter Milage:')
    cylinder = st.number_input('Number of Cylinders:',min_value=2,max_value=8)
    gear_box = st.selectbox('Gear Box Type:', df['Gear box type'].unique())
    drive_wheels = st.selectbox('Drive Wheels:', df['Drive wheels'].unique())
    doors = st.number_input('Enter Doors:',min_value=2,max_value=6)
    wheel = 4
    color = st.selectbox('Color:', df['Color'].value_counts().head(5).index.unique())
    airbags = st.number_input('Enter Number of Airbags:',min_value=1, max_value=8)
    

# Function to categorize the year
def year_range(year):
    if year<1969:
        return 'vintage'
    elif 1960<year<1969:
        return '1960s'
    elif 1970<year<1979:
        return '1970s'
    elif 1980<year<1989:
        return '1980s'
    elif 1990<year<1999:
        return '1990s'
    elif 2000<year<2009:
        return '2000s'
    elif 2010<year<2019:
        return '2010s'
    else:
        return '2020s'


# Pre processing input data
input_lst = [levy, manufacturer, model, category, leather, fuel_type, engine_volume, milage, cylinder, gear_box, drive_wheels, doors, wheel, color, airbags, year_range(year)]
data = pd.DataFrame([input_lst], columns=[
    'Levy', 'Manufacturer', 'Model', 'Category', 'Leather interior', 
    'Fuel type', 'Engine volume', 'Mileage', 'Cylinders', 
    'Gear box type', 'Drive wheels', 'Doors', 'Wheel', 'Color', 
    'Airbags', 'year_cat'
])

data_object=data.select_dtypes(include='object')




if(st.button('Predict')):
  le=LabelEncoder()
  for col in data_object.columns:
        data[col]=le.fit_transform(data[col])
  
  result=model_loaded.predict(data)
  st.write(f"**Predicted Car Price: $** {round(result[0],2)}")



