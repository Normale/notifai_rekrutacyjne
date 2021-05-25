from sqlalchemy.orm import Session
import models
import schemas


def read_message(db: Session, message_nr: int):
    return db.query(models.Message).filter(models.Message.nr == message_nr).first()


def create_message(db: Session, message_text: str):
    db_item = models.Message(text=message_text)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_message(db: Session, message_nr: int, new_text: str):
    db_item = read_message(db, message_nr)
    db_item.text = new_text
    db_item.views = 0
    db.commit()
    db.refresh(db_item)
    return db_item


def increment_views(db: Session, message_nr: int):
    # use read_only views later
    db_item = read_message(db, message_nr)
    if db_item is None:
        return None
    db_item.views += 1
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_message(db: Session, message_nr: int):
    """
        Returns True if successfully deleted, False otherwise.
    """
    # use read_only id
    db_item = read_message(db, message_nr)
    if db_item is None:
        return False
    db.delete(db_item)
    db.commit()
    return True
