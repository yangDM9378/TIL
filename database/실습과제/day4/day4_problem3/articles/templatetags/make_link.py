# "오늘 #장고 #진짜 #힘들다"

# '오늘' -> pass
# '#장고' -> 해시태그 -> <a> 로 묶어줌

# 결과 : "오늘 <a href='~~'>#장고</a> ... "

from django import template
import re                       # 정규표현식 용

register = template.Library()


@register.filter
def add_link(value):
    # value = article
    # 전달된 value 객체의 content 멤버변수를 가져온다.
    content = value.content

    # article 에 포함된 hashtag -> 링크를 걸어서 갈 수 있도록 구현
    # 전달된 value 객체에 포함된 hashtags 전체를 가져오는 queryset
    tags = value.hashtags.all()

    # tags 순회하면서, content 내에서 해당 문자열을 링크로 변경
    for tag in tags:
        content = re.sub(tag.content, '<a href="/articles/' + str(tag.id) + '/hashtag/">'+tag.content+'</a>', content)
    return content