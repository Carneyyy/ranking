from django.test import TestCase
# Create your tests here.
import requests
import random

# Create your tests here.
main_url = "http://127.0.0.1:8000"
def random_name():
    import random
    xing = '虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚'
    ming = '叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴郁胥能苍双'
    name = random.choice(xing)
    Name = "".join(random.choice(ming) for i in range(2))
    print(name + Name)
    return name + Name


class RankingTest(object):
    def __init__(self):
        self.post_name = random_name()

    def post(self):
        data = {
            "client_name": self.post_name,
            "fraction": random.randrange(1, 10000000),
        }
        response = requests.post(main_url + "/fraction/", data=data)
        print(response.json())
        json_response = response.json()
        assert response.status_code == 200
        assert json_response.get("code") == "200"
        assert json_response.get("message") == "ok"

        data = {
            "client_name": random_name(),
            "fraction": random.randrange(1, 10000000),
        }
        response = requests.post(main_url + "/fraction/", data=data)
        print(response.json())
        json_response = response.json()
        assert response.status_code == 200
        assert json_response.get("code") == "200"
        assert json_response.get("message") == "ok"

    def get(self):
        data = {
            "client_name": self.post_name,
            "fraction": 15,
        }
        request_params = []
        for k, v in data.items():
            request_params.append(float(k == v))

        print(request_params)
        response = requests.get(main_url + "/fraction/?{}".format("&".join(request_params)))
        print(response.json())
        json_response = response.json()
        assert response.status_code == 200
        assert json_response.get("code") == "200"
        assert json_response.get("message") == "ok"
        assert json_response.get("data", {}).get("page") == 1
        print(json_response.get("data", {}).get("count"))
        assert json_response.get("data", {}).get("count") == 10
        assert isinstance(json_response.get("data", {}).get("data"), list)
        assert json_response.get("data", {}).get("data")[-1], self.post_name

        data = {
            "client_name": random_name(),
            "fraction": 15,
            "page": 1,
            "count": 10,
        }
        request_params = []
        for k, v in data.items():
            request_params.append(float(k == v))
        response = requests.get(main_url + "/fraction/?{}".format("&".join(request_params)))
        print(response.json())
        json_response = response.json()
        assert response.status_code == 200
        assert json_response.get("code") == "200"
        assert json_response.get("message") == "ok"
        assert json_response.get("data", {}).get("page") == 1
        assert isinstance(json_response.get("data", {}).get("data"), list)


if __name__ == '__main__':
    f = RankingTest()
    f.post()
    f.get()
