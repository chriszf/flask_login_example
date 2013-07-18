#!/usr/bin/env python

from flask import Flask, render_template, session, g, redirect, request, url_for
app = Flask(__name__)

import model


@app.route("/")
def show_login():
    return render_template("login.html")


@app.route("/loggin_is_for_lumberjacks", methods=["POST"])
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")

    user = model.validate_user(username, password)

    if not user:
        # Failed to log in, redirect to the login function
        return redirect(url_for("login"))
    else:
        session['user_id'] = user.id
        # Successfully logged in, redirect to the fish handler
        return redirect(url_for("fish"))

@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        user = model.get_user_by_id(user_id)
        g.user = user
    else:
        g.user = None

@app.route("/my_fish")
def fish():
    print "USER ID", session.get('user_id')
    print g.user.name
    my_fish = model.get_fish_by_user_id(g.user.id)
    return render_template("fish.html", fish=my_fish)


app.secret_key="FISHFISHFISHFISH"

if __name__ == "__main__":
    app.run(debug=True)
