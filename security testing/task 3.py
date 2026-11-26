from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


class FeedbackHandler(BaseHTTPRequestHandler):
    def send_page(self, body: str, status: int = 200) -> None:
        page = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Feedback</title>
</head>
<body>
    <h1>Feedback Form</h1>
    <form method="post">
        <label for="feedback">Your feedback:</label>
        <textarea id="feedback" name="feedback" maxlength="1000"
                  required></textarea>
        <button type="submit">Submit</button>
    </form>
    {body}
</body>
</html>"""

        encoded_page = page.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded_page)))
        self.send_header(
            "Content-Security-Policy",
            "default-src 'none'; style-src 'self'; form-action 'self'; "
            "base-uri 'none'; frame-ancestors 'none'"
        )
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(encoded_page)

    def do_GET(self):
        self.send_page("")

    def do_POST(self):
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_page("<p>Invalid request.</p>", status=400)
            return

        if content_length < 0 or content_length > 10_000:
            self.send_page("<p>Request is too large.</p>", status=413)
            return

        form_data = self.rfile.read(content_length).decode(
            "utf-8", errors="replace"
        )
        fields = parse_qs(form_data, max_num_fields=10)
        feedback = fields.get("feedback", [""])[0].strip()

        if not feedback or len(feedback) > 1000:
            self.send_page("<p>Feedback must be 1–1000 characters.</p>", 400)
            return

        safe_feedback = escape(feedback)
        self.send_page(f"<h2>Submitted feedback</h2><p>{safe_feedback}</p>")

    def log_message(self, format_string, *args):
        # Avoid logging submitted content.
        pass


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), FeedbackHandler)
    print("Open http://127.0.0.1:8000 in your browser. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()