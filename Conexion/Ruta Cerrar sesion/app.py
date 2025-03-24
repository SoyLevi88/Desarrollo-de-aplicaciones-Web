@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión", "success")
    return redirect(url_for("login"))