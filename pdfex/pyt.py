from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from flask import Flask,render_template
import os
import shutil

packet = io.BytesIO()

app = Flask(__name__)



@app.route("/")



def hello():
    cwd = os.getcwd()
    input_path = cwd+"/PDF/"
    input_files = [f for f in os.listdir(input_path) if f.endswith('.pdf')]
    destination_path = cwd +"/OUT/"
    destination_files = [f for f in os.listdir(destination_path) if f.endswith('.pdf')]
    

    
    

    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(100, 100, "Hello world")
    
    can.save()
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open("test.pdf", "rb"))
    x= existing_pdf.getNumPages()
        
    
    

    return render_template("home.html",x=x)

    
    

    


if __name__ == "__main__":
    app.run(debug=1)
    


