from starlette.config import Config

config = Config(".env")

VERSION: str = "1.0"
PROJECT_NAME: str = config("PROJECT_NAME", default="LGU_ESP_PROJECT API")
DESCRIPTION: str = config(
    "DESCRIPTION", default="---espresomedia lgu+ project---")
