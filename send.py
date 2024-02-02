import requests


# Replace with your server's IP address and port
server_url = 'http://172.31.211.241:5000/upload_file'

# Specify the file you want to send
file_to_send = 'test.txt'

# Prepare the file to be sent
files = {'file': open(file_to_send, 'rb')}

try:
    # Send the file to the server
    response = requests.post(server_url, files=files)

    # Check the response status code
    if response.status_code == 200:
        print(f"File '{file_to_send}' sent successfully.")
    else:
        print(f"Failed to send file. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")
