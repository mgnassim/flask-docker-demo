# test_app.py
import pytest
from app import app, redis_client
from unittest.mock import patch, MagicMock

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Canario" in response.data

@patch("app.redis_client")
def test_about_with_cache(mock_redis, client):
    # Mock Redis response for cached data
    mock_redis.get.return_value = (
        '{"story": "Cached story", "values": ["Cached value 1", "Cached value 2"]}'
    )
    response = client.get('/about')
    assert response.status_code == 200
    assert b"Cached story" in response.data
    assert b"Cached value 1" in response.data
    assert b"Cached value 2" in response.data
    mock_redis.get.assert_called_with("about_page_data")

@patch("app.redis_client")
def test_about_without_cache(mock_redis, client):
    # Simulate cache miss
    mock_redis.get.return_value = None

    # Use mock for Redis setex to validate cache storage
    mock_redis.setex = MagicMock()

    response = client.get('/about')
    assert response.status_code == 200
    assert b"Canario was founded on the belief" in response.data
    mock_redis.setex.assert_called_once_with(
        "about_page_data",
        300,
        '{"story": "Canario was founded on the belief that websites should be as unique as the people they represent.", "values": ["Creativity: Every project is approached with fresh, innovative ideas.", "Reliability: Our websites are built to last, with no compromises.", "Customer Satisfaction: We are committed to meeting the needs of our clients and exceeding expectations."]}',
    )

@patch("app.redis_client")
def test_portfolio_with_cache(mock_redis, client):
    # Mock Redis response for cached data
    mock_redis.get.return_value = (
        '[{"title": "Cached Project", "description": "Cached Description", "img_url": "https://example.com/cached.jpg"}]'
    )
    response = client.get('/portfolio')
    assert response.status_code == 200
    assert b"Cached Project" in response.data
    assert b"Cached Description" in response.data
    mock_redis.get.assert_called_with("portfolio_page_data")

@patch("app.redis_client")
def test_portfolio_without_cache(mock_redis, client):
    # Simulate cache miss
    mock_redis.get.return_value = None

    # Use mock for Redis setex to validate cache storage
    mock_redis.setex = MagicMock()

    response = client.get('/portfolio')
    assert response.status_code == 200
    assert b"Custom website for a famous musician" in response.data
    mock_redis.setex.assert_called_once_with(
        "portfolio_page_data",
        300,
        '[{"title": "Project 1", "description": "Custom website for a famous musician.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"}, '
        '{"title": "Project 2", "description": "Website redesign for a luxury brand.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"}, '
        '{"title": "Project 3", "description": "Web app for a high-profile sports team.", "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-lacdSV_hfHAguoMmCKYJ9cyvVTJkyEP-ZQ&s"}]'
    )

def test_contact(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact Us" in response.data
