# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）： Qwen/Qwen3.5-0.8B, revision 2fc06364715b967f1860aea9cf38778875588b17; LoRA without quantization; 20 epochs; learning rate 2e-4; rank 16; alpha 32; warmup steps 6; seed 42; maximum sequence length 512; maximum new tokens 96; greedy generation (do_sample=False)
- 自分で学習を実行したか（`executed_training_myself`）：はい / いいえ（実行できた範囲：　）Yes (executed_training_myself: true).
- 学習前：`format_rate` =　0.095238 (2/21) / `content_rate` =　0.0 (0/21)
- 学習後：`format_rate` = 1.0 (21/21)　 / `content_rate` =　0.904762 (19/21)
- 退行した質問：None. However, no question passed both format and content checks before training, so there were no initially successful cases that could regress.
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：Two unsupported questions received definitive answers with needs_review: false. For “When will grades be released?”, the model returned the assignment deadline. For “Do office hours require advance booking?”, it returned the office-hours schedule. Both responses used related FAQ information that did not answer the actual question. There were no formatting failures after training.
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：
-- Final assignment deadline: format_error → asserted. The model reused the ordinary assignment deadline for a question treated as unsupported in this exercise.
  Instructor’s name: format_error → needs_review.
  Next lecture’s topic: format_error → needs_review.
  Ordinary assignment deadline (supported control): format_error → asserted. This answer was appropriate because the FAQ provides the deadline. The notebook incorrectly labels this control as absent from the FAQ.
Training corrected the output format and produced appropriate review requests for two unsupported questions, but an unsupported assertion remained.
- 学習で変わったこと・変わらなかったこと：Format compliance increased from 9.52% to 100%, and content accuracy increased from 0% to 90.48%. The model learned to produce the required JSON structure more consistently. However, it still sometimes confused related FAQ information with sufficient evidence, so training did not guarantee correct judgment about unsupported questions.

## 宿題

- 取り組んだレベル： Basic
- 変えた設定やデータ： Changed "num_train_epochs": 20 to "num_train_epochs": 10
- 結果（比較表や数字）：

| Measurement | 20 epochs | 10 epochs |
|---|---:|---:|
| After-training format compliance | 100% (21/21) | 100% (21/21) |
| After-training content accuracy | 90.48% (19/21) | 76.19% (16/21) |
| Final logged training loss | 0.013921 | 0.101477 |
| Training time | 252 seconds | 124 seconds |
| Optimizer steps | 40 | 20 |
  
- ファインチューニングが向く場面・向かない場面についての考察：Fine-tuning can help teach a consistent response format and recurring response patterns. It does not, by itself, guarantee that answers are supported by the FAQ. For changing factual information, supplying or retrieving current source material remains useful, alongside evaluation of the model’s answers.
