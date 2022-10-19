from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from components.core.config import DESCRIPTION, PROJECT_NAME, VERSION

app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]


def create_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME,
                          version=VERSION, description=DESCRIPTION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("start", create_start_app_handler())
    application.add_event_handler("end", create_stop_app_handler())
    return application

# @app.get("/")
# async def first_get():
#     example = '안녕하세애애애요'
#     return example


# @app.post("/")
# async def create_upload_files(files: List[UploadFile] = File(...)):
#     upload_directory = "./"
#     for file in files:
#         contents = await file.read()
#         file_path = os.path.join(upload_directory, file.filename)
#         print('++++++++++', contents)
#         with open(file_path, "wb") as fp:
#             fp.write(contents)

#         # image = cv2.imread(file_path)
#         # print('------------', image)
#         # return image
#     return '테스트'
