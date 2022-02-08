from flask import Flask, jsonify, url_for, request, redirect
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from oauthlib.oauth2 import WebApplicationClient
import json
import os
import sqlite3
import requests
from db import init_db_command
from user import User, History, Service, Payments, db
from datetime import datetime
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")
print(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET)
login_manager = LoginManager()
login_manager.init_app(app=app)
CORS(app)
mail = Mail(app)

USER = []




try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

client = WebApplicationClient(GOOGLE_CLIENT_ID)
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@app.route("/")
def index():
    print(current_user.id)
    if current_user.is_authenticated:
        return redirect('http://localhost:8080/Room')
    else:
        return '<a class="button" href="/login">Google Login</a>'


@app.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    print(request.base_url)
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    user = User(id_=unique_id, name=users_name, email=users_email, profile_pic=picture, balance=5000, date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 5000)

    login_user(user)


    return redirect('/')

@app.route('/user')
def initUser():
    print(current_user.id)
    response_object = {"status": "susses"}
    if current_user.is_authenticated:
        response_object['data_user'] = {
            'id': current_user.id,
            'register': current_user.date,
            'email': current_user.email,
            'balance': current_user.balance
        }
    return jsonify(response_object)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('http://localhost:8080')


@app.route('/history', methods=['GET'])
@login_required
def getHistory():
    response_object = {"status": "susses"}
    data = History.query.all()
    history = []
    for hist in data:
        history.append(
            {
                "id": hist.id,
                "date": hist.date,
                "service": hist.service,
                "price": hist.price,
                "balance": hist.balance
            }
        )
    response_object['data_history'] = history
    return jsonify(response_object)

@app.route('/payments', methods=['GET', 'POST'])
#@login_required
def getPayments():
    response_object = {"status": "susses"}
    if request.method == 'POST':
        post_data = request.get_json()

        USER[0]['balance'] = USER[0]["balance"]-post_data.get("price")

        #User.query.filter_by(id=USER[0]['id']).all().update({"balance": USER[0]['balance']})

        new_history = History(date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                              service=post_data.get("service"),
                              price=post_data.get("price"),
                              balance=USER[0]["balance"])######дописать
        db.session.add(new_history)
        db.session.commit()

        Payments.update(post_data)
        if Payments.get_pay(post_data) != None:
            new_payment = Payments(date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                                   service=post_data.get('service'),
                                   price=post_data.get('price'),
                                   status='Оплачено')
            db.session.add(new_payment)
            db.session.commit()

    else:
        data = Payments.query.all()
        payments = []
        for pay in data:
            payments.append(
                {
                    "id": pay.id,
                    "data": pay.date,
                    "service": pay.service,
                    "price": pay.price,
                    "status": pay.status,
                }
            )
        response_object['data_payments'] = payments
    return jsonify(response_object)

@app.route('/services', methods=['GET', 'POST'])
#@login_required
def getServices():
    response_object = {"status": "susses"}
    if request.method == 'POST':
        post_data = request.get_json()
        #User.query.filter_by(id=USER[0]['id']).update({"balance": USER[0]['balance']})
        if post_data.get('status') == 'Отключена':
            USER[0]['balance'] = USER[0]["balance"] - post_data.get("price")
            new_history = History(date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                                  service=post_data.get("service"),
                                  price=post_data.get("price"),
                                  balance=USER[0]["balance"])
            db.session.add(new_history)



            new_payment = Payments(date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                                   service=post_data.get('service'),
                                   price=post_data.get('price'),
                                   status="Оплачено")
            db.session.add(new_payment)
            db.session.commit()

            Service.query.filter_by(id=USER[0]['id']).update({"status": "Подключена"})
        else:
            Service.query.filter_by(id=USER[0]['id']).update({"status": "Отключена"})
    else:
        Service.query.all()
        service = [{"id": serv.id, "service": serv.service, "price": serv.price, "status": serv.status} for serv in Service.query.all()]

        response_object['data_services'] = service

    return jsonify(response_object)

#дописать для send PDF
@app.route('/sendDetails', methods=['GET', 'POST'])
#@login_required
def sendEmail():
    response_object = {'status': 'susses'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)

        data = [{'date': hist.date, 'service': hist.service, 'price': hist.price, 'balance': hist.balance} for hist in History.query.all()]
        msg = Message(str(data), recipients=[post_data.get('email')])
        msg.body = "Example"
        mail.send(msg)
    return jsonify(response_object)

@app.route('/exit', methods=['GET'])
def exitUser():
    response_object = {"status": "susses"}
    USER.clear()
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(ssl_context="adhoc")
