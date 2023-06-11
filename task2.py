from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        

        headers = {"Authorization":  "OAuth " + self.token}


        resources_upload = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                                        params = {"path": file_path},
                                        headers = headers
                                        )
        href = resources_upload.json()['href']


        with open(file_path, 'rb') as f:
            resp = requests.put(href, files={"file": f}, headers= headers)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "main.py"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
