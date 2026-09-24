import requests

class ClientError(Exception):
    pass

class ServerError(Exception):
    pass

TARGET_URL = "https://jsonplaceholder.typicode.com/posts"
#TARGET_URL = "https://jsonplaceholder.typicode.com/invalid-route"

try:
    response = requests.get(TARGET_URL)
    print("Status Code:",response.status_code)

    status_class = response.status_code // 100

    if status_class == 2:
        print("Status:","Success")
        payload = response.json()

        first_post = payload[0]
        title = first_post.get("title", "Default Token").strip()

        print("Title:", title)
        print("Title Length:", len(title))

    elif status_class == 4:
        print("Status:","Client Error")
        raise ClientError("Client error received")
    
    elif status_class == 5:
        print("Status:","Server Error")
        raise ServerError("Server error received")
    
    else:
        print("Status:","Other Status")

except ClientError as error:
    print("Exception:",error)

except ServerError as error:
    print("Exception:",error)

except requests.exceptions.RequestException:
    print("Request failed")