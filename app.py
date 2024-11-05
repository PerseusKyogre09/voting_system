# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from zk_proofs import generate_proof, verify_proof

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Simulated encrypted data storage
user_data = {}
votes = {
    "candidate_1": [],
    "candidate_2": []
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")

        # Generate ZKP for identity and store in user_data
        encrypted_identity = generate_proof(f"{first_name} {last_name} {email}")
        user_data[email] = encrypted_identity

        # Store email in session for access control
        session['user_email'] = email
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/vote", methods=["GET", "POST"])
def index():
    if "user_email" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        candidate = request.form.get("candidate")
        if candidate in votes:
            encrypted_vote = generate_proof(candidate)
            votes[candidate].append(encrypted_vote)
        return redirect(url_for("thank_you"))  # Redirect to thank_you page after voting
    return render_template("index.html")

@app.route("/thank_you")
def thank_you():
    if "user_email" not in session:
        return redirect(url_for("login"))
    return render_template("thank_you.html")

@app.route("/results")
def results():
    if "user_email" not in session:
        return redirect(url_for("login"))

    candidate_1_votes = sum(1 for v in votes['candidate_1'] if verify_proof(v) == 'candidate_1')
    candidate_2_votes = sum(1 for v in votes['candidate_2'] if verify_proof(v) == 'candidate_2')
    return render_template("results.html", candidate_1_votes=candidate_1_votes, candidate_2_votes=candidate_2_votes)

@app.route("/logout")
def logout():
    session.pop("user_email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
