import requests
import response 
import argparse
OAuth = 'AQAAAAAudcyyAAgGh2GQf9VpU0cPoump_hoWhcI'
YandexDownloadUrl = "https://cloud-api.yandex.net/v1/disk/resources/upload"
headers = {'Accept' : 'application/json', 'Authorization' : OAuth}
# file_path = './studentID.jpg'
Content_type = "image/jpeg"
# filename = "studentID.jpg"

def GetDownloadUrl(download_path, headers) -> str:
    request = requests.get(YandexDownloadUrl, headers=headers, params={'path' : download_path})
    if request.status_code != 200 :
        print("something goes wrong : " + str(request.status_code))
        return ""
    return request.json()['href']
def PutFile(url, headers, file_path) :
    request = requests.put(url, data=open(file_path, 'rb'), headers=headers)
    if request.status_code != 201 and request.status_code != 202 :
        print("something goes wrong : " + str(request.status_code))
        return False
    return True
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="%(prog)s [-u] FILE...",
        description="Download your file to your YandexDisk."
    )
    # For now we let user download only one file at the time
    parser.add_argument('-upload', '--upload', '-u', type=str, nargs=1)
    file_path = parser.parse_args().upload[0]
    filename = file_path[file_path.rfind('/') + 1 :]
    headers_send = {'Content-type' : Content_type, 'Slug' : filename}
    download_url = GetDownloadUrl("/test/Student1ID.jpeg", headers)
    if download_url == "" :
        exit()
    PutFile(download_url, headers_send, file_path)