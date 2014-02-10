from models import Presentation


def get_presentations(request):
    return {'presentations_list': Presentation.objects.values('title')}