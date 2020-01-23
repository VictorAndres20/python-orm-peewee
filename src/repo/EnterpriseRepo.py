from src.entities.Enterprise import Enterprise

class EnterpriseRepo:

    def create_enterprise(self, name):
        return Enterprise.create(name=name)

    def find_by_name(self, name):
        return Enterprise.get(name=name)

    def edit(self, enterprise):
        enterprise.save()
    
    def find_all(self):
        return Enterprise.select().order_by(Enterprise.name.desc())