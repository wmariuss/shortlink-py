from flask import render_template, redirect, url_for, request
from app import app, db, SHORTENED_LENGTH
from app.forms import EnterShortURLForm, ReturnToMainButton
from app.url_manager import url_manager
from app.url_verifier import UrlVerifier
from app.url_parser import UrlParser

APP_TITLE = "ShortLink"


@app.route("/", methods=["GET", "POST"])
def index():
    all_data = url_manager.get_all_previous_data()
    print(url_manager.get_hash_table_usage())

    form = EnterShortURLForm()

    if form.validate_on_submit():
        long_url = form.url.data
        return redirect(url_for("short", url=form.url.data, short_url=""))

    return render_template("index.html", title=APP_TITLE, form=form, all_data=all_data)


@app.route("/short", methods=["GET", "POST"])
def short():
    back_btn = ReturnToMainButton()
    if back_btn.validate_on_submit():
        return redirect("/")

    long_url = request.args["url"]

    protocol, long_url = UrlParser.parse(long_url)
    is_url_valid = UrlVerifier.is_url_valid(protocol, long_url)

    if not is_url_valid:
        return redirect_invalid("Type a valid URL")

    short_url = request.args["short_url"]
    if short_url is not "":
        if url_manager.is_short_url_exists(short_url):
            return redirect_invalid("Short URL taken")
        else:
            url_manager.set_short_url(long_url, short_url)
    elif short_url is "":
        short_url = url_manager.get_short_url(long_url)

    short_url = app.config["URL_APP"] + short_url
    return render_template(
        "result.html", title=APP_TITLE, short_url=short_url, back_btn=back_btn
    )


@app.route("/<short_url>", methods=["GET", "POST"])
def long(short_url):
    back_btn = ReturnToMainButton()
    if back_btn.validate_on_submit():
        return redirect("/")

    if len(short_url) != SHORTENED_LENGTH:
        return redirect_invalid("Short URL is invalid.")

    long_url = url_manager.get_long_url(short_url)

    if long_url is None:
        return redirect_invalid("Short URL is invalid.")

    return redirect("http://" + long_url, code=302)


@app.route("/delete/<short_url>", methods=["GET", "POST"])
def delete(short_url):
    if url_manager.is_short_url_exists(short_url):
        url_manager.delete_short_url(short_url)
        return redirect_invalid("Short URL has been removed")
    else:
        return redirect_invalid("Short URL does not exist")


def redirect_invalid(message):
    back_btn = ReturnToMainButton()
    if back_btn.validate_on_submit():
        return redirect("/")

    return render_template(
        "invalid.html", title=APP_TITLE, message=message, back_btn=back_btn
    )

