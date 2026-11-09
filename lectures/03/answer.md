# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：When asked what “lecNN-start” means in AIE2026, the raw LLM incorrectly interpreted “NN” as “Neural Network” and suggested that the tag marks the beginning of a neural-network section. The agent correctly explained that it is a Git tag marking the starting code for a particular lecture, such as lec03-start. It also explained that students can start from this tag even if earlier exercises are unfinished, and cited Lecture 1.
- `--trace` で見えたツール呼び出し（ツール名と引数）：
For “LoRAとQLoRAの違いは？”:
  - search_glossary({'query': 'LoRA'})
  - search_glossary({'query': 'QLoRA'})

  For “第2回の内容から確認問題を1問出して”:
  - make_quiz({'lecture': 2})
    
- 1つの質問での LLM 呼び出し回数（`requests`）：Both traced runs used 2 LLM requests. In the LoRA/QLoRA run, the model requested two glossary searches, then used their results to answer. In the quiz run, it requested make_quiz, then used the returned question to respond. The runs used 2 and 1 tool calls, respectively.
- 追加したツールと、docstring に書いた説明：I added make_quiz(lecture: int) -> str in app/tools.py and registered it in app/agent.py using agent.tool_plain(tools.make_quiz).

The tool selects glossary entries belonging to the specified lecture, randomly chooses one term, and returns a question, its answer, and the lecture number as a JSON string. It returns an explanatory message if no terms match the lecture.The docstring explains that the tool returns one review question and its answer from a specified lecture, and should be used when a learner requests a review or confirmation question for that lecture. I verified that the agent called make_quiz({'lecture': 2}). The tool returned a question about overfitting and its definition. The agent displayed the question and invited the learner to think before revealing the answer. All 11 tests passed.

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
