import os
import django
import random
import string


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from m2m.models import *


post_count = 30
tag_count = 100
rel_count = 150


def gen_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


tags = Tag.objects.bulk_create([
    Tag(
        name=gen_random_string(10), 
        text=gen_random_string(15)
    ) for i in range(tag_count)
])

posts = Post.objects.bulk_create([
    Post(
        text=gen_random_string(15)
    ) for i in range(post_count)
])

through_ids = list(set([
    (
        random.randint(1,post_count),
        random.randint(1,tag_count)   
    ) for i in range(rel_count)
]))

through_objs = [
    Post.tag.through(
        post_id=ids[0],
        tag_id=ids[1],
    ) for ids in through_ids
]

Post.tag.through.objects.bulk_create(through_objs)