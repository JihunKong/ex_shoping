import streamlit as st
from openai import OpenAI
import os

def calculate_total(cart):
    """Calculates the total price of items in the cart."""
    total = 0
    for item in cart:
        total += item['price'] * item['quantity']
    return total

def get_ai_feedback(mission_name, cart, budget, total_spent):
    """
    Generates feedback using OpenAI API based on the user's shopping list.
    """
    api_key = os.environ.get("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
    
    if not api_key:
        return "⚠️ OpenAI API 키가 설정되지 않았습니다. 환경 변수나 secrets.toml을 확인해주세요."

    client = OpenAI(api_key=api_key)

    # Construct the prompt
    cart_items_str = ", ".join([f"{item['name']}({item['quantity']}개)" for item in cart])
    
    prompt = f"""
    당신은 초등학생들에게 합리적인 소비를 가르쳐주는 친절한 선생님입니다.
    학생이 '{mission_name}' 미션을 수행하기 위해 30,000원 예산으로 쇼핑을 했습니다.
    
    [쇼핑 목록]
    {cart_items_str}
    
    [총 지출]
    {total_spent}원 (예산: {budget}원)
    
    학생의 소비가 합리적이었는지, 미션에 적합한 물건을 샀는지 평가해주세요.
    칭찬할 점과 아쉬운 점을 부드러운 말투로 설명해주세요. 
    이모지를 적절히 사용하여 아이들이 읽기 좋게 해주세요.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 초등학생을 위한 경제 교육 선생님입니다."},
                {"role": "user", "content": prompt}
            ],
            stream=True,
        )
        return response
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"
