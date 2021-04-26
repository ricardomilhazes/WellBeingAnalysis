import pymongo
import pandas as pd
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["reviews"]

question_col = database["question"]
session_col = database["session"]
system_col = database["system"]
