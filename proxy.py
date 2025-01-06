from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:url>')
def proxy(url):
    # Установка заголовков
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    full_url = f"https://nt0.napr.gov.ge/{url}"
    response = requests.get(full_url, headers=headers, params=request.args)

    return Response(response.content, content_type=response.headers.get('Content-Type'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
