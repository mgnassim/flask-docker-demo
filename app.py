from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the app with a service account key
cred = credentials.Certificate('path-to-your-service-account-key.json')  # Ensure this path is correct
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

app = Flask(__name__, static_folder='templates/static')

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Store data in Firestore
        doc_ref = db.collection('contacts').add({
            'name': name,
            'email': email,
            'message': message
        })

        return redirect('/')
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    projects = [
        {"title": "Project 1", "description": "Custom website for a famous musician.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"},
        {"title": "Project 2", "description": "Website redesign for a luxury brand.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"},
        {"title": "Project 3", "description": "Web app for a high-profile sports team.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"}
    ]
    return render_template('portfolio.html', projects=projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
