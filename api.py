from fastapi import FastAPI
from sysutil import all_detail
# fastapi is file and FastAPI is class
# pip install fastapi
# pip install "fastapi [satandard]"
#  import all_detail function from sysutil file
app=FastAPI(title="utilities")

@app.get("/home")

def home():

 return {"Hello" : "testing for api " }



@app.get("/info")
# creatin app when type "/info"  fuction call
def info(): 

   return all_detail()


# To execute fastapi use  fastapi dev



