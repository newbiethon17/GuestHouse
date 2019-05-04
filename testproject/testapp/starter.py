from .models import Post


def startpost():
        a=2
        Post(owner_email="xxx@xxxx.xxx",
        concert_name="xxxxxx콘서트",
        singer="xxx",
        concert_date=5,
        post_date=5,).save()
