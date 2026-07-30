from sqlmodel import Session, create_engine

import models

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/app_db"

engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session