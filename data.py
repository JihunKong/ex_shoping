# data.py
import urllib.parse

MISSIONS = {
    "여행": {
        "budget": 30000,
        "description": "친구들과 당일치기 기차 여행을 떠나요! 기차표와 간식을 3만원 안에서 해결해보세요.",
        "emoji": "🚂"
    },
    "캠핑": {
        "budget": 30000,
        "description": "가족들과 주말 캠핑을 가요. 저녁 식사 재료와 필요한 도구를 3만원으로 준비해보세요.",
        "emoji": "⛺"
    },
    "요리": {
        "budget": 30000,
        "description": "부모님 생신상을 차려드려요. 맛있는 미역국과 반찬 재료를 3만원에 맞춰보세요.",
        "emoji": "🍳"
    }
}

def get_img(keyword):
    # Use Pollinations.ai for generated images based on keywords
    # Adding 'minimal', 'illustration' to keep style consistent and simple
    prompt = f"{keyword}, minimal, cute illustration, white background"
    encoded_prompt = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=300&height=300&nologo=true"

PRODUCTS = {
    "여행": [
        {"name": "기차표(어린이)", "price": 8000, "emoji": "🎫", "category": "교통", "image": get_img("train ticket")},
        {"name": "김밥", "price": 3500, "emoji": "🍙", "category": "식사", "image": get_img("kimbap sushi")},
        {"name": "삶은 계란(2개)", "price": 2000, "emoji": "🥚", "category": "간식", "image": get_img("boiled eggs")},
        {"name": "사이다", "price": 1500, "emoji": "🥤", "category": "음료", "image": get_img("cider soda bottle")},
        {"name": "과자", "price": 2000, "emoji": "🍪", "category": "간식", "image": get_img("cookies snack")},
        {"name": "여행용 티슈", "price": 1000, "emoji": "🧻", "category": "필수품", "image": get_img("pocket tissue")},
        {"name": "기념품 자석", "price": 5000, "emoji": "🧲", "category": "기념품", "image": get_img("fridge magnet souvenir")},
        {"name": "즉석카메라 필름", "price": 12000, "emoji": "📸", "category": "취미", "image": get_img("instant camera film")},
    ],
    "캠핑": [
        {"name": "삼겹살(300g)", "price": 12000, "emoji": "🥩", "category": "식사", "image": get_img("pork belly meat raw")},
        {"name": "상추/깻잎", "price": 3000, "emoji": "🥬", "category": "식사", "image": get_img("lettuce vegetables")},
        {"name": "라면(5개)", "price": 4500, "emoji": "🍜", "category": "식사", "image": get_img("ramen noodles packet")},
        {"name": "마시멜로", "price": 3000, "emoji": "🍡", "category": "간식", "image": get_img("marshmallows on stick")},
        {"name": "장작", "price": 8000, "emoji": "🪵", "category": "도구", "image": get_img("firewood logs")},
        {"name": "부탄가스", "price": 2000, "emoji": "🔥", "category": "도구", "image": get_img("butane gas canister")},
        {"name": "일회용 접시", "price": 2000, "emoji": "🍽️", "category": "도구", "image": get_img("paper plates")},
        {"name": "물(2L)", "price": 1500, "emoji": "💧", "category": "음료", "image": get_img("bottled water plastic")},
    ],
    "요리": [
        {"name": "소고기(국거리)", "price": 10000, "emoji": "🥩", "category": "재료", "image": get_img("raw beef meat chunk")},
        {"name": "자른 미역", "price": 3000, "emoji": "🌿", "category": "재료", "image": get_img("dried seaweed")},
        {"name": "두부", "price": 1500, "emoji": "🧊", "category": "재료", "image": get_img("tofu block")},
        {"name": "케이크(조각)", "price": 6000, "emoji": "🍰", "category": "디저트", "image": get_img("strawberry shortcake slice")},
        {"name": "꽃다발", "price": 15000, "emoji": "💐", "category": "선물", "image": get_img("flower bouquet")},
        {"name": "잡채용 당면", "price": 4000, "emoji": "🍝", "category": "재료", "image": get_img("glass noodles dry")},
        {"name": "시금치", "price": 2500, "emoji": "🥬", "category": "재료", "image": get_img("fresh spinach bunch")},
        {"name": "생일 초", "price": 1000, "emoji": "🕯️", "category": "기타", "image": get_img("birthday candles")},
    ]
}
