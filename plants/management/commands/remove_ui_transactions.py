from django.core.management.base import BaseCommand, CommandError
from frontend.models import Actions, Transactions
from login.models import AuthUser

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("deleting UI transactions!!!")
# 1. Make a list of users whos data that we are deleting
        users = AuthUser.objects.filter(is_data_import = False)
# 2. Make of list of transaction IDs for the transactions made by the users whos data we want to delete
        for u in users:
            transactions = Transactions.objects.filter(users_id = u.id)    
# 3. For each transaction ID, we want to look up all of the actions asocciated with the transaction ID, and delete the transactions
            for t in transactions:
                Actions.objects.filter(transactions_id = t.id).delete()
                t.delete()