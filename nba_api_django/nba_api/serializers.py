from rest_framework import serializers
from .models import Conference, Team, Player


class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        many=True,
        read_only=True
    )

    conference_url = serializers.ModelSerializer.serializer_url_field(
        view_name='conference_detail'
    )

    class Meta:
        model = Conference
        fields = ('id', 'teams', 'conference_url', 'name')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    conference = serializers.HyperlinkedRelatedField(
        view_name='conference_detail',
        read_only=True
    )

    conference_id = serializers.PrimaryKeyRelatedField(
        queryset=Conference.objects.all(),
        source='conference'
    )

    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team_detail'
    )

    class Meta:
        model = Team
        fields = ('id', 'conference', 'conference_id', 'players', 'team_url', 'name', 'location', 'wins',
                  'losses', 'conf_championships', 'nba_championships')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )

    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )

    class Meta:
        model = Player
        fields = ('id', 'team', 'team_id',
                  'name', 'position', 'age')
