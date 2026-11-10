from fastapi import Depends
from role.role_enum import TicketStatus
from dto.dto_ticket import dto_ticket_create
from repositories.repo_ticket import Repo_Ticket

class Service_Ticket :

    def __init__(self , repo  = Depends(Repo_Ticket)):
        self.repo = repo

    def create_ticket(self, data : dto_ticket_create , customer_id : str ):
        data_dict = data.model_dump()

        data_dict["status"] = TicketStatus.OPEN.value
        data_dict["customer_id"] = customer_id

        result =  self.repo.create_ticket_repo(data_dict)
        return {
            "message" : "ticket berhasil dibuat" ,
            "id" : str(result.inserted_id)
        }