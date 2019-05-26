from io import BytesIO
from PIL import Image,ImageTk
import folium
import urllib.request
import xml.etree.ElementTree as etree
from tkinter import *
from tkinter import font
import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("1080x600+250+100")
photo = PhotoImage(file="kpu_logo_2.gif")
DataList=[]
ToiletNmList=[]

def initTopText():
    tempFont = font.Font(g_Tk, size=20, weight='bold', family='consolas')
    MainText = Label(g_Tk, font=tempFont, text="[경기도 화장실 정보 App]",width=25,borderwidth=12,relief='ridge')
    MainText.pack()
    MainText.place(x=5)
def initToiletListBox():
    global ToiletBox
    ToiletBoxScrollBar = Scrollbar(g_Tk)
    ToiletBoxScrollBar.pack()
    ToiletBoxScrollBar.place(x=525,y=235)
    tempFont = font.Font(g_Tk, size=15, weight='bold', family='consolas')
    ToiletBox = Listbox(g_Tk,font=tempFont, activestyle='none', width=45,height=15,borderwidth=12,relief='ridge', yscrollcommand=ToiletBoxScrollBar.set)
    ToiletBox.pack()
    ToiletBox.place(x=5, y=165)
    ToiletBoxScrollBar.config(command=ToiletBox.yview)
def initSearchListBox():
    global SearchListBox
    ListBoxScrollBar = Scrollbar(g_Tk)
    ListBoxScrollBar.pack()
    ListBoxScrollBar.place(x=150,y=60)
    tempFont = font.Font(g_Tk, size=15,weight='bold',family='consolas')
    SearchListBox = Listbox(g_Tk,font=tempFont, activestyle='none', width=10,height=1,borderwidth=12,relief='ridge', yscrollcommand=ListBoxScrollBar.set)
    SearchListBox.insert(1, "남성용 정보")
    SearchListBox.insert(2, "여성용 정보")
    SearchListBox.insert(3, "위치 정보")
    SearchListBox.pack()
    SearchListBox.place(x=5, y=60)
    ListBoxScrollBar.config(command=SearchListBox.yview)
def initInputPic():
    global InputPic
    InputPic = Label(g_Tk, image=photo, borderwidth=5,relief='ridge')
    InputPic.pack()
    InputPic.place(x=392, y=0)
def initInputLabel():
    global InputLabel
    tempFont = font.Font(g_Tk, size=18,weight='bold',family='consolas')
    InputLabel = Entry(g_Tk,font=tempFont,width=38,borderwidth=12,relief='ridge')
    InputLabel.pack()
    InputLabel.place(x=5,y=110)
def initToiletButton():
    tempFont = font.Font(g_Tk, size=15,weight='bold',family='consolas')
    SearchButton = Button(g_Tk,font=tempFont,text="확인",command=ToiletButtonAction, borderwidth=12,relief='ridge')
    SearchButton.pack()
    SearchButton.place(x=525,y=165)
def initSearchButton():
    tempFont = font.Font(g_Tk, size=15,weight='bold',family='consolas')
    SearchButton = Button(g_Tk,font=tempFont,text="검색",command=SearchButtonAction, borderwidth=12,relief='ridge')
    SearchButton.pack()
    SearchButton.place(x=525,y=105)
def initBookmarkin_Button():
    tempFont = font.Font(g_Tk, size=13, weight='bold', family='consolas')
    Bookmarkin_Button = Button(g_Tk, font=tempFont, text="IN 북마크", command= BookmarkinAction, borderwidth=12,relief='ridge')
    Bookmarkin_Button.pack()
    Bookmarkin_Button.place(x=605)
def initBookmarkout_Button():
    tempFont = font.Font(g_Tk, size=13, weight='bold', family='consolas')
    Bookmarkout_Button = Button(g_Tk, font=tempFont, text="OUT 북마크", command= BookmarkoutAction, borderwidth=12,relief='ridge')
    Bookmarkout_Button.pack()
    Bookmarkout_Button.place(x=715)
def initMailButton():
    tempFont = font.Font(g_Tk, size=13,weight='bold',family='consolas')
    SearchButton = Button(g_Tk,font=tempFont,text="Email",command=MailButtonAction, borderwidth=12,relief='ridge')
    SearchButton.pack()
    SearchButton.place(x=835)
def initGraphButton():
    tempFont = font.Font(g_Tk, size=13,weight='bold',family='consolas')
    SearchButton = Button(g_Tk,font=tempFont,text="그래프 그리기",command=GraphButtonAction, borderwidth=12,relief='ridge')
    SearchButton.pack()
    SearchButton.place(x=915)
def initRenderText():
    global RenderText
    RenderTextScrollBar = Scrollbar(g_Tk)
    RenderTextScrollBar.pack()
    RenderTextScrollBar.place(x=400,y=200)

    tempFont = font.Font(g_Tk, size=15, weight='bold', family='consolas')
    RenderText = Text(g_Tk,width=61,height=15, borderwidth=12,relief='ridge',yscrollcommand=RenderTextScrollBar.set)
    RenderText.pack()
    RenderText.place(x=605,y=60)
    RenderTextScrollBar.config(command=RenderText.yview)
    RenderTextScrollBar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')
def GraphButtonAction():
    pass
def MailButtonAction():
    pass
def ToiletButtonAction():
    global ToiletBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    isSearchindex = ToiletBox.curselection()[0]
    if isSearchindex == 0:
        ManInfo()
    elif isSearchindex == 1:
        WomanInfo()
    elif isSearchindex == 2:
        LocalInfo()
def SearchButtonAction():
    global SearhListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    isSearchindex = SearchListBox.curselection()[0]
    if isSearchindex == 0:
        ManInfo()
    elif isSearchindex == 1:
        WomanInfo()
    elif isSearchindex == 2:
        LocalInfo()
    RenderText.configure(state='disabled')
def BookmarkinAction():
    pass
def BookmarkoutAction():
    pass
def ManInfo():
    where = InputLabel.get()
    hangul_utf8 = urllib.parse.quote(where)
    print(where, hangul_utf8)

    key = "225d1f29c04841e8897b5d7508abb557"
    url = 'https://openapi.gg.go.kr/Publtolt'+'?SIGUN_NM='+hangul_utf8
    print("key를 통해 url에 접속중..")
    data = urllib.request.urlopen(url).read()
    print("읽기 성공")
    f = open("TEST.xml", "wb")
    f.write(data)
    f.close()
    print("XML 작성 \n")

    tree = etree.parse('TEST.xml')
    root = tree.getroot()

    for a in root.findall('row'):
        ToiletNmList.append(a.findtext('PBCTLT_PLC_NM'))
        DataList.append(a.findtext('PBCTLT_PLC_NM')) #화장실 명
        DataList.append(a.findtext('REFINE_LOTNO_ADDR')) #소재지 지번주소
        DataList.append(a.findtext('OPEN_TM_INFO')) #개방시간

        DataList.append(a.findtext('MALE_FEMALE_TOILET_YN')) #남녀공용화장실
        DataList.append(a.findtext('MALE_WTRCLS_CNT')) #남성용 대변기
        DataList.append(a.findtext('MALE_UIL_CNT')) #남성용 소변기
        DataList.append(a.findtext('MALE_DSPSN_WTRCLS_CNT')) #남성용 장애인 대변기
        DataList.append(a.findtext('MALE_DSPSN_UIL_CNT')) #남성용 장애인 소변기
        DataList.append(a.findtext('MALE_CHILDUSE_WTRCLS_CNT')) #남성용 어린이 대변기
        DataList.append(a.findtext('MALE_CHILDUSE_UIL_CNT')) #남성용 어린이 소변기

    for i in range(len(ToiletNmList)):
        ToiletBox.insert(i, ToiletNmList[i])

    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "화장실 명: ")
        RenderText.insert(INSERT, DataList[i*10])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "지번 주소: ")
        RenderText.insert(INSERT, DataList[i*10 +1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "개방 시간: ")
        RenderText.insert(INSERT, DataList[i*10 +2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "남녀 공용화장실 여부: ")
        RenderText.insert(INSERT, DataList[i*10 +3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "남성용 대변기 갯수: ")
        RenderText.insert(INSERT, DataList[i*10 +4]+" ")
        RenderText.insert(INSERT, "/ 남성용 소변기 갯수: ")
        RenderText.insert(INSERT, DataList[i * 10 + 5])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "장애인 남성용 대변기 갯수: ")
        RenderText.insert(INSERT, DataList[i*10 +6]+" ")
        RenderText.insert(INSERT, "/ 장애인 남성용 소변기 갯수: ")
        RenderText.insert(INSERT, DataList[i * 10 + 7])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "남아용 대변기 갯수: ")
        RenderText.insert(INSERT, DataList[i*10 +6]+" ")
        RenderText.insert(INSERT, "/ 남아용 소변기 갯수: ")
        RenderText.insert(INSERT, DataList[i * 10 + 7])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "\n\n")
def WomanInfo():
    where = InputLabel.get()
    hangul_utf8 = urllib.parse.quote(where)
    print(where, hangul_utf8)

    key = "225d1f29c04841e8897b5d7508abb557"
    url = 'https://openapi.gg.go.kr/Publtolt'+'?SIGUN_NM='+hangul_utf8
    print("key를 통해 url에 접속중..")
    data = urllib.request.urlopen(url).read()
    print("읽기 성공")
    f = open("TEST.xml", "wb")
    f.write(data)
    f.close()
    print("XML 작성 \n")

    tree = etree.parse('TEST.xml')
    root = tree.getroot()

    for a in root.findall('row'):
        DataList.append(a.findtext('PBCTLT_PLC_NM')) #화장실 명
        DataList.append(a.findtext('REFINE_LOTNO_ADDR')) #소재지 지번주소
        DataList.append(a.findtext('OPEN_TM_INFO')) #개방시간

        DataList.append(a.findtext('MALE_FEMALE_TOILET_YN')) #남녀공용화장실
        DataList.append(a.findtext('FEMALE_WTRCLS_CNT')) #여성용 대변기
        DataList.append(a.findtext('FEMALE_DSPSN_WTRCLS_CNT')) #여성용 장애인 대변기
        DataList.append(a.findtext('FEMALE_CHILDUSE_WTRCLS_CNT')) #여성용 어린이 대변기


    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "화장실 명: ")
        RenderText.insert(INSERT, DataList[i*7])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "지번 주소: ")
        RenderText.insert(INSERT, DataList[i*7 +1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "개방 시간: ")
        RenderText.insert(INSERT, DataList[i*7 +2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "남녀 공용화장실 여부: ")
        RenderText.insert(INSERT, DataList[i*7 +3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "여성용 대변기 갯수: ")
        RenderText.insert(INSERT, DataList[i*7 +4]+" ")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "장애인 여성용 대변기 갯수: ")
        RenderText.insert(INSERT, DataList[i*7 +5]+" ")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "여아용 대변기 갯수: ")
        RenderText.insert(INSERT, DataList[i*7 +6]+" ")
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "\n\n")
def LocalInfo():
    where = InputLabel.get()
    hangul_utf8 = urllib.parse.quote(where)
    print(where, hangul_utf8)

    key = "225d1f29c04841e8897b5d7508abb557"
    url = 'https://openapi.gg.go.kr/Publtolt'+'?SIGUN_NM='+hangul_utf8
    print("key를 통해 url에 접속중..")
    data = urllib.request.urlopen(url).read()
    print("읽기 성공")
    f = open("TEST.xml", "wb")
    f.write(data)
    f.close()
    print("XML 작성 \n")

    tree = etree.parse('TEST.xml')
    root = tree.getroot()

    for a in root.findall('row'):
        DataList.append(a.findtext('PBCTLT_PLC_NM')) #화장실 명
        DataList.append(a.findtext('REFINE_LOTNO_ADDR')) #소재지 지번주소
        DataList.append(a.findtext('REFINE_WGS84_LAT')) #위도
        DataList.append(a.findtext('REFINE_WGS84_LOGT')) #위도

    map_osm = folium.Map(location=[DataList[2], DataList[3]], zoom_start=12)
    for i in range(5):
        folium.Marker(location=[DataList[i*4+2], DataList[i*4+3]], popup=DataList[4*i]).add_to(map_osm)
    map_osm.save('osm.html')

initTopText()
initSearchListBox()
initInputLabel()
initSearchButton()
initInputPic()
initRenderText()
initGraphButton()
initMailButton()
initBookmarkin_Button()
initBookmarkout_Button()
initToiletListBox()
initToiletButton()


g_Tk.mainloop()

"""

"""