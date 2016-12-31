import falcon
import json
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from textsum import textsum
from wsgiref import simple_server



class TextSumAPI:
	def on_get(self, req, resp):
		text = req.get_param('t', '') or req.get_param('q', '')
		if not text:
			resp.body = json.dumps({ "error": "Please using 'q' param." })
			return

		try:
			resp.status = falcon.HTTP_200
			result = { "result": textsum.summarize(text) }
		except ValueError as e:
			print "==> Error:", e
			resp.status = falcon.HTTP_500
			result = { "error": str(e) }

		resp.body = json.dumps(result)

api = falcon.API()
api.add_route('/', TextSumAPI())

if __name__ == '__main__':
    host, port = '127.0.0.1', 8000
    httpd = simple_server.make_server(host, port, api)
    print "Service listening on %s:%s" % (host, port)
    httpd.serve_forever()
