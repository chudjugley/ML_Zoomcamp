import pickle
import requests


#model = 'pipeline.bin'

#with open(model, 'rb') as f:
#    pipeline = pickle.load(f)

# request url
url = 'http://localhost:9696/predict'

customer = {
  "lead_source": "organic_search",
  "industry": "technology",
  "employment_status": "employed",
  "location": "europe",
  "number_of_courses_viewed": 4,
  "annual_income": 80304.0,
  "interaction_count": 7,
  "lead_score": 0.74
}

#prob = pipeline.predict_proba(customer)[:,1]
#print(prob)

# use web service
response = requests.post(url, json=customer).json()
print(response)