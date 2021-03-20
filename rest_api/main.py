
from fastapi import FastAPI
from mongo_connect import electronic_collection
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    p_id: str = Field(...)
    name: str = Field(...)
    price: str = Field(...)

def ErrorRepsonse(error, code, message):
    return {
        "error" : error,
        "code"  : code,
        "message" : message
        }

@app.post("/products/")
async def create_item(product: Product):
    print(Product)
    input_item = jsonable_encoder(product)
    print(input_item)
    insert_act = await electronic_collection.insert_one(input_item)
    return True

def get_json_from_doc(product_document):
    rt_rec = {}
    all_keys = list(product_document)
    all_keys.remove('_id')
    for key in all_keys:
        rt_rec[key] = product_document[key]
    return rt_rec

@app.get("/products/{product_id}")
async def create_item(product_id):
    query_product = await electronic_collection.find_one({"p_id": product_id})
    if query_product:
        print(query_product)
        return get_json_from_doc(query_product)
    else:
        return ErrorRepsonse('Not_found', 404, 'Product not found')

