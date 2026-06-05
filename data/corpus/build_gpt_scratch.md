
# Let's Build GPT From Scratch

The goal of this tutorial is to build a GPT-like model from scratch.
We're going to start with a simple bigram language model and work up to the full transformer.

## The Setup

First, let me define what we're doing. We have a text corpus (I'll use Shakespeare).
We want to train a model that can generate text character by character, or token by token.

**This is the essence of what GPT is doing — it's a sequence model predicting the next token.**

## Step 1: Tokenization

For simplicity, let's use character-level tokenization:

```python
# read the corpus
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# all unique characters
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))  # !$&', -.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
print(vocab_size)  # 65

# tokenizer: simple char-to-int mapping
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

## Step 2: Self-Attention — The Heart of the Transformer

The key insight is **communication between tokens**. Every token needs to look at the other tokens
and decide what information to aggregate.

```python
class Head(nn.Module):
    """One head of self-attention — the fundamental building block."""
    
    def __init__(self, head_size):
        super().__init__()
        self.key   = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)    # (B, T, head_size)
        q = self.query(x)  # (B, T, head_size)
        
        # Scaled dot-product attention
        # "affinities" — how much does each token attend to each other token?
        wei = q @ k.transpose(-2, -1) * (k.shape[-1] ** -0.5)  # (B, T, T)
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))  # causal mask
        wei = F.softmax(wei, dim=-1)  # normalize: weights sum to 1
        wei = self.dropout(wei)
        
        # Weighted aggregation of values
        v = self.value(x)  # (B, T, head_size)
        out = wei @ v       # (B, T, head_size)
        return out
```

Notice: the `tril` mask is what makes this a **decoder** (causal) model.
Tokens can only look *back* in time, never forward. At inference time, this doesn't matter —
we generate left to right anyway.

## Why Attention Works

Think about it from first principles. Each token emits:
- A **query**: "what am I looking for?"
- A **key**: "what do I have to offer?"  
- A **value**: "what information will I actually pass if attended to?"

The dot product of Q and K gives you the affinity. Softmax normalizes it.
Then we do a weighted sum of V. **It's a differentiable, learnable lookup table.**

The network is just learning to route information between tokens in a task-relevant way.
It's not magic, it's just matrix multiplications with a masking trick.
