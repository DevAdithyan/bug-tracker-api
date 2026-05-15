from rest_framework import serializers

from issues.models import Issue


class IssueSerializer(serializers.ModelSerializer):

    assigned_to_username = serializers.CharField(
        source='assigned_to.username',
        read_only=True
    )

    class Meta:
        model = Issue

        fields = '__all__'

    def validate(self, attrs):

        status = attrs.get('status')

        valid_statuses = [
            'OPEN',
            'IN_PROGRESS',
            'RESOLVED',
            'CLOSED'
        ]

        if status not in valid_statuses:
            raise serializers.ValidationError(
                "Invalid issue status."
            )

        return attrs