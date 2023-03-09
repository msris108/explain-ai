import environ
import openai
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

openai.api_key =  env('OPENAI_KEY')

def ChatGPT(query, model):
   """
   This function uses the OpenAI API to generate a response to the given
   user_query using the ChatGPT model
   """
   # Use the OpenAI API to generate a response
   completion = openai.Completion.create(
      engine=model,
      prompt=query,
      max_tokens=1024,
      n=1,
      temperature=0.5,
   )
   response = completion.choices[0].text
   return response


@api_view(['GET'])
def getApiRoutes(request): 
    routes = [
        "/api/token", 
        "/api/token/refresh",
        "/api/getPrompt/"
    ]
    return Response(routes)

@api_view(['GET'])
def getPrompt(request, query, model, level): 
    prompt = {
        "query": query,
        "model": model,
        "level": level,
        "prompt": ChatGPT("Explain " + query + " to a " + level + " old kid.", model),
    }
    return Response(prompt)

@api_view(['GET'])
def getLinkedInPost(request, query): 
    prompt = {
        "query": query,
        "prompt": ChatGPT("Write a small linkedIn post about" + query, "text-davinci-003"),
    }
    return Response(prompt)


@api_view(['GET'])
def getMovieSummary(request, query): 
    prompt = {
        "query": query,
        "prompt": ChatGPT("Summarize the movie" + query + "If it exists, else just tell me to look for another movie", "text-davinci-003"),
    }
    return Response(prompt)