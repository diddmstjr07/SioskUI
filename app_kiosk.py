import flet as ft
from flet import View, RouteChangeEvent
import os
import random
import time
import ast
import re
import threading
import requests
import Siosk.package.download as download
from auto.clear_terminal import clear_terminal
from Siosk.package.TTS import TextToSpeech
from Siosk.package.scan import find_process_by_port_Voice
from Siosk.package.model import API
import asyncio
from pydub import AudioSegment
from pydub.playback import play

current_working_directory = os.path.abspath(".") + "/SioskUI"
drinks = ["Coffee", "Smoothe", "Beverage", "Tea", "Ade"]
ip_store = []

class UI:
    def __init__(self) -> None:
        self.TextToSpeech = TextToSpeech()
        self.sound = AudioSegment.from_file("assets/audio/click.wav", format="wav")
        while True:
            bool = input("Korean or English (한국어, 영어)? (K/E): ")
            if bool == "K" or bool == "k" or bool == "한국어" or bool == "Korean" or bool == "korean":
                os.system(clear_terminal())
                while True:
                    bool = input("시오스크 서버가(SioskServer) 본인 PC에서 실행중인가요? (Y/N): ")
                    if bool == "Y" or bool == "y" or bool == "Yes" or bool == "y":
                        ip_address = "127.0.0.1"
                        os.system(clear_terminal())
                        break
                    elif bool == "N" or bool == "n" or bool == "No" or bool == "no":
                        os.system(clear_terminal())
                        ip_address = input('\033[91m' + "[!중요!] " + '\033[0m' + "시오스크서버와 클라이언트 코드가 동일한 네트워크에 접속되어있어야합니다(와이파이)\n시오스크서버가(SioskServer) 실행중인 아이피 주소를 입력해주십시오. \n\nWindows인 경우, ipconfig \nMac OS인 경우, ifconfig\n\n새창 터미널에 입력하여 나온 192.168~~ 아이피 주소를 입력해주세요: ")
                        break
                    else:
                        print("Y 또는 N만 입력해주십시오")
                while True:
                    bool = input("TTS 오디오 초기화를 진행할까요? (Y 입력 권장) (Y/N): ")
                    if bool == "Y" or bool == "y" or bool == "Yes" or bool == "y":
                        os.system(clear_terminal())
                        asyncio.run(self.TextToSpeech.downloading())
                        break
                    elif bool == "N" or bool == "n" or bool == "No" or bool == "no":
                        os.system(clear_terminal())
                        break
                    else:
                        print("Please enter keyword Only Y or N")
                        os.system(clear_terminal())
                break

            elif bool == "E" or bool == "e" or bool == "English" or bool == "english" or bool == "영어":
                os.system(clear_terminal())
                while True:
                    bool = input("Is SioskServer is Running on your own PC? (Y/N): ")
                    if bool == "Y" or bool == "y" or bool == "Yes" or bool == "y":
                        ip_address = "127.0.0.1"
                        os.system(clear_terminal())
                        break
                    elif bool == "N" or bool == "n" or bool == "No" or bool == "no":
                        ip_address = input('\033[91m' + "[!IMPORTANT!] " + '\033[0m' + "Your Server and Client must be connected in same Network device (WIFI)\nlease type IP Address SioskServer is running. \n\nIf you Operating System is Windows, type 'ipconfig' in new window termial\nElse if Mac OS or Linux or System included in Uninx, type 'ifconfig' in new window termial\n\nPlease find texture start as 192.168~~ and type: ")
                        os.system(clear_terminal())
                        break
                    else:
                        print("Please enter keyword Only Y or N")
                while True:
                    bool = input("Initializing TTS audio? (Y Recommened) (Y/N): ")
                    if bool == "Y" or bool == "y" or bool == "Yes" or bool == "y":
                        os.system(clear_terminal())
                        asyncio.run(self.TextToSpeech.downloading())
                        break
                    elif bool == "N" or bool == "n" or bool == "No" or bool == "no":
                        os.system(clear_terminal())
                        break
                    else:
                        print("Please enter keyword Only Y or N")
                break
            else:
                print("Please enter keyword Only E or K")
        
        save_dir = "Siosk/package/" # Conversation.json이 있는지 확인하고 없으면 서버에서 다운로드
        download.download_file(file="conversation.json", save_dir=save_dir) # Conversation.json이 있는지 확인하고 없으면 서버에서 다운로드
        ip_store.append(ip_address)

        if ip_address == "127.0.0.1":
            bool_data = find_process_by_port_Voice(9460)
            if bool_data == True:
                self.api = API(
                    token="SioskKioskFixedTokenVerifyingTokenData",
                    url="http://" + ip_address
                )
            elif bool_data == False:
                self.api = API(
                    token="SioskKioskFixedTokenVerifyingTokenData",
                    url="https://anoask.site"
                )
        else:
            self.api = API(
                token="SioskKioskFixedTokenVerifyingTokenData",
                url="http://" + ip_address
            ) 
        self.api.preparing() # Mic selection, storing class elements declaring as instant variable

    def ask_res(self):
        while True:
            A = self.api.detecting() # As Thread run, detecting my voice and convert as text to get response of question
            if A == "결제페이지로 이동하겠습니다":
                print("Breaking")
                break

    def main(self, page: ft.Page):
        '''
        Kiosk, Siosk UI Version
        '''
        MENU = []
        Menu = []
        key_data = []
        data_arrange = []
        drink_items = [ 
            (f"coffee/iceamericano.png", "아이스 아메리카노\n3000원", "Coffee"),
            (f"coffee/younyu_latte.png", "연유 라테\n3000원", None),
            (f"coffee/kapuchino.png", "카푸치노\n3000원", None),
            (f"coffee/Hazelnut_Latte.png", "헤이즐넛 라테\n3000원", None),
            (f"coffee/Hazelnut_Americano.png", "헤이즐넛 아메리카노\n3000원", None),
            (f"coffee/Coldbrew_Latte.png", "콜드브루 라테\n3000원", None),
            (f"coffee/cold_brew_original.png", "콜드브루\n3000원", None),
            (f"coffee/Caramel_Macchiato.png", "카라멜 마키아또\n3000원", None),
            (f"coffee/Caffe_Mocha.png", "카페 모카\n3000원", None),
            (f"frappe/Mint_Frappe.png", "민트 프라페\n3000원", None),
            (f"frappe/Green_Tea_Frappe.png", "녹차 프라페\n3000원", "Smoothe"),
            (f"frappe/Unicorn_Frappe.png", "유니콘 프라페\n3000원", None),
            (f"pongcrush/Banana_Pongcrush.png", "바나나 퐁크러쉬\n3000원", "Beverage"),
            (f"pongcrush/Chocolate_Honey_Pong_Crush.png", "초콜릿허니 퐁크러쉬\n3000원", None),
            (f"pongcrush/Choux_Cream_Honey_Pong_Crush.png", "슈크림허니 퐁크러쉬\n3000원", None),
            (f"pongcrush/Plain_Pongcrush.png", "플래인 퐁크러쉬\n3000원", None),
            (f"pongcrush/Strawberry_pongcrush.png", "딸기 퐁크러쉬\n3000원", None),
            (f"pongcrush/Strawberry_Cookie_Frappe.png", "딸기쿠키 프라페\n3000원", None),
            (f"smoothie/Mango_Yogurt_Smoothie.png", "망고요거트 스무디\n3000원", None),
            (f"smoothie/Plain_Yogurt_Smoothie.png", "플래인요거트 스무디\n3000원", None),
            (f"smoothie/Strawberry_Yogurt_Smoothie.png", "딸기요거트 스무디\n3000원", None),
            (f"ade/Blue_Lemon_Ade.png", "블루 레몬에이드\n3000원", "Ade"),
            (f"ade/Cherry_Coke.png", "체리콕\n3000원", None),
            (f"ade/Grapefruit_Ade.png", "자몽 에이드\n3000원", None),
            (f"ade/Lemon_Ade.png", "레몬 에이드\n3000원", None),
            (f"ade/Lime_Mojito.png", "라임 모히또\n3000원", None),
            (f"ade/MEGA_Ade.png", "메가 에이드\n3000원", None),
            (f"tea/Hot_lemon_tea.png", "레몬차\n3000원", None),
            (f"tea/Applecitron_Tea.png", "사과 유자차\n3000원", "Tea"),
            (f"tea/Chamomile.png", "케모마일 차\n3000원", None),
            (f"tea/Green_Tea.png", "녹차\n3000원", None),
            (f"tea/Earl_Grey.png", "얼그레이\n3000원", None),
            (f"tea/Hot_Grapefruit_tea.png", "자몽차\n3000원", None),
        ]
        page.title = "시오스크"
        page.window_width = 700
        page.window_height = 1600
        # route_history = []

        def senior_mode(e):
            voice = threading.Thread(target=self.ask_res)
            voice.start()
            page.go('/siosk_order')
            voice.join()

        page.fonts = {
            "NanumGothic": "SioskUI/assets/fonts/NanumGothic-Bold.ttf"
        }

        img0 = ft.Image(
            src=f"{current_working_directory}/assets/images/logo/general.png",
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        )

        shadowed_img0 = ft.Container(
            img0,
            padding=10
        )
        width_ele = page.window_width
        height_ele = page.window_height

        img1 = ft.Image(
            src=f"{current_working_directory}/assets/images/logo/siosk.png",
            width=300,
            height=300,
            fit=ft.ImageFit.CONTAIN,
        )

        shadowed_img1 = ft.Container(
            img1,
            padding=10
        )

        def store_getting_lowdata(e, low_data):  # 로우 데이터 Insult를 하거나, Gettig(Polling)을 해주는 함수
            if e == 0:
                data_arrange.clear()
                data_arrange.append(low_data)
                print(data_arrange)
                print("data insulting")
                return None
            elif e == 1:
                try:
                    print("data getting")
                    print(data_arrange[0])
                    return data_arrange[0]
                except IndexError:
                    return None # 이부분은 개발이 완료되어지면 보안을 위해서 꼭 os._exit(0)으로 변환해주어야함.
                except Exception as e:
                    print(e)
            else:
                os._exit(0)

        def build_home_view():
            content0 = ft.Column(
                [
                    ft.Container(
                        shadowed_img0,
                        alignment=ft.alignment.center,
                        on_click=lambda _: page.go('/general_order')
                    ),
                    ft.Text(
                        "일반주문",
                        size=40,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.BLACK,
                        width=width_ele,
                        font_family="NanumGothic"
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )

            content1 = ft.Column(
                [
                    ft.Container(
                        shadowed_img1,
                        alignment=ft.alignment.center,
                        on_click=senior_mode
                    ),
                    ft.Text(
                        "노인주문",
                        size=40,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.BLACK,
                        width=width_ele,
                        font_family="NanumGothic"
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            )

            return View(
                route="/",
                controls=[
                    ft.Row(
                        [
                            # ft.Container(
                            #     ft.TextButton("admin", on_click=lambda _:page.go("/admininstrator_page")),
                            # ),
                            ft.Container(
                                content0,
                                bgcolor='#fefcf6',
                                border=None,
                                alignment=ft.alignment.center,
                                expand=True,
                            ),
                            ft.Container(
                                content1,
                                bgcolor='#e6d5b8',
                                border=None,
                                alignment=ft.alignment.center,
                                expand=True,
                            )
                        ],
                        spacing=0,
                        expand=True,
                    )
                ]
            )

        def build_general_order_view():
            def close_dlg(e):
                dlg_modal.open = False
                page.update()

            dlg_modal = ft.AlertDialog(
                modal=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    "메뉴를 적어도 한개 이상 선택해주세요", 
                    color='#55443d',
                    font_family="NanumGothic",
                ),
                actions=[
                    ft.TextButton(
                        "확인", 
                        on_click=close_dlg,
                        style=ft.ButtonStyle(
                            color=ft.colors.BLACK,
                        )
                    ),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )

            def open_dlg_modal(e):
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()
            
            def rnd():
                for _ in range(len(drinks)):
                    key_value = drinks[random.randint(0, len(drinks) - 1)]
                    return key_value
            text_size = 15
            text_color = "#55443d"
            text_weight = ft.FontWeight.W_900

            text_tuples = [
                ("추천", rnd),
                ("커피", lambda: "Coffee"),
                ("스무디\n프라페", lambda: "Smoothe"),
                ("음료", lambda: "Beverage"),
                ("에이드", lambda: "Ade"),
                ("차(Tea)", lambda: "Tea"),
                ("디저트", None)
            ]

            text_array = [
                ft.Container(
                    ft.Text(
                        text,
                        size="20",
                        color=text_color,
                        font_family="NanumGothic",
                        weight=text_weight
                    ),
                    ft.padding.only(bottom=60),
                    on_click=(lambda e, key=key: orderment.scroll_to(key=key(), duration=1000) if key else None)
                ) for text, key in text_tuples
            ]

            text_column = ft.Column(
                [ft.Container(text, alignment=ft.alignment.center) for text in text_array],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )

            def start_menu_click(e):
                print("\nData Initing -> Client Pressed home button")
                print("------------------------------------------")
                print(data_arrange)
                print("------------------------------------------\n")
                MENU.clear()
                Menu.clear()
                key_data.clear()
                data_arrange.clear()
                page.go('/')
            
            display = ft.Container(
                ft.Column(
                    [
                        text_column,
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Icon(name=ft.icons.HOME_ROUNDED, size=40, color=text_color),
                                        alignment=ft.alignment.center,
                                        on_click=start_menu_click
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            "처음으로",
                                            size=15,
                                            color=text_color,
                                            font_family="NanumGothic",
                                            weight=text_weight
                                        ),
                                        alignment=ft.alignment.center,
                                        padding=ft.padding.only(bottom=30)
                                    )
                                ]
                            ),
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
                bgcolor='#FFD700',
                height=3000,
                expand=True
            )

            def fee_sum_data():
                fee = 0
                for menu in range(len(Menu)):
                    # print(MENU[menu])
                    select_drink = ast.literal_eval(str(Menu[menu])[5:])['value']
                    result = str(select_drink).split(' ')[-2]
                    fee += int(result[:-1])
                return fee
            
            def check_duplicated():
                amount_menus = []  
                for menu in range(len(Menu)):
                    updated = ""                                                                                                                                     
                    for drink_item in drink_items:
                        select_drink = ast.literal_eval(str(Menu[menu])[5:])['value']
                        data = str(drink_item[1]).split("\n")[0]
                        if str(data).split(' ')[0] == str(data).split(' ')[-1]:
                            result = str(data).split(' ')[0] 
                        else:
                            result = str(data).split(' ')[0] + " " + str(data).split(' ')[-1]
                        pattern = r"(.+)\s(\d+)원"
                        match = re.match(pattern, str(select_drink))
                        if match:
                            item = match.group(1)
                            if result == item:
                                for index, val in enumerate(amount_menus):
                                    raw_data = str(val).split(" | ")[0]
                                    cal_data = str(val).split(" | ")[1]
                                    if raw_data == item:
                                        amount_menus[index] = f"{item} | {int(cal_data) + 1} | {str(match.group(0).split(item)[1])[1:]}"
                                        key_data.append(item)
                                        updated += "1"
                                if updated == "":
                                    menu_data = f"{item} | 1 | {str(match.group(0).split(item)[1])[1:]}"
                                    amount_menus.append(menu_data)
                # print(amount_menus)
                store_getting_lowdata(0, amount_menus) # 데이터를 삽입하도록 호출
                return amount_menus

            def on_click_handler(e):
                click(e.control)
                container = e.control.data # 클릭한 부분의 Container 데이터 가지고 오기
                datas = str(container).split('\n') # 줄 나눔하기 메뉴랑 가격이랑 다른줄로 나누어져 있기때문에
                texture = "" # 가격이랑 상품명을 한줄로 만들어서 textture 변수에 문자열로 저장해주기
                for data in range(len(datas)):
                    texture += str(datas[data] + " ")
                order_menu = ft.Text(
                    value=texture,
                    size=text_size,
                    color=text_color,
                    font_family="NanumGothic",
                    weight=text_weight
                ) # flet Text Container 만들어주기 여기에는 지금 가격이랑 상품명을 한줄로 나타내줌
                Menu.append(order_menu) # Menu 항목에 append 해주기
                total = fee_sum_data() # 총 금액 변수에 저장
                amount_orders = check_duplicated() # 겹친것이나 여러가지 요소들을 처리해주기
                order_list.clean() # 리스트 초기화하기
                for amount_order in range(len(amount_orders)):
                    data_str = str(amount_orders[amount_order]).split(" | ")[0]
                    data_int = str(amount_orders[amount_order]).split(" | ")[1]
                    data_price = str(amount_orders[amount_order]).split(" | ")[2]
                    # print(data_str)
                    list_result = ft.Text(
                        value=data_str + " " + data_price + f" x {data_int}",
                        size=text_size,
                        color=text_color,
                        font_family="NanumGothic",
                        weight=text_weight,
                        key=data_str
                    )
                    MENU.append(list_result)
                    order_list.update()
                sum_dataa = ft.Text(
                    value="  " + str(total) + "원",
                    size=text_size,
                    color=text_color,
                    font_family="NanumGothic",
                    weight=text_weight,
                )
                sum.controls = [sum_dataa] 
                sum.update()
                # print(f'Clicked on: {container}')

            def click(env):
                animations = [
                    ft.Offset(0, 2.0), ft.Offset(0, 1.9), ft.Offset(0, 1.8),
                    ft.Offset(0, 1.7), ft.Offset(0, 1.6), ft.Offset(0, 1.5),
                    ft.Offset(0, 1.4), ft.Offset(0, 1.3), ft.Offset(0, 1.2),
                    ft.Offset(0, 1.1), ft.Offset(0, 1.0), ft.Offset(0, 0.9),
                    ft.Offset(0, 0.8), ft.Offset(0, 0.7), ft.Offset(0, 0.6),
                    ft.Offset(0, 0.5), ft.Offset(0, 0.4), ft.Offset(0, 0.3),
                    ft.Offset(0, 0.2), ft.Offset(0, 0.1), ft.Offset(0, 0.0),
                    ft.Offset(0, 0.1), ft.Offset(0, 0.2), ft.Offset(0, 0.3),
                    ft.Offset(0, 0.4), ft.Offset(0, 0.5), ft.Offset(0, 0.6),
                    ft.Offset(0, 0.7), ft.Offset(0, 0.8), ft.Offset(0, 0.9),
                    ft.Offset(0, 1.0), ft.Offset(0, 1.1), ft.Offset(0, 1.2),
                    ft.Offset(0, 1.3), ft.Offset(0, 1.4), ft.Offset(0, 1.5),
                    ft.Offset(0, 1.6), ft.Offset(0, 1.7), ft.Offset(0, 1.8),
                    ft.Offset(0, 1.9), ft.Offset(0, 2.0)
                ]
                for offset in animations:
                    env.shadow = ft.BoxShadow(blur_radius=10, offset=offset)
                    env.update()
                    time.sleep(0.005)

            def submit(e): # e 값을 받아서 open_dlg_model을 호출하자 -> Kiosk에 대해서
                if len(data_arrange) != 0: # data_arrange는 최종적으로 메뉴를 포함하고 있는 배열의 정보이다. 
                    page.go('/from_general_order') # 이부분은 결제하기를 눌렀을때 나오는 페이지를 뜻함
                elif len(data_arrange) == 0:
                    open_dlg_modal(e) # 0개인 경우에는 alert함수 호출

            def create_menu_item(image, text, key):
                container = ft.Container(
                    ft.Image(
                        src=f"{current_working_directory}/assets/images/{image}",
                        width=360,
                        height=360,
                    ),
                    padding=ft.padding.only(top=20),
                    margin=ft.margin.only(top=20, left=21),
                    alignment=ft.alignment.top_left,
                    width=180,
                    height=264,
                    bgcolor='#ffffff',
                    border_radius=ft.border_radius.all(10),
                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        offset=ft.Offset(0, 3)
                    ),
                    on_click=on_click_handler,
                    key=key if key else None
                )
                container.data = text  
                return ft.Column([
                    container,
                    ft.Container(
                        ft.Text(
                            text,
                            size=15,
                            color=text_color,
                            font_family="NanumGothic",
                            weight=text_weight,
                            text_align=ft.alignment.top_left
                        ),
                        margin=ft.margin.only(left=25)
                    )
                ])

            rows = []
            for i in range(0, len(drink_items), 4):
                menu_cols = [create_menu_item(*item) for item in drink_items[i:i+4]]
                rows.append(ft.Row(menu_cols))

            sum = ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
            )

            order_list = ft.Column(
                MENU,
                scroll='always',
                auto_scroll=True,
                expand=True,
                # key를 활용해서 key 이동이 되어지도록
            )

            row_sum = ft.Row(
                [
                    order_list,
                    sum
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )

            order_box = ft.Container(
                ft.Row(
                    [
                        ft.Container(
                            row_sum,
                            width=640,
                            height=100,
                            border=ft.border.all(4, color='#aba5a0'),
                            border_radius=ft.border_radius.all(10),
                            margin=ft.margin.only(left=10),
                            padding=ft.padding.only(top=15, bottom=15, left=20, right=20)
                        ),
                        ft.Container(
                            ft.Text(
                                "결제하기",
                                size=25,
                                color=text_color,
                                font_family="NanumGothic",
                                weight=text_weight,
                            ),
                            padding=ft.padding.only(top=28, left=44),
                            width=180,
                            height=100,
                            border=None,
                            border_radius=ft.border_radius.all(10),
                            margin=ft.margin.only(right=20),
                            bgcolor='#FFD700',
                            on_click=submit # 메뉴가 있는지 확인하는 함수에 있어서 e를 받기 위해서는 함수 그대로를 호출해주어야한다.
                        )
                    ]
                ),
                height=110,
                alignment=ft.alignment.center
            )

            orderment = ft.Column(
                rows,
                scroll='always',
                expand=True
            )

            return View(
                route="/general_order",
                controls=[
                    ft.Row(
                        [
                            display,
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Container(height=20),
                                        orderment,
                                        order_box
                                    ],
                                ),
                                bgcolor='#fefcf6',
                                border=None,
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(left=40),
                                width=940
                            ),
                        ],
                        spacing=0,
                        expand=True,
                    )
                ]

            )
        
        def build_siosk_order_view(page: ft.Page):
            def close_dlg(e):
                dlg_modal.open = False
                page.update()
                
            dlg_modal = ft.AlertDialog(
                modal=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Text(
                    "메뉴를 적어도 한개 이상 선택해주세요", 
                    color='#55443d',
                    font_family="NanumGothic",
                ),
                actions=[
                    ft.TextButton(
                        "확인", 
                        on_click=close_dlg,
                        style=ft.ButtonStyle(
                            color=ft.colors.BLACK,
                        )
                    ),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )

            menu_array = []
            amount_array = []
            file_path = "Siosk/package/log/logger.log"
            def checker():
                def counting():
                    file = open(file_path, 'r', encoding='utf-8')
                    line_count = 0
                    try:
                        for line in file:
                            line_count += 1
                        return line_count
                    finally:
                        file.close()
                cnt_start = counting()
                while True:
                    try:
                        cnt = counting()
                        if cnt != cnt_start:
                            with open(file_path, 'r', encoding='utf-8') as r:
                                lines = r.readlines()
                                if lines:
                                    line = lines[-1]
                                    classified, flag = line.split(" | ")
                                    print("Checker, New string detected: " + classified)
                                    print("Checker, New flag detected: " + flag)
                                    try:
                                        hint = update_standard(classified=classified, flag=flag)
                                        if hint == False:
                                            break
                                    except:
                                        pass
                                else:
                                    pass
                        cnt_start = cnt
                        time.sleep(1)
                    except FileNotFoundError:
                        break

            detecting = threading.Thread(target=checker)
            detecting.start()
            
            def update_standard(classified, flag): # Analyzing logged data + Adding to orderment array 
                if flag == '3':
                    menu_array.append(classified)
                elif flag == '4':
                    amount_array.append(classified)
                elif flag == '6':
                    bool_data = classified
                    if bool_data == 'True':
                        print("Audio selected menu: " + menu_array[0])
                        print("Audio selected amount: " + amount_array[0])
                        print("Audio selected bool data: " + bool_data)
                        automatic_updater(menu=menu_array[0], amount=amount_array[0])
                        menu_array.clear()
                        amount_array.clear()
                    elif bool_data == 'False':
                        print("Order Canceled: " + bool_data)
                elif flag == '7':
                    submit_audio_version()
                    with open('Siosk/package/log/logger.log', 'w', encoding='utf-8') as file:
                        pass
                    return False
                elif flag == 'Gemini':
                    pass

            def open_dlg_modal(e):
                page.dialog = dlg_modal
                dlg_modal.open = True
                page.update()
            
            def rnd():
                for _ in range(len(drinks)):
                    key_value = drinks[random.randint(0, len(drinks) - 1)]
                    return key_value
            text_size = 15
            text_color = "#55443d"
            text_weight = ft.FontWeight.W_900

            text_tuples = [
                ("추천", rnd),
                ("커피", lambda: "Coffee"),
                ("스무디\n프라페", lambda: "Smoothe"),
                ("음료", lambda: "Beverage"),
                ("에이드", lambda: "Ade"),
                ("차(Tea)", lambda: "Tea"),
                ("디저트", None)
            ]

            text_array = [
                ft.Container(
                    ft.Text(
                        text,
                        size="25",
                        color=text_color,
                        font_family="NanumGothic",
                        weight=text_weight
                    ),
                    ft.padding.only(bottom=70),
                    on_click=lambda e, key=key: (orderment.scroll_to(key=key(), duration=1000) if key else None)
                ) for text, key in text_tuples
            ]

            text_column = ft.Column(
                [ft.Container(text, alignment=ft.alignment.center) for text in text_array],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )

            def start_menu_click(e):
                MENU.clear()
                Menu.clear()
                page.go('/')
            
            display = ft.Container(
                ft.Column(
                    [
                        text_column,
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Container(
                                        ft.Icon(name=ft.icons.HOME_ROUNDED, size=60, color=text_color),
                                        alignment=ft.alignment.center,
                                        on_click=start_menu_click
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            "처음으로",
                                            size=25,
                                            color=text_color,
                                            font_family="NanumGothic",
                                            weight=text_weight
                                        ),
                                        alignment=ft.alignment.center,
                                        padding=ft.padding.only(bottom=30)
                                    )
                                ]
                            ),
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
                bgcolor='#e6d5b8',
                height=3000,
                expand=True
            )

            def fee_sum_data():
                fee = 0
                for menu in range(len(Menu)):
                    # print(MENU[menu])
                    select_drink = ast.literal_eval(str(Menu[menu])[5:])['value']
                    result = str(select_drink).split(' ')[-2]
                    fee += int(result[:-1])
                return fee
            
            def check_duplicated():
                amount_menus = []  
                for menu in range(len(Menu)):
                    updated = ""                                                                                                                                     
                    for drink_item in drink_items:
                        select_drink = ast.literal_eval(str(Menu[menu])[5:])['value']
                        data = str(drink_item[1]).split("\n")[0]
                        if str(data).split(' ')[0] == str(data).split(' ')[-1]:
                            result = str(data).split(' ')[0] 
                        else:
                            result = str(data).split(' ')[0] + " " + str(data).split(' ')[-1]
                        pattern = r"(.+)\s(\d+)원"
                        match = re.match(pattern, str(select_drink))
                        if match:
                            item = match.group(1)
                            if result == item:
                                for index, val in enumerate(amount_menus):
                                    raw_data = str(val).split(" | ")[0]
                                    cal_data = str(val).split(" | ")[1]
                                    if raw_data == item:
                                        amount_menus[index] = f"{item} | {int(cal_data) + 1} | {str(match.group(0).split(item)[1])[1:]}"
                                        key_data.append(item)
                                        updated += "1"
                                if updated == "":
                                    menu_data = f"{item} | 1 | {str(match.group(0).split(item)[1])[1:]}"
                                    amount_menus.append(menu_data)
                print(amount_menus)
                store_getting_lowdata(0, amount_menus) # 데이터를 삽입하도록 호출 -> 시오스크
                return amount_menus
            
            def on_click_handler(e):
                click(e.control)
                container = e.control.data # 클릭한 부분의 Container 데이터 가지고 오기
                datas = str(container).split('\n') # 줄 나눔하기 메뉴랑 가격이랑 다른줄로 나누어져 있기때문에
                texture = "" # 가격이랑 상품명을 한줄로 만들어서 textture 변수에 문자열로 저장해주기
                for data in range(len(datas)):
                    texture += str(datas[data] + " ")
                order_menu = ft.Text(
                    value=texture,
                    size="30",
                    color=text_color,
                    font_family="NanumGothic",
                    weight=text_weight
                ) # flet Text Container 만들어주기 여기에는 지금 가격이랑 상품명을 한줄로 나타내줌
                Menu.append(order_menu) # Menu 항목에 append 해주기
                total = fee_sum_data() # 총 금액 변수에 저장
                amount_orders = check_duplicated() # 겹친것이나 여러가지 요소들을 처리해주기
                order_list.clean() # 리스트 초기화하기
                for amount_order in range(len(amount_orders)):
                    data_str = str(amount_orders[amount_order]).split(" | ")[0]
                    data_int = str(amount_orders[amount_order]).split(" | ")[1]
                    data_price = str(amount_orders[amount_order]).split(" | ")[2]
                    # print(data_str)
                    list_result = ft.Text(
                        value=data_str + " " + data_price + f" x {data_int}",
                        size="30",
                        color=text_color,
                        font_family="NanumGothic",
                        weight=text_weight,
                        key=data_str
                    )
                    MENU.append(list_result)
                    order_list.update()
                sum_dataa = ft.Text(
                    value="  " + str(total) + "원",
                    size="30",
                    color=text_color,
                    font_family="NanumGothic",
                    weight=text_weight,
                )
                sum.controls = [sum_dataa] 
                sum.update()
                # print(f'Clicked on: {container}')
            
            def extracting_fee(drink_name):
                drink_prices = {item[1].split('\n')[0]: item[1].split('\n')[1] for item in drink_items}
                expanded_drink_prices = {}
                for key, value in drink_prices.items():
                    expanded_drink_prices[key] = value
                    expanded_drink_prices[key.replace(" ", "")] = (key, value)

                # 음료 이름으로 가격을 검색
                price = drink_prices.get(drink_name)
                if price:
                    return drink_name, price
                else:
                    price_re = expanded_drink_prices.get(drink_name)
                    if price_re:
                        print(price_re)
                        return price_re
                    else:
                        print(expanded_drink_prices)
                        return None

            def automatic_updater(menu, amount):
                price = extracting_fee(menu)
                # print(price)
                # print(menu)
                texture = price[0] + " " + price[1] + " "
                '''
                text {'value': '아이스 아메리카노 3000원 ', 'fontfamily': 'NanumGothic', 'size': '30', 'weight': 'w900', 'color': '#55443d'} -> 일반 클릭
                text {'value': '아이스 아메리카노 3000원', 'fontfamily': 'NanumGothic', 'size': 15, 'weight': 'w900', 'color': '#55443d'} -> 음성 클릭
                '''
                for _ in range(int(amount)):
                    order_menu = ft.Text(
                        value=texture,
                        size="30",
                        color=text_color,
                        font_family="NanumGothic",
                        weight=text_weight
                    )
                    Menu.append(order_menu)
                total = fee_sum_data()
                amount_orders = check_duplicated()
                order_list.clean()
                for amount_order in range(len(amount_orders)):
                    data_str = str(amount_orders[amount_order]).split(" | ")[0]
                    data_int = str(amount_orders[amount_order]).split(" | ")[1]
                    data_price = str(amount_orders[amount_order]).split(" | ")[2]
                    # print(data_str)
                    list_result = ft.Text(
                        value=data_str + " " + data_price + f" x {data_int}",
                        size="30",
                        color=text_color,
                        font_family="NanumGothic",
                        weight=text_weight,
                        key=data_str
                    )
                    MENU.append(list_result)
                    order_list.update()
                sum_dataa = ft.Text(
                    value="  " + str(total) + "원",
                    size="30",
                    color=text_color,
                    font_family="NanumGothic",
                    weight=text_weight,
                )
                sum.controls = [sum_dataa] 
                sum.update()
                play(self.sound)
                # print(f'Clicked on: {container}')

            def click(env):
                animations = [
                    ft.Offset(0, 2.0), ft.Offset(0, 1.9), ft.Offset(0, 1.8),
                    ft.Offset(0, 1.7), ft.Offset(0, 1.6), ft.Offset(0, 1.5),
                    ft.Offset(0, 1.4), ft.Offset(0, 1.3), ft.Offset(0, 1.2),
                    ft.Offset(0, 1.1), ft.Offset(0, 1.0), ft.Offset(0, 0.9),
                    ft.Offset(0, 0.8), ft.Offset(0, 0.7), ft.Offset(0, 0.6),
                    ft.Offset(0, 0.5), ft.Offset(0, 0.4), ft.Offset(0, 0.3),
                    ft.Offset(0, 0.2), ft.Offset(0, 0.1), ft.Offset(0, 0.0),
                    ft.Offset(0, 0.1), ft.Offset(0, 0.2), ft.Offset(0, 0.3),
                    ft.Offset(0, 0.4), ft.Offset(0, 0.5), ft.Offset(0, 0.6),
                    ft.Offset(0, 0.7), ft.Offset(0, 0.8), ft.Offset(0, 0.9),
                    ft.Offset(0, 1.0), ft.Offset(0, 1.1), ft.Offset(0, 1.2),
                    ft.Offset(0, 1.3), ft.Offset(0, 1.4), ft.Offset(0, 1.5),
                    ft.Offset(0, 1.6), ft.Offset(0, 1.7), ft.Offset(0, 1.8),
                    ft.Offset(0, 1.9), ft.Offset(0, 2.0)
                ]
                for offset in animations:
                    env.shadow = ft.BoxShadow(blur_radius=10, offset=offset)
                    env.update()
                    time.sleep(0.005)
                    
            def submit(e): # e 값을 받아서 open_dlg_model을 호출하자 -> Siosk에 대해서
                if len(data_arrange) != 0: # data_arrange는 최종적으로 메뉴를 포함하고 있는 배열의 정보이다. 
                    page.go('/from_siosk_order') # 이부분은 결제하기를 눌렀을때 나오는 페이지를 뜻함
                elif len(data_arrange) == 0:
                    open_dlg_modal(e) # 0개인 경우에는 alert함수 호출

            def submit_audio_version(): # e 값을 받아서 open_dlg_model을 호출하자 -> Siosk에 대해서
                page.go('/from_siosk_order') # 이부분은 결제하기를 눌렀을때 나오는 페이지를 뜻함
                play(self.sound)

            def create_menu_item(image, text, key):
                container = ft.Container(
                    ft.Image(
                        src=f"{current_working_directory}/assets/images/{image}",
                        width=750,
                        height=750,
                    ),
                    padding=ft.padding.only(top=20),
                    margin=ft.margin.only(top=50, left=30),
                    alignment=ft.alignment.top_left,
                    width=375,
                    height=550,
                    bgcolor='#ffffff',
                    border_radius=ft.border_radius.all(10),
                    shadow=ft.BoxShadow(
                        blur_radius=10,
                        offset=ft.Offset(0, 3)
                    ),
                    on_click=on_click_handler,
                    key=key if key else None
                )
                container.data = text  
                return ft.Column([
                    container,
                    ft.Container(
                        ft.Text(
                            text,
                            size=25,
                            color=text_color,
                            font_family="NanumGothic",
                            weight=text_weight,
                            text_align=ft.alignment.top_left
                        ),
                        margin=ft.margin.only(top=10, left=25)
                    )
                ])

            rows = []
            for i in range(0, len(drink_items), 2):
                menu_cols = [create_menu_item(*item) for item in drink_items[i:i+2]]
                rows.append(ft.Row(menu_cols))

            sum = ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
            )

            order_list = ft.Column(
                MENU,
                scroll='always',
                auto_scroll=True,
                expand=True,
                # key를 활용해서 key 이동이 되어지도록
            )

            row_sum = ft.Row(
                [
                    order_list,
                    sum
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )

            submit_button_click_handler = submit

            order_box = ft.Container(
                ft.Row(
                    [
                        ft.Container(
                            row_sum,
                            width=610,
                            height=180,
                            border=ft.border.all(4, color='#aba5a0'),
                            border_radius=ft.border_radius.all(20),
                            margin=ft.margin.only(left=10),
                            padding=ft.padding.only(top=15, bottom=15, left=20, right=20)
                        ),
                        ft.Container(
                            ft.Text(
                                "결제하기",
                                size=40,
                                color=text_color,
                                font_family="NanumGothic",
                                weight=text_weight,
                            ),
                            padding=ft.padding.only(top=60, left=33),
                            width=220,
                            height=180,
                            border=None,
                            border_radius=ft.border_radius.all(20),
                            margin=ft.margin.only(right=20),
                            bgcolor='#E6D5B8',
                            on_click=submit # 메뉴가 있는지 확인하는 함수에 있어서 e를 받기 위해서는 함수 그대로를 호출해주어야한다.
                        )
                    ]
                ),
                height=200,
                alignment=ft.alignment.center
            )

            orderment = ft.Column(
                rows,
                scroll='always',
                expand=True
            )

            def animate_containers(containers):
                for container in containers:
                    page.add(container)  # 각 컨테이너를 페이지에 추가

                def toggle_height():
                    while True:
                        for container in containers:
                            new_height = random.randint(50, 200)
                            container.height = new_height
                            page.update()  # 이제 안전하게 업데이트 가능
                        time.sleep(0.5)
                thread = threading.Thread(target=toggle_height)
                thread.daemon = True
                thread.start()

            containers = [
                ft.Container(
                    bgcolor=ft.colors.BLACK,
                    width=45,
                    height=90,
                    border_radius=ft.border_radius.all(30),
                    animate=ft.Animation(600, "easeInOut"),
                ) for _ in range(4)
            ]

            centered_content = ft.Row(
                controls=ft.Container(
                    containers,
                    expand=True
                ),
                alignment=ft.MainAxisAlignment.END,
            )

            column_content = ft.Column(
                [
                    ft.Container(
                        centered_content,
                        margin=ft.margin.only(right=60, bottom=10),
                        expand=True
                    ),
                ],
            )
            
            page.add(column_content)
            animate_containers(containers)
            return View(
                route="/general_order",
                controls=[
                    ft.Row(
                        [
                            display,
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.Row(
                                                controls=containers,
                                                alignment=ft.MainAxisAlignment.END,
                                            ),
                                            margin=ft.margin.only(right=60),
                                            height=230,
                                        ),
                                        orderment,
                                        order_box
                                    ],
                                ),
                                bgcolor='#fefcf6',
                                border=None,
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(left=20),
                                width=900,
                            ),
                        ],
                        spacing=0,
                        expand=True,
                    )
                ],
            )
        
        # store_getting_lowdata(1, None) 주문했던걸 반환해줌
        def build_payment_order_view():
            # if route_history[0] == "/general_order":
            future_route = "/general_order"
            # route_history.clear()
        
        def from_general_order():
            return View(
                route="/from_siosk_order",
                controls=[
                    ft.Container(
                        ft.Text("Hello Fucking World")
                    ),
                    ft.Container(
                        ft.TextButton("movement to Administrator Page", on_click=lambda _:page.go("/admininstrator_page"))
                    )
                ]
            )
        
        def from_siosk_order():
            def background_function(column_content, containers): # Background Process Threading 등등
                page.add(column_content) # 에니매이션 처리
                animate_containers(containers) # 에니매이션 처리
                result = store_getting_lowdata(1, None) # 삽입되어진 값들을 호출 -> 키오스크
                names, amounts, prices, images = get_picture_link() # Picture Link를 받아오는 함수로써 이름, 양, 이미지 경로를 받아오는 역할을 한다.
                for beverage_index, beverage_val in enumerate(names):
                    table_format = f"| {names[beverage_index]} | {amounts[beverage_index]} | {prices[beverage_index]} | {images[beverage_index]} |"
                    print(table_format)
                return names, amounts, prices, images

            def get_price_by_name(drink_name, drink_items): # 이름을 활용해서 이미지 경로 배열에서 이미지 경로를 추출
                for image, name_price, category in drink_items: # for 문으로 검사
                    name, price = name_price.split("\n")  # 이름과 가격 분리
                    if name == drink_name:
                        return image
                return -1  

            def prettier_order_array(e):
                try:
                    name = str(data_arrange[0][e]).split(' | ')[0]
                    amount = str(data_arrange[0][e]).split(' | ')[1]
                    price = str(data_arrange[0][e]).split(' | ')[2]
                    return name, amount, price
                except IndexError:
                    print("Please add least fake array valument")

            def get_picture_link():
                names = []
                amounts = []
                prices = []
                images = []
                for data_arrange_index, data_arrange_val in enumerate(data_arrange[0]):
                    name, amount, price = prettier_order_array(data_arrange_index)
                    image = get_price_by_name(name, drink_items=drink_items)
                    names.append(name)
                    amounts.append(amount)
                    prices.append(price) 
                    images.append(image)
                return names, amounts, prices, images

            def animate_containers(containers):
                for container in containers:
                    page.add(container)  # 각 컨테이너를 페이지에 추가

                def toggle_height():
                    while True:
                        for container in containers:
                            new_height = random.randint(50, 200)
                            container.height = new_height
                            page.update()  # 이제 안전하게 업데이트 가능
                        time.sleep(0.5)
                thread = threading.Thread(target=toggle_height)
                thread.daemon = True
                thread.start()

            containers = [
                ft.Container(
                    bgcolor=ft.colors.BLACK,
                    width=45,
                    height=90,
                    border_radius=ft.border_radius.all(30),
                    animate=ft.Animation(600, "easeInOut"),
                ) for _ in range(4)
            ]

            centered_content = ft.Row(
                controls=ft.Container(
                    containers,
                    expand=True
                ),
                alignment=ft.MainAxisAlignment.END,
            )

            column_content = ft.Column(
                [
                    ft.Container(
                        centered_content,
                    ),
                ],
            )
            
            names, amounts, prices, images = background_function(column_content=column_content, containers=containers)
            
            def total_amount():
                sum_data = []
                for beverage_sum_index, beverage_sum_val in enumerate(names):
                    price_total = int(amounts[beverage_sum_index]) * int(str(prices[beverage_sum_index])[:-1])
                    sum_data.append(price_total)
                return sum_data, sum(sum_data)

            def creating_containers():
                elements = []
                def update_amount(e, name, change):
                    print(name)
                    print(names.index(name))
                    print(amounts)
                    amounts[int(names.index(name))] = int(amounts[int(names.index(name))]) + change
                    page.update()

                for beverage_final_index, beverage_final_val in enumerate(names):
                    
                    element = ft.Container(
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Image(
                                        src=f"{current_working_directory}/assets/images/{images[beverage_final_index]}",
                                        width=400,
                                        height=400,
                                        fit=ft.ImageFit.CONTAIN,
                                    ),
                                    width=300,
                                    height=400,
                                    border_radius=ft.border_radius.all(10),
                                    shadow=ft.BoxShadow(
                                        blur_radius=10,
                                        offset=ft.Offset(0, 3)
                                    ),
                                    margin=ft.margin.only(left=40, bottom=20, top=10),
                                    bgcolor='#ffffff',
                                ),
                                ft.Container(
                                    ft.Column( 
                                        [
                                            ft.Text(
                                                names[beverage_final_index],
                                                size=30,
                                                text_align=ft.TextAlign.CENTER,
                                                color=ft.colors.BLACK,
                                                font_family="NanumGothic"
                                            ),
                                            ft.Text(
                                                prices[beverage_final_index],
                                                size=30,
                                                text_align=ft.TextAlign.CENTER,
                                                color=ft.colors.BLACK,
                                                font_family="NanumGothic"
                                            ),
                                        ],
                                    ),
                                    width=300,
                                    margin=ft.margin.only(left=50)
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.IconButton(
                                                ft.icons.REMOVE,
                                                icon_color=ft.colors.BLACK,
                                                # on_click=lambda e: update_amount(e, names[beverage_final_index], -1)
                                            ),
                                            ft.Text(
                                                value=amounts[int(names.index(names[beverage_final_index]))],
                                                size=20, 
                                                text_align=ft.TextAlign.CENTER, 
                                                color=ft.colors.BLACK,
                                                width=40,
                                                font_family="NanumGothic",
                                            ),
                                            ft.IconButton(
                                                ft.icons.ADD,
                                                icon_color=ft.colors.BLACK,
                                                # on_click=lambda e: update_amount(e, names[beverage_final_index], 1)
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    width=200,
                                    border=ft.border.all(5, "#999999"),
                                    border_radius=9
                                ),
                            ],
                            spacing=0
                        )
                    )
                    elements.append(element)
                return elements
            
            money_list, money_sum = total_amount()
            money_sum = "{:,}원".format(money_sum)
            elements_array = creating_containers()
            text_color = "#55443d"
            text_weight = ft.FontWeight.W_900

            def connection(names, amounts, prices):
                print(names)
                print(amounts)
                print(prices)
                requests.get(f"http://{ip_store[0]}:946", params={'names': str(names), 'amounts': str(amounts), 'prices': str(prices)})
                MENU.clear()
                Menu.clear()
                data_arrange.clear()
                page.go('/')

            return View(
                route="/from_general_order",
                controls=[
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Container(
                                                ft.Text(
                                                    "주문을 확인해주세요.",
                                                    size=35,
                                                    text_align=ft.TextAlign.CENTER,
                                                    color=ft.colors.BLACK,
                                                    font_family="NanumGothic"
                                                ),
                                                ft.margin.only(left=40, right=400, top=100),
                                            ),
                                            ft.Container(
                                                ft.Row(
                                                    controls=containers,
                                                ),
                                                margin=ft.margin.only(right=60),
                                                height=300
                                            ),
                                        ]
                                    ),
                                    bgcolor=ft.colors.WHITE,
                                ),
                                ft.Container(
                                    ft.Column(
                                        controls=elements_array,
                                        scroll='always',
                                    ),
                                    height=1300,
                                    bgcolor=ft.colors.WHITE,
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Container(
                                                ft.Row(
                                                    [
                                                        ft.Text(
                                                            f"총 금액:",
                                                            size=40,
                                                            color=text_color,
                                                            font_family="NanumGothic",
                                                            weight=text_weight,
                                                        ),
                                                        ft.Text(
                                                            money_sum,
                                                            size=40,
                                                            color=text_color,
                                                            font_family="NanumGothic",
                                                            weight=text_weight,
                                                        ),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                ),
                                                width=510,
                                                height=180,
                                                border=ft.border.all(5, color='#aba5a0'),
                                                border_radius=ft.border_radius.all(20),
                                                margin=ft.margin.only(left=10),
                                                padding=ft.padding.only(top=15, bottom=15, left=20, right=20)
                                            ),
                                            ft.Container(
                                                ft.Text(
                                                    "메뉴",
                                                    size=40,
                                                    color=text_color,
                                                    font_family="NanumGothic",
                                                    weight=text_weight,
                                                ),
                                                width=200,
                                                height=180,
                                                border=ft.border.all(5, color='#aba5a0'),
                                                border_radius=ft.border_radius.all(20),
                                                margin=ft.margin.only(left=10),
                                                padding=ft.padding.only(top=55, bottom=15, left=57, right=20),
                                                on_click=lambda _: page.go('/siosk_order')
                                            ),
                                            ft.Container(
                                                ft.Text(
                                                    "결제하기",
                                                    size=40,
                                                    color=text_color,
                                                    font_family="NanumGothic",
                                                    weight=text_weight,
                                                ),
                                                padding=ft.padding.only(top=60, left=70),
                                                width=290,
                                                height=180,
                                                border=None,
                                                border_radius=ft.border_radius.all(20),
                                                margin=ft.margin.only(left=10),
                                                bgcolor='#E6D5B8',
                                                on_click=lambda _: connection(names, amounts, prices)
                                            )
                                        ]
                                    ),
                                    height=200,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(top=45)
                                )
                                # ft.Container(
                                #     ft.TextButton("/admininstrator_page", on_click=lambda _: page.go('/admininstrator_page')),
                                #     bgcolor=ft.colors.WHITE,
                                # ),
                            ],
                            spacing=0
                        ),
                        width=10000,
                        height=10000,
                        bgcolor=ft.colors.WHITE
                    )
                ],
            )

        def administrator_page():
            def initing():
                print("\nData Initing -> Client Pressed home button")
                print("------------------------------------------")
                print(data_arrange)
                print("------------------------------------------\n")
                MENU.clear()
                Menu.clear()
                data_arrange.clear()

            def adding(e):
                try:
                    amount = str(data_arrange[0][0]).split(' | ')[1]
                    data_arrange.clear()
                    temp_fake_array = []
                    temp_fake_array.append(f'카페 모카 | {int(amount) + 1} | 3000원')
                    data_arrange.append(temp_fake_array)
                    print("data insulting")
                    print(data_arrange)
                except IndexError:
                    temp_fake_array = []
                    temp_fake_array.append(f'카페 모카 | {e} | 3000원')
                    data_arrange.append(temp_fake_array)
                    print("data insulting")
                    print(data_arrange)

            return View(
                route="/admininstrator_page",
                controls=[
                    ft.Container(
                        height=1000
                    ),
                    ft.Container(
                        ft.TextButton("/", on_click=lambda _:page.go("/")) # lamba를 쓰는 이유는 즉석 Function을 만들어내기 위함에 있음, 즉시 함수를 생성하여 Onclick 넣어주기
                    ),
                    ft.Container(
                        ft.TextButton("/general_order", on_click=lambda _:page.go("/general_order"))
                    ),
                    ft.Container(
                        ft.TextButton("/siosk_order", on_click=lambda _:page.go("/siosk_order"))
                    ),
                    ft.Container(
                        ft.TextButton("/from_general_order", on_click=lambda _:page.go("/from_general_order"))
                    ),
                    ft.Container(
                        ft.TextButton("/from_siosk_order", on_click=lambda _:page.go("/from_siosk_order"))
                    ),
                    ft.Container(
                        ft.TextButton("Initing", on_click=lambda _: initing())
                    ),
                    ft.Container(
                        ft.TextButton("Adding", on_click=lambda _: adding(1))
                    )
                ]
            )

        def route_change(event: RouteChangeEvent):
            page.views.clear()
            if page.route == "/":
                page.views.append(build_home_view())
            elif page.route == "/general_order":
                page.views.append(build_general_order_view())
            elif page.route == "/siosk_order":
                page.views.append(build_siosk_order_view(page=page))
            elif page.route == "/admininstrator_page":
                page.views.append(administrator_page())
            elif page.route == "/from_general_order":
                page.views.append(from_general_order())
            elif page.route == "/from_siosk_order":
                page.views.append(from_siosk_order())
            page.update()
        
        page.on_route_change = route_change
        page.go(page.route)
