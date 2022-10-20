import os
import cv2
import logging

from pydantic import BaseModel

from fastapi import APIRouter, FastAPI, File, status

from fastapi.responses import JSONResponse

from components.utils.file import file_cp
from components.triton.inference import ModelInferencer
# from inference.infer import ModelInferencer

# from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


log = logging.getLogger("uvicorn")
router = APIRouter(prefix="/esp/api/v1", tags=["SR"])


class image_folder(BaseModel):
    path: str


@router.post(
    "/dir_SR",
    summary="폴더 전체 복사 후 SR",
    status_code=201,
)
async def create_upload_files(
    image_folder: image_folder,
):
    image_folder_path = image_folder.path
    folder_path = f"/components/original/{image_folder_path.split('/')[-1]}"
    sr_folder_path = folder_path.replace('original', 'sr')+"_SR"

    files = file_cp(image_folder_path, folder_path, sr_folder_path)

    if len(files) != 0:
        for file in files:
            file_path = f"{image_folder_path}/{file}"

            output_file_name = file.split('.')[0] + "_SR"
            image = cv2.imread(file_path)

            trtis_server = ModelInferencer("localhost:8001")

    return {'test1': folder_path, "test2": sr_folder_path, "test3": files}
# response = {
#     "status_code": 201,
#     "message": "폴더 내 SR이 완료 되었습니다.",
#     "detail": "Success"
# }

# return JSONResponse(
#     response,
#     status_code=status.HTTP_201_CREATED
# )
# @router.post(
#     "/dir_sr",
#     summary="폴더 SR",
#     status_code=201
# )
# def create_upload_files(
#     image_folder: image_folder,
# ):
#     image_folder = image_folder.path

#     return 'test AA'
