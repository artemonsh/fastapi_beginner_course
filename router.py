from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post(
        "/",
        description="Добавляет таску в базу данных, а еще ....",
        summary="Добавляет таску в базу данных",
        response_description="Вот такой ответ придет",
)
async def add_task(task: STaskAdd = Depends()) -> STaskId:
    new_task_id = await TaskRepository.add_task(task)
    return {"id": new_task_id}


@router.get("/")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks
