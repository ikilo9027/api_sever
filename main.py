import fastapi.openapi.utils as fu

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from components.file import api as file_api
from components.core.config import DESCRIPTION, PROJECT_NAME, VERSION
from components.core.events import create_start_app_handler, create_stop_app_handler


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
    application.add_event_handler("startup", create_start_app_handler())
    application.add_event_handler("shutdown", create_stop_app_handler())
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(file_api.router)
    return application


app = create_application()

fu.validation_error_response_definition = {
    "title": "HTTPValidationError",
    "type": "object",
    "properties": {
        "error": {"title": "Message", "type": "string"},
    },
}


@app.head(
    "/api/v1/alive",
    tags=["common"],
    summary="health check",
    responses={204: {"description": "Alive Server"}},
    status_code=204,
)
def server_check():
    """
    check server alive
    """
    data = {"ping": "pong"}

    return JSONResponse(content=jsonable_encoder(data), status_code=204)
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
