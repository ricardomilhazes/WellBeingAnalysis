import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["reviews"]

question = database["question"]
question_df = pd.DataFrame(list(question.find()))
date_col = question_df.pop("date")
question_col = question_df.pop("question")
question_df = pd.concat(
    [question_df, date_col.apply(pd.Series), question_col.apply(pd.Series)], axis=1
)

session = database["session"]
session_df = pd.DataFrame(list(session.find()))
date_col = session_df.pop("date")
session_col = session_df.pop("question")  # change to session
session_df = pd.concat(
    [session_df, date_col.apply(pd.Series), session_col.apply(pd.Series)], axis=1
)

system = database["system"]
system_df = pd.DataFrame(list(system.find()))
date_col = system_df.pop("date")
user_col = system_df.pop("user")
system_df = pd.concat(
    [system_df, date_col.apply(pd.Series), user_col.apply(pd.Series)], axis=1
)


def get_domains(inquiry):
    if inquiry == "question":
        return question_df["domain"].unique().tolist()
    elif inquiry == "session":
        return session_df["domain"].unique().tolist()

    return print("The inquiry you selected does not exist")


def get_subdomains(inquiry):
    if inquiry == "question":
        return question_df["subdomain"].unique().tolist()
    elif inquiry == "session":
        return session_df["subdomain"].unique().tolist()

    return print("The inquiry you selected does not exist")


def get_dates(inquiry):
    if inquiry == "question":
        return question_df["date"].unique().tolist()
    elif inquiry == "session":
        return session_df["date"].unique().tolist()
    elif inquiry == "system":
        return system_df["date"].unique().tolist()

    return print("The inquiry you selected does not exist")


def get_users(inquiry):
    if inquiry == "question":
        return question_df["user"].unique().tolist()
    elif inquiry == "session":
        return session_df["user"].unique().tolist()
    elif inquiry == "system":
        return system_df["user"].unique().tolist()

    return print("The inquiry you selected does not exist")
