
from flask import Flask, render_template,request,jsonify 
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

@app.route('/') 
def home(): 
    return "Welcome to KaamNoKing AI Backend!"

@app.route('/generate-image', 
           methods=['POST']) 
def generate_image(): 
    prompt = request.json.get('prompt') 
    return jsonify({"image_url": f"Generated image from prompt: {prompt}"})

@app.route('/generate-caption', 
           methods=['POST']) 
def generate_caption(): 
    topic = request.json.get('topic') 
    return jsonify({"caption": f"This is a powerful caption about {topic}"})

@app.route('/generate-meme',
            methods=['POST']) 
def generate_meme(): 
    idea = request.json.get('idea') 
    return jsonify({"meme": f"Funny meme on: {idea}"})

@app.route('/gujarati-text',
            methods=['POST']) 
def gujarati_text(): 
    idea = request.json.get('idea') 
    return jsonify({"gujarati": f"Gujarati content on: {idea}"})

@app.route('/resume', 
           methods=['POST']) 
def resume(): 
    name = request.json.get('name')
    return jsonify({"resume": f"Generated resume for {name}"})

@app.route('/code',
            methods=['POST']) 
def code(): 
    language = request.json.get('language') 
    task = request.json.get('task') 
    return jsonify({"code": f"Generated {language} code to {task}"})

@app.route('/logo', 
           methods=['POST']) 
def logo(): 
    brand = request.json.get('brand') 
    return jsonify({"logo_url": f"AI-generated logo for {brand}"})

@app.route('/tts', 
           methods=['POST']) 
def tts(): 
    text = request.json.get('text') 
    return jsonify({"audio_url": f"Audio from text: {text}"})

@app.route('/translate',
            methods=['POST']) 
def translate(): 
    text = request.json.get('text') 
    language = request.json.get('language')
    return jsonify({"translated": f"Translated '{text}' into {language}"})

@app.route('/chat',
            methods=['POST']) 
def chat(): 
    message = request.json.get('message')
    return jsonify({"reply": f"AI says: {message}"})

@app.route('/blog',
            methods=['POST']) 
def blog(): 
    topic = request.json.get('topic') 
    return jsonify({"blog": f"SEO blog on: {topic}"})

@app.route('/ad-copy',
            methods=['POST'])
def ad_copy(): 
    product = request.json.get('product')
    return jsonify({"ad": f"Buy {product} now! Limited offer!"})

if __name__ == '__main__': app.run(debug=True)