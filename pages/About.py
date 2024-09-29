import streamlit as st



# Set the title
st.title("Pridiction Model Terminologies and Info")

def set_bg_hack_url():
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.pexels.com/photos/450055/pexels-photo-450055.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack_url()


st.write(f'Dataset for the model can be found at {'https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge/data'}')

st.markdown('''
            ---
            ''')
# Create a section for explaining the terminologies
st.subheader("Terminologies Explained")


st.markdown("""
            
 ### Levy
A levy is a type of tax or duty imposed by a government on goods or services. In the context of car data, it may refer to additional charges related to the vehicle.

### Manufacturer
The manufacturer is the company that produces the car. Some of the top manufacturers in this dataset include:
- **Toyota**
- **BMW**
- **Mercedes-Benz**
- **Honda**
- **Audi**

### Model
The model refers to a specific version of a car produced by a manufacturer. Each model may have different specifications and features. Examples of top models are:
- **Toyota Corolla**
- **BMW X5**
- **Honda Accord**
- **Mercedes-Benz C-Class**
- **Audi A4**

### Category
A category represents the type or class of the vehicle. Categories can vary based on size, shape, or purpose. Some common categories are:
- **SUV**
- **Sedan**
- **Truck**
- **Coupe**
- **Hatchback**

### Leather
Indicates whether the car's interior (usually seats) is made of leather. This is a common feature in luxury vehicles.

### Fuel Type
Refers to the type of fuel the vehicle uses. Common fuel types are:
- **Petrol**
- **Diesel**
- **Electric**
- **Hybrid**

### Engine Volume
Engine volume refers to the capacity of the engine, usually measured in liters (L). It indicates how much air and fuel the engine can intake to produce power.

### Mileage
Mileage refers to the distance a car has traveled, usually measured in kilometers (km) or miles. It gives an idea of how much the car has been used.

### Cylinder
The number of cylinders in the engine indicates the engine's power potential. More cylinders usually mean more power but also higher fuel consumption.

### Gear Box
Gear box refers to the transmission type in the vehicle. Common types are:
- **Manual**
- **Automatic**

### Drive Wheels
This indicates which wheels of the car receive power from the engine. Some common drive wheels are:
- **Front-Wheel Drive (FWD)**
- **Rear-Wheel Drive (RWD)**
- **All-Wheel Drive (AWD)**

### Doors
The number of doors a vehicle has, typically 2, 4, or 5 (for SUVs or hatchbacks).

### Wheel
Refers to the car's wheels, which are usually categorized based on size and material.

### Color
Indicates the exterior color of the car. Popular colors include black, white, silver, blue, and red.

### Airbags
Airbags are safety features in a car that inflate upon impact to protect passengers. The more airbags, the safer the vehicle.

### Year Range
The year range indicates the manufacturing years of the car model. For example, a car model produced from 1940-2024 has a year range of 1940-2024.
""")



# Add a footer for additional context
st.markdown("""
---
*This file provides explanations of the terminologies used in our car price prediction model*
""")
