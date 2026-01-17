from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # <-- mandatory for session to work

def ask_rag_bot(question):
    return f"This is a response to: {question}"  # dummy bot

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []  # initialize chat history

    if request.method == "POST":
        question = request.form.get("question")
        answer = ask_rag_bot(question)
        session["history"].append({"question": question, "answer": answer})
        session.modified = True  # tell Flask that session has changed

    return render_template("index.html", history=session["history"])
    
if __name__ == "__main__":
    app.run(debug=True)
