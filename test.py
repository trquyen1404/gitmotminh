from flask import Flask, request, render_template_string
import base64
import io

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)
#aaaa
HTML = """<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>Thống kê sinh viên</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 720px; margin: 40px auto; }
    input, button { padding: 8px; margin: 4px; }
    .error { color: #b00020; }
  </style>
</head>
<body>
  <h1>Biểu đồ sinh viên nam nữ</h1>
  <form method="post">
    <label>Nam: <input type="number" name="nam" min="0" value="{{ nam }}" required></label>
    <label>Nữ: <input type="number" name="nu" min="0" value="{{ nu }}" required></label>
    <button type="submit">Vẽ biểu đồ</button>
  </form>
  {% if error %}<p class="error">{{ error }}</p>{% endif %}
  {% if chart %}
    <p>Tổng số sinh viên: <strong>{{ nam + nu }}</strong></p>
    <img src="data:image/png;base64,{{ chart }}" alt="Biểu đồ cột nam nữ">
  {% endif %}
</body>
</html>"""


@app.route("/", methods=["GET", "POST"])
def index():
    nam = nu = 0
    chart = error = None
    if request.method == "POST":
        try:
            nam = int(request.form["nam"])
            nu = int(request.form["nu"])
            if nam < 0 or nu < 0:
                raise ValueError
            fig, ax = plt.subplots(figsize=(6, 4))
            bars = ax.bar(["Nam", "Nữ"], [nam, nu], color=["#4E79A7", "#E15759"])
            ax.set_title("Số sinh viên nam và nữ")
            ax.set_ylabel("Số sinh viên")
            ax.bar_label(bars)
            ax.set_ylim(0, max(nam, nu, 1) + 2)
            buffer = io.BytesIO()
            fig.tight_layout()
            fig.savefig(buffer, format="png")
            plt.close(fig)
            chart = base64.b64encode(buffer.getvalue()).decode()
        except (KeyError, ValueError):
            error = "Vui lòng nhập hai số nguyên không âm."
    return render_template_string(HTML, nam=nam, nu=nu, chart=chart, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5175, debug=True)