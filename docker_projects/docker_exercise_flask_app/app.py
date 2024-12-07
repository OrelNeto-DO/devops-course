from flask import Flask, render_template
from sqlalchemy import create_engine, text
import os
import random


app = Flask(__name__)


DB_USER = "root"
DB_PASSWORD = "rootpassword"
DB_HOST = "mysql"
DB_PORT = "3306"
DB_NAME = "mydatabase"


DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URL)


@app.route("/")
def index():

    with engine.connect() as connection: 
        result = connection.execute(text("SELECT image_url from images"))
        images = [row["image_url"] for row in result]



    url = random.choice(images) 
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port =int(os.environ.get("PORT", 5000)))

