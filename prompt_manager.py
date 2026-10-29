CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

prompts = [
    {
        "title": "자동화 워크플로우 설계 도우미",
        "content": (
            "당신은 Make와 Zapier에 능숙한 노코드 자동화 전문가입니다.\n"
            "제가 반복하는 업무를 설명하면 Trigger, Action, 조건 분기로 나눠 워크플로우를 설계해주세요.\n"
            "각 단계에서 사용할 모듈 이름과 예상되는 오류, 그리고 오류 처리 방법도 함께 알려주세요."
        ),
        "category": "자동화",
        "favorite": False,
    },
    {
        "title": "기상청 API 데이터 가공 도우미",
        "content": (
            "기상청 단기예보 API 응답에는 수백 개의 항목이 배열로 들어 있습니다.\n"
            "이 중 category가 POP(강수확률)이고, 오늘 날짜이며, 확률이 50% 이상인 시간대만 골라서\n"
            "Make의 Iterator, Filter, Text Aggregator를 어떻게 연결해야 하는지 단계별로 설명해주세요."
        ),
        "category": "자동화",
        "favorite": False,
    },
    {
        "title": "자동화 도구 비교 보고서",
        "content": (
            "Make와 Zapier를 UI/UX, 설정 난이도, 연동 범위, 무료 플랜 범위, 로그 확인 방식으로 비교하는 표를 만들어주세요.\n"
            "각 도구의 장단점과, 어떤 상황에 어느 도구가 적합한지도 정리해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "우산 알림 메일 문구 작성",
        "content": (
            "비가 올 예정인 시간대 목록을 받아서, 아침에 읽기 좋은 짧은 우산 알림 이메일을 써주세요.\n"
            "제목은 한 줄, 본문은 3문장 이내로 하고, 친근한 말투로 작성해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": False,
    },
    {
        "title": "노코드 자동화 멘토",
        "content": (
            "당신은 노코드 자동화를 가르치는 친절한 멘토입니다.\n"
            "제가 만든 워크플로우를 설명하면 개선할 점, 실패 시 재시도 전략, "
            "다른 지역이나 업무로 확장하는 방법을 초보자가 이해할 수 있게 알려주세요."
        ),
        "category": "페르소나",
        "favorite": False,
    },
]


def input_required(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("값이 비어 있습니다. 다시 입력해주세요.")


def choose_category():
    print("카테고리 선택:")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")
    print("0) 직접 입력")

    while True:
        choice = input("선택: ").strip()
        if choice == "0":
            return input_required("카테고리 이름: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("잘못된 입력입니다. 다시 선택해주세요.")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input_required("제목: ")
    content = input_required("내용: ")
    category = choose_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("프롬프트가 추가되었습니다!")


def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"{i}) {name}")

    choice = input("선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 입력입니다.")
        return

    category = CATEGORIES[int(choice) - 1]
    found = [p for p in prompts if p["category"] == category]

    if not found:
        print(f"[{category}] 카테고리에 프롬프트가 없습니다.")
        return

    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, p in enumerate(found, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")
    print(f"총 {len(found)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input_required("검색어: ").lower()

    found = [
        p for p in prompts
        if keyword in p["title"].lower() or keyword in p["content"].lower()
    ]

    if not found:
        print("검색 결과가 없습니다.")
        return

    print("검색 결과:")
    for i, p in enumerate(found, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"{len(found)}개의 프롬프트를 찾았습니다.")


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("번호 입력: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print(f"잘못된 번호입니다. 1~{len(prompts)} 사이의 번호를 입력해주세요.")
        return

    p = prompts[int(choice) - 1]
    star = "⭐" if p["favorite"] else "-"
    line = "─" * 28

    print(line)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print(line)
    print("내용:")
    print(p["content"])
    print(line)


def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    choice = input("프롬프트 번호 입력: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print(f"잘못된 번호입니다. 1~{len(prompts)} 사이의 번호를 입력해주세요.")
        return

    p = prompts[int(choice) - 1]
    p["favorite"] = not p["favorite"]

    if p["favorite"]:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [p for p in prompts if p["favorite"]]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, p in enumerate(favorites, start=1):
        print(f"{i}. [{p['category']}] {p['title']} ⭐")
    print(f"총 {len(favorites)}개의 즐겨찾기")


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        else:
            print("잘못된 입력입니다. 0~7 사이의 번호를 입력해주세요.")


if __name__ == "__main__":
    main()