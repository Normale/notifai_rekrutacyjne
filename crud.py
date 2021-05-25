import models
import schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import load_only


async def read_message(db: AsyncSession, message_nr: int):
    result = (await db.execute(select(models.Message).where(models.Message.nr == message_nr))).fetchone()
    if result is None:
        return None
    return result["Message"]


async def create_message(db: AsyncSession, message_text: str):
    db_item = models.Message(text=message_text)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def update_message(db: AsyncSession, message_nr: int, new_text: str):
    db_item = await read_message(db, message_nr)
    if db_item is None:
        return None
    db_item.text = new_text
    db_item.views = 0
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def increment_views(db: AsyncSession, message_nr: int):
    db_item = await read_message(db, message_nr)
    if db_item is None:
        return None
    db_item.views += 1
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def _read_message_nr(db: AsyncSession, message_nr: int):
    result = (await db.execute(select(models.Message).where(
        models.Message.nr == message_nr)
        .options(load_only('nr')))).fetchone()
    if result is None:
        return None
    return result["Message"]


async def delete_message(db: AsyncSession, message_nr: int):
    """
        Returns True if successfully deleted, False otherwise.
    """
    # use read_only id
    db_item = await _read_message_nr(db, message_nr)
    if db_item is None:
        return False
    await db.delete(db_item)
    await db.commit()
    return True
