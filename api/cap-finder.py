from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(
            str(datetime.now().strftime('%m-%Y-%d %H:%M:%S')).encode())
        return

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "name" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["name"])
            data = r.json()
            capital = data[0]["capital"][0]
            name = data[0]["name"]["common"]
            message = "The capital of {} is {}.".format(name, capital)

        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            print(data)
            name = data[0]["name"]["common"]
            capital = data[0]["capital"][0]
            message = "{} is the capital of {}.".format(capital, name)
            # message = f'{capital}'

        else:
            message = "Try a different Capital or Country"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return