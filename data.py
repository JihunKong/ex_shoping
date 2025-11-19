# data.py

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

PRODUCTS = {
    "여행": [
        {"name": "기차표(어린이)", "price": 8000, "emoji": "🎫", "category": "교통"},
        {"name": "김밥", "price": 3500, "emoji": "🍙", "category": "식사"},
        {"name": "삶은 계란(2개)", "price": 2000, "emoji": "🥚", "category": "간식"},
        {"name": "사이다", "price": 1500, "emoji": "🥤", "category": "음료"},
        {"name": "과자", "price": 2000, "emoji": "🍪", "category": "간식"},
        {"name": "여행용 티슈", "price": 1000, "emoji": "🧻", "category": "필수품"},
        {"name": "기념품 자석", "price": 5000, "emoji": "🧲", "category": "기념품"},
        {"name": "즉석카메라 필름", "price": 12000, "emoji": "📸", "category": "취미"},
    ],
    "캠핑": [
        {"name": "삼겹살(300g)", "price": 12000, "emoji": "🥩", "category": "식사"},
        {"name": "상추/깻잎", "price": 3000, "emoji": "🥬", "category": "식사"},
        {"name": "라면(5개)", "price": 4500, "emoji": "🍜", "category": "식사"},
        {"name": "마시멜로", "price": 3000, "emoji": "🍡", "category": "간식"},
        {"name": "장작", "price": 8000, "emoji": "🪵", "category": "도구"},
        {"name": "부탄가스", "price": 2000, "emoji": "🔥", "category": "도구"},
        {"name": "일회용 접시", "price": 2000, "emoji": "🍽️", "category": "도구"},
        {"name": "물(2L)", "price": 1500, "emoji": "💧", "category": "음료"},
    ],
    "요리": [
        {"name": "소고기(국거리)", "price": 10000, "emoji": "🥩", "category": "재료"},
        {"name": "자른 미역", "price": 3000, "emoji": "🌿", "category": "재료"},
        {"name": "두부", "price": 1500, "emoji": "🧊", "category": "재료"},
        {"name": "케이크(조각)", "price": 6000, "emoji": "🍰", "category": "디저트"},
        {"name": "꽃다발", "price": 15000, "emoji": "💐", "category": "선물"},
        {"name": "잡채용 당면", "price": 4000, "emoji": "🍝", "category": "재료"},
        {"name": "시금치", "price": 2500, "emoji": "🥬", "category": "재료"},
        {"name": "생일 초", "price": 1000, "emoji": "🕯️", "category": "기타"},
    ]
}
