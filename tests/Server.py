from flask import Flask, request, jsonify
import whisper
import requests

app = Flask(__name__)


model = whisper.load_model("base")


api_key = "SG_6854e6dc1f9115e2"
url = "https://api.segmind.com/v1/face-to-sticker" 


def summarize_with_segmind(text):
    data = {
        "text": text   
    }

    headers = {'x-api-key': api_key}

   
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result.get('summary', 'No summary available')  
    else:
        return f"Error: {response.status_code}"

@app.route('/transcribe', methods=['POST'])
def transcribe():

    audio = request.files['audio']
    audio_path = "/tmp/audio.wav" 
    audio.save(audio_path)


    result = model.transcribe(audio_path)
    transcribed_text = result['text']
    

    summary = summarize_with_segmind(transcribed_text)
    

    return jsonify({
        "text": transcribed_text,
        "summary": summary
    })

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)