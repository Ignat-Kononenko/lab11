from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<html>
<head><title>CI/CD Demo</title></head>
<body>
    <h2>Форма приветствия</h2>
    <form method="post">
        <label>Ваше имя:</label>
        <input type="text" name="username" required>
        <button type="submit">Отправить</button>
    </form>
    {% if greeting %}
        <h3>{{ greeting }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = None
    if request.method == 'POST':
        name = request.form.get('username', 'Гость')
        greeting = f'Привет, {name}!'
    return render_template_string(HTML_FORM, greeting=greeting)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)