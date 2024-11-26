# השתמש בתמונה של Python כבסיס
FROM python:3.8-slim

# הגדר את תיקיית העבודה בקונטיינר
WORKDIR /app

# העתק את קובץ requirements.txt לתוך הקונטיינר
COPY requirements.txt .

# התקן את התלויות (Flask ומודולים נוספים)
RUN pip install --no-cache-dir -r requirements.txt

# העתק את כל קבצי הפרויקט לתוך הקונטיינר
COPY . .

# הצג את הפורט שבו יאזין Flask (פורט 5000)
EXPOSE 5000

# הפעל את אפליקציית Flask
CMD ["python", "app.py"]
