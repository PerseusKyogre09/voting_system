# Private Voting System with Zero-Knowledge Proof (ZKP)
This is a secure, private voting web application built with Flask that leverages Zero-Knowledge Proofs (ZKP) to protect user identities and vote data. The application ensures that user votes remain anonymous and that only the final results are revealed.

## Project Overview
The Private Voting System enables registered users to log in, securely cast votes for candidates, and view the voting results. The system uses Zero-Knowledge Proofs (ZKP) to verify identities and securely encrypt votes, ensuring privacy and data security throughout the voting process. The voting page design mimics a government interface, adding a professional and authoritative look to the system.

### Features
- User Authentication with ZKP: Users log in with their personal information, which is encrypted and stored using Zero-Knowledge Proof techniques.
- Anonymous Voting: Vote data is encrypted to maintain user anonymity.
- Results Page: Only final results are visible to authorized users, preserving individual vote privacy.
- Responsive Design: The interface is styled to be professional and easy to navigate, with visual cues for candidates.

## Screenshots
- Login Page: Users enter their first name, last name, and email to log in securely.
- Voting Page: Users select their preferred candidate and cast their vote.
- Thank You Page: Confirms the vote has been cast with a link to the results page.
- Results Page: Displays the final vote tally for each candidate without revealing individual votes.

## Installation and Setup
### Prerequisites
- Python 3.x
- Flask
- Dependencies: Listed in `requirements.txt`

### Steps to Set Up Locally
1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```
2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the Application
```bash
flask run
```
5. Access the Application
 - Open your web browser and navigate to `http://127.0.0.1:5000` to start the voting process.

## Usage
1. Login: Start at the login page, where you enter your name and email. Your identity is verified and encrypted with ZKP.
2. Cast a Vote: Select a candidate and submit your vote, which is stored securely.
3. View Results: After voting, access the final tally on the results page.

## Technology Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Security: RSA Encryption, Zero-Knowledge Proofs (ZKP)

## License
This project is licensed under terms defined in the `LICENSE` file. Please check the file for further details.

