def display_question(question, number):
    print(f"\n{number}. {question['text']}")
    for idx, option in enumerate(question['options'], 1):
        print(f"  {idx}. {option}")

def get_user_choice():
    while True:
        try:
            choice = int(input("답 번호를 입력하세요 (1~4): "))
            if 1 <= choice <= 4:
                return choice - 1
        except ValueError:
            pass
        print(" 유효한 번호(1~4)를 입력해주세요.")

def display_result(score, total_questions):
    print("\n 퀴즈 종료!")
    print(f"총 점수: {score}점 (총 문항 수: {total_questions}문제)")

def ask_retry():
    retry = input("\n틀린 문제를 다시 풀어보시겠습니까? (yes/no): ").lower()
    if retry != "yes":
        print("실행을 종료합니다.")
    return retry == "yes"