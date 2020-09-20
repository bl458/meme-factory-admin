from dotenv import load_dotenv, find_dotenv
from admin import login_admin, upload_files_admin
from os import listdir, getenv

# Check gitignore
IMG_DIR = '../assets'

if __name__ == "__main__":
    # Load from .env
    load_dotenv(find_dotenv())
    ADMIN_EMAIL = getenv('ADMIN_EMAIL')
    ADMIN_PW = getenv('ADMIN_PW')

    # Login as admin
    session_token = login_admin(ADMIN_EMAIL, ADMIN_PW)

    # Process files inside assets
    files = ['../assets/' + i for i in listdir('../assets')]

    # Upload files as admin
    upload_files_admin(files, session_token)
