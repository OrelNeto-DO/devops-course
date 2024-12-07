#what base layer image to use:
FROM python:3.8 

#path to our wordkir app + wordkir definition:
WORKDIR /usr/src/app 

#copy all the files to the workdir in the container:
COPY . .

#install dependencies:
RUN pip install --no-cache-dir -r requirements.txt

#what port to expose (the port that the container listen to):
EXPOSE 5000

#run the application with command:
CMD ["python", "./app.py"]
