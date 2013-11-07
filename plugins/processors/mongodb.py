from pymongo import MongoClient
from datetime import datetime
import time

client = MongoClient()
# getting database "log_db"
db = client.log_db
# getting collection "log_items"
log_items = db.log_items

def process_nginx(log_item):
    # get the timestamp from log_item and removes the timezone
    timestamp = log_item["timestamp"].split(" ")[0]
    # convert the timestamp to a python datetime instance
    log_time = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")
    # exchange the timestamp for the datetime instance
    log_item["timestamp"] = log_time
    # insert into the collection
    log_items.insert(log_item)