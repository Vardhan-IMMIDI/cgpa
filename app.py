from flask import Flask, render_template, request

app = Flask(__name__)

# Grade Mapping (O and S both are 10)
m = {'O': 10, 'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 0}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            n = int(request.form["num_subjects"])
            grades = request.form.getlist("grades[]")
            credits = request.form.getlist("credits[]")

            s, c = 0, 0
            for i in range(n):
                ts = grades[i].upper().strip()  # Convert to uppercase & remove spaces
                tc = float(credits[i])

                if ts not in m:
                    return render_template("index.html", error=f"Invalid grade '{ts}' entered. Please enter O, S, A, B, C, D, E, or F.")

                s += m[ts] * tc
                c += tc

            cgpa = round(s / c, 2) if c > 0 else 0
            return render_template("index.html", cgpa=cgpa)

        except ValueError:
            return render_template("index.html", error="Please enter valid numbers for credits.")
        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
