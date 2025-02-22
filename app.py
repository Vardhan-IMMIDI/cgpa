from flask import Flask, render_template, request

app = Flask(__name__)

# Grade Mapping
m = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 0}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            n = int(request.form["num_subjects"])
            grades = request.form.getlist("grades[]")
            credits = request.form.getlist("credits[]")

            s, c = 0, 0
            for i in range(n):
                ts = grades[i].upper()
                tc = float(credits[i])  # Convert credits to float
                s += m.get(ts, 0) * tc
                c += tc

            cgpa = round(s / c, 2) if c > 0 else 0
            return render_template("index.html", cgpa=cgpa)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
