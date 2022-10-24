import os
from xmlrpc.client import boolean
import cv2
import logging
import time

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

# class Stop_test(BaseModel):


@router.post(
    "/dir_SR",
    summary="폴더 전체 복사 후 SR",
    status_code=201,
)
async def create_upload_files(
    image_folder: image_folder,
):
    # 클라이언트에서 보낸 폴더 파일 경로
    image_folder_path = image_folder.path
    # 원본파일 경로
    folder_path = f"/components/original/{image_folder_path.split('/')[-1]}"
    # sr파일 경로
    sr_folder_path = folder_path.replace('original', 'sr')+"_SR"

    # sr, original 폴더 생성 & original 이미지 파일 복사
    files = file_cp(image_folder_path, folder_path, sr_folder_path)

    if len(files) != 0:
        for file in files:

            # 클라이언트에서 보낸 폴더 파일 경로 + 파일 경로 안에 있는 파일이름
            file_path = f"{image_folder_path}/{file}"

            # 파일이름 뒤에 + _SR
            output_file_name = file.split('.')[0] + "_SR"
            # 이미지 파일 읽기
            image = cv2.imread(file_path)

            trtis_server = ModelInferencer("localhost:8002")
            output_data = trtis_server.infer(image)

            print('output---->', output_data)

            # 이미지 파일 저장
            # cv2.imwrite(
            #     f"{sr_folder_path}/{output_file_name}.{file.split('.')[-1]}",output_data)

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


@router.get(
    "/testart",
    summary="시작 테스트",
    status_code=201,
)
async def test_start():
    #
    #     time.sleep(1)
    #     print("wake up!", i)
    # global isStop
    for i in range(0, 20):
        print(isOpen)
        if isOpen != "False":
            time.sleep(1)
            print("wake up!", i)
        else:
            print("wake down!", i)

    return {'test1': isOpen}


@router.post(
    "/testop",
    summary="정지 테스트",
    status_code=201,
)
async def test_stop(isStop=True):
    # print(isStop)
    global isOpen
    isOpen = isStop
    print(type(isOpen))
    # testAAA = isStop
    # a = isStop

    return {'test1': isStop}
