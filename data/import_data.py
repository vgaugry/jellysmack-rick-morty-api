import os
import sqlite3
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def create_tables(db_connection):
    create_table_character = """CREATE TABLE characters(
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                status TEXT NOT NULL,
                                species TEXT NOT NULL,
                                type TEXT,
                                gender TEXT NOT NULL);
                                """

    create_table_episode = """CREATE TABLE episodes(
                                id INTEGER PRIMARY KEY ,
                                name TEXT NOT NULL,
                                air_date TEXT NOT NULL,
                                episode TEXT NOT NULL);
                                """

    create_table_assoc = """CREATE TABLE assoc_characters_episodes(
                                id INTEGER PRIMARY KEY,
                                character_id int NOT NULL,
                                episode_id TEXT NOT NULL,
                                FOREIGN KEY (character_id) REFERENCES characters(id),
                                FOREIGN KEY (episode_id) REFERENCES episodes(id))
                                """

    cursor = db_connection.cursor()
    cursor.execute(create_table_character)
    cursor.execute(create_table_episode)
    cursor.execute(create_table_assoc)


def create_characters_data(db_connection, file_name):
    with open(os.path.join(__location__, file_name)) as characters_file:
        characters_dict = json.load(characters_file)

    query = """INSERT INTO characters (id, name, status, species, type, gender) VALUES 
            (?, ?, ?, ?, ?, ?)"""
    cursor = db_connection.cursor()
    for character in characters_dict:
        cursor.execute(query, (character["id"], character["name"], character["status"], character["species"],
                               character["type"], character["gender"]))

    db_connection.commit()


def create_episodes_data(db_connection, file_name):
    with open(os.path.join(__location__, file_name)) as episodes_file:
        episodes_dict = json.load(episodes_file)
    query = """INSERT INTO episodes (id, name, air_date, episode) VALUES 
                    (?, ?, ?, ?)"""
    cursor = db_connection.cursor()
    for episode in episodes_dict:
        cursor.execute(query, (episode["id"], episode["name"], episode["air_date"], episode["episode"]))

        db_connection.commit()


def create_assoc_data(db_connection, file_name):
    with open(os.path.join(__location__, file_name)) as characters_file:
        characters_dict = json.load(characters_file)
    assoc_dict = {}
    for character in characters_dict:
        assoc_dict[character["id"]] = character["episode"]

    query = "INSERT INTO assoc_characters_episodes (character_id, episode_id) VALUES (?, ?)"
    cursor = db_connection.cursor()

    for character_id, episodes in assoc_dict.items():
        for episode in episodes:
            cursor.execute(query, (character_id, episode))

    db_connection.commit()


if __name__ == "__main__":
    db_name = "rick-morty-api.db"
    character_file_name = "rick_morty-characters_v1.json"
    episodes_file_name = "rick_morty-episodes_v1.json"

    file_path = os.path.abspath(db_name)
    connection = sqlite3.connect(file_path)

    create_tables(connection)
    create_characters_data(connection, character_file_name)
    create_episodes_data(connection, episodes_file_name)
    create_assoc_data(connection, character_file_name)

    connection.close()


