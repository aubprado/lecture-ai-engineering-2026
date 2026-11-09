"""第1回: 素のLLMに質問し、会話を続けるスクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールは使わず、会話履歴を保って質問を続ける「素の」呼び出し。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse
import time

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def ask(question: str, history: list[dict[str, object]]) -> str:
    client = genai.Client(api_key=get_api_key())
    user_message = {"role": "user", "parts": [{"text": question}]}
    start_time = time.perf_counter()
    response = client.models.generate_content(
        model=MODEL,
        contents=[*history, user_message],
    )
    response_time = time.perf_counter() - start_time
    print(f"[time] response={response_time:.2f}s")

    usage = response.usage_metadata
    if usage is not None:
        print(
            f"[tokens] input={usage.prompt_token_count}, "
            f"output={usage.candidates_token_count}"
        )

    answer = response.text or ""
    history.extend([user_message, {"role": "model", "parts": [{"text": answer}]}])
    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    history: list[dict[str, object]] = []
    question = args.question

    while True:
        print(f"[質問] {question}\n")
        try:
            print(ask(question, history))
        except errors.APIError as e:
            print(api_error_message(e.code, e.message))
            raise SystemExit(1)

        question = input("\nFollow-up (or /quit): ").strip()
        if question.lower() in {"/quit", "quit", "exit"}:
            break


if __name__ == "__main__":
    main()
