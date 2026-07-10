from flask import Flask, request, jsonify
import cv2
import numpy as np
import mediapipe as mp

app = Flask(__name__)

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)

@app.route('/scan', methods=['POST'])
def scan_palm():
    # Frontend se aayi photo ko receive karna
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # AI Logic (Yahan hum lakirein detect karenge)
    # Filhal ke liye hum ek dummy result bhej rahe hain
    result = {
        "heart_line": "Aapka emotional nature bohot stable hai.",
        "head_line": "Aap bohot logical insaan hain."
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
  
