from fastapi import Depends
from dto.dto_faq import create_dto_faq
from repositories.repo_faq import Repo_Faq

class Service_Faq :
    def __init__(self, repo = Depends(Repo_Faq)):
        self.repo = repo

    def create_faq_service(self, new_faq : create_dto_faq):
        new_faq_dict = new_faq.model_dump()
        result = self.repo.create_faq(new_faq_dict)
        return {
            "message" : "berhasil di buat",
            "id" : str(result.inserted_id)
        }

    def get_all_faqs_service(self):
        return self.repo.get_all_faqs()    