from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from teaching_values.users.api.serializers import UserModelSerializer

User = get_user_model()


class RetrieveUserView(RetrieveAPIView):
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]
