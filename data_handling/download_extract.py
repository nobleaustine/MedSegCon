
# required libraries
import zipfile
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

# function to download zip file
def download_zip(key_path,file_id):

    # setting up credentials and google drive API
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=['https://www.googleapis.com/auth/drive.readonly'])
    service = build('drive', 'v3', credentials=credentials)

    # downloading the file
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

    # saving the downloaded file as a zip file
    file_path = "../DATA/zip_files/c_1_5.zip"
    with open(file_path, 'wb') as f:
        f.write(fh.getvalue())
    return file_path

# function to extract zip
def extract_zip(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as file:
        file.extractall(extract_to)

if __name__ == "__main__":

    # google authentication credentials and file id
    key_path = 'credentials.json'
    file_id = '1XpgkYPnzieSvh3gogt5pYS_d0W2e1y3o'

    # downloading and returning file path
    zip_file_path = download_zip(key_path,file_id)
    
    
    # extraction from zip
    extract_directory = '../DATA/heart_1_5'
    try:
        extract_zip(zip_file_path, extract_directory)
        print(f"Contents of {zip_file_path} extracted to {extract_directory}")
    except Exception as e:
        print("Error: ",e)
        
    

    
