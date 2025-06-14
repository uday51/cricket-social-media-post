import requests
import google.generativeai as genai
from datetime import datetime


print("Hi")

CRIC_API_KEY =  # Your CricAPI key
GEMINI_API_KEY = Your Gemini API key
MATCH_ID = ""

#configure Gemini

genai.configure(api_key=GEMINI_API_KEY)
model=genai.GenerativeModel("gemini-1.5-flash")

def get_match_data():
  url=url = f"https://api.cricapi.com/v1/match_info?apikey={CRIC_API_KEY}&id={MATCH_ID}"
  response=requests.get(url)
  data=response.json()
  
  if data.get("status") !="success":
    raise Exception ("Failed to get match data")
  return data["data"]
  
def generate_social_media_post(match_data):
  teams=" vs ".join(match_data["teams"])
  status=match_data["status"]
  venue=match_data["venue"]
  
  scores=[]
  for inning in match_data.get("score",[]):
   scores.append(f"{inning["inning"]}:{inning['r']/inning['w']} ({inning['o']}) overs")
   scores_text="\n" .join(scores) if scores else "No Scorecard yet"
   
   prompt = f"""Create an engaging social media post about this cricket match:
   Match: {teams}
   Status: {status}
   Venue: {venue}
   Scores:{scores_text}

   - Make it exciting and conversational
   - Include relevant hashtags (max 5)
   - Keep it under 280 characters
   - Add emojis where appropriate
   - Don't include URLs or special characters like *
    """
    
   response=model.generate_content(prompt)
   return response.text
    
    
    
  

get_data=get_match_data()
print(get_data)
post=generate_social_media_post(get_data)
print(post)
print("completed")
