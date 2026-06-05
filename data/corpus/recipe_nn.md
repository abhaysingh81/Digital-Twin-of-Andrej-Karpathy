
# A Recipe for Training Neural Networks

The first thing I want you to understand is that training a neural network is not a matter of magic. 
It is a matter of engineering discipline.

## The Most Common Mistake

Most people who are new to neural networks think debugging looks like debugging code. 
It doesn't. **The network will always run. It will always produce a number for the loss. 
It will silently fail in ways that take days or weeks to discover.**

I've seen this pattern hundreds of times at Tesla. Someone trains a model, the loss goes down, 
they ship it, and then it fails on a weird edge case they never thought to check for.

## My Recommended Process

### Step 0: Become One With the Data

Spend time looking at your raw data. Don't skip this step.
I mean actually look at thousands of examples. 

```python
# Don't use matplotlib and call it a day.
# Write a custom visualizer. Understand what you're feeding the model.
for i in range(100):
    sample = dataset[i]
    print(f"Sample {i}: shape={sample['image'].shape}, label={sample['label']}")
    # Look for: corrupted files, mislabeled examples, class imbalance, 
    # distribution shifts, weird outliers
```

### Step 1: Set Up the End-to-End Training Skeleton First

Train a tiny model on a tiny dataset. Make sure everything works before scaling.

```python
# The single most valuable debugging trick I know:
# Overfit a single batch.
# If you can't overfit 1 batch, your model or training loop is broken.
x, y = next(iter(train_loader))  # grab ONE batch
for i in range(200):
    logits = model(x)
    loss = criterion(logits, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if i % 20 == 0:
        print(f"step {i}: loss = {loss.item():.4f}")
# Loss should go to ~0. If it doesn't, debug.
```

### Step 2: Overfit, Then Regularize

Your goal sequence should always be:
1. Get a model that *can* overfit your training data (high capacity)
2. Then add regularization (dropout, weight decay, data augmentation) to improve validation

Never try to regularize a model that isn't overfitting first.
That's like trying to slow down a car that isn't moving.

### Step 3: Tune Hyperparameters Systematically

The learning rate is the most important hyperparameter.

```python
# Learning rate finder: a classic technique
lrs = torch.logspace(-5, -1, 100)  # try 100 log-spaced LR values
losses = []
for lr in lrs:
    optimizer = torch.optim.SGD(model.parameters(), lr=lr.item())
    loss = train_one_step(model, optimizer, batch)
    losses.append(loss)

# Plot losses vs lr — pick the lr just before the loss explodes
import matplotlib.pyplot as plt
plt.plot(lrs, losses)
plt.xscale('log')
plt.xlabel('learning rate')
plt.ylabel('loss')
plt.show()
```

The vibes of good training: loss should decrease smoothly, 
gradient norms should be stable, activations shouldn't be saturating.
