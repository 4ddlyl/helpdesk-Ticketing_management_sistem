from fastapi import Depends, HTTPException
from repositories.repo_category import Repo_Category
from role.role_enum import TicketStatus
from dto.tickets.dto_ticket import dto_ticket_create
from repositories.repo_ticket import Repo_Ticket

class Service_Ticket :

    def __init__(self , repo  = Depends(Repo_Ticket) , repo_category = Depends(Repo_Category)):
        self.repo = repo 
        self.repo_category = repo_category   

    def create_ticket(self, data : dto_ticket_create , customer_id : str ):
        check = self.repo_category.find_by_id_Category(data.category_id)
        if check is None:
            raise HTTPException(400 , "not valid")
         
        data_dict = data.model_dump()

        data_dict["status"] = TicketStatus.OPEN.value
        data_dict["customer_id"] = customer_id
        

        result =  self.repo.create_ticket_repo(data_dict)
        return {
            "message" : "ticket berhasil dibuat" ,
            "id" : str(result.inserted_id)
        }