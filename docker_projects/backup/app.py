from flask import Flask, render_template
from sqlalchemy import create_engine, text
import os
import random
from dotenv import load_dotenv

# טוען את משתני הסביבה מתוך קובץ .env
load_dotenv()

app = Flask(__name__)

# קריאת משתני הסביבה
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "mysql")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "mydatabase")

# כתובת חיבור ל-MySQL
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URL)


@app.route("/")
def index():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT image_url FROM images"))
        images = [row["image_url"] for row in result]

    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))