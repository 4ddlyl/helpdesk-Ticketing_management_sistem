from fastapi import Depends, HTTPException
from dto.dto_rating_feedback import dto_rating_feedback
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

    def find_ticket_by_aggent(self, aggent_id : str):
        result = self.repo.find_by_agent_id(aggent_id)
        if not result:
            raise HTTPException(404, "not found")
        return result

    def update_status_ticket(self ,ticket_id : str, agent_id : str , new_status : TicketStatus):
        check = self.repo.find_ticket_by_id(ticket_id)
        if check.status == TicketStatus.RESOLVED or check.status == TicketStatus.CLOSED:
            raise HTTPException(400 , "impossible to edit , it has been resolved/closed")
        result = self.repo.upadate_status_ticket(ticket_id,agent_id , new_status)
        if result is None :
            raise HTTPException(404 , "not found")
        status_lama = result.status.value
        return {
            "message" : f"berhasil update dari {status_lama} to {new_status.value}"
        }

    def resolve_ticket_by_agent(self , ticket_id : str, agent_id :str):
        check = self.repo.resolve_ticket_by_agent_repo(ticket_id)
        if check is None:
            raise HTTPException(404 , "not found")
        if check.agent_id != agent_id:
            raise HTTPException(403, "ain't your dutty")
        if check.status == TicketStatus.CLOSED or check == TicketStatus.RESOLVED :
            raise HTTPException(400, "closed , impossible to edit")
        return {
            "message" : "tiket berhasil diselesaikan"
        }

    def rating_and_feedback(self , ticket_id : str , data : dto_rating_feedback , customer_id : str):
        check = self.repo.find_ticket_by_id(ticket_id)
        if check is None:
            raise HTTPException(404 ,"Not found")
        if check.status != TicketStatus.RESOLVED:
            raise HTTPException(400 , "impossible to edit")
        if check.customer_id != customer_id:
            raise HTTPException(403 , "not yours")
        result = self.repo.rating_and_feedback_repo(ticket_id, data.rating , data.ulasan)
        return {
            "message" : "success"
        }

    def get_dashboard(self) :
        total = self.repo.count_total_ticket()
        by_status = self.repo.get_stats_by_status()
        by_priority = self.repo.get_stats_by_priority()
        by_agent = self.repo.get_stats_by_agent()
        unassigned_agent = self.repo.ticket_unsassigned_agent()
        daily_tickets_trend = self.repo.get_daily_tickets_trend()

        status_dict = {}
        for i in by_status :
            key = i["_id"]
            value = i["total"]
            status_dict[key] = value

        priority_dict = {}
        for i in by_priority:
            key = i["_id"]
            value = i["total"]
            priority_dict[key] = value

        dates = []
        totals = []
        for i in daily_tickets_trend:
            dates.append(i["_id"])
            totals.append(i["total"])
        dates.reverse()
        totals.reverse()    
            

        return {
            "total tickets" : total,
            "tickets by status" : status_dict,
            "tickets by priority" : priority_dict,
            "agent performance" : by_agent,
            "unassigned agent" : unassigned_agent,
            "daily ticket trend" : {
                "tanggal" : dates,
                "total" : totals
            }
        }         