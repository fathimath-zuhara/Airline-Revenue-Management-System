from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

# Ticket rates
ECONOMY_RATE = 5
BUSINESS_RATE = 8
FIRST_RATE = 12


# PASSWORD VALIDATION
def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r"[A-Za-z]", password):
        return False, "Password must contain at least one letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, ""


# REVENUE CALCULATION
def calculate_revenue(economy, business, first, distance, aircraft):
    total_passengers = economy + business + first

    economy_revenue = economy * distance * ECONOMY_RATE
    business_revenue = business * distance * BUSINESS_RATE
    first_revenue = first * distance * FIRST_RATE

    base_revenue = economy_revenue + business_revenue + first_revenue
    final_revenue = base_revenue

    if total_passengers > 300:
        final_revenue += base_revenue * 0.10

    if distance > 5000:
        final_revenue -= base_revenue * 0.05

    if aircraft == "A380" and total_passengers > 250:
        final_revenue += 100000

    return {
        "economy_revenue": economy_revenue,
        "business_revenue": business_revenue,
        "first_revenue": first_revenue,
        "base_revenue": base_revenue,
        "final_revenue": final_revenue
    }

@app.route("/logout")
def logout():
    return redirect("/")


# LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "Admin" and password == "Admin@123":
            return redirect("/index")
        else:
            return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        employee_id = request.form["employee_id"]
        department = request.form["department"]
        role = request.form["role"]
        password = request.form["password"]

        # Company email validation
        if not email.endswith("admin@aeroplan.com"):
            return render_template("register.html",
                                   error="Only admin@aeroplan.com emails allowed.")

        # Password validation
        valid, message = is_valid_password(password)
        if not valid:
            return render_template("register.html", error=message)

        return render_template("login.html",
                               error="Registration successful. Contact admin for activation.")

    return render_template("register.html")


# INDEX
@app.route("/index")
def index():
    return render_template("index.html")


# CALCULATE
@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        economy = int(request.form["economy"])
        business = int(request.form["business"])
        first = int(request.form["first"])
        distance = int(request.form["distance"])
        aircraft = request.form["aircraft"]

        if economy < 0 or business < 0 or first < 0:
            return render_template("index.html",
                                   error="Passenger numbers must be positive.")

        if distance <= 0:
            return render_template("index.html",
                                   error="Distance must be greater than 0.")

        result = calculate_revenue(economy, business, first, distance, aircraft)

        return render_template("result.html", result=result)

    except:
        return render_template("index.html",
                               error="Invalid input values.")


if __name__ == "__main__":
    app.run(debug=True)