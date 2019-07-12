from flask import Flask, render_template







from pdf2image import convert_from_path, convert_from_bytes



import os



from PIL import Image



import pytesseract



import mysql.connector



import pymysql



app = Flask(__name__)



@app.route("/")



def hello():
	f=open("text.txt","r")
	content = f.readlines()
	return render_template("home1.html",f=content)

if __name__ == "__main__":



       app.run(debug=1)



