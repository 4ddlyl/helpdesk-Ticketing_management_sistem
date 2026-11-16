from datetime import datetime, timezone

from fastapi import Depends, HTTPException

from repositories.repo_ticket import Repo_Ticket
from dto.messages import dto_message_create,dto_message_response
from repositories.repo_message_ticket import Repo_Message_Ticket


class Service_Message_ticket :
    def __init__(self , repo = Depends(Repo_Message_Ticket) , repo_ticket = Depends(Repo_Ticket)):
        self.repo = repo
        self.repo_ticket = repo_ticket

    def kirim_message(self , data : dto_message_create, ticket_id : str):
        validation = self.repo_ticket.find_ticket_by_id(ticket_id)
        if validation is None:
            raise HTTPException(404, "not found")

        data_dict = data.dict()                 
        result = self.repo.kirim_message(data_dict)
        return {
            "messsage" : f"{result} berhasil dikirim"
        }    