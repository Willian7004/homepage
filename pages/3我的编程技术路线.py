import streamlit as st

st.title("我的编程技术路线")
st.sidebar.title("我的编程技术路线")
st.sidebar.write("1.始于课程")
st.sidebar.write("2.兴于嵌入式")
st.sidebar.write("3.陷于桌面")
st.sidebar.write("4.盛于AI")
st.sidebar.write("5.终于电路")
st.subheader("1.始于课程", divider=True)
st.write("我接触编程也是在课程中。当时有一个C语言课程，我在学习课程内容的同时也对见到的程序进行一些改进，这部分项目发布在https://github.com/Willian7004/William-7004-C-Programs 。由于相关例程较少，后来就没有开发C语言桌面程序。")
st.write("我在另一个课程接触了用于机器人开发的ROS系统，尝试了相关例程，还接触了OpenCV，由于开发流程较为复杂并且难以开发解决生活中的问题的程序，后来也基本没有开发了。")
st.subheader("2.兴于嵌入式", divider=True)
st.write("我在嵌入式领域最早因科研团队考核接触了stm32，基于例程做了不少新的程序。但由于stm32的库文件引入和引脚设定等较为复杂，开发内容没有明显超出例程的范围。这部分项目根据开发板型号，分别发布在https://github.com/Willian7004/Programs-for-STM32F103C6T6和https://github.com/Willian7004/Programs-for-STM32F103RCT6。")
st.write("为了开发更多项目，我接触了更容易开发的MicroPython，硬件为ESP32。MicroPython本身的功能远比C语言丰富，在用过ESP32的较大的版本甚至有HTML服务器功能，需要外设时直接上传相应库文件就能使用，并且Python的语法更为简洁，因此这段时间是我开发新项目最为频繁的时期。相关项目上传到https://github.com/Willian7004/Programs-for-ESP32-MicroPython- 。")
st.write("这一时期我也做了其它的一些项目，包括接触MicroPython后进一步了解Python做出的Python桌面项目，在https://github.com/Willian7004/Python-Programs-of-William7004 仓库较早的部分。为了提高程序可读性、使用高集成度单片机和使用更为方便的图片、字体转换功能接触了Scratch的嵌入式开发，项目发布到https://github.com/Willian7004/ESP32-Arduino-Mind- 。为了进一步了解Scratch的功能接触了Scratch的桌面开发，项目发布到https://github.com/Willian7004/Scratch-Programs ，转换为HTML的版本发布在https://github.com/Willian7004/HTML-Programs 仓库的Scratch项目。")
st.subheader("3.陷于桌面", divider=True)
st.write("我在嵌入式开发后期，由于已使用过绝大多数类型的硬件，后续开发空间不大，并且在图形界面和HTML服务器方面的项目遇到明显的性能瓶颈，就决定进一步了解桌面开发。刚开始继续从之前熟悉的Runoob学习了大量Python库，包括Numpy、Scipy、Matplotlib和Pandas，但都缺少开发自己的程序的灵感。")
st.write("后来希望了解图形界面开发，想到很多程序是基于web的，就在Runoob学习了HTML、CSS和JavaScript，开发了少量项目，在https://github.com/Willian7004/HTML-Programs 仓库较早的部分。由于纯HTML开发较为繁琐，后面又在Runoob学习了AngularJS、Vue、Chart.js、Ionic，还从官方文档学习了three.js，由于开发流程仍较为复杂，基本没有开发新的项目。")
st.subheader("4.盛于AI", divider=True)
st.write("我在Ollama发布0.1版本时就开始部署AI模型，之前部署过Qwen1.5 7b和14b版本，后来Qwen2发布，72b版本性能接近GPT4，实测可靠性也较高，就尝试用来开发一些我尚不了解相关api或开发繁琐的项目，包括https://github.com/Willian7004/Python-Programs-of-William7004 和https://github.com/Willian7004/HTML-Programs 仓库后面的部分。")
st.write("此前部署Qwen2 72b是本地运行，大部分层加载在CPU，速度很慢。后面发布的Deepseek Coder v2编程能力更高，定价低并且网页版免费，就改用Deepseek Coder v2进行开发。开发时也开始尝试在一个程序中实现多个步骤，比较有代表性的是RSS总结项目，发布在https://github.com/Willian7004/Python-Programs-of-William7004/blob/main/rss%E6%80%BB%E7%BB%93%EF%BC%88%E5%8D%95%E6%96%87%E4%BB%B6%EF%BC%89.py 。我在仓库中也给出了提示词方便参考。尝试复杂提示词后又开发了一些包含多个程序的项目，均为AI应用，包括https://github.com/Willian7004/LLM-Code-Tools 、https://github.com/Willian7004/LLM-Document-Tools 、https://github.com/Willian7004/LLM-novel-writer/tree/v0.9 。这部分应用也表现了当时我对于AI应用的探索。")
st.write("近期我进行编程也有一些新的方向。一方面转向语法简单并且我更为熟悉的的Python语言，学习了Streamlit和NiceGUI用于快速制作网页。另一方面新出现的思维链模型具有更高的编程能力，可以尝试在提示词中描述程序功能而非具体步骤以节省开发时间。")
st.subheader("5.终于电路", divider=True)
st.write("考虑到使用大量编程语言在语法上容易造成混淆，除c语言和python外基本都不使用了。后来因为希望了解电路设计，参加了一生一芯项目，接触到了Verilog和Chisel。Verilog在风格上接近c语言，而Chisel是Java风格的，又考虑到语法复杂度和部署难度等因素，选择使用Verilog作为我进行电路设计的主要编程语言。考虑到语法混淆问题，短期内也不会大规模使用其它编程语言了。")