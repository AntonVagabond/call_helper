from django.contrib.auth import get_user_model

from common.serializers.mixins import DictMixinSerializer
from breaks.models import dicts

User = get_user_model()
