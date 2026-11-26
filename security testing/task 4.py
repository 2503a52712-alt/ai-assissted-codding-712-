from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json


ALLOWED_HOST = "api.example.com"


def fetch_api_data(url: str) -> dict:
    parsed = urlparse(url)

    # Require HTTPS and an exact approved host.
    if parsed.scheme != "https" or parsed.hostname != ALLOWED_HOST:
        raise ValueError("Only the approved HTTPS API host is allowed.")

    request = Request(
        url,
        headers={"Accept": "application/json"},
        method="GET"
    )

    try:
        with urlopen(request, timeout=5) as response:
            if response.status != 200:
                raise RuntimeError(f"API returned status {response.status}")

            content_type = response.headers.get_content_type()
            if content_type != "application/json":
                raise ValueError("API did not return JSON.")

            raw_data = response.read(1_000_001)
            if len(raw_data) > 1_000_000:
                raise ValueError("API response is too large.")

            return json.loads(raw_data.decode("utf-8"))

    except HTTPError as error:
        raise RuntimeError(f"HTTP error: {error.code}") from error
    except URLError as error:
        raise RuntimeError("Could not connect to the API.") from error


if __name__ == "__main__":
    api_url = f"https://{ALLOWED_HOST}/data"

    try:
        result = fetch_api_data(api_url)
        print(json.dumps(result, indent=2))
    except (ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"Request failed: {error}")