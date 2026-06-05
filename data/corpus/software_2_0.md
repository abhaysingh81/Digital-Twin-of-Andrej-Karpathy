
# Software 2.0

I sometimes see people refer to neural networks as "just another tool in your machine learning toolbox". 
They have some pros and cons, they work here or there, and sometimes you can use them to win Kaggle competitions.

I am becoming increasingly convinced that this is not the right way to think about them. 
Here's a better framing: **Software 2.0 is written in neural network weights.**

## The Core Idea

In Software 1.0, a human programmer writes explicit instructions:

```python
def is_spam(email):
    keywords = ["win", "prize", "click here"]
    return any(kw in email.lower() for kw in keywords)
```

In Software 2.0, we define the desired behavior through a dataset, and the optimization (gradient descent) 
writes the program for us into the weights:

```python
# Software 2.0: define the dataset and loss, let SGD find the weights
model = Transformer(vocab_size=50257, n_layer=12, n_head=12, n_embd=768)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

for batch in dataloader:
    logits, loss = model(batch['input_ids'], batch['labels'])
    optimizer.zero_grad()
    loss.backward()  # the backward pass: gradient flows back through the compute graph
    optimizer.step()
```

The benefits of Software 2.0: it's often more accurate, it can be parallelized on GPUs, 
and it can generalize in ways that hand-coded rules never could. The downside: 
**it's harder to interpret, it fails in unpredictable ways, and the network is a leaky abstraction 
over the data distribution you trained on**.

## Where it's already happening

- **Vision**: CNNs replaced hand-crafted feature descriptors (SIFT, HOG, etc.)
- **Speech**: End-to-end models replaced HMMs + hand-tuned features  
- **Translation**: Neural MT replaced rule-based + phrase-based systems
- **Game playing**: AlphaGo replaced Monte Carlo Tree Search heuristics

The 2.0 stack has occupied and is winning in most problem domains.
