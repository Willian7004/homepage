import streamlit as st

st.title("电脑性能与二手硬件杂谈")
st.sidebar.title("电脑性能与二手硬件杂谈")
st.sidebar.write("1.本代游戏环境：钉子户与渣优化齐聚")
st.sidebar.write("2.DCC软件：性能需求上限高")
st.sidebar.write("3.二手GPU：矿卡崛起、计算卡衰落")
st.sidebar.write("4.二手CPU：从E5 v3到EPYC二代")
st.sidebar.write("5.关于低功耗处理器")
st.subheader("1.本代游戏环境：钉子户与渣优化齐聚", divider=True)
st.write("我第一台电脑也就是现在用的电脑GPU为RTX3070m，CPU为5600h，屏幕用了2.5k 165hz的。虽然时间上是本世代，但我也玩过不少上世代的游戏。我选择游戏时，画质是一大门槛。刺客信条：奥德赛、泰坦陨落2、极限竞速：地平线4这个级别的游戏全高画质能达到45帧以上，在2.5k屏幕上也达到了比较好的画质表现。")
st.write("本世代初期比较优秀的游戏，例如极限竞速：地平线5、光环：无限、超级房车赛：传奇和影子武士3，由于制作基准提高，比上世代后期的游戏光照更为真实，而性能要求基本一致。本世代也有不少表现较差的游戏，例如星空的优化问题和龙腾世纪：影障守护者的DEI问题导致不少投入大量资源制作的游戏变得不适合玩。后面的讨论排除这部分游戏。")
st.write("本世代部分游戏开始使用全局动态光照，常见的实现方式包括光线追踪和Lumen。Lumen是虚幻5的渲染器，虽然不少人认为难优化，但瘟疫传说：安魂曲等游戏在使用虚幻5的情况下仍有比较好的优化表现。目前大部分使用光线追踪的游戏把部分提升明显的渲染管线改用光线追踪，例如幽灵线：东京，这部分游戏因为开启光线追踪时帧率下降较大，关闭光线追踪时光照不如之前使用光栅的游戏而受到批评，不过也不排除光源复杂的情况下光线追踪的画质表现优于Lumen（这一问题还没有定论，不过根据我在Twinmotion的测试可能成立）。另外，一些游戏为了达到更好的光照效果，提供把所有渲染管线改用光线追踪的选项，称为路径追踪。这部分游戏包括赛博朋克2077和心灵杀手2 等，虽然效果略有提升但在目前的硬件条件下性价比不如前面两种渲染管线。")
st.write("到了本世代中期，一些游戏开始尝试更高的画质，但由于画面解析度此前已达到上限，在本世代渲染基准下实际画质提升空间不大。如果降到相当于实际画质上限的画质，并且使用帧生成，在相同硬件上能达到的帧率反而高于之前的游戏。以下是我使用黑神话：悟空测试工具的测试结果：")
st.image("files/wukong.jpg")
st.write("总的来说，本世代如果不无脑开最高画质、只玩优化水平正常的游戏的话，根据对帧率的要求不同已经有不少硬件能成为钉子户了。")
st.subheader("2.DCC软件：性能需求上限高", divider=True)
st.write("虽然前面提到本世代游戏解析度到达上限，但这主要受到本世代开发基准限制，在DCC软件中可以使用更高面数。游戏中同时加载的面数较多的有数百万面，而在DCC软件中由于可以使用更高精度的模型，我制作的场景一般在一千到三千万面，在电影制作中一个模型能达到数亿面。加载更多面的显存要求和渲染的算力消耗会提高。我在虚幻5使用Megascans资源制作了一些场景，实时运行帧率约为7帧，如果使用高端卡能流畅运行，但高端电脑也可以制作更大的场景以及提高模型精度。")
st.image("files/UE5_1.jpg")
st.image("files/UE5_2.jpg")
st.image("files/UE5_3.jpg")
st.subheader("3.二手GPU：矿卡崛起、计算卡衰落", divider=True)
st.write("二手硬件市场是长期存在的，我在接触“垃圾佬”文化后，更偏向性价比有明显优势的硬件。")
st.write("曾经有性价比优势的二手GPU是英伟达Tesla系列的计算卡。当时AI绘画模型开始流行而显存优化措施较少，就有不少人入手显存大的Tesla m40等计算卡。由于热度上升使这部分计算卡价格上升，并且这部分计算卡对低精度计算支持较差，性价比优势逐渐消失。")
st.write("随着矿潮结束，大量矿卡流入二手市场，部分加密货币也禁止GPU挖矿,也带来了一些性价比优势明显的GPU，比较有代表性的有RX580、P106和40hx等型号，虽然矿卡可靠性较差，但在低端DIY电脑中比较有优势。其它GPU受二手市场和AI热度的影响，特别是大显存和低精度算力高的适合AI应用的GPU性价比优势不大。")
st.subheader("4.二手CPU：从E5 v3到EPYC二代", divider=True)
st.write("相比二手GPU，二手服务器CPU容易获得性价比优势，这是因为偏向多核性能的CPU不适合常规桌面应用和游戏以及受AI影响较小。")
st.write("二手CPU中最热门的是英特尔至强E5 v3系列，双路多核性能上限大致相当于AMD 5950x或英特尔12900k，第三方的主板和散热器等配件也比较完善。相比E5 v4系列，由于兼容ddr3内存，能降低内存成本。相比消费级处理器，有更多的内存通道（双路共8通道）和Pcie通道，扩展内存和存储空间比较方便，也可以提高内存和硬盘的总速度。以下是官网上该系列的所有CPU，可以根据内核数和频率推测实际性能")
st.image("files/e5v3.jpeg")
st.write("如果对性能和内存带宽要求更高甚至代替GPU用于AI应用，AMD EPYC二代是比较好的选择，虽然受缺少第三方主板、无锁CPU较少等问题影响，组双路最低也要接近主流配置电脑的价格，但在对CPU性能要求较高的应用中有优势，双路能达到400g带宽。在AI应用中对比GPU，其中性能最高的方案是使用双路共128核的7742，性能相当于RTX3090。接近主流价位的方案有双路共64核的7502（性能相当于2070Super）以及双路96核但内存带宽少25%的7k62（性能相当于2080ti）。以下是官网上该系列所有CPU（7k62是厂商特供型号，不在官方列表）")
st.image("files/epyc7002.jpeg")
st.write("对于性能要求不高的使用场景，二手CPU也有其它方案。希望用低成本运行主流桌面程序特别是需要核显时可以选至强E3 v3系列，性能略高于第九代酷睿i3。用于低功耗场景可以考虑瘦客户机。我入手了一台瘦客户机作为Linux物理机，在前面的Linux部分有详细说明。")
st.subheader("5.关于低功耗处理器", divider=True)
st.write("热度相对较高的低功耗处理器有j1800、j4100、n100等型号，这些处理器TDP在10w以内，适合用于NAS或家庭服务器。需要注意的是，n100由于用了大小核架构中的小核，核间延迟较高，实际表现反而不如上一代的n5095。以后最低就只能考虑15w级别的了。")
st.write("考虑到大小核的兼容性问题，我目前只了解了锐龙系列中的型号。低成本的选择有3500u，高性能的选择有6800u。6800u的性能大约是3500u的3倍，比7840hs低大约1/3，核显性能相当于1050ti。与手机处理器对比，性能相当于8gen3，功耗高一些。")
st.write("如果用于笔记本电脑，使用TDP在28到45w的移动端标压处理器可以做到比较好的散热和续航表现，但用于掌机的话还是需要低压处理器才能在控制重量的情况下达到较好的续航（参考AYANEO AIR Plus，使用6英寸屏幕、46.2Wh电池，重量525g）。")
