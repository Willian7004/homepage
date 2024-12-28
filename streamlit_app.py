import streamlit as st

st.title("首页")
st.sidebar.title("首页")
st.sidebar.write("1.创建本项目的原因")
st.write("本项目是我的个人主页，用于分享一些文章和我创建的其它网页，主要面向我在GitHub的观众和其他对软件/硬件领域有兴趣的观众。我在GitHub的名称是Willian7004，在创建时笔误了，我创建的网页的域名中会使用William7004的名称。")
st.write("本项目各页面分别讨论不同话题并持续更新，在更新中会删减过时内容。在边栏中选择其它页面，页面宽度较小时需要通过右上角的Menu按钮展开边栏。")
st.subheader("1.创建本项目的原因", divider=True)
st.write("我此前发布的文字内容主要位于知乎和CSDN，知乎把回答内容也一起显示会比较碎片化，CSDN由于过度商业化的问题已弃用。")
st.write("在社交平台发布的文章受审核机制影响，在我遇到的情况中，介绍自己用过的硬件可能被认为是广告，而在对于广告管理不严的平台中软广会挤占真实体验的热度。")
st.write("本项目采用通过一个页面展示一个话题并持续更新的形式，在社交平台难以保持热度。")
st.subheader("2.我的项目", divider=True)
st.write("Github仓库：https://github.com/Willian7004 这里不另外介绍单独的仓库，后面的文章中会提及部分仓库。以下为部署在Streamlit Cloud的项目：")
st.write("AI-note项目，用于记录当前各类AI模型中有优势的模型、相关运行案例、我对AI推理硬件方案的考虑以及对AI模型发展路线的看法：https://william7004-ai-note.streamlit.app")

