from dataclasses import dataclass


@dataclass
class configuration:
    # Application options
    application_cwd: str = ""  # This gets changed on first start

    # Database confic options
    text_directory: str = "TextFiles"
    database_name: str = "userlogindata.db"
