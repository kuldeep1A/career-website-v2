from flask import Flask, render_template, jsonify
from databases import  load_jobs_from_db
app = Flask(__name__)

@app.route("/")
def hello_k():
    jobs_list = load_jobs_from_db()
    return render_template("home.html", jobs=jobs_list)


@app.route("/api/jobs")
def list_jobs():
    jobs_list = load_jobs_from_db()
    return jsonify(jobs_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
