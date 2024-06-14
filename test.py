import flet as ft

def main(page: ft.Page):
    # AlertDialog 닫기 함수
    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    # AlertDialog 정의
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("알림", style=ft.TextStyle(size=20, weight="bold")),  # 타이틀 추가
        content=ft.Column([
            ft.Text("메뉴를 적어도 한개 이상 선택해주세요."),
            ft.Text("다른 메시지를 여기에 추가할 수 있습니다.")
        ]),
        actions=[
            ft.TextButton("확인", on_click=close_dlg),
            ft.TextButton("취소", on_click=lambda e: print("취소 버튼 클릭"))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    # AlertDialog 열기 함수
    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    # 버튼을 클릭하면 AlertDialog 열기
    open_dlg_button = ft.ElevatedButton(text="알림 열기", on_click=open_dlg_modal)

    # 페이지에 버튼 추가
    page.add(open_dlg_button)

# flet 앱 실행
ft.app(target=main)
