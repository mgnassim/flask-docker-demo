from flask import Flask, render_template
from google.cloud import firestore

app = Flask(__name__, static_folder='templates/static')

# Initialize Firestore DB
db = firestore.Client()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    about_info = {
        "story": "Canario was founded on the belief that websites should be as unique as the people they represent.",
        "values": [
            "Creativity: Every project is approached with fresh, innovative ideas.",
            "Reliability: Our websites are built to last, with no compromises.",
            "Customer Satisfaction: We are committed to meeting the needs of our clients and exceeding expectations."
        ]
    }
    return render_template('about.html', about_info=about_info)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    projects_ref = db.collection('projects')
    projects = [doc.to_dict() for doc in projects_ref.stream()]
    return render_template('portfolio.html', projects=projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)