import json
from sqlalchemy.ext.declarative import DeclarativeMeta


class TimerEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return {
                'id': obj.id,
                'from_date': obj.from_date.isoformat(),
                'is_private': obj.is_private,
                'is_stopped': obj.is_stopped,
                'timer_title': obj.timer_title,
                'timer_text': obj.timer_text
            }

        return json.JSONEncoder.default(self, obj)
