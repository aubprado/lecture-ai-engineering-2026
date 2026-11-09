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

- 取り組んだレベル：基
- やったこと：  I tested whether removing the explicit requirement to search the
  glossary would change the agent's behavior.

  I first ran the following command with the original instructions:
    uv run python -m app.agent --trace "LoRAとQLoRAの違いは？"

  I then removed only this line from INSTRUCTIONS in app/agent.py:
  「用語や講座に固有のことを答える前に、必ず search_glossary で用語集を確認する。」

  This instruction requires the agent to check the glossary before
  answering about terms or course-specific matters.

  I saved the file and repeated the identical command. The model,
  registered tools, and tool docstrings were unchanged between runs.
- 結果：Both runs called the same tools in the same order:
  1. search_glossary({'query': 'LoRA'})
  2. search_glossary({'query': 'QLoRA'})

  Before: requests=2, tool_calls=2.
  After: requests=2, tool_calls=2.

  Both answers explained that LoRA trains small adapter matrices while
  keeping the base-model weights frozen, whereas QLoRA additionally
  quantizes the base-model weights to reduce memory use.
  Both cited Lecture 2. The wording differed slightly, but the main
  explanation and tool-use pattern remained the same.
- 気づき・疑問：Removing the explicit search requirement did not change tool use in
  this comparison. The search_glossary docstring still instructed the
  model to search before answering about AI engineering terms, which
  may explain why the searches continued.