from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/add_notification', methods=['POST'])
def add_notification():
    data = request.json
    new_notification = Notification(
        customer_name=data.get("customer_name"),
        product=data.get("product"),
        location=data.get("location")
    )
    db.session.add(new_notification)
    db.session.commit()
    return jsonify({"message": "Notification added successfully!"}), 201

@app.route('/get_notifications', methods=['GET'])
def get_notifications():
    notifications = Notification.query.order_by(Notification.timestamp.desc()).limit(5).all()
    return jsonify([
        {"customer_name": n.customer_name, "product": n.product, "location": n.location, "timestamp": n.timestamp} 
        for n in notifications
    ])

if __name__ == '__main__':
    app.run(debug=True)
