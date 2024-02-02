from flask import Flask, send_file, request
import os

app = Flask(__name__)

curr_file_directory = '.'
upload_directory = './uploads'

@app.route('/get_file/<filename>', methods=['GET'])
def get_file(filename):
    # Assuming the file is in the same directory as the script
    file_path = os.path.join(curr_file_directory, filename)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"File {filename} not found", 404
    
@app.route('/upload_file', methods=['POST'])
def upload_file():
    try:
        print("Checking...")
        if 'file' not in request.files:
            return "No file part", 404

        file = request.files['file']

        if file.filename == '':
            return "No selected file", 400

        # Print debug information
        print(f"Received file: {file.filename}")
        print(f"Saving file to: {os.path.join(upload_directory, file.filename)}")

        # Save the uploaded file
        file.save(os.path.join(upload_directory, file.filename))
        return f"File '{file.filename}' uploaded successfully"

    except Exception as e:
        return f"An error occurred: {e}"

    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

