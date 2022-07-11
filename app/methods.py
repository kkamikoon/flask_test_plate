from app import app

from flask import (
    request,
    render_template,
    render_template_string,
    abort
)

@app.route("/test", methods=['GET'])
def test_get():
    return render_template("get.html")


@app.route("/test/<data>", methods=['GET'])
def test_get_parameters(data):
    print(f"data : {data} - (type : {type(data)})")
    return render_template("get.html", data=data)


@app.route("/test/post", methods=['GET', 'POST'])
def test_post():
    if request.method == "POST":
        # Database connection or some logic
        data = request.form.get("var1", type=str, default=None)
        
        print(f"data : {data} - (type : {type(data)})")

        if not data:
            return abort(400)

        return render_template("post.html", data=data)

    return render_template("post.html")


@app.route("/test/ssti", methods=['GET', 'POST'])
def test_ssti():
    if request.method == "POST":
        # Database connection or some logic
        data = request.form.get("var1", type=str, default=None)
        
        print(f"data : {data} - (type : {type(data)})")

        ssti_html = render_template("ssti.html")
        additional = f"Test Input : <p>{data}</p>"

        if not data:
            return abort(400)

        return render_template_string(ssti_html + additional)

    return render_template("ssti.html")