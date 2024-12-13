from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self) -> None:
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open('templates/contacts.html', encoding='utf-8') as file:
            html_content = file.read()
        self.wfile.write(bytes(html_content, "utf-8"))

    def do_POST(self) -> None:
        """ Метод для обработки входящих POST-запросов """
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        response = post_data.decode('utf-8')
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        print(f'Получено от пользователя: {response}')



if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")