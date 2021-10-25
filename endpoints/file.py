import os
import uuid
from datetime import datetime

from fastapi.param_functions import File


def get_by_folder_name() -> str:
    name = datetime.now().strftime("%Y%m%d")
    if not os.path.exists(f"upload_data/{name}"):
        os.mkdir(f"upload_data/{name}")
    return name


async def create_file(file: File) -> str:
    file.filename = f"{uuid.uuid4()}.jpg"
    path = f"upload_data/{get_by_folder_name()}/{file.filename}"
    contents = await file.read()
    with open(path, "wb") as f:
        f.write(contents)
    return file.filename


def delete_file(frame: object):
    folder = "".join((str(frame.created_at).split(" "))[0].split("-"))
    cur_dir = os.path.join(os.getcwd(), f"upload_data/{folder}/")

    while True:
        file_list = os.listdir(cur_dir)
        if frame.name in file_list:
            os.remove(os.path.join(cur_dir, frame.name))
            break
    if not len(os.listdir(cur_dir)):
        os.rmdir(cur_dir)
