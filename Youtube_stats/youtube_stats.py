import pandas as pd

api_key = "AIzaSyDOVaoNBtG1FCpeJmmsFw775RsU7LX_tMM" #api key has been expired so it won't work again
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)


def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
  #  playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId='PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC', 
                                           part='snippet',
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

videos = get_channel_videos('UCEDEKrjFZFp3Br3ENlYomdA')
video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos))
#print(len(video_ids)) will print 507

stats = []
for i in range(0, len(video_ids)):
  res = (youtube).videos().list(id=','.join(video_ids[i]),part='statistics').execute()
  stats += res['items']
#print(stats)
print(int((stats['statistics']['viewCount'])))
# for video in videos:
#     print(video['snippet']['title'])
#     print(video['snippet']['publishedAt']) 
#     print(video['statistics']['viewCount'])

title=[ ]
liked=[ ]
disliked=[ ]
views=[ ]
url=[ ]
comment=[ ]
videoid = []
publishedDate = []
video_description = []

for i in range(0,len(video_ids)):
 # print(i)
  # i += 1
 title.append((videos[i])['snippet']['title'])
 publishedDate.append((videos[i])['snippet']['publishedAt'])
# print((int((stats[i])['statistics']['viewCount'])))
 video_description.append((videos[i])['snippet']['description'])
 liked.append(int((stats[i])['statistics']['likeCount']))
 disliked.append(int((stats[i])['statistics']['dislikeCount']))
 views.append(int((stats[i])['statistics']['viewCount']))
#  comment.append(int((stats[i])['statistics']['commentCount']))
 videoid.append(videos[i]['snippet']['resourceId']['videoId'])

data={'title':title,'publishedDate':publishedDate}
df=pd.DataFrame(data)
print(df)  

df.to_csv('extractdata.csv', index=False)
