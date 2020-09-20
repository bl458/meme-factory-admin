import os
from dotenv import load_dotenv, find_dotenv
from memeData import login_admin


if __name__ == "__main__":
    # Load from .env
    load_dotenv(find_dotenv())
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
    ADMIN_PW = os.getenv('ADMIN_PW')

    print(login_admin(ADMIN_EMAIL, ADMIN_PW))
