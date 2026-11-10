from fastapi import APIRouter, Depends
from dto.dto_category import dto_category_create
from services.service_category import Service_Category


router_category = APIRouter(prefix="/category" , tags=["categories"])

@router_category.post("/create")
def create_category(new_category : dto_category_create , service_category = Depends(Service_Category)) :
    return service_category.create_category(new_category)

@router_category.get("/all")
def get_all_categories(service_category = Depends(Service_Category)):
    return service_category.find_all_categories()

@router_category.put("/update")
def update_category(id : str, new_name :str, new_desc :str , service_category = Depends(Service_Category)):
    return service_category.update_category(id, new_name ,new_desc)

@router_category.delete("/delete/{id}")
def delete_category(id : str ,service_category = Depends(Service_Category)):
    return service_category.delete_category(id)