# app.py
from flask import Flask, render_template, request, redirect, url_for
from zk_proofs import generate_proof, verify_proof

app = Flask(__name__)

# Simulate storage for encrypted votes
votes = {
    'candidate_1': [],
    'candidate_2': []
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        candidate = request.form.get("candidate")
        if candidate in votes:
            encrypted_vote = generate_proof(candidate)
            votes[candidate].append(encrypted_vote)
        return redirect(url_for("results"))
    return render_template("index.html")

@app.route("/results")
def results():
    candidate_1_votes = sum(1 for v in votes['candidate_1'] if verify_proof(v) == 'candidate_1')
    candidate_2_votes = sum(1 for v in votes['candidate_2'] if verify_proof(v) == 'candidate_2')
    return render_template("results.html", candidate_1_votes=candidate_1_votes, candidate_2_votes=candidate_2_votes)

if __name__ == "__main__":
    app.run(debug=True)
