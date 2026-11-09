# 第1回 解答

## 演習

- 講座に固有の質問（宿題の3レベル）へのモデルの回答（要約でよい）：
- 用語集の正しい意味と比べて気づいたこと：
- 表示できたトークン数（入力 / 出力）：

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
I first tried 3 models, namely (1) Gemini 3.8 Flash, (2) Gemini 3.6 Flash, and (3) Gemini 3.5 Flash-Lite to ask the question "What is LoRA?".

I also tried the Implementation task by asking in the chat how to modify the code to ask follow-up questions while keeping the conversation history. 

In ask.py, it suggested to modify the ask function to pass a history list to each Gemini request, then save deach successful user message and model response to that list. it the main() function to accept and reuse history.

Finally, I tried the advanced task by again using the chat to provide suggestion on how to measure response time. It ssugested to use the function time.perf_counter() from the time package.


- 結果：
A. Foundation
Gemini 3.8 Flash did not return any result: "モデルが混み合っています（503）。少し待ってから再実行してください。"

While both Gemini 3.6 Flash and Gemini 3.5 Flash-Lite both provided responses following a similar structure (i.e., definition, problems LoRA solves, how LoRA works, key benefits, and application), Gemini 3.6 Flash gave a more comprehensive and detailed explanation, including a numerical illustration, summary. By contrast, the explanation of Gemini 3.5 Flash-Lite is shallower but good enough for an overview.

B. Implementation
The suggested code by the Chat worked. It was able to implement the follow-up loop in ask.py and ran a mock session. When I was prompted to ask a follow-up or quit after asking "What is LoRA?", I asked "Provide an actual example of LoRA." It provided an actual application (i.e., Smart Agriculture - Vineyard Monitoring), including an illustrative scenario, how LoRA solves the problem, and the outcome.

C. Advanced
The code to record response time worked. Each request now pronts elpsed time alongside the existing input and output token counts.

- 気づき・疑問：
With respect to the Advanced Task, Gemini 3.6 Flash produced a more detailed and technical answer than Gemini 3.5 Flash-Lite for the prompt "What is LoRA?". 

However, it has higher token usage (6 input + 861 output = 867 tokens) than Gemini 3.5 Flash-Lite (6 input + 703 output = 709 tokens). It also has a longer response time (12.79s versus 3.00s). Since free-tier quotas are generally constrained by token usage and request limits, Flash-Lite is more economical for high-volume queries.

For Gemini 3.8 Flash, I wonder what causes the model to overwhelm. Is it the no. of users?


