from flask import Flask, request, render_template_string

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Matematika</title>
</head>
<body>
    <h2>Kalkulator + Cek Bilangan Prima</h2>

    <form method="post">
        <p>Masukkan angka / operasi (contoh: 2+3, 2**3, 7):</p>
        <input type="text" name="inputan" required>
        <button type="submit">Proses</button>
    </form>

    {% if hasil %}
        <h3>Hasil: {{ hasil }}</h3>
    {% endif %}

    {% if prima is not none %}
        <h3>Status Prima: {{ prima }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    hasil = None
    prima = None

    if request.method == "POST":
        try:
            user_input = request.form["inputan"]

            # hitung kalkulator
            hasil_hitung = eval(user_input)

            hasil = hasil_hitung

            # cek prima kalau bilangan bulat
            if isinstance(hasil_hitung, int):
                if is_prime(hasil_hitung):
                    prima = "Bilangan Prima"
                else:
                    prima = "Bukan Bilangan Prima"

        except:
            hasil = "Input tidak valid!"

    return render_template_string(HTML, hasil=hasil, prima=prima)

app.run(debug=True)