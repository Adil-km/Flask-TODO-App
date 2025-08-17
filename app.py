from datetime import datetime
from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}"

@app.before_first_request
def create_tables():
    db.create_all()

# Routes
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        content = request.form['content']
        try:
            task = Task(task=content)
            db.session.add(task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error: {e}"
    else:
        contents = Task.query.order_by(Task.created_at.desc()).all()
        return render_template("index.html", contents=contents)

@app.route("/delete/<int:id>")
def delete(id):
    task = db.get_or_404(Task, id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    task = db.get_or_404(Task, id)
    if request.method == "POST":
        task.task = request.form['content']
        db.session.commit()
        return redirect("/")
    else:
        return render_template('edit.html', content=task)

if __name__ == "__main__":
    app.run()