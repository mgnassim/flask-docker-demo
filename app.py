from flask import Flask, render_template, jsonify
import redis
import json

app = Flask(__name__, static_folder='templates/static')

# Initialize Redis connection
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

def cache_data(key, data, ttl=300):
    """Cache data in Redis with a Time-To-Live (TTL)."""
    redis_client.setex(key, ttl, json.dumps(data))

def get_cached_data(key):
    """Retrieve cached data from Redis."""
    cached_data = redis_client.get(key)
    return json.loads(cached_data) if cached_data else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    cache_key = "about_page_data"
    cached_data = get_cached_data(cache_key)
    
    if cached_data:
        about_info = cached_data
    else:
        about_info = {
            "story": "Canario was founded on the belief that websites should be as unique as the people they represent.",
            "values": [
                "Creativity: Every project is approached with fresh, innovative ideas.",
                "Reliability: Our websites are built to last, with no compromises.",
                "Customer Satisfaction: We are committed to meeting the needs of our clients and exceeding expectations."
            ]
        }
        cache_data(cache_key, about_info, ttl=300)
    
    return render_template('about.html', about_info=about_info)

@app.route('/portfolio')
def portfolio():
    cache_key = "portfolio_page_data"
    cached_data = get_cached_data(cache_key)
    
    if cached_data:
        projects = cached_data
    else:
        projects = [
            {"title": "Project 1", "description": "Custom website for a famous musician.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"},
            {"title": "Project 2", "description": "Website redesign for a luxury brand.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"},
            {"title": "Project 3", "description": "Web app for a high-profile sports team.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"}
        ]
        cache_data(cache_key, projects, ttl=300)
    
    return render_template('portfolio.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
