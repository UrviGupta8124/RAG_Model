from flask import Flask, render_template, request
from rag_pipeline import run_query  # your refactored function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        query = request.form.get("query")
        response = run_query(query)  # call your RAG query function
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
    