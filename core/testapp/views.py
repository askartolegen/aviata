import time
import json
import xml.etree.ElementTree as et
from urllib.request import urlopen
from xml.etree import ElementTree as etree
import requests
import uuid
import datetime


from rest_framework.views import APIView


class ProviderAView(APIView):
    def post(self, request):
        xml_data = open('response_a.xml', 'r').read()
        root = et.XML(xml_data)
        for i, child in enumerate(root):
            if True:
                time.sleep(30)
                yield child


class ProviderBView(APIView):
    def post(self, request):
        xml_data = open('response_b.xml', 'r').read()
        root = et.XML(xml_data)
        for i, child in enumerate(root):
            if True:
                time.sleep(60)
                yield child


class AirflowView(APIView):
    def get(self, request):
        now = datetime.datetime.now()
        exchange = []
        if now.strftime("%H:%M") == "12:00":
            with urlopen(f"https://www.nationalbank.kz/rss/get_rates.cfm?fdate={now.strftime('%d.%m.%Y')}",
                         timeout=10) as r:
                for element in etree.parse(r).findall('item'):
                    exchange.append([element.find('title').text, element.find('description').text])

    def post(self, request):
        requests.post('http://127.0.0.1:9000/search/provider_a/')
        requests.post('http://127.0.0.1:9000/search/provider_b/')
        dictionary = {"search_id": str(uuid.uuid4())}
        res = json.dumps(dictionary, indent=4)
        return res
