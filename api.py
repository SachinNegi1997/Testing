from fastapi import FastAPI
# fastapi is file and FastAPI is class
# pip install fastapi
# pip install "fastapi [satandard]"

app=FastAPI(title="utilities")

@app.get("/home")

def home():

 return {"hello" : "this is return"}

# To execute fastapi use  fastapi dev



