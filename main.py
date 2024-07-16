from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key for Google Generative AI
genai.configure(api_key='AIzaSyCaJrDBIXDRQlQismh6jeZ5vGlRNyzSaGQ')

# Initialize the generative model
model = genai.GenerativeModel(model_name="gemini-pro")


# Function to convert text into a poetic expression
def make_poetry(text):
    response = model.generate_content(
        f"Please change this into a poetic expression: {text}. Please print it out as a poetic expression of the same language as the language in {text}. If {text} is one sentence, print about one sentence. Don't try to write down the title of the poem, If {text} is Korean, print it out in Korean, If {text} is English, it must be printed in English."
    )
    return response.text


# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    poetry = ""
    if request.method == 'POST':
        text = request.form['text']
        poetry = make_poetry(text)
    return render_template('index.html', poetry=poetry)


if __name__ == '__main__':
    app.run(debug=True)
