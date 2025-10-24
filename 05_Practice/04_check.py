import pyautogui
import time

# 예시 좌표! 직접 사이트에서 확인 후 수정하세요. (화면 크기에 따라 달라질 수 있음)
# 아래는 설명용 임의 좌표입니다.

start_year_pos = (500, 300)     # 시작년도 입력란 좌표
start_month_pos = (500, 340)    # 시작월 입력란 좌표
end_year_pos = (700, 300)       # 종료년도 입력란 좌표
end_month_pos = (700, 340)      # 종료월 입력란 좌표
search_button_pos = (800, 400)  # 검색 버튼 좌표
download_button_pos = (1000, 500) # 엑셀 다운로드 버튼 좌표

time.sleep(2)  # 준비시간

def year_click(year):
    # 1. 시작년도 클릭 & 입력 & 엔터
    pyautogui.click(start_year_pos)
    time.sleep(0.5)
    pyautogui.typewrite(year)
    pyautogui.press('enter')
    time.sleep(0.5)

    # 3. 종료년도 클릭 & 입력 & 엔터
    pyautogui.click(end_year_pos)
    time.sleep(0.5)
    pyautogui.typewrite(year)
    pyautogui.press('enter')
    time.sleep(0.5)

def month_click(start_m, end_m):
    # 2. 시작월 클릭 & 입력 & 엔터
    pyautogui.click(start_month_pos)
    time.sleep(0.5)
    pyautogui.write(start_m)
    pyautogui.press('enter')
    time.sleep(0.5)

    # 4. 종료월 클릭 & 입력 & 엔터
    pyautogui.click(end_month_pos)
    time.sleep(0.5)
    pyautogui.write(end_m)
    pyautogui.press('enter')
    time.sleep(0.5)

def download():
    # 5. 검색 클릭
    pyautogui.click(search_button_pos)
    time.sleep(30)  # 검색 후 데이터 로드 대기

    # 6. 다운로드 버튼 클릭 & 엔터
    pyautogui.click(download_button_pos)
    time.sleep(0.5)
    pyautogui.press('enter')

years = [2023,2024,2025]
start_ms =[1,7]
end_ms = [6,12]
month_pair = [(1,6),(7,12)]

for year in years:
    print('각 버튼의 좌표ㅡㄹ 마우스로 확인해서 아래에 입력하세요.')
    time.sleep(2)  # 준비시간
    year_click(year)

    for start_m, end_m in month_pair:

print("매크로 완료!")
