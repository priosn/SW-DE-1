import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or \
                                        "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Connection(db.Model):
    __tablename__ = "connections"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Page not found Error 404</h1>"


@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>Internal Server Error 500</h1>"


@app.route("/")
def index():
    connection = Connection()
    db.session.add(connection)
    db.session.commit()
    return "<h1>Welcome Seddi!</h1>"


# Question 1
# Implement a GET method to show all the connections stored in the database
@app.route("/getdata", methods=['GET'])
def getdata():
    try:
        query = Connection.query.all()
        data = []
        if query:
            for row in query:
                data.append(
                    {
                        'id': row.id,
                        'date': row.created_date}
                )
            return jsonify({'connections': data}), 200
        # If database is empty
        return jsonify({'Error': "No data found"}), 200
    # If there is an error
    except Exception as e:
        return jsonify({'Error': "No database found"}), 404


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True)
