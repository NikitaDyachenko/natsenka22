from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class JSONData(BaseModel):
    GrossProfit: float
    RealizationProduct: float

app = FastAPI()

@app.get("/GrossProfitability/")
async def products_man(item: JSONData):
    GrossProfitability = str(round((item.GrossProfit/item.RealizationProduct)*100,2)) + " %"
    info = {"GrossProfitability": GrossProfitability}
    return JSONResponse(content=jsonable_encoder(info))

@app.get("/ExtraCharge")
async def get_extracharge(CostPrice, percent):
    extracharge = (double(CostPrice)/100-double(percent)) * 100;
    return {"Итоговая цена товара = ": str(extracharge)}

