from django.shortcuts import render
import json
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from .Serializer import serializers_link

from urllib.parse import urlencode
import requests
import dropbox
# Create your views here.
app_key='b1uu9f8z5n891fe'
app_secret='xgqfaqnss9qggqj'
base_code='http://127.0.0.1:8000/dropboxapi'
refress_token="hJGRDU99BekAAAAAAAAAASSRpRrvjnyet0UcsiKfXuNUrI_zqFU5vSOILBIquiXL"


def dropbox_oauth(request):
    # return redirect(f"https://www.dropbox.com/oauth2/authorize?client_id={app_key}&redirect_uri={base_code}/authorized&response_type=code")
      return  redirect(f"https://www.dropbox.com/oauth2/authorize?client_id={app_key}&redirect_uri={base_code}/authorized&token_access_type=offline&response_type=code")



def Get_Refresh_Token(request):
    code=request.GET['code']
    # Replace 'YOUR_APP_KEY', 'YOUR_APP_SECRET', 'YOUR_AUTHORIZATION_CODE', and 'YOUR_REDIRECT_URI' with your actual values.
    APP_KEY = 'b1uu9f8z5n891fe'
    APP_SECRET = 'xgqfaqnss9qggqj'

    REDIRECT_URI = 'http://127.0.0.1:8000/dropboxapi/authorized'

    # Prepare the request parameters
    data = {
        'code': code,
        'grant_type': 'authorization_code',
        'client_id': APP_KEY,
        'client_secret': APP_SECRET,
        'redirect_uri': REDIRECT_URI
    }

    # URL-encode the data
    encoded_data = urlencode(data)

    # Set the Content-Type header
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Make the POST request to exchange the authorization code for tokens
    response = requests.post('https://api.dropboxapi.com/oauth2/token', data=encoded_data, headers=headers)
    response_json = response.json()
    access_token = response_json['access_token']
    refresh_token = response_json['refresh_token']

    # Now you have the access token and refresh token
    print(f"Access token: {access_token}")
    print(f"Refresh token: {refresh_token}")
    return JsonResponse(response.json())

@api_view(['POST','GET'])
def shared_link(request):
    APP_KEY = 'b1uu9f8z5n891fe'
    APP_SECRET = 'xgqfaqnss9qggqj'

    dbx = dropbox.Dropbox(
        app_secret=APP_SECRET,
        app_key=APP_KEY,
        oauth2_refresh_token= "F9NFTbcrkKIAAAAAAAAAAdrLvlD5HxOTv91jU2hn8cxBBtYQVOUfZd_fm3oCAzM9"

    )

    if request.method=='POST':
        serializer=serializers_link(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data['pathname'])
            try:
                # '/demo.webm'
                shared_link = dbx.sharing_create_shared_link_with_settings("/calculator4.jpg")
                temporary_link = dbx.files_get_temporary_link(serializer.data['pathname'])
                shared_link = shared_link
                print(temporary_link.link, '[[[[[[]]]]]]')
                preview_url = shared_link
                # print(f"Preview URL: {preview_url}")
                return Response({"link":temporary_link.link})


            except dropbox.exceptions.ApiError as err:
                print(f"Error creating shared link: {err}")
                preview_url = shared_link
                # print(f"Preview URL: {preview_url}")
                return HttpResponse(err)

    return Response('signup successfully ')


    # Replace 'ACCESS_TOKEN' with your Dropbox access token
    # For example, ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN'
    # ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN'
    #
    # Create a Dropbox client instance



