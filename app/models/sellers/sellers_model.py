from dataclasses import dataclass
from http import HTTPStatus
from apiflask import HTTPError


class SellersModel:
    def __init__(self, connection) -> None:
        self.conn = connection
        self.create_table()
    
    def create_table(self) -> None:
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS sellers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name VARCHAR(150),
                    last_name VARCHAR(150),
                    company_name VARCHAR(255),
                    document VARCHAR(18)
                )
                """
            )
    
    def new_seller(self, first_name: str, last_name: str, company_name: str, document: str) -> None:
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO sellers (first_name, last_name, company_name, document)
                VALUES (%s, %s, %s, %s)
                """, (first_name, last_name, company_name, document)
            )
