from fastapi import APIRouter, Depends, HTTPException
from schemas import MessageCreate, Message, json_detailed_responses
import crud
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from dependency import has_access


router = APIRouter()


@router.post("/", response_model=Message, responses=json_detailed_responses([403]))
async def create_message(message: MessageCreate,  db: AsyncSession = Depends(get_db), auth=Depends(has_access),):
    """
    Create message (string with length 1(min) to 160(max)).\n
    Requires authentication (Throws 403 if token is incorrect)
    """
    db_message = await crud.create_message(db, message.text)
    return db_message


@router.put("/{message_nr}", response_model=Message, responses=json_detailed_responses([403, 404]))
async def edit_message(message_nr: int, message: MessageCreate, db: AsyncSession = Depends(get_db), auth=Depends(has_access)):
    """
    Edit message with id `message_nr`. Message length should be in range [1,160]\n
    Requires authentication (Throws 403 if token is incorrect)\n
    If message is not found, returns 404.
    """
    db_message = await crud.update_message(db, message_nr, message.text)
    if db_message is None:
        raise HTTPException(
            status_code=404, detail=f"Message with id {message_nr} not found")
    return db_message


@router.delete("/{message_nr}", responses=json_detailed_responses([200, 403, 404]))
async def delete_message(message_nr: int, db: AsyncSession = Depends(get_db), auth=Depends(has_access)):
    """
        Delete a message with id `message_nr`\n
        Requires authentication (Throws 403 if token is incorrect)\n
        If message is not found, returns 404.
    """
    deleted = await crud.delete_message(db, message_nr)
    if not deleted:
        raise HTTPException(
            status_code=404, detail=f"Message with id {message_nr} not found")
    return {"detail": "Message successfully deleted"}


@router.get("/{message_nr}", response_model=Message, responses=json_detailed_responses([404]))
async def view_message(message_nr: int, db: AsyncSession = Depends(get_db)):
    """
        Read a message with id `message_nr`.\n
        If message is not found, returns 404.
    """
    db_message = await crud.increment_views(db, message_nr)
    if db_message is None:
        raise HTTPException(
            status_code=404, detail=f"Message with id {message_nr} not found")
    return db_message
