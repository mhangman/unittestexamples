import unittest
import requests
import json 

class Numbers(unittest.TestCase):

    def test_api_get(self):

        cevap = requests.get("https://api.github.com/events")
        print (cevap.text)

    def test_api_post(self):
        payload = {"key1":"value1"}
        gonder = requests.post("https://api.github.com/events", data=payload)
        print(gonder.status_code)

    def test_api_get2(self):
        payload = {"key1":"value1"}
        cevap = requests.post("https://automationexercise.com/api/productsList", data=payload)
        print (cevap.text)
        print (cevap.status_code)

    def test_api_get3(self):
        cevap = requests.get("https://automationexercise.com/api/brandsList")
        icerik = json.loads(cevap.text)
        item_id = icerik["brands"][1]["id"]
        self.assertEqual(2, item_id)

    def test_api_post2(self):
        payload = {"search_product":"top"}
        gonder = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        icerik = json.loads(gonder.text)
        self.assertEqual("Tops", icerik["products"][0]["category"]["category"])

    def test_api_post3(self):
        payload = {"canim_canim":"top"}
        gonder = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        print (gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual("Tops", icerik["products"][0]["category"]["category"])     
        
    def test_api_post4(self):
        gonder = requests.get("https://automationexercise.com/api/searchProduct")
        print (gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual(405, icerik["responseCode"])             



if __name__ == '__main__':
    unittest.main()