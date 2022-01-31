from googleapiclient.discovery import build
import os
import webbrowser
keyword=input("what you want to search: ")
try:
    api_key=os.environ.get('youtube_api_key')
    #create an api specific service object
    youtube=build('youtube','v3',developerKey=api_key)
    while True:
        request=youtube.search().list(part='snippet',q=keyword,maxResults=50)
        response=request.execute()
        items=response['items']
        #set chrome browsert
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'))
        for item in items:
            webbrowser.get('chrome').open('https://www.youtube.com/watch?v='+item['id']['videoId'])
            if input("Enter 'y' for continue: ")=='y':
                pass
            else:
                exit()
        nextPageToken=response.get('nextPageToken')
        if not nextPageToken:
            break
except Exception as e:
    print("Your Request can not be successed")