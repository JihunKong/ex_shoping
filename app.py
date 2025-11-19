import streamlit as st
import time
from data import MISSIONS, PRODUCTS
from utils import calculate_total, get_ai_feedback

# Page Config
st.set_page_config(
    page_title="슬기로운 소비 생활",
    page_icon="🛒",
    layout="centered"
)

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    .mission-card {
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #f0f2f6;
        text-align: center;
        margin-bottom: 10px;
        cursor: pointer;
    }
    .mission-card:hover {
        border-color: #ff4b4b;
        background-color: #fff9f9;
    }
    .price-tag {
        font-size: 1.2em;
        font-weight: bold;
        color: #2c3e50;
    }
    .total-display {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 999;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'mission' not in st.session_state:
    st.session_state.mission = None

def navigate_to(page):
    st.session_state.page = page
    st.rerun()

def add_to_cart(item):
    # Check if item already in cart
    for cart_item in st.session_state.cart:
        if cart_item['name'] == item['name']:
            cart_item['quantity'] += 1
            return
    # Add new item
    new_item = item.copy()
    new_item['quantity'] = 1
    st.session_state.cart.append(new_item)

def remove_from_cart(item_name):
    st.session_state.cart = [item for item in st.session_state.cart if item['name'] != item_name]

def update_quantity(item_name, change):
    for item in st.session_state.cart:
        if item['name'] == item_name:
            item['quantity'] += change
            if item['quantity'] <= 0:
                remove_from_cart(item_name)
            return

# --- Page 1: Start Screen ---
if st.session_state.page == 'start':
    st.title("🛒 슬기로운 소비 생활")
    st.subheader("오늘의 장보기 미션을 선택해주세요!")
    st.write("3만원으로 가장 합리적인 소비를 해볼까요?")

    col1, col2, col3 = st.columns(3)
    
    missions_list = list(MISSIONS.items())
    
    with col1:
        st.info(f"**{missions_list[0][0]}**\n\n{missions_list[0][1]['emoji']}")
        if st.button("선택하기", key="m1"):
            st.session_state.mission = missions_list[0][0]
            st.session_state.cart = []
            navigate_to('shop')
            
    with col2:
        st.success(f"**{missions_list[1][0]}**\n\n{missions_list[1][1]['emoji']}")
        if st.button("선택하기", key="m2"):
            st.session_state.mission = missions_list[1][0]
            st.session_state.cart = []
            navigate_to('shop')

    with col3:
        st.warning(f"**{missions_list[2][0]}**\n\n{missions_list[2][1]['emoji']}")
        if st.button("선택하기", key="m3"):
            st.session_state.mission = missions_list[2][0]
            st.session_state.cart = []
            navigate_to('shop')

    st.markdown("---")
    st.caption("초등학생을 위한 경제 교육 앱입니다.")

# --- Page 2: Shopping Screen ---
elif st.session_state.page == 'shop':
    mission_name = st.session_state.mission
    mission_data = MISSIONS[mission_name]
    budget = mission_data['budget']
    
    # Sidebar for Cart
    with st.sidebar:
        st.header(f"{mission_data['emoji']} 장바구니")
        current_total = calculate_total(st.session_state.cart)
        
        if not st.session_state.cart:
            st.write("장바구니가 비었습니다.")
        else:
            for item in st.session_state.cart:
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.write(f"{item['emoji']} {item['name']}")
                    st.caption(f"{item['price']:,}원 x {item['quantity']}")
                with c2:
                    if st.button("➕", key=f"add_{item['name']}"):
                        update_quantity(item['name'], 1)
                        st.rerun()
                with c3:
                    if st.button("➖", key=f"sub_{item['name']}"):
                        update_quantity(item['name'], -1)
                        st.rerun()
            
            st.divider()
            st.metric("총 합계", f"{current_total:,}원")
            
            remaining = budget - current_total
            if remaining < 0:
                st.error(f"예산 초과! ({remaining:,}원)")
            else:
                st.success(f"남은 돈: {remaining:,}원")

        if st.button("계산하러 가기 💳", type="primary"):
            if current_total > budget:
                st.toast("예산을 초과했습니다! 물건을 조금 덜어내주세요.", icon="⚠️")
            elif current_total == 0:
                st.toast("장바구니가 비어있습니다!", icon="⚠️")
            else:
                navigate_to('result')
        
        if st.button("처음으로 돌아가기"):
            navigate_to('start')

    # Main Content
    st.title(f"🛒 {mission_name} 장보기")
    st.info(mission_data['description'])
    
    # Progress bar for budget
    progress = min(current_total / budget, 1.0)
    st.progress(progress, text=f"예산 사용률: {int(progress*100)}%")

    st.subheader("물건 목록")
    
    products = PRODUCTS[mission_name]
    
    # Grid layout for products
    cols = st.columns(2)
    for idx, product in enumerate(products):
        with cols[idx % 2]:
            with st.container(border=True):
                # Display large emoji instead of external image for instant loading and cute look
                st.markdown(f"<div style='text-align: center; font-size: 80px; margin-bottom: 10px;'>{product['emoji']}</div>", unsafe_allow_html=True)
                st.markdown(f"### {product['name']}")
                st.write(f"**{product['price']:,}원**")
                st.caption(product['category'])
                if st.button("담기", key=f"prod_{idx}"):
                    add_to_cart(product)
                    st.rerun()

# --- Page 3: Result Screen ---
elif st.session_state.page == 'result':
    st.title("🧾 영수증 리뷰")
    
    mission_name = st.session_state.mission
    budget = MISSIONS[mission_name]['budget']
    total_spent = calculate_total(st.session_state.cart)
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("나의 예산", f"{budget:,}원")
    with c2:
        st.metric("총 지출", f"{total_spent:,}원", delta=budget-total_spent)
        
    st.divider()
    
    st.subheader("🤖 AI 선생님의 평가")
    
    if 'feedback_generated' not in st.session_state:
        with st.spinner("AI 선생님이 장바구니를 확인하고 있어요..."):
            feedback_stream = get_ai_feedback(mission_name, st.session_state.cart, budget, total_spent)
            st.write_stream(feedback_stream)
            st.session_state.feedback_generated = True
    else:
        # Re-generate button if needed, or just show a message that it's done. 
        # Since we streamed it, we can't easily persist the stream content without capturing it.
        # For simplicity in this version, we'll just let it re-generate if they refresh, 
        # or we could store the full text. 
        # Given the constraints, let's just allow re-generation or simple "Done".
        st.info("평가가 완료되었습니다! 다시 하려면 아래 버튼을 눌러주세요.")

    st.divider()
    if st.button("다시 시작하기 🔄", type="primary"):
        st.session_state.page = 'start'
        st.session_state.cart = []
        st.session_state.mission = None
        if 'feedback_generated' in st.session_state:
            del st.session_state.feedback_generated
        st.rerun()
