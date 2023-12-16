from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'Bangaluru, india',
    'salary': '50,00,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Pune, india',
    'salary': '30,00,000'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Delhi, india',
    'salary': '15,00,000'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'Anand, india'
  },
  {
    'id': 5,
    'title': 'Backend Engineer',
    'location': 'Surat, india',
    'salary': '50,00,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='GAJERA')
print(__name__)

@app.route("/api/jobs")
def hello_gajera():
  return jsonify(JOBS)
print(__name__)
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
  print("I'm inside the if now !") 
