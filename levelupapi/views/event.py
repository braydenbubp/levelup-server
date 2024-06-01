from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from levelupapi.models import Event, Gamer, Game, EventGamer

class EventView(ViewSet):

    def retrieve(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        events = Event.objects.all()
        
        game = request.query_params.get('game', None)
        if game is not None:
            events = events.filter(game_id=game)
        
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        organizer = Gamer.objects.get(uid=request.data["userId"])
        game = Game.objects.get(pk=request.data["game"])
        
        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            organizer=organizer,
            game=game,
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
        
    def update(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        
        game = Game.objects.get(pk=request.data["game"])
        event.game = game
        event.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """post req for user to sign up for event"""
        
        gamer = Gamer.objects.get(uid=request.data["userId"])
        event = Event.objects.get(pk=pk)
        attendee = EventGamer.objects.create(
            gamer = gamer,
            event = event
        )
        
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """post req for user to leave an event"""
        
        gamer = Gamer.objects.get(uid=request.data["userId"])
        event = Event.objects.get(pk=pk)
        attendee = EventGamer.objects.get(event_id=event.id, gamer_id=gamer.id)
        attendee.delete()
        
        return Response({'message': 'Gamer removed'}, status=status.HTTP_204_NO_CONTENT)

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('id', 'description', 'date', 'time', 'organizer', 'game')
        depth = 2
