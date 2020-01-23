from src.entities.Enterprise import Enterprise
from src.repo.EnterpriseRepo import EnterpriseRepo

class EnterpriseService:

    def __init__(self):
        self.repo = EnterpriseRepo()

    def create(self, name):
        self.repo.create_enterprise(name)

    def find_by_name(self, name):
        try:
            return self.repo.find_by_name(name)
        except:
            return None

    def edit(self, name, new_name):
        enterprise = self.find_by_name(name)
        if(enterprise == None):
            return False
        else:
            enterprise.name = new_name
            self.repo.edit(enterprise)
            return True

    def find_all(self):
        return self.repo.find_all()