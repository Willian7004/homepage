本项目使用Streamlit创建，用于发布我的一些文章和创建的网页，主要面向我在GitHub的观众和其他对软件/硬件领域有兴趣的观众。
本项目已在Streamlit Cloud部署，域名为https://william7004-homepage.streamlit.app
本项目使用release记录更改，此前每创建新文章都发布release，会导致发布过于频繁。考虑到git具有记录更改的功能，后续改为每月发布release。
本地部署流程

建议使用Python=3.10环境

1.安装依赖
pip install -r requirements.txt

2.运行应用

streamlit run streamlit_app.py
