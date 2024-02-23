import csv
import psycopg2

from src.config import DB_HOST, DB_NAME, DB_USER, DB_PASS


def get_data_from_csv_question(questions):
    data = []
    with open(questions, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row['id'], row['question_text'], row['survey_id']))
    return data


def get_data_from_csv_survay(surveys):
    data = []
    with open(surveys, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row['id'], row['name_survey'], row['type_of_establishment']))
    return data


def connect_to_database():
    conn = psycopg2.connect(
        host=f"{DB_HOST}",
        database=f"{DB_NAME}",
        user=f"{DB_USER}",
        password=f"{DB_PASS}"
    )
    return conn


def insert_data(conn, questions, survey):
    cur = conn.cursor()
    for sur in survey:
        cur.execute("INSERT INTO survey (id, name_survey, type_of_establishment) VALUES (%s, %s, %s)", sur)
    for question in questions:
        cur.execute("INSERT INTO question (id, question_text, survey_id) VALUES (%s, %s, %s)", question)
    conn.commit()




data_survey = get_data_from_csv_survay("Survey_2024-02-22_03-55-23.csv")
data_question = get_data_from_csv_question("Question_2024-02-22_17-04-57.csv")

conn = connect_to_database()

insert_data(conn, data_question, data_survey)
conn.close()
