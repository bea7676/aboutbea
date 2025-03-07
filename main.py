from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route("/")
def home():
    return render_template("rawr.html")  # Renders the index.html file

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
