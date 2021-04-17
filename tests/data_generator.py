from faker import Faker
import pymongo
import json
import shortuuid
import random
import calendar

# Connection to mongo database ('reviews') and to its collections ('question', 'session' and 'system')
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["reviews"]
question = database["question"]
session = database["session"]
system = database["system"]

# This method creates mock user data; flag is used to determine if profile is to be added to the data
def user_data(flag):
    # Faker is a Python package that generates fake data; in this instance it will generate random portuguese names
    fake = Faker("pt_PT")
    random_users = []

    for _ in range(10):
        if flag:
            # Profile can be either student ('st') or professor ('pr')
            profiles = ["st", "pr"]
            user = (fake.name(), random.choice(profiles))
            random_users.append(user)
        else:
            random_users.append(fake.name())

    return random_users


# This method create mock data for the domain of a question or session
def domain_data():
    random_domains = []

    domain1 = {"domain": "Database Systems", "subdomain": "SQL", "subsubdomain": ""}

    domain2 = {
        "domain": "Database Systems",
        "subdomain": "SQL",
        "subsubdomain": "Queries",
    }

    domain3 = {
        "domain": "Artificial Intelligence",
        "subdomain": "Machine Learning",
        "subsubdomain": "Decision Trees",
    }

    domain4 = {
        "domain": "Natural Language Processing",
        "subdomain": "Stemming",
        "subsubdomain": "",
    }

    random_domains.extend((domain1, domain2, domain3, domain4))
    return random_domains


# This method generates random question reviews
def qr_generator(entries):
    question_reviews = []
    fake = Faker()
    users = user_data(False)
    domains = domain_data()

    for _ in range(entries):
        question_review = {}
        question_review["_id"] = shortuuid.uuid()
        question_review["user"] = random.choice(users)

        date = fake.date_time_between(start_date="-2y", end_date="now")
        question_review["date"] = {}
        question_review["date"]["date"] = date.strftime("%Y-%m-%d:%H:%M.%S")
        question_review["date"]["weekday"] = calendar.day_name[date.weekday()]
        question_review["date"]["month"] = calendar.month_name[date.month]
        question_review["date"]["year"] = date.year

        domain = random.choice(domains)
        question_review["question"] = {}
        question_review["question"]["id_question"] = shortuuid.uuid()
        question_review["question"]["language"] = random.choice(["UK", "PT"])
        question_review["question"]["difficulty_level"] = random.randint(1, 5)
        question_review["question"]["domain"] = domain["domain"]
        question_review["question"]["study_cycle"] = "University Course"
        question_review["question"]["scholarity"] = "Informatics Engineering"
        question_review["question"]["subdomain"] = domain["subdomain"]
        question_review["question"]["sub_subdomain"] = domain["subsubdomain"]

        question_review["difficulty"] = random.randint(1, 5)
        question_review["time"] = random.randint(1, 5)
        question_review["clarity"] = random.randint(1, 5)
        question_review["content"] = random.randint(1, 5)
        question_review["knowledge"] = random.randint(1, 5)
        question_review["interactivity"] = random.randint(1, 5)
        question_review["comment_rating"] = random.randint(1, 5)

        question_reviews.append(question_review)

    return question_reviews


# This method generates random session reviews
def ser_generator(entries):
    session_reviews = []
    fake = Faker()
    users = user_data(False)
    domains = domain_data()

    for _ in range(entries):
        session_review = {}
        session_review["_id"] = shortuuid.uuid()
        session_review["user"] = random.choice(users)

        date = fake.date_time_between(start_date="-2y", end_date="now")
        session_review["date"] = {}
        session_review["date"]["date"] = date.strftime("%Y-%m-%d:%H:%M.%S")
        session_review["date"]["weekday"] = calendar.day_name[date.weekday()]
        session_review["date"]["month"] = calendar.month_name[date.month]
        session_review["date"]["year"] = date.year

        domain = random.choice(domains)
        session_review["question"] = {}
        session_review["question"]["id_question"] = shortuuid.uuid()
        session_review["question"]["language"] = random.choice(["UK", "PT"])
        session_review["question"]["difficulty_level"] = random.randint(1, 5)
        session_review["question"]["domain"] = domain["domain"]
        session_review["question"]["study_cycle"] = "University Course"
        session_review["question"]["scholarity"] = "Informatics Engineering"
        session_review["question"]["subdomain"] = domain["subdomain"]
        session_review["question"]["sub_subdomain"] = domain["subsubdomain"]

        session_review["sequence"] = random.randint(1, 5)
        session_review["time"] = random.randint(1, 5)
        session_review["variability"] = random.randint(1, 5)
        session_review["difficulty"] = random.randint(1, 5)
        session_review["sophistication"] = random.randint(1, 5)
        session_review["evaluative"] = random.randint(1, 5)
        session_review["knowledge"] = random.randint(1, 5)
        session_review["interactivity"] = random.randint(1, 5)
        session_review["comment_rating"] = random.randint(1, 5)

        session_reviews.append(session_review)

    return session_reviews


# This method generates random system reviews
def syr_generator(entries):
    system_reviews = []
    fake = Faker()
    users = user_data(True)

    for _ in range(entries):
        system_review = {}
        system_review["_id"] = shortuuid.uuid()

        user = random.choice(users)
        system_review["user"] = {}
        system_review["user"]["user"] = user[0]
        system_review["user"]["profile"] = user[1]

        date = fake.date_time_between(start_date="-2y", end_date="now")
        system_review["date"] = {}
        system_review["date"]["date"] = date.strftime("%Y-%m-%d:%H:%M.%S")
        system_review["date"]["weekday"] = calendar.day_name[date.weekday()]
        system_review["date"]["month"] = calendar.month_name[date.month]
        system_review["date"]["year"] = date.year

        system_review["interface"] = random.randint(1, 5)
        system_review["interactivity"] = random.randint(1, 5)
        system_review["gamification"] = random.randint(1, 5)
        system_review["infovis"] = random.randint(1, 5)
        system_review["dialogues"] = random.randint(1, 5)
        system_review["facility"] = random.randint(1, 5)
        system_review["performance"] = random.randint(1, 5)
        system_review["accessibility"] = random.randint(1, 5)
        system_review["availability"] = random.randint(1, 5)
        system_review["help"] = random.randint(1, 5)
        system_review["comment_rating"] = random.randint(1, 5)

        system_reviews.append(system_review)

    return system_reviews


entries = input("How many data entries do you wish to generate: ")

question_reviews = qr_generator(int(entries))
question.insert_many(question_reviews)

session_reviews = ser_generator(int(entries))
session.insert_many(session_reviews)

system_reviews = syr_generator(int(entries))
system.insert_many(system_reviews)
