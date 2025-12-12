from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)
FOLDER = r"D:\Movies"

TEMPLATE = """
<h2>Index of {{ path }}</h2>
<ul>
  {% for name in dirs %}
    <li><a href="{{ name }}/">{{ name }}/</a></li>
  {% endfor %}
  {% for name in files %}
    <li><a href="{{ name }}">{{ name }}</a></li>
  {% endfor %}
</ul>
"""

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def dir_listing(req_path):
    abs_path = os.path.join(FOLDER, req_path)

    if not os.path.exists(abs_path):
        return "404 Not Found", 404

    # If it's a file, serve it
    if os.path.isfile(abs_path):
        return send_from_directory(FOLDER, req_path)

    # It's a folder → list contents
    files = []
    dirs = []

    for name in os.listdir(abs_path):
        if os.path.isdir(os.path.join(abs_path, name)):
            dirs.append(name)
        else:
            files.append(name)

    return render_template_string(TEMPLATE, files=files, dirs=dirs, path=req_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
