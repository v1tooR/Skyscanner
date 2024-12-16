import json
import requests

def python_function(data):
    # Sua lógica aqui
    result = data['input'] * 2
    return {'result': result}

# Executa a função Python no navegador
result = python_function({"input": 5})
print(json.dumps(result))

def create_search(origin, destination, departure_date, adults):
    url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"
    
    payload = {
        "market": "BRA",
        "locale": "pt-BR",
        "currency": "BRL",
        "queryLegs": [{"OriginStationCode": origin, "DestinationStationCode": destination, "DepartureDate": departure_date}],
        "adults": adults
    }
    
    headers = {
        "Authorization": f"Bearer {YOUR_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def poll_search(session_token):
    url = f"https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/poll/{session_token}"
    
    headers = {
        "Authorization": f"Bearer {YOUR_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, headers=headers)
    return response.json()