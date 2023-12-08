import re
from bs4 import BeautifulSoup

forum_list = ['lumpini', 'rajdumnern', 'silom', 'mbk', 'klaibann', 'horoscope',
    'siliconvalley', 'theoldsiam', 'library', 'camera', 'jatujak',
    'region', 'gallery', 'greenzone', 'tvshow', 'beauty', 'home',
    'food', 'chalermkrung', 'chalermthai', 'family', 'writer',
    'blueplanet', 'pantip', 'ratchada', 'social', 'religious',
    'supachalasai', 'siam', 'sinthorn', 'wahkor', 'art', 'cartoon',
    'bangrak', 'korea', 'gadget', 'isolate']

def clean_text(text):
    text = re.sub(r'[\t\u00a0\xa0\u3000\u2002-\u200a\u202f]+', ' ', text) # shrink whitespaces e.g. good  boy -> good boy
    text = re.sub(r'[\r\u200b\ufeff]+', '', text) # remove non-breaking space
    return text

def get_one_post(soup:BeautifulSoup):
    url = soup.select_one('meta[property="og:url"]').get('content')
    post_category = soup.select_one('meta[name="lead:category1"]').get('content')

    ## get forum - it should be in the list above
    forum = None
    for tag1 in soup.select('meta[name="lead:tag1"]'):
        if tag1.get('content') in forum_list:
            forum = tag1.get('content')
    
    ## main post
    main_post = soup.select_one('div.main-post-inner')
    ## remove edit history
    if main_post.select_one('div.edit-history'):
        main_post.select_one('div.edit-history').decompose()

    title = main_post.h2.text.strip()
    tags = [tag.text.strip() for tag in main_post.select('a.tag-item')]
    text = main_post.select_one('div.display-post-story').get_text(separator='\n').strip()
    profile_name = main_post.select_one('a.display-post-name.owner').text
    profile_url = main_post.select_one('div.display-post-avatar').a.get('href')
    like = int(main_post.select_one('span.like-score').text)
    emotions = [int(x.text) for x in main_post.select_one('div.emotion-vote-choice').select('span.emotion-choice-score')[1:]]
    time = main_post.select_one('span.display-post-timestamp').select_one('abbr').get('data-utime')
    
    ## comments
    try:
        n_comment = int(soup.select_one('#comments-counts').text.split()[0])
    except:
        n_comment = 0
    comments = []
    for comment in soup.select('div:not(.sub-comment).section-comment'):
        comments.append({
            'comment': clean_text(comment.select_one('div.display-post-story').text.strip()),
            'like': int(comment.select_one('span.like-score').text),
            'profile_name': comment.select_one('a.display-post-name').text,
            'profile_url': 'https://pantip.com' + comment.select_one('a.display-post-name').get('href'),
            'time': comment.select_one('abbr').get('data-utime')
        })

    return {
        'url': url,
        'time': time,
        'title': clean_text(title),
        'post_category': post_category,
        'tags': tags,
        'text': clean_text(text),
        'profile_name': profile_name,
        'profile_url': profile_url,
        'forum': forum,
        'like': like,
        'emotion_heart': emotions[0],
        'emotion_laugh': emotions[1],
        'emotion_love': emotions[2],
        'emotion_sad': emotions[3],
        'emotion_horror': emotions[4],
        'emotion_wow': emotions[5],
        'num_comment': n_comment,
        'comments': comments
    }