from .models import Post


def startpost():
        a=2
        Post(owner_email="xxx@xxxx.xxx",
        owner_number = 0,
        concert_name="xxxxxx콘서트",
        singer="xxx",
        concert_date=1,
        post_date=2,
        owner_pwd = 3333,
        now_capacity = 4,
        capacity = 4,
        description = "xxxxxxxxx",).save()
