#
# Complete the 'getArticleTitles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
# 
# URL for cut and paste: 
# https://jsonmock.hackerrank.com/api/articles?author=<authorName>&page=<num>
# 
#
import json,os
import requests

def getArticleTitles(author):
    # Write your code here
    #return "".join(author)
    url="https://jsonmock.hackerrank.com/api/articles?author="+author
    resp=requests.get(url)
    #print(resp.json())
    json_resp=resp.json()
    
    #print(json_resp['data'])
    
    print(json_resp)
    res=json_resp['data']
    
    
    l=[]
    #l=[json_resp['data'][i]['title'] for i in len(res)]
    for i in range(len(res)):
        title=json_resp['data'][i]['title']
        
        story_title=json_resp['data'][i]['story_title']
        
        if title is not None:
            l.append(title)
        
        elif title is None and story_title is not None:
            l.append(story_title)
        
        else:
            pass
            
            
        
        #l.append()
    
    return l
        
    
#print(getArticleTitles())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    author = input()

    result = getArticleTitles(author)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
