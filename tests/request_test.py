import requests


url = "http://143.47.241.141:5000/transcribe" 


with open('C:/Users/yossi/OneDrive/Desktop/face/file.mp3', 'rb') as file:
    files = {'audio': file}
    response = requests.post(url, files=files)


if response.status_code == 200:
    result = response.json()
    print("Transcribed Text:", result.get('text', 'No text found'))
    print("Analysis:", result.get('analysis', 'No analysis found'))
else:
    print(f"Error: {response.status_code}")
