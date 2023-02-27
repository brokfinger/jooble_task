from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests


def parse(url: str):
    try:
        domain_name = urlparse(url).netloc
        request = requests.get(url)
        soup = BeautifulSoup(request.content, 'html.parser')

        if soup.find("title"):
            title = soup.find("title").string
        else:
            title = ""

        if request.history:
            status_code = request.history[0].status_code
            final_status_code = request.status_code
            final_url = request.url
            from manage import app
            app.logger.info("Redirect: ", status_code)
        else:
            status_code = request.status_code
            final_status_code = ""
            final_url = ""
    except Exception:
        return 'Maybe url broken or request not valid', 400

    from api.models import save_db
    # also (import circle error)
    answer = save_db(url, status_code, final_url,
                     final_status_code,
                     domain_name, str(title))

    if answer:
        response = {
            "status_code": status_code,
            "final_url": final_url,
            "final_status_code": final_status_code,
            "domain_name": domain_name,
            "title": title,
        }
        return response, 200
    else:
        return "Don't save in database", 500
