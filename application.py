# flask , pandas, scikit-learn , pickle-mixin
import pandas as pd
from flask import Flask,render_template

app = Flask(__name__)
car = pd.read_csv("cleaned car data.csv")

@app.route("/")
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()
    return render_template("index.html", companies = companies, car_models = car_models,  years = years, fuel_types= fuel_types)

if __name__ == "__main__":
    app.run(debug=False)