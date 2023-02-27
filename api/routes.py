from flask import request
from flask_restful import Resource

from api.parsing import parse


class EndpointOne(Resource):
    """
    Web-page visit registration + data collection.
    """
    def get(self):
        return "Use only POST requests", 400

    def post(self):
        url = request.json
        return parse(url['url'])


class EndpointTwo(Resource):
    """
    Obtaining statistics by domain.
    """
    def get(self):
        return "Use only POST requests", 400

    def post(self):
        try:
            domain_name = request.json
            url = domain_name['domain_name']

            from api.models import URLData
            urls = URLData.query.filter_by(domain_name=url).all()

            url_list = list()
            total_page_count = 0
            active_page_count = 0
            for url in urls:
                url_list.append(url.request_url)
                total_page_count += 1
                if url.status_code == 200:
                    active_page_count += 1

            response = {
                'total_page_count': total_page_count,
                'active_page_count': active_page_count,
                'url_list': url_list,
            }
            return response, 200
        except Exception as E:
            return f"{E}", 500
