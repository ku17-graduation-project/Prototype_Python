PLACES_KEYWORDS = {'교내': ['지름길', '자판기'], '카페': ['맛집', '학생할인'], '식당': ['맛집', '점심', '해장', '저녁'], '공통': ['공부', '콘센트많음', '공강', '만쥬', '건덕', '24시', '팀플', '무료']}

def get_all_keywords():
    res = []
    for key in PLACES_KEYWORDS:
        res.extend(PLACES_KEYWORDS[key])
        
    return res