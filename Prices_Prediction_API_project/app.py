# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------
#                   R E N T   P R I C E   P R E D I C T I O N S   W I T H    F A S T   A P I    (Getaround Project)       
# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

# DOYON-DOUSSE Doriane (ds-fs-od-03) *****************************************************************************************



# ----------------------------------------------------------------------------------------------------------------------------
# Librairy importations °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

import json
import joblib
import uvicorn
import numpy as np
import pandas as pd 
from typing import List
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Request



# ----------------------------------------------------------------------------------------------------------------------------
# Description °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

presentation = """

---
<br />
<br />

## Predict your car renting price per day ! 💸 ##
⇢ Hello there and welcome the GetAround API ! 👋🏽   
⇢ **DOYON-DOUSSE Doriane** made this API documentation with passion, enjoy it 🩵 ✨ 🍀

<br />
<br />
---

### 🔸 What is Getaround API ? 🔸 ###

‣ Thanks to this API, you will be able to determine what your Getaround renting is going to cost you per day and in euro!  €

‣ Isn't it magic ?  🪄 

‣ Yep it is, all you will have to do is to enter different car characteristics like engine power, 
   fuel type, model, mileage, paint color, many others criterias are available and the API will return 
   you the rental price per day!  (Well the magic resides in the use of Machine Learning Model (**Random Forest Regressor**)
   working behind the scenes, but hey, act like nobody told you 🤫   

<br />
<br />
    
### 🔹 INPUT DATA : How is the input data formated ? 🔹 ###

‣ Be careful how you enter data, car cretirias are in JSON format, so in order to retrieve predictions you will have to write 
    carrefully and as the exact same format as the example bellow ✅

👇🏽 The car criteria should be a JSON, written exactly as in the example following : 👇🏽

```json
{
    "model_key": "Audi",
    "mileage": 97153,
    "engine_power": 160,
    "fuel": "diesel",
    "paint_color": "black",
    "car_type": "sedan",
    "private_parking_available": true,
    "has_gps": true,
    "has_air_conditioning": true,
    "automatic_car": false,
    "has_getaround_connect": true,
    "has_speed_regulator": true,
    "winter_tires": true
}
```

<br />
<br />

### ♦️ OUTPUT DATA : What type of output data should I receive ? ♦️ ###

‣ Here is the answer that you would receive for the example above:

```
[
  Taking into consideration all car characteristics inserted, here is the predicted rental price per day : 132.46 $
]
```

<br />
<br />


### 🚨 BE CAREFUL OF INPUT WRITTING : Can you explain again what should I insert carrefully ? 🚨 ###

‣ Okay, we understand how frustrating it can be when you can't retrieve informations because of the unclarity of the 
  API documentation... We've been there before! So don't worry, here's a little reminder of the exact way to enter 
  data in the input, so that you won't tear your hair out (your hairdresser says thanks 💇🏻‍♂️)  

‣ Even if a variable do not interest you, do not delete it in the input, make sure to complete every criterias 🫡

‣ The True or False variable has to be written in SMALL CAPS like this ➡️ true false 🤏🏽

👇🏽 Do not hesitate to copy/paste some of car characteristics listed here: 👇🏽

```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- model_key: it is the car brand your are looking for ----->  
             'Citroën', 'Peugeot', 'PGO', 'Renault', 'Audi', 'BMW', 'Ford', 'Mercedes', 'Opel', 'Yamaha',
             'Porsche', 'Volkswagen', 'KIA Motors', 'Alfa Romeo', 'Ferrari', 'Fiat', 'Lamborghini', 'Toyota',
             'Maserati', 'Lexus', 'Honda', 'Mazda', 'Mini', 'Mitsubishi', 'Nissan', 'SEAT', 'Subaru', 'Suzuki'. 

- mileage: it is the searched car's mileage --------------->  
             enter a positive number (integer <= 0)

- engine_power: it is the car's engine power -------------->  
             enter a positive number (integer < 0)

- fuel: it is the fuel of the car ------------------------->  
             'hybrid', 'diesel', 'petrol', 'electric'

- paint_color: it is the fuel of the car ------------------>  
             'blue', 'orange', 'white', 'red', 'brown', 'green', 'black', 'grey', 'beige', 'silver'

- car_type: it is the fuel of the car --------------------->  
             'estate', 'coupe', 'sedan', 'suv', 'van', 'hatchback', 'convertible', 'subcompact'

- private_parking_available: has a private parking or not ->  
             true / false 

- has_gps: if the car has or not GPS integrated ----------->  
             true / false 

- has_air_conditioning: if the car has or not A/C --------->  
             true / false 

- automatic_car: if the car is automatic or not ----------->  
             true / false 

- has_getaround_connect: car has GetAroundConnect or not -->  
             true / false 

- has_speed_regulator: car has speed regulator or not ----->  
             true / false 

- winter_tires: car has winter tires or not --------------->  
             true / false 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

<br />
<br />



---



"""


# ----------------------------------------------------------------------------------------------------------------------------
# Defining app & tags °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

tags_metadata = [
    {
        "name": "Machine Learning ENDPOINT",
        "description": "This is the endpoint where you can do your rental prices predictions",
    },
    {
        "name": "Random Data",
        "description": "Get random data information about 5 cars"
    },
]

app = FastAPI(
    title="🪄 GetAround API 🚖",
    description=presentation,
    version="0.1",
    contact={"name": "DOYON-DOUSSE Doriane"},
    openapi_tags=tags_metadata
)




# ----------------------------------------------------------------------------------------------------------------------------
# Building Pydantic class  °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Here we create a Pydantic class 
# Pydantic will permit us to do data validation so that we can write requests by our own
# Inside Base model there are all car variables or characteristics the user can enter with the associated data type 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class CarCharacteristics(BaseModel):
    model_key: str = 'Audi'
    mileage: Union[int, float] = 110000
    engine_power: Union[int, float] = 100
    fuel: str = "diesel"
    paint_color: str = "black"
    car_type: str = "sedan"
    private_parking_available: bool
    has_gps: bool
    has_air_conditioning: bool
    automatic_car: bool
    has_getaround_connect: bool
    has_speed_regulator: bool
    winter_tires: bool



# ----------------------------------------------------------------------------------------------------------------------------
# Building endpoints  °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°


@app.get("/data", tags=["Random Data"])
async def read_rental_cars_sample():
    getaround = pd.read_csv("https://jedha-deployment.s3.amazonaws.com/get_around_pricing_project.csv", index_col=0)
    rental = getaround.sample(5)
    return rental.to_dict("index")


@app.post("/predict", tags=["Machine Learning ENDPOINT"])
async def predict(CarCharacteristics: CarCharacteristics):
    data = pd.DataFrame(dict(CarCharacteristics), index=[0])
    try:
        machine_learning_model = joblib.load('RF_REG.joblib')
        data_preprocessor = joblib.load('preprocessor.joblib')
    except Exception as dosh:
        return {"ERROR : something went wrong...": str(dosh)}  
    try:
        X = data_preprocessor.transform(data)
    except Exception as dosh:
        return {"ERROR : something went wrong...": str(dosh)}  
    try:
        predictions_made = machine_learning_model.predict(X)
        return {f"Taking into consideration all car characteristics inserted, here is the predicted rental price per day : {round(predictions_made[0],2)} €"}
    except Exception as dosh:
        return {"ERROR : something went wrong...": str(dosh)}  




# ----------------------------------------------------------------------------------------------------------------------------
# Running Fast API  °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) 




# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------
#                                                 E N D   O F   T H E   S C R I P T
# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------