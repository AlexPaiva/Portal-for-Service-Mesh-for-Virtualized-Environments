from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests

app = Flask(__name__, template_folder='templates', static_folder= 'static')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///factory_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    factory_id = db.Column(db.Integer, nullable=False)

class FactoryData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    factory_id = db.Column(db.Integer, nullable=False)
    material_in = db.Column(db.Integer, nullable=False)
    product_out = db.Column(db.Integer, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('index.html')

@app.route('/api/factory-data')
@login_required
def factory_data():
    factory_ids = [current_user.factory_id] if current_user.factory_id != 0 else [1, 2]
    data = []
    for factory_id in factory_ids:
        factory_service_name = f"factory{factory_id}-service.default.svc.cluster.local"
        try:
            response = requests.get(f"http://{factory_service_name}/api/data")
            if response.status_code == 200:
                factory_data = response.json()
                factory_data['factory_id'] = factory_id
                data.append(factory_data)
            else:
                raise Exception(f"Failed to fetch factory {factory_id} data.")
        except Exception as e:
            print(e)

    return jsonify(data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/login')
@login_required
def dashboard():
    idCurr = factory_id=current_user.factory_id
    if (str(idCurr) == "0"):
        factory_data = FactoryData.query.filter_by().all()
    else:
        factory_data = FactoryData.query.filter_by(factory_id=current_user.factory_id).all()
    return render_template('dashboard.html', factory_data=factory_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)