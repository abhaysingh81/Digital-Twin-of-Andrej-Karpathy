🎬 Video: State of GPT | BRK216HFS
🔗 Source: [youtube.com](https://youtube.com/watch?v=bZQun8Y4L2A)
📅 Saved on June 5, 2026
🐿️ Created with [savemarkdown.co](https://www.savemarkdown.co)

---

## Overview
Andrej Karpathy, a founding member of OpenAI, outlines the four-stage recipe for training GPT assistant models: pretraining, supervised finetuning (SFT), reward modeling, and reinforcement learning from human feedback (RLHF). He then delves into effective strategies for leveraging these models for applications, emphasizing prompt engineering techniques that compensate for the cognitive differences between human brains and LLMs, and concludes with practical recommendations and current limitations.

## Key Points
*   **Four Stages of GPT Training:** The process involves pretraining on vast datasets, supervised finetuning with high-quality prompt-response pairs, reward modeling based on human preferences, and reinforcement learning guided by these rewards.
*   **Base Models vs. Assistant Models:** Base models complete documents, while assistant models answer questions, achieved through SFT and RLHF.
*   **Prompt Engineering is Crucial:** LLMs lack human-like internal monologue, self-reflection, and explicit knowledge of their own strengths/weaknesses, requiring sophisticated prompting to simulate these "System 2" capabilities.
*   **Advanced Prompting Techniques:** Chain-of-Thought, Self-Consistency, Self-Reflection, Tool Use, and Retrieval-Augmented Generation (RAG) significantly improve LLM performance.
*   **Fine-tuning Considerations:** While prompting is powerful, fine-tuning (especially parameter-efficient methods like LoRA) can be beneficial for specific applications, though RLHF remains complex research territory.
*   **LLM Limitations:** Models are prone to bias, hallucination, reasoning errors, knowledge cut-offs, and various attacks, necessitating human oversight and use in low-stakes applications.

## Detailed Summary

### Introduction to GPT Training (0:21)
Andrej Karpathy introduces the talk, divided into two main parts: how GPT assistants are trained and how to use them effectively for applications. The training recipe is still rapidly evolving.

### The Four Stages of Training GPT Assistants (0:46)
The training process consists of four serial stages:
1.  **Pretraining**: Builds a "base model."
2.  **Supervised Finetuning (SFT)**: Creates an SFT model.
3.  **Reward Modeling**: Trains a reward model.
4.  **Reinforcement Learning (RLHF)**: Refines the model using the reward model.

#### 1. Pretraining: Building the Base Model (1:23)
This stage is the most computationally intensive, accounting for 99% of compute time and flops, using thousands of GPUs over months.
*   **Data Collection (1:59)**: Involves internet-scale datasets (e.g., CommonCrawl, C4) mixed with high-quality sources like GitHub, Wikipedia, Books, and Stock Exchange data, sampled proportionally.
*   **Tokenization (2:43)**: Raw text is converted into sequences of integers (tokens) using algorithms like Byte Pair Encoding, a lossless translation.
*   **Hyperparameters (3:23)**:
    *   Vocabulary size: ~10,000s of tokens.
    *   Context length: 2,000-100,000 tokens (max integers GPT considers).
    *   Parameters: LLaMA (65B) vs. GPT-3 (175B). LLaMA is more powerful due to longer training (1.4 trillion tokens vs. 300 billion). Model power shouldn't be judged solely by parameter count.
    *   Training cost: LLaMA 65B trained with 2,000 GPUs for 21 days cost several million dollars.
*   **Pretraining Objective (4:57)**: The transformer predicts the next token in a sequence, given the preceding tokens. It processes data in batches, packing documents and delimiting them. The model's weights are updated based on the probability of the correct next token (lower loss means higher probability). Training progresses from random outputs to coherent, consistent samples over time (e.g., Shakespeare example).

#### Evolution of Base Models & Prompting (8:06)
*   **GPT-1 Era: Fine-tuning (8:06)**: Early models (GPT-1) were fine-tuned for specific downstream tasks (e.g., sentiment classification) using small datasets, leveraging the general representations learned during pretraining.
*   **GPT-2 Era: Prompting (9:09)**: It was discovered that models could perform tasks through "prompt engineering" by tricking them into completing "fake documents" (e.g., few-shot prompting for QA). This shifted focus from fine-tuning to prompting.
*   **Base Models are Not Assistants (10:32)**: Base models are document completers. They don't inherently "answer" questions but continue patterns. To make them act as assistants, specific prompting (e.g., "Here's a poem about bread and cheese:") or few-shot human-assistant dialogue formats are needed, though this is unreliable.

#### 2. Supervised Finetuning (SFT) (11:32)
*   **Data Collection (11:39)**: Human contractors generate high-quality prompt-response pairs (tens of thousands). These responses follow extensive labeling instructions (helpful, truthful, harmless).
*   **Training (11:58)**: The base model undergoes language modeling on this new, low-quantity, high-quality Q&A dataset.
*   **Result (12:11)**: An SFT model, which functions as an actual assistant to some extent (e.g., Vicuna-13B, Koala).

#### 3. & 4. Reward Modeling & Reinforcement Learning from Human Feedback (RLHF) (12:59)
This pipeline further refines SFT models.
*   **Reward Modeling (13:16)**:
    *   **Data Collection**: Humans rank multiple completions generated by the SFT model for a given prompt. This comparison task is easier for humans than generating ideal responses.
    *   **Training**: A separate neural network (the reward model) is trained to predict a scalar "reward" score for a given prompt and completion, consistent with human rankings.
*   **Reinforcement Learning (RL) (15:15)**:
    *   **Process**: The SFT model is updated using the fixed reward model. The language modeling loss for generated tokens is weighted by the reward score from the reward model. High-scoring completions are reinforced, while low-scoring ones are discouraged.
    *   **Result**: An RLHF model, which is highly preferred by humans (e.g., ChatGPT, GPT-4).
*   **Why RLHF Works Better (17:12)**: The asymmetry between generating a good response (hard for humans) and judging/comparing multiple responses (easier for humans) makes human feedback through comparisons a more efficient way to leverage human judgment.
*   **Limitations of RLHF Models (18:40)**: While preferred by humans, RLHF models can have lower entropy than base models, leading to less diverse outputs. Base models are sometimes better for open-ended generation tasks (e.g., generating Pokemon names).

#### Current State of Assistant Models (19:41)
*   **Ranking**: GPT-4 is currently the top model, followed by Claude, GPT-3.5 (all RLHF). Other models like Vicuna and Koala are SFT models.

### Effectively Using GPT Assistant Models (20:15)

#### Human Cognitive Process vs. LLM (20:27)
Karpathy illustrates the difference using an example of generating a sentence like "California's population is 53 times that of Alaska." Humans engage in a complex internal monologue involving self-knowledge, tool use (Wikipedia, calculator), reflection, and self-correction. LLMs, in contrast, are token simulators that process each token with roughly equal computational effort, lacking inherent self-awareness or reflection. They do not know what they don't know or correct mistakes without explicit instruction.

#### LLM "Cognitive Advantages" (23:43)
*   **Vast Fact-based Knowledge**: Stored in billions of parameters.
*   **Perfect Working Memory (Finite)**: Whatever fits in the context window is immediately and losslessly accessible via self-attention.

#### Prompting to Bridge the Cognitive Gap (24:27)
Prompt engineering aims to simulate human "System 2" thinking (slow, deliberate planning) within LLMs.
*   **"Tokens to Think" (Chain of Thought) (24:45)**: Spread reasoning over more tokens. Techniques like few-shot examples showing step-by-step thinking or simply prompting "Let's think step-by-step" improve performance on reasoning tasks.
*   **Self-Consistency / Multiple Samples (25:46)**: Sample multiple completions for a prompt and then use a process (e.g., voting, selection) to find the best one, mimicking human ability to try again. LLMs can get "unlucky" and go down blind alleys in a single sample.
*   **Self-Reflection / Self-Correction (26:40)**: Explicitly ask the LLM to check its own work (e.g., "Did you meet the assignment?"). GPT-4, for instance, often "knows" it failed but won't correct itself unless prompted.
*   **Recreating System 2 Thinking with Glue Code (27:28)**: Advanced techniques like Tree of Thought (maintaining multiple completions and scoring them), React (Thought-Action-Observation sequence), and AutoGPT (recursive task breakdown) use Python glue code to string together multiple prompts and algorithms, mimicking human planning and reflection. This is analogous to AlphaGo's Monte Carlo Tree Search.
*   **LLMs Imitate, Not Necessarily Succeed (30:16)**: LLMs are trained on data with varying quality. To elicit high-quality outputs, explicitly ask for it (e.g., "to be sure we have the right answer," "You are a leading expert on this topic," "Pretend you have IQ 120"). Avoid overly high IQ prompts (e.g., 400) which might lead to out-of-distribution or role-playing responses.
*   **Tool Use (32:02)**: Integrate external tools like calculators, code interpreters, or search. Explicitly inform the LLM about its weaknesses (e.g., mental arithmetic) and instruct it on how and when to use these tools.
*   **Retrieval-Augmented Generation (RAG) (32:54)**: Augment the LLM's context window with relevant external documents (e.g., LlamaIndex). This is crucial because LLMs have perfect but finite working memory; loading pertinent information improves performance significantly, similar to humans referencing textbooks.
*   **Constraint Prompting (34:35)**: Techniques (e.g., Microsoft's Guidance) force LLMs to output in specific formats (e.g., JSON) by clamping token probabilities, ensuring structured and usable outputs.

#### Fine-tuning Models (35:20)
*   **Accessibility**: Fine-tuning is becoming more accessible with techniques like Parameter-Efficient Fine-Tuning (PEFT) such as LoRA, which only trains small, sparse parts of the model, making it cheaper and allowing for low-precision inference on clamped parts. Open-source base models like LLaMA also contribute to this.
*   **Caveats**: Fine-tuning is technically involved, requires human or synthetic data pipelines, slows iteration cycles, and RLHF in particular is highly unstable and difficult research territory, not recommended for beginners.

### Recommendations and Limitations (37:11)

#### Default Recommendations (37:11)
1.  **Achieve Top Performance**:
    *   Use GPT-4 (most capable).
    *   Craft very detailed prompts with extensive context and instructions.
    *   Retrieve and add relevant context (RAG).
    *   Experiment with few-shot examples (show, don't just tell).
    *   Leverage tools and plugins.
    *   Think in multi-prompt chains and reflection loops rather than single Q&A interactions.
2.  **Optimize Performance (Cost)**:
    *   After exhausting prompt engineering, consider fine-tuning (SFT) for your application, but expect slower iteration.
    *   Avoid self-implementing RLHF due to its complexity and instability.
    *   For cost optimization, explore lower-capacity models or shorter prompts where appropriate.

#### LLM Limitations (39:12)
LLMs currently have significant limitations:
*   Bias
*   Fabrication/Hallucination of information
*   Reasoning errors
*   Struggles in certain application classes
*   Knowledge cut-offs (e.g., September 2021)
*   Susceptibility to attacks (prompt injection, jailbreak, data poisoning)

#### Use Cases (39:54)
Karpathy recommends using LLMs in:
*   Low-stakes applications.
*   Combined with human oversight.
*   As sources of inspiration and suggestions (co-pilots), not fully autonomous agents.

### Conclusion (40:11)
GPT-4 is an amazing artifact with vast knowledge and capabilities in math, code, and more. A thriving ecosystem is building around it. Its power is accessible with simple API calls. Karpathy shares an inspirational message generated by GPT-4 for the Microsoft Build audience, highlighting its proficiency in such tasks.

## Quotes
*   "You shouldn't judge the power of a model by the number of parameters that it contains." (4:17)
*   "Basically these transformers are just like token simulators, they don't know what they don't know." (23:21)
*   "These transformers need tokens to think." (25:04)
*   "LLMs don't want to succeed, they want to imitate. You want to succeed, and you should ask for it." (30:23)
*   "If you don't ask it to check, it's not going to check by itself, it's just a token simulator." (27:17)

## Key Takeaways
1.  **Understand the LLM's "Brain":** Recognize that LLMs are advanced token predictors, not human-like thinkers. They lack inherent self-reflection, tool-use intuition, or explicit knowledge of their limitations.
2.  **Master Prompt Engineering First:** Before considering fine-tuning, invest heavily in sophisticated prompt engineering. This includes providing detailed instructions, few-shot examples, explicitly asking for high-quality outputs, and breaking down complex tasks.
3.  **Compensate for LLM Weaknesses:** Actively prompt LLMs to "think step-by-step," encourage multiple samples for self-consistency, instruct them to self-reflect and check their work, and integrate external tools (calculators, search) for tasks where LLMs are weak.
4.  **Leverage Context with RAG:** Provide relevant external information to the LLM's context window (Retrieval-Augmented Generation) to significantly improve factual accuracy and performance.
5.  **Fine-tuning is an Advanced Tool:** Supervised fine-tuning (especially with PEFT methods like LoRA) is becoming more accessible and can optimize models for specific needs, but RLHF remains a complex, research-level endeavor.
6.  **Use LLMs Responsibly:** Be aware of inherent limitations like bias, hallucination, and security vulnerabilities. Deploy LLMs in low-stakes scenarios, always with human oversight, viewing them as powerful co-pilots rather than fully autonomous agents.

---

*Saved markdowns are formatted and summarized for [LLM Wikis](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)*.
