from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=True)
    create=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self)->str:
        return f"{self.sno} - {self.title}"
    def __init__(self,sno,title,desc):
        
        self.sno = sno
        self.title = title
        self.desc = desc
        

@app.route("/")
def hello_world():
    todo=Todo(title="first Todo",desc="Start investing in stock market")
    db.session(todo)
    db.commit()
    return render_template('index.html')

@app.route("/product")
def prouct():
    return "<p>This is product , World!</p>"

with app.app_context():
    db.create_all()

if __name__ =="main":
    app.run(debug=True)