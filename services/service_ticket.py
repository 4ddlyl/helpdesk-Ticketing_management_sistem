from fastapi import Depends, HTTPException
from repositories.repo_category import Repo_Category
from role.role_enum import TicketStatus
from dto.tickets.dto_ticket import dto_ticket_create
from dto.tickets.dto_ticket_response import dto_ticket_response
from repositories.repo_ticket import Repo_Ticket
from datetime import datetime, timezone

class Service_Ticket :

    def __init__(self , repo  = Depends(Repo_Ticket) , repo_category = Depends(Repo_Category)):
        self.repo = repo 
        self.repo_category = repo_category   

    def create_ticket(self, data : dto_ticket_create , customer_id : str ):
        check = self.repo_category.find_by_id_Category(data.category_id)
        if check is None:
            raise HTTPException(400 , "not valid")
         
        data_dict = data.model_dump()

        #count tiket hari ini
        count_today = self.repo.count_tickets_today()
        #create no urut
        urutan  = str(count_today + 1).zfill(4)
        #ambil tgl hari ini
        tanggal = datetime.now(timezone.utc).strftime("%Y%m%d")
        #gabungin
        data_dict["ticket_number"] = f"TKT--{tanggal}--{urutan}"
        data_dict["created_at"] = datetime.now(timezone.utc)  
        data_dict["status"] = TicketStatus.OPEN.value
        data_dict["customer_id"] = customer_id
        data_dict["agent_id"] = None
        

        result =  self.repo.create_ticket_repo(data_dict)
        return {
            "message" : "ticket berhasil dibuat" ,
            "id" : str(result.inserted_id)
        }

    def get_all_ticket(self) :
        result =  self.repo.get_all_tickets()
        if result is None:
            raise HTTPException(404, "not found")

        return {
            "result" : result
        }

    def get_my_tickets(self , customer_id : str):
        result = self.repo.get_id_tickets(customer_id)
        if not result:
            raise HTTPException(404, "not found")

        return result


