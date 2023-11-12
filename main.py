from fastapi import FastAPI

app = FastAPI()
@app.get("/ExtraCharge")
async def get_extracharge(CostPrice, Percent):
    extracharge = (float(CostPrice))/(100-float(Percent)) * 100;
    return {"Итоговая цена товара = ": str(extracharge)}

