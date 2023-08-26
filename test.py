import requests
def postProduct(name, price):
        api_url = 'http://127.0.0.1:8000/api' #ローカルサーバー
        Headers = { "Authorization" : "Token 2e4e2bad93059c80f095576a3debdba12c371eec"}
        x = requests.post(api_url, headers=Headers, data={'name': name, 'price': price})
        print(x.text)
def getProduct():
    api_url = 'http://127.0.0.1:8000/api' #ローカルサーバー
    Headers = { "Authorization" : "Token 2e4e2bad93059c80f095576a3debdba12c371eec"}
    res = requests.get(api_url, headers=Headers)
    print(res.text)

postProduct('商品1', 200)
getProduct()

def postGeneral(deadline, requiredtime):
    api_url = 'http://127.0.0.1:8000/general' #ローカルサーバー
    y = requests.post(api_url, data={'deadline': deadline, 'requiredtime': requiredtime})
    print(y.text)

def getGeneral():
    api_url = 'http://127.0.0.1:8000/general'
    res = requests.get(api_url)
    print(res.text)

postGeneral('2021-01-01', '00:00:00')
getGeneral()