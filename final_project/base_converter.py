# ella ballou
# software development fundamentals
# final project

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("converter.html")


@app.route("/dec_to_bin")  # converts decimal to binary using build in operator
def dec_to_bin():
    try:
        dec = int(request.values.get("dec"))
        bi = bin(dec).replace("0b", "")
        return render_template("result.html", u1=dec, u2=bi, unit1="decimal", unit2="binary")
    except:
        return render_template("result2.html")


@app.route("/dec_to_hex")  # converts decimal to hex using built in operator
def dec_to_hex():
    try:
        dec = int(request.values.get("dec"))
        hx = hex(dec).replace("0x", "")
        return render_template("result.html", u1=dec, u2=hx, unit1="decimal", unit2="hexadecimal")
    except:
        return render_template("result2.html")


@app.route("/dec_to_oct")  # converts decimal to octal
def dec_to_oct():
    try:
        dec = int(request.values.get("dec"))
        oc = oct(dec).replace("0o", "")
        return render_template("result.html", u1=dec, u2=oc, unit1="decimal", unit2="octadecimal")
    except:
        return render_template("result2.html")


@app.route("/bin_to_dec")  # converts binary to decimal
def bin_to_dec():
    try:
        bi = request.values.get("bin")
        dec = int(bi, 2)
        return render_template("result.html", u1=bi, u2=dec, unit1="binary", unit2="decimal")
    except:
        return render_template("result2.html")


@app.route("/hex_to_dec")  # converts hexadecimal to decimal
def hex_to_dec():
    try:
        hx = request.values.get("hex")
        dec = int(hx, 16)
        return render_template("result.html", u1=hx, u2=dec, unit1="hexadecimal", unit2="binary")
    except:
        return render_template("result2.html")


@app.route("/oct_to_dec")  # converts octaldecimal to decimal
def oct_to_dec():
    try:
        oc = request.values.get("oct")
        dec = int(oc, 8)
        return render_template("result.html", u1=oc, u2=dec, unit1="octaldecimal", unit2="decimal")
    except:
        return render_template("result2.html")


if __name__ == '__main__':
    app.run()