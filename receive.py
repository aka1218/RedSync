import requests

# Replace with your server's IP address and port
server_url = 'http://172.31.211.241:5000/get_file/hello.txt'

response = requests.get(server_url)

if response.status_code == 200:
    # Save the received file locally
    with open('received_file.txt', 'wb') as f:
        f.write(response.content)
    print("File received successfully.")
else:
    print(f"Failed to retrieve file. Status code: {response.status_code}")