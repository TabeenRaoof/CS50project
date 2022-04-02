from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    breakEven=""

    if request.method=="POST":
        if not request.form.get("fixedCost"):
            return render_template("index.html", message1="Please input Fixed Costs")
        setUpCost=float(request.form.get("fixedCost"))


        if not request.form.get("itemCost"):
            return render_template("index.html", message2="Please input Cost Per Item")
        perItemCost=float(request.form.get('itemCost'))

        if not request.form.get("shippingCost"):
            return render_template("index.html", message3="Please input Shipping Cost - Put 0 if there is no shipping cost)")
        shipCost=float(request.form.get("shippingCost"))

        if not request.form.get("otherCosts"):
            return render_template("index.html", message4="Please input Other Costs - Put 0 if there are nbo other costs")
        otherCosts=float(request.form.get("otherCosts"))

        if not request.form.get("price"):
            return render_template("index.html", message5="Please input Cost Per Item")
        salePrice=float(request.form.get("price"))


        breakEven = round(setUpCost / (salePrice - (perItemCost + shipCost + otherCosts)))
        if not breakEven > 0:
            return render_template("index.html", message6= "Price shouldn't be smaller than combined variable costs (Item Cost + Shipping Cost + Other Costs)")

    return render_template("index.html", BREAKEVEN=breakEven)
