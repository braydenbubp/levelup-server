from levelupapi.models import Gamer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    '''checks to see if User has Associated Gamer
      Method args: request -- full HTTP request obj
    '''
    uid = request.data['uid']
    
    #use built in auth method to verify
    #auth returns user obj or None if no user found
    gamer = Gamer.objects.filter(uid=uid).first()
    
    #if auth successful respond with their token
    if gamer is not None:
        data = {
            'id': gamer.id,
            'uid': gamer.uid,
            'bio': gamer.bio
        }
        return Response(data)
    else:
        #bad login details provided so no login
        data = { 'valid': False }
        return Response(data)
      
@api_view(['POST'])
def register_user(request):
    '''handle creation of new gamer for auth'''

    #now save user info in levelupapi_gamer table
    gamer = Gamer.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    #return gamer info to client
    data = {
        'id': gamer.id,
        'uid': gamer.uid,
        'bio': gamer.bio
    }
    return Response(data)
