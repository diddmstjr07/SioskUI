import flet as ft
from flet import View, RouteChangeEvent
import os
import random
import time
import ast
import re
from auto.delete import delete_dot_underscore_files

current_working_directory = os.getcwd()
drinks = ["Coffee", "Smoothe", "Beverage", "Tea", "Ade"]

def main(page: ft.Page):
    drink_items = [ 
        ("coffee/iceamericano.png", "아이스 아메리카노\n3000원", "Coffee"),
        ("coffee/younyu_latte.png", "연유 라테\n3000원", None),
        ("coffee/kapuchino.png", "카푸치노\n3000원", None),
        ("coffee/Hazelnut_Latte.png", "헤이즐넛 라테\n3000원", None),
        ("coffee/Hazelnut_Americano.png", "헤이즐넛 아메리카노\n3000원", None),
        ("coffee/Coldbrew_Latte.png", "콜드브루 라테\n3000원", None),
        ("coffee/cold_brew_original.png", "콜드브루\n3000원", None),
        ("coffee/Caramel_Macchiato.png", "카라멜 마키아또\n3000원", None),
        ("coffee/Caffe_Mocha.png", "카페 모카\n3000원", None),
        ("frappe/Mint_Frappe.png", "민트 프라페\n3000원", None),
        ("frappe/Green_Tea_Frappe.png", "녹차 프라페\n3000원", "Smoothe"),
        ("frappe/Unicorn_Frappe.png", "유니콘 프라페\n3000원", None),
        ("pongcrush/Banana_Pongcrush.png", "바나나 퐁크러쉬\n3000원", "Beverage"),
        ("pongcrush/Chocolate_Honey_Pong_Crush.png", "초콜릿허니 퐁크러쉬\n3000원", None),
        ("pongcrush/Choux_Cream_Honey_Pong_Crush.png", "슈크림허니 퐁크러쉬\n3000원", None),
        ("pongcrush/Plain_Pongcrush.png", "플래인 퐁크러쉬\n3000원", None),
        ("pongcrush/Strawberry_pongcrush.png", "딸기 퐁크러쉬\n3000원", None),
        ("pongcrush/Strawberry_Cookie_Frappe.png", "딸기쿠키 프라페\n3000원", None),
        ("smoothie/Mango_Yogurt_Smoothie.png", "망고요거트 스무디\n3000원", None),
        ("smoothie/Plain_Yogurt_Smoothie.png", "플래인요거트 스무디\n3000원", None),
        ("smoothie/Strawberry_Yogurt_Smoothie.png", "딸기요거트 스무디\n3000원", None),
        ("ade/Blue_Lemon_Ade.png", "블루 레몬에이드\n3000원", "Ade"),
        ("ade/Cherry_Coke.png", "체리콕\n3000원", None),
        ("ade/Grapefruit_Ade.png", "자몽 에이드\n3000원", None),
        ("ade/Lemon_Ade.png", "레몬 에이드\n3000원", None),
        ("ade/Lime_Mojito.png", "라임 모히또\n3000원", None),
        ("ade/MEGA_Ade.png", "메가 에이드\n3000원", None),
        ("tea/Hot_lemon_tea.png", "레몬차\n3000원", None),
        ("tea/Applecitron_Tea.png", "사과 유자차\n3000원", "Tea"),
        ("tea/Chamomile.png", "케모마일 차\n3000원", None),
        ("tea/Green_Tea.png", "녹차\n3000원", None),
        ("tea/Earl_Grey.png", "얼그레이\n3000원", None),
        ("tea/Hot_Grapefruit_tea.png", "자몽차\n3000원", None),
    ]
    MENU = []
    Menu = []
    key_data = []
    data_arrange = []
    page.title = "시오스크"
    page.window_width = 700
    page.window_height = 1600

    page.fonts = {
        "NanumGothic": "fonts/NanumGothic-Bold.ttf"
    }

    img0 = ft.Image(
        src=f"{current_working_directory}/assets/images/logo/general.png",
        width=200,
        height=200,
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
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    shadowed_img1 = ft.Container(
        img1,
        padding=10
    )

    def store_getting_lowdata(e, low_data): 
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
                os._exit(0)
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
                    on_click=lambda _: page.go('/siosk_order')
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
                    size=text_size,
                    color=text_color,
                    font_family="NanumGothic",
                    weight=text_weight
                ),
                ft.padding.only(bottom=30),
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
        
        def payment_recheck(e):
            if Menu == []:
                open_dlg_modal(e)
            else:
                page.go('/payment_recheck')
        
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
            bgcolor='#e6d5b8',
            height=height_ele,
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
            store_getting_lowdata(0, amount_menus)
            return amount_menus

        def on_click_handler(e):
            click(e.control)
            container = e.control.data
            datas = str(container).split('\n')
            texture = ""
            for data in range(len(datas)):
                texture += str(datas[data] + " ")
            order_menu = ft.Text(
                value=texture,
                size=text_size,
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

        def create_menu_item(image, text, key):
            container = ft.Container(
                ft.Image(
                    src=f"{current_working_directory}/assets/images/{image}",
                    width=300,
                    height=300,
                ),
                padding=ft.padding.only(top=20),
                margin=ft.margin.only(top=20, left=21),
                alignment=ft.alignment.top_left,
                width=150,
                height=220,
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
        for i in range(0, len(drink_items), 3):
            menu_cols = [create_menu_item(*item) for item in drink_items[i:i+3]]
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
                        width=340,
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
                        bgcolor='#E6D5B8',
                        on_click=payment_recheck
                    )
                ]
            ),
            height=110,
            width=width_ele - 150,
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
                            width=width_ele - 150
                        ),
                    ],
                    spacing=0,
                    expand=True,
                )
            ]
        )
    
    def build_siosk_order_view():
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
                    size=text_size,
                    color=text_color,
                    font_family="NanumGothic",
                    weight=text_weight
                ),
                ft.padding.only(bottom=30),
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
        
        def payment_recheck(e):
            if Menu == []:
                open_dlg_modal(e)
            else:
                page.go('/payment_recheck')
        
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
            bgcolor='#e6d5b8',
            height=height_ele,
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
            store_getting_lowdata(0, amount_menus)
            return amount_menus

        def on_click_handler(e):
            click(e.control)
            container = e.control.data
            datas = str(container).split('\n')
            texture = ""
            for data in range(len(datas)):
                texture += str(datas[data] + " ")
            order_menu = ft.Text(
                value=texture,
                size=text_size,
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

        def create_menu_item(image, text, key):
            container = ft.Container(
                ft.Image(
                    src=f"{current_working_directory}/assets/images/{image}",
                    width=300,
                    height=300,
                ),
                padding=ft.padding.only(top=20),
                margin=ft.margin.only(top=20, left=21),
                alignment=ft.alignment.top_left,
                width=150,
                height=220,
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
        for i in range(0, len(drink_items), 3):
            menu_cols = [create_menu_item(*item) for item in drink_items[i:i+3]]
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
                        width=340,
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
                        bgcolor='#E6D5B8',
                        on_click=payment_recheck
                    )
                ]
            ),
            height=110,
            width=width_ele - 150,
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
                            width=width_ele - 150
                        ),
                    ],
                    spacing=0,
                    expand=True,
                )
            ]
        )

    def build_payment_order_view():
        return View(
            route="/payment_recheck",
            controls=[
                ft.Container(
                    ft.Text(
                        store_getting_lowdata(1, None),
                    ),
                ),
                ft.Container(
                    ft.Container(
                        ft.Text(
                            "돌아가기",
                            font_family="NanumGothic",
                            color=ft.colors.BLACK,
                        ),
                        alignment=ft.alignment.center,
                        width=100,
                        height=50,
                        on_click=lambda _: page.go('/general_order'),
                        bgcolor=ft.colors.BLUE_100, 
                        border_radius=15
                    ),
                    alignment=ft.alignment.bottom_right,
                    expand=True
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
            page.views.append(build_siosk_order_view())
        elif page.route == "/payment_recheck":
            page.views.append(build_payment_order_view())
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    delete_dot_underscore_files()
    ft.app(target=main)