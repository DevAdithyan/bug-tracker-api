from rest_framework import serializers

from issues.models import Issue


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['created_by']

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