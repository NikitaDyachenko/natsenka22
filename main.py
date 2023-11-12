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

@app.get("/GrossProfitability")
async def get_profitability(GrossProfit, RealizationProduct):
    GrossProfitability = float(GrossProfit) / float(RealizationProduct)
    percent_value = GrossProfitability * 100;
    result = str(percent_value) + ' %'
    return {"Валовая рентабельность продукции = ": result}

@app.get("/Revenue_forecast_by_the_end_of_the_month")
async def get_revenue_forecast_by_the_end_of_the_month(Fact_revenue, Lasts_days, Remains_days):
    FORECAST = int(Fact_revenue)/(int(Lasts_days)*int(Remains_days))
    return {"Прогноз выручки до конца месяца = ": str(FORECAST)}

@app.get("/The_forecast_of_the_implementation_of_the_plan_as_a_percentage")
async def get_forecast_of_the_implementation_of_the_plan_as_a_percentage(FORECAST, Plan_revenue):
    PERCENTAGE_FORECAST = (int(FORECAST)*100)/int(Plan_revenue)
    return {"Выполнение плана на % (прогноз) = ": str(PERCENTAGE_FORECAST) + ' %'}

@app.get("/Hello/")
async def root():
    return {"message": "Hello World"}
