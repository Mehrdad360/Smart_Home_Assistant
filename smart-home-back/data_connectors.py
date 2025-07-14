# data_connectors.py

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")

if not OPENWEATHER_API_KEY:
    print("Warning: OPENWEATHER_API_KEY not found in .env. Weather functions may not work.")
if not NEWSAPI_API_KEY:
    print("Warning: NEWSAPI_API_KEY not found in .env. News functions may not work.")


def get_current_weather(location: str) -> str:
    if not OPENWEATHER_API_KEY:
        return "Weather service is not configured. Please set OPENWEATHER_API_KEY in .env."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric" 
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        data = response.json()

        if data.get("cod") != 200:
            return f"Could not retrieve weather for {location}: {data.get('message', 'Unknown error')}"

        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return (
            f"The weather in {location} is currently {weather_description}, "
            f"with a temperature of {temperature}°C (feels like {feels_like}°C). "
            f"Humidity is {humidity}% and wind speed is {wind_speed} m/s."
        )
    except requests.exceptions.RequestException as e:
        return f"Error connecting to weather service: {e}"
    except Exception as e:
        return f"An unexpected error occurred while getting weather: {e}"


def get_latest_news(query: str = "general", language: str = "en") -> str:
    if not NEWSAPI_API_KEY:
        return "News service is not configured. Please set NEWSAPI_API_KEY in .env."

    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": language,
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_API_KEY,
        "pageSize": 3 
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        data = response.json()

        articles = data.get("articles", [])
        if not articles:
            return f"No news found for '{query}' in {language}."

        news_summary = [f"Latest news about '{query}' in {language}:"]
        for i, article in enumerate(articles):
            title = article.get("title", "No title")
            source = article.get("source", {}).get("name", "Unknown source")
            description = article.get("description", "No description available")
            url = article.get("url", "#")
            news_summary.append(f"{i + 1}. {title} (Source: {source}) - {description} Read more: {url}")

        return "\n".join(news_summary)
    except requests.exceptions.RequestException as e:
        return f"Error connecting to news service: {e}"
    except Exception as e:
        return f"An unexpected error occurred while getting news: {e}"


def get_current_date_time() -> str:
    """
    Returns the current date and time.
    """
    now = datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"The current date and time is {formatted_date_time}."
