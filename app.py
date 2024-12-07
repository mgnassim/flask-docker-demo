from flask import Flask, render_template

app = Flask(__name__)

# Dynamic home route
@app.route('/')
def home():
    return render_template('index.html', title="Canario - Home", intro_text="Transforming Ideas into Digital Art")

# Dynamic about page route
@app.route('/about')
def about():
    return render_template('about.html', title="Canario - About", story="Our Story", values=["Creativity", "Reliability", "Customer Satisfaction"])

# Dynamic contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html', title="Canario - Contact", contact_message="If you're interested in working with Canario, we'd love to hear from you!")

# Dynamic portfolio page route
@app.route('/portfolio')
def portfolio():
    projects = [
        {"name": "Project 1", "description": "Custom website for a famous musician.", "image": "https://via.placeholder.com/300x200"},
        {"name": "Project 2", "description": "Website redesign for a luxury brand.", "image": "https://via.placeholder.com/300x200"},
        {"name": "Project 3", "description": "Web app for a high-profile sports team.", "image": "https://via.placeholder.com/300x200"}
    ]
    return render_template('portfolio.html', title="Canario - Portfolio", projects=projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
