from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/laws")
def laws():
    return render_template("laws.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/download/tax-form")
def download_tax_form():
    return render_template("tax_form.html")


@app.route("/download/passport-form")
def download_passport_form():
    return render_template("passport_form.html")


@app.route("/download/id-form")
def download_id_form():
    return render_template("id_form.html")


@app.route("/download/police-form")
def download_police_form():
    return render_template("police_report_form.html")


@app.route("/download/military-form")
def download_military_form():
    return render_template("military_form.html")


@app.route("/download/citizenship-form")
def download_citizenship_form():
    return render_template("citizenship_form.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
