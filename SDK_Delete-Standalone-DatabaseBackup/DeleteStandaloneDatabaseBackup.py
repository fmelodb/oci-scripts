import oci
import datetime as dt
from datetime import timezone

compartmentOCID = "ocid1.compartment.oc1..aaaaaaaaic2ic...[example]"

MONTH_RET_DAYS = 31
YEAR_RET_DAYS  = 365
FIVE_YEAR_RET_DAYS = (YEAR_RET_DAYS*5)

client = oci.database.DatabaseClient(oci.config.from_file())
listBackups = client.list_backups(compartment_id=compartmentOCID)

today = dt.datetime.now(timezone.utc)

for i in listBackups.data:
    days = abs((today - i.time_started).days)

    if 'MONTH' in i.display_name and days > MONTH_RET_DAYS:
        print('deleting ' + i.display-name + ' after ' + str(days) + ' days')
        delete_backup_response = client.delete_backup(backup_id = i.id)
    
    if 'YEAR' in i.display_name and days > YEAR_RET_DAYS:
        print('deleting ' + i.display-name + ' after ' + str(days) + ' days')
        delete_backup_response = client.delete_backup(backup_id = i.id)
        
    if 'FIVE_YEAR' in i.display_name and days > FIVE_YEAR_RET_DAYS:
        print('deleting ' + i.display-name + ' after ' + str(days) + ' days')
        delete_backup_response = client.delete_backup(backup_id = i.id)
