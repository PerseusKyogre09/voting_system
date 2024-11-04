from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import Config
from zk_proofs import generate_proof, verify_proof

app = Flask(__name__)
app.config.from_object(Config)

votes = {
    "candidate_1": [],
    "candidate_2": []
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        candidate = request.form['candidate']
        if candidate not in votes:
            flash("Invalid candidate")
            return redirect(url_for('index'))

        # Generate proof for vote
        vote_proof = generate_proof(candidate)
        votes[candidate].append(vote_proof)
        flash("Vote cast successfully!")
        return redirect(url_for('results'))
    return render_template('index.html')

@app.route('/results')
def results():
    candidate_1_votes = sum(1 for v in votes['candidate_1'] if verify_proof(v) == 'candidate_1')
    candidate_2_votes = sum(1 for v in votes['candidate_2'] if verify_proof(v) == 'candidate_2')
    results = {
        'candidate_1': candidate_1_votes,
        'candidate_2': candidate_2_votes
    }
    return render_template('result.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
