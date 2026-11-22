from typing import List
from datetime import datetime, timezone
from fastapi import Depends
from pydantic import TypeAdapter
from pymongo.synchronous.database import Database
from role.role_enum import TicketStatus
from models.model_common import PyObjectId
from models.model_ticket import Model_Ticket
from config.database import get_db

class Repo_Ticket :

    def __init__(self , db : Database = Depends(get_db)):
        self.collection = db.get_collection("tickets")

    def count_tickets_today(self):
        today_start = datetime.now(timezone.utc).replace(hour=0 , minute=0, second=0, microsecond=0)

        #hitung berapa dokumen dibuat setelah jamm 00:00 pada hari ini    
        return self.collection.count_documents({"created_at" : {"$gte" : today_start}})

    def create_ticket_repo(self , data : dict) :
        return self.collection.insert_one(data) 

    def find_ticket_by_id(self , ticket_id : str):
        result = self.collection.find_one({"_id" : PyObjectId(ticket_id)})
        if result is not None:
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Ticket).validate_python(result)

    def get_all_tickets(self) :
        result = self.collection.find({})
        cursor = []
        for i in result :
            if "_id" in i :
                i["_id"] = str(i["_id"])
            cursor.append(i)
        return TypeAdapter(List[Model_Ticket]).validate_python(cursor) 

    def get_id_tickets(self , customer_id : str):
        result = self.collection.find({"customer_id" : customer_id})
        wrapper = []
        for i in result:
            if "_id" in i :
                i["_id"] = str(i["_id"])
            wrapper.append(i)    
        return TypeAdapter(List[Model_Ticket]).validate_python(wrapper)

    def find_by_agent_id(self , aggent_id : str):
        result = self.collection.find({"agent_id" : aggent_id})
        wrapper = []
        for i in result:
            if "_id" in i:
                i["_id"] = str(i["_id"])
            wrapper.append(i)
        return TypeAdapter(List[Model_Ticket]).validate_python(wrapper)

    def upadate_status_ticket(self ,ticket_id : str, agent_id : str , new_status : TicketStatus):
        result = self.collection.find_one_and_update({"_id" : PyObjectId(ticket_id) ,"agent_id" : agent_id} , {"$set" : {"status" : new_status}})
        if result is not None :
            if "_id" in result:
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Ticket).validate_python(result)

    def resolve_ticket_by_agent_repo(self, ticket_id : str):
        result = self.collection.find_one_and_update({"_id" : PyObjectId(ticket_id)} , {"$set" : {"status" : TicketStatus.RESOLVED.value}})
        if result is not None:
            if "_id" in result:
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Ticket).validate_python(result)

    def rating_and_feedback_repo(self ,ticket_id : str, rating : int , ulasan_new : str):
        result = self.collection.find_one_and_update({"_id" : PyObjectId(ticket_id)} , {"$set" : {"rating_feedback" : rating , "ulasan" : ulasan_new , "status" : TicketStatus.CLOSED.value}} , return_document=True)
        if result is not None :
            if "_id" in result :
                result["_id"] = str(result["_id"])
            return TypeAdapter(Model_Ticket).validate_python(result)

    def count_total_ticket(self):
        return self.collection.count_documents({})

    def get_stats_by_status(self):
        pipeline = [
            {
                "$group" : {"_id" : "$status", "total" : {"$sum" : 1}}
            },
            {
                "$sort" : {"_id" : 1}
            }
        ]
        return list(self.collection.aggregate(pipeline))

    def get_stats_by_priority(self):
        pipeline = [
            {
                "$group" : {"_id" : "$priority" , "total" : {"$sum" : 1}}
            }
        ]
        return list(self.collection.aggregate(pipeline))

    def get_stats_by_agent(self):
        pipeline = [
            {
                #get ticket who has aggent_id
                "$match" : {"agent_id" : {"$ne" : None}}
            },
            {
                #grouping by agent_id then count
                "$group" : {"_id" : "$agent_id" , "total_tickets" : {"$sum" : 1}}
            }
        ]
        return list(self.collection.aggregate(pipeline))

    def ticket_unsassigned_agent(self):
        return self.collection.count_documents({"agent_id" : None})

    def get_daily_tickets_trend(self):
        pipeline = [
            {
                "$group" : {"_id" : {"$dateToString" :  {"format" : "%Y-%m-%d" , "date" : "$created_at"}},
                "total" : {"$sum" : 1},
            }},
            {"$sort" : {"_id" : 1}},
            {"$limit" : 7},
        ]
        return list(self.collection.aggregate(pipeline))        