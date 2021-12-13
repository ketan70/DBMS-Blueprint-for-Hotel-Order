from flask import Flask ,render_template ,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)



class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True) 
    Name = db.Column(db.String(100),nullable=False)
    PNo= db.Column(db.Integer,nullable=False)
    Mobile_No= db.Column(db.Integer,nullable=False)
    email_ID= db.Column(db.String(200),nullable=False)
    room = db.Column(db.String(200),nullable=False) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

 
    def __repr__(self):
        return f"{self.sno} - {self.Name}"



class emp(db.Model):
    no = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100),nullable=False)
    mobile_no= db.Column(db.Integer,nullable=False)
    email_id= db.Column(db.String(200),nullable=False)
    Type= db.Column(db.String(200),nullable=False)
    drc = db.Column(db.String(200),nullable=False) 
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.no} - {self.name}"



@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/form",methods=["GET","POST"])
def hello_form():
    if request.method == "POST":
        name = request.form['name']
        people = request.form['ppl']
        Phone_number = request.form['pno']
        Email_address = request.form['em']
        select = request.form.get('comp_select')
        admin = Todo(Name=name, email_ID=Email_address,PNo=people,Mobile_No=Phone_number,room=select)
        db.session.add(admin)
        db.session.commit()

    return render_template('form.html')


@app.route("/show")
def hello_show():
    Alldata = Todo.query.all()
    return render_template('show.html', Alldata=Alldata)



@app.route('/delete/<int:sno>')
def hello_update(sno):
    d = Todo.query.filter_by(sno=sno).first()
    db.session.delete(d)
    db.session.commit()
    return redirect("/update")


@app.route("/update")
def hello_up():
    Alldata = Todo.query.all()
    return render_template('update.html',Alldata=Alldata)

@app.route("/update_form/<int:sno>",methods=["GET","POST"])
def hello_form_up(sno):
    if request.method == "POST":
        p = Todo.query.filter_by(sno=sno).first()
        db.session.delete(p)
        db.session.commit()
        name = request.form['name']
        people = request.form['ppl']
        Phone_number = request.form['pno']
        Email_address = request.form['em']
        select = request.form.get('comp_select')
        admin = Todo(Name=name, email_ID=Email_address,PNo=people,Mobile_No=Phone_number,room=select)
        db.session.add(admin)
        db.session.commit()


    d = Todo.query.filter_by(sno=sno).first()
    return render_template('update_form.html',d=d)

@app.route("/employee_form",methods=["GET","POST"])
def hello_Ef():
    if request.method == "POST":
        name = request.form['na']
        Phone = request.form['ph']
        Email = request.form['e']
        type = request.form.get('comp')
        dec = request.form['dec']
        admin = emp(name=name, mobile_no=Phone, email_id=Email, Type=type, drc=dec)
        db.session.add(admin)
        db.session.commit()
    return render_template('employee.html')


if __name__=="__main__":
    app.run(debug=True, port=8000)

