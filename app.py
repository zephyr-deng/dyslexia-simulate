import streamlit as st
import random

# 页面基础配置，美化界面
st.set_page_config(page_title="阅读障碍模拟工具", layout="wide")

# 页面标题
st.title("📖 阅读障碍视觉模拟系统")
st.caption("Streamlit 一小时挑战项目")

# 侧边滑块：调节障碍效果严重程度
strength = st.slider("调节障碍效果强度", min_value=1, max_value=5, value=3)

# 文本输入框
original_text = st.text_area(
    "请输入需要模拟的文字内容",
    placeholder="在这里输入你想要测试的段落文字...",
    height=250
)

# 核心：阅读障碍文字效果处理函数
def dyslexia_effect(text, level):
    if not text:
        return ""
    result = []
    # 根据滑动条强度，计算字符扭曲概率
    change_prob = 0.12 * level

    for char in text:
        # 空格、换行全部保留，不做修改
        if char.isspace():
            result.append(char)
            continue
        
        rand = random.random()
        # 效果1：字符上下轻微跳动偏移
        if rand < change_prob * 0.4:
            offset = random.randint(-4, 4)
            char = f'<span style="position:relative;top:{offset}px">{char}</span>'
        # 效果2：字符透明度模糊
        elif rand < change_prob * 0.8:
            opacity = round(0.4 + random.random() * 0.5, 2)
            char = f'<span style="opacity:{opacity}">{char}</span>'
        # 效果3：字间距错乱挤压/拉开
        elif rand < change_prob:
            space = random.randint(1, 5)
            char = f'<span style="letter-spacing:{space}px">{char}</span>'
        
        result.append(char)
    return "".join(result)

# 生成按钮
if st.button("开始生成模拟效果", type="primary"):
    # 左右分栏对比展示
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ 普通人正常阅读视角")
        st.write(original_text)
    with col2:
        st.subheader("🔴 阅读障碍人群视觉视角")
        dyslexia_text = dyslexia_effect(original_text, strength)
        # 安全渲染HTML样式，实现视觉扭曲效果
        st.markdown(dyslexia_text, unsafe_allow_html=True)