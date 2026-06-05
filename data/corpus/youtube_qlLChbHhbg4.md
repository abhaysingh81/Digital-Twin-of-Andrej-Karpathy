# YouTube Transcript: qlLChbHhbg4

So before we get dive into some of the
material today uh on loss functions and
optimization I wanted to uh go over some
administrative things first. Uh just as
a reminder the first assignment is due
on next Wednesday. So you have roughly 9
days left. And just as a warning Monday
is holidays so there will be no class no
office hours. So plan out your time
accordingly uh to make sure that you can
complete the assignment in time. Of
course, you also have some late days
that you can use and allocate among your
assignments uh as you see fit. Okay, so
diving into the material. First, I'd
like to remind you where we are
currently. Last time we looked at uh
this problem of visual recognition and
specifically at image classification and
we were talking about the fact that uh
this is actually a very difficult
problem, right? So if you just consider
the cross productduct of all the
possible variations that we have to be
uh robust to when we recognize any of
these categories such as cat, it just
seems like such an intractable
impossible problem. And not only do we
know how to solve these problems now,
but we can solve this problem for
thousands of categories. And uh the
state-of-the-art methods work almost at
human accuracy or even slightly
surpassing it in some of those uh
classes. And it's also runs nearly in
real time on your phone. And so
basically and all of this also happened
in the last 3 years and also you'll be
experts by the end of this class on all
of this technology. So it's really cool
and exciting. Okay. So that's the
problem of image classification and
visual recognition. We talked
specifically about the datadriven
approach and the fact that we can't just
explicitly hardcode these classifiers.
So we have to actually train them from
data. And so we looked at the idea of
having different the training data
having different validation splits where
we test out our hyperparameters and a
test set that you don't touch too much.
We looked specifically at the example of
the nearest neighbor classifier and uh
so on and the k nearest neighbor
classifier and I talked about the CR10
data set which is our tow data set that
we play with uh during this class. uh
then I introduced the idea of uh this
approach that I termed parametric
approach uh which is really that we're
writing a function f from image directly
to the raw 10 scores if you have 10
classes and this parametric form we
assume to be linear first so we just
have f equals wx and we talked about the
interpretations of this linear
classifier the fact that you can
interpret it as matching templates or
that you can interpret it as these
images being in a very high dimensional
space and our linear classifiers are
kind of going in and u coloring this
space by class scores so so to speak.
And so um by the end of the class we got
to this picture where we suppose we have
a training example set of just three
images here along the columns and we
have some classes say 10 classes in C410
and basically this function f is
assigning scores for every single one of
these images uh with some particular
setting of weights which I've chosen
randomly here we get some scores out and
so some of these results are good and
some of them are bad. So if you inspect
the scores for example in the first
image you can see that the correct class
which is cat got a score of 2.9 and
that's kind of in the middle. So some uh
some classes here received a higher
score which is not very good. Some
classes received a much lower score
which is good for that particular image.
Uh the car was very well classified
because the class score of car was much
higher than all of the other ones and
the frog was not very well classified at
all. Right? So, we have this notion that
um for different weights, these
different weights work better or worse
on different images. And of course,
we're trying to find weights that give
us scores that are consistent with all
the ground truth labels, all the labels
in the data. And so, what we're going to
do now is so far we've only eyeballed
what I just described like this is good
or that's not so good and so on. But we
have to actually give it we actually
quantify this notion. we have to say
that this particular set of weights W is
say like 12 bad or 1.5 bad or whatever.
And then once we have this loss
function, we're going to minimize it. So
we're going to find W that gets us
lowest loss. And we're going to look
into that today. So we're going to look
specifically into how we can define a
loss function that measures this
unhappiness. And then we're actually
going to look at two different cases, a
SVM cost and a softmax cost or a cross
entropy cost. And then we're going to
look into the process of optimization
which is how do you start off with these
random weights and how do you actually
find very very good setting of weights
efficiently. Okay. So I'm going to
downsize this example so that we have a
nice working example to work with. Uh so
suppose we only had three classes
instead of you know tens of thousands
and we have these three images and these
are our scores for some set of W's and
we're going to now try to write down
exactly our unhappiness with this
result. So the first loss we're going to
look into is termed a multiclass SPM
loss. This is a generalization of a
binary support vector machine that you
may have seen already in different
classes. I think 229 covers it as well.
And so the setup here is that uh we have
the score function, right? So S is a
vector of class scores. These are our S
vectors. And there's a specific term
here loss equals to stuff. And I'm going
to interpret this loss now for you. So
that and we're going to see through a
specific example uh into why this
expression makes sense. Effectively what
the SVM loss is saying is that it's
summing across all the incorrect
examples. So all the all the it's
summing across all the incorrect scores
um classes. So for every single example
we have that loss and it's summing
across all the incorrect classes and
it's comparing the score that the
correct class received and the score
that the incorrect class received. J
minus S of Y I Y I being the correct
label plus one and then that's maxed of
zero. So what's going on here is we're
comparing the difference in the scores
and this particular loss is saying that
not only do I want the correct score to
be higher than the incorrect score, but
there's actually a safety margin that
we're putting on. We're put we're using
a safety margin of exactly one and uh
we're going to go into why one makes
sense um to use as opposed to some other
hyperparameter that we have to choose
there. And intuitively uh you can look
into notes for a much more rigorous
derivation of exactly why that one
doesn't matter. But intuitively to think
about this uh the scores are kind of
scale free because I can scale my w I
can make it larger or smaller and you're
going to get larger or smaller scores.
So really there's this free parameter of
these scores and how large or small they
can be that is tied to how large your
weights are in magnitude. And so these
scores are kind of arbitrary. So using
one is just an arbitrary choice to some
to some extent. Okay. So let's see
specifically how this expression works
with a concrete example. So here I'm
going to evaluate that loss for the
first example. So here we're computing
we're plugging in uh these scores. So we
see that we're comparing the score we
got for car which is 5.1 minus 3.2 which
is the correct class score and then
adding our safety margin of one and the
max of zero and that is really what it's
doing is it's going to be clamping
values at zero. Right? So if we get a
negative result we're going to just
clamp it at zero. So if you see for the
second class score the incorrect class
of frog 1.7 subtract it from 3.2 add a
safety margin and we
get3.9 and then when you work this
through you get a loss of 2.9. So
intuitively what you can see here the
way this worked out is intuitively the
cat score is 3.2. So according to the
SVM loss we what we would like ideally
is that the scores for all the incorrect
classes are up to at most 2.2. But the
car class actually had much higher much
higher score 5.1. And this difference in
what we would have liked which is 2.2
and what actually happened which is 5.1
is exactly this difference of 2.9 which
is how bad of a score outcome this was.
And um in the other case in frog case
you can see that the frog score was
quite a bit lower below 2.2. And so the
way that works out in the math is that
you end up getting a negative number
when you compare the scores and then the
max of zero clamps it at zero. So you
get a zero loss contribution for that
particular part and you end up with a
loss of 2.9. Okay. So that's the loss
for this first image. For the second
image, we're going to again do the same
thing. Plug in the numbers. We're
comparing the cat score to the car
score. So we get uh 1.3 - 4.9 add a
safety margin and the same for uh for
the other class. So when you plug it in,
you actually end up with a loss of zero.
And loss of zero intuitively is because
the car score here is it is true that
the car score is higher than all the
other scores for that image by at least
one. Right? That's why we got zero
score. Zero loss that is. So the
constraint was satisfied and so we get
zero loss. And in this frog case we end
up with a very bad loss because of
course the frog class received a very
low score but the other classes received
quite high score. So this adds up to an
unhappiness of 10.9. And now if we
actually want to combine all of this
into a single loss function, we're going
to do the relatively intuitive uh
transformation here where we just take
the average across all the losses we
obtain over the entire training set. And
so we would say that the loss at the end
when you average these numbers is 4.6.
So this particular setting of W on this
training
data gives us some scores which we plug
into the loss function and we given we
get an unhappiness of 4.6 with this
result. Okay. So I'm now going to ask
you a series of questions to kind of
test your understanding a bit about how
this works. Uh I'll get into questions
in a bit. Let me just pose my f my own
questions first. Um first of
all, what if that sum over there, which
is the sum over all the incorrect
classes of J, what if that was instead
sum over all the classes, not just the
incorrect ones. So what if we allowed J
to equal to Yi? Why am I actually adding
that small constraint in the sum over
there? You're adding one.
Sorry. Go ahead. You're adding the delta
instead of the one. Uh, yes. So, in
effect, what would have happened is the
reason that that's a J not equal to Yi
is if we allow J to equal to Yi, then
score of Yi cancel of Yi, you end up
with a zero. And really, what you're
doing is you're adding a constant of
one. So, if that sum was over all the
scores, then really we'd be just
inflating the loss by a constant of one.
So, that's why that's there. Um, second,
what if we used a mean instead of a sum?
Right? So, I'm summing up over all these
constraints. What if I use the
mean? Just like I'm using mean to
actually average over all the losses for
all the examples. What if I use the mean
over the scores, the score constraints?
Go ahead. You have too many classes that
would sort of dilute the loss possible.
So you're saying if there were too many
classes that would dilute the loss or
like the So you're right in that the
absolute value of the loss would be
lower.
It would actually just be a constant
factor. So it would be a constant
factor. Why? It would be the number of
cloud. You divide by the number of
clouds. That's right. Yeah. So this any
of these choices kind of don't matter
for your optimization, right? Uh some of
these choices matter, but yes. Uh so
basically what you're pointing out is if
we did actually do an average here, we'd
be averaging over the number of classes
here, but there's a constant number of
classes, say three in this specific
example. So that amounts to putting an a
constant of 1/3 in front of the loss.
And since we're always in the end, so
that would make the loss lower, just
like you pointed out. But in the end,
what we're always interested in is we're
going to minimize a W over that loss. So
if you're shifting your loss up by one
or if you're scaling it with a constant,
this actually doesn't change your
solutions, right? you're still going to
end up with the same optimal W's. So
these choices are kind of basically free
parameters. Uh doesn't matter. So for
convenience, I'm adding a J not equal to
Yi and I'm not actually taking a mean
although it's the same thing. And the
same also goes for us for whether or not
we average or sum across the examples.
Um okay, next question. What if we
instead used not the formulation over
there, but a very similar looking
formulation, but there's an additional
squared at the end. So we're taking the
difference between scores plus one this
margin and then we're squaring
that. Do we obtain the same or different
loss when you think do we obtain the
same or different loss in a sense that
if you were to optimize this and find
the best W do we get the same result
or not?
Yes. Yeah. Because you're thresholding
it at zero.
So, uh, I like the fact that it's
divided. You would in fact get a
different loss. Um, it's not as obvious
to see, but what, uh, one way to see it
is that we're not just clearly scaling,
um, we're not just clearly scaling, uh,
the loss up or down by a constant or
shifting it by a constant. We're
actually changing the difference. we
we're changing the trade-offs
nonlinearly in terms of how the SVM the
supervisor machine is going to go there
and trade off the different score
margins in different examples but it's
not obvious to see but basic it's not
very clear but I wanted to illustrate
that not all changes to this loss are
completely uh a noop and um the second
formulation here is in fact something we
call a squared hinge loss instead of the
one on top which we call hinge loss and
you can use two different it's kind of a
hyperparameter which one you use most
often you see the first formulation
that's what we use most of the time but
sometimes you can see data sets where
the squared hinge loss ends up working
better so that's something you play with
that's really a hyperparameter but it's
most often used uh form is the first one
let's also think about the scale of this
loss uh what is the min and the max
possible loss that you can achieve uh
with the multiclass SVM on on your
entire data set what is the smallest
value zero zero good is the highest
value
Yeah, it's infinite, right? So basically
these scores could be arbitrarily
terrible. So if your assigned score to
the correct example is very very small,
then you're going to get your loss going
to infinity. Okay. And one more question
uh which becomes kind of um important
when we start doing optimization.
Usually when we actually optimize these
loss functions, we start off with a
initialization of W that are very small
weights. So what ends up happening is
that the scores at the very beginning of
optimization are roughly near zero. All
of these are like small numbers near
zero. So what is the loss when all these
are near zero in this particular case?
That's right. Number of classes minus
one. So if all the scores are zero then
with this particular loss I put down
here and by doing an average across this
way we would have achieved a loss of
two. Okay. So this is not very
important. Where it's important is for
sanity checks when you're actually
starting optimization and you're
starting with very small numbers W and
you print out your first loss as you're
starting the optimization and you want
to make sure that you kind of understand
the functional forms and that you can
think through whether or not the number
you get makes sense. So if I'm seeing
two in this case then I'm happy that the
f the loss is maybe implemented
correctly but I'm not 100% sure but
certain certainly there's nothing wrong
with it right away. So, uh, it's
interesting to think about these. Um,
let's see. I'm going to go more into
this loss a tiny bit, but is there a
question in terms of this slide right
now? Go ahead. You're suming over J not
equal to Yi. Wouldn't it be more
efficient to not do that so that you can
take the matrix over the whole matrix
without asking you to remove every Oh
yeah. So the question is, and I was
asked to repeat the questions. Would it
be not efficient to actually not have
this ugly constraint ji because it makes
it more difficult to actually do these
easy vectorzed implementations of this
loss implementation? So that actually
predicts my next slide to some degree.
So let me just go into that. So here's
some numpy code for how I would write
out this loss function in vectorized
numpy code. So here we're evaluating li
in vectorzed numpy. We're getting a
single example here. So x is a single
column vector, y is an integer
specifying the label and w is our weight
matrix. So what we do is we evaluate the
scores which is just w * x. Then we
compute these margins which is the
difference between the scores we obtain
and the correct score plus one. So these
are numbers between zero and whatever.
And then see this additional line
margins at y equals
z. Why is that there?
It's the same as yeah exactly. So
basically I'm doing this efficient
vectorz implementation which goes to
your point and then I want to erase that
margin there because I'm certain that
margins at y currently is one and I
don't want to inflate uh my score and so
I'll set that to zero. Sorry, couldn't
we just subtract one at the end? Uh yes,
I suppose you could subtract one at the
end as well. Very slightly faster cash
flow. That's right. So we can optimize
this if we want, but we're not we're not
going to think about this too much. If
you're do if you do in your assignment,
that's very welcome for extra bonus
points. uh and then we're summing up
this margins and so we get lost in the
end.
Okay. Um going back to this slide, any
more questions about this uh
formulation? And by the way, this
formulation if you wanted to make it if
you actually write it down for uh just
two classes, you'll see that it reduces
to a binary support vector machine
loss. Okay, cool. Uh so we'll see a
different loss function soon and then
we're going to look at comparisons of
them as well. uh but for now actually so
at this point what we have is we have
this linear mapping uh to get scores and
then we have this loss function which I
have now written out in its full form
where we have these differences between
the scores uh plus one sum over the
incorrect classes and the sum and the
average across all the examples right so
that's the loss function right now I'd
like to convince you that there's
actually a bug with this loss function
in other words if I'd like to use this
loss on some data set in practice
um I might get some not very nice
properties. Okay, if this if this was
the only thing I was using by itself and
it's not completely obvious to see
exactly what the issue is. So I'll give
you guys a hint. Um in particular
suppose that we found the W such that
we're getting zero loss okay on some
data
set. And now the question is um is this
W uh
unique or phrased in another way can you
give me a W that would be different but
also definitely achieves a zero loss in
the back scale with constant
that's right and u so you're saying we
can scale it by some constant alpha and
in particular alpha must obey some
constraint
there than one you'd probably want it to
be yeah greater than one right so
basically what I can do is I can if I
change my weights and I make them larger
and larger all I would be doing is I'm
just create making this score difference
larger and larger as I scal W right
because of the linear loss form here so
basically that's not a very desirable
property because we have the this entire
subspace of W that is optimal and all of
them are according to this loss function
completely the same but intuitively
that's not like a very nice property to
have and so just to see this numerically
to convince yourself that this is the
case. I've taken this example where we
achieved previously zero loss there
before and now suppose I multiply my wi
twice uh I mean this is a very simple
math going on here but basically I would
be inflating all my scores by two times
and so their difference would also
become just larger so if all your score
differences inside the max of zero were
already negative then they're just going
to become more and more negative and so
you end up with larger and larger
negative values inside the maxis and
this just becomes zero all the time
right go ahead scale to be larger than
one.
Um, so alpha the scaling factor would
have to be larger than one because
uh let's see the margin of
yeah so there's that added margin of one
which is complicating things. Yep. Okay.
Uh another question.
Yeah. Would the scaling apply to the
bias part of W as well? Uh would the
scaling apply to this uh uh to the bias
part? So here I'm just I guess I'm not
assuming the bias for simplicity.
Um but yeah basically these scores are
wx plus b. So so you're just uh yeah
forget the bias and we're just scaling
the w by
itself. Okay cool. So the way to fix
this is intuitively we have this entire
subspace of W's and it all works the
same according to this loss function.
And what we'd like to do is we'd like to
have a preference over some W's over
others just based on intrinsic you know
what what do we desire of W to look like
forget what the data is just what what
are nice things to have about a W. And
so this introduces the notion of
regularization which we're going to be
appending to our loss function. So we
have an additional term there which is
lambda times a regularization function
of W. And the regularization function
measures the niceness of your W. Okay.
And so we don't only want to fit the
data but we also want W to be nice. And
we're going to see some um ways of uh
framing that and exactly why they make
sense. And intuitively what's going on
is regularization is a way of trading
off your training act your training loss
and your generalization loss on a test
set. So intuitively regularization is a
set of techniques where we're adding
objectives to the loss which will be
fighting with this guy. So this guy just
wants to fit your training data. And
that guy wants W to look some particular
way. And so they're fighting each other
sometimes in your objective because we
want to simultaneously to achieve both
of them. But it turns out that adding
these regularization techniques, even if
it makes your training error worse. So
we're not correctly classifying all the
examples. What you notice is that the
test set performance ends up being
better. And we'll see an example of why
that might be actually with the next.
For now I just wanted to point out in
the next slide but for now I just wanted
to point out that the most common form
of regularization is the what we call L2
regularization or weight decay. And
really what we're doing is suppose W in
this case is a 2D matrix. So I have two
sums over K and L the rows and columns.
But really it's just all the element
wise W's squared and we're just putting
them all into the loss. Okay. So this
this particular regularization it likes
W's to be uh zero right. So when W is
all zero then regularization is happy.
But of course W can't be all zero
because then you can't classify. So
these guys will fight each other. Um
there are different forms of
regularization with different pros and
cons. Uh we'll go into some of them much
later in the class. And uh I just like
to say for now that basically L2
regularization is the most common form
and that's what you'll use uh quite
often in this class as well. So now I'd
like to convince you I'd like to
convince you that this is a reasonable
thing to want out of a W that its
weights are small. So consider this very
simple cooked up example to get the
intuition. Suppose we have an example um
where we are in fourdimensional space
where we're doing this classification
and we have an input vector of just all
ones x and now suppose we have these two
candidate weight matrices or weight
single weights I suppose right now. So
one of them is 1 0 0 and the other is
0.25 25 everywhere. Since we have linear
loss functions, you'll see that their
effects are the same. So basically the
way we're evaluating score is by wx. So
the dotproduct with x is identical for
both of these. The scores would come out
both of these. But regularization would
strictly favor one of these over the
other. Which one would the
regularization cost favor? Even though
their effects are the same, which one is
better in terms of the regularization?
The second one. Right? And so the
regularization would tell you that even
though they're achieving the same
effects in terms of the data loss
classification down the road, we
actually significantly prefer the second
one. What's better about the second one?
Why is that a good idea to have?
Sorry, can you repeat that? It takes
account more of your x values.
That's correct. So well, that's one
that's the interpretation I like the
most as well. It takes into account the
most number of things in your X vector.
Right? So what this alterization wants
to do is it wants to spread out your W's
as much as possible so that you're
taking into account all the input
features or all the input pixels. It
wants to use as much of those as many of
those dimensions as it likes if it's
achieving the same effect uh intuitively
speaking. And so that's better than just
um focusing on just one input dimension.
It's just a nice
um it's something that often works in
practice basically just the way things
are data sets are
arranged and the properties that they
usually have statistically. Okay, any
questions about this? So regularization
good idea everyone is sold. Okay, great.
Uh so basically our losses will always
have this form where we we have the data
loss and then we'll also have a
regularization. It's a very common thing
to have in practice. Okay, I'm now going
to go into the second classifier, the
softmax classifier, and we'll see some
um differences between the uh support
vector machine and this softmax
classifier. In practice, these are kind
of like these two choices that you can
have, either SVM or softmax, the most
two commonly used linear classifiers.
Often you'll see that softmax classifier
is preferred. Uh and I'm not exactly
sure why because usually they end up
working about the same. And I just like
to mention that this is also sometimes
called multinomial logistic regression.
So if you're familiar with logistic
regression, this is just a
generalization of it into multiple
dimensions or in this case multiple um
classes, not just two. Was there a
question over there or Yeah. So I was
wondering on a higher level why you
would want to do regularization
um is it to truth which weight is better
given that they have the same laws.
Uh yes. So the question is why do we
want to use regularization basically? So
I don't think I sold it very well.
um if you're com suppose you have all
this entire subspace of waste that is
all achieving the same effects we'd like
to pick between them in some way and I
think what I'm arguing for is that
wanting low W's is a reasonable way to
pick among them and the L2
regularization will favor diffused W's
like this case here and one of the
intuitive ways in which I can try to
pitch why this is a good idea is that uh
diffuse weights basically
Um, see this W1 is completely ignoring
your inputs 2, three, and four, but W2
is using all of the inputs, right?
Because the weights are more diffuse.
And so intuitively, this just ends up
usually working better at um at test
time um because more evidence is being
accumulated into your decisions instead
of just one single evidence, one single
feature. And Paul, so you added as a
part of the song, right? That's right.
And so in this case, W2 would have a
higher value than W1. That's right. It
would have a higher loss. That's right.
So the the idea here is that these two
W1 and W2, they're achieving the same
effect. So this data loss suppose that
that's basically it doesn't care between
the two, but the regularization
expresses preference for them. And since
we have it in the objective and we're
going to end up optimizing over this
loss function. So we're going to find a
W that simultaneously accomplishes both
of those. And so we end up with W that
not only classifies correctly but we
also have this added preference that
actually we want it to be in we want it
to be diffuse as much as possible. Makes
sense. Awesome. Go ahead.
Um yes. So in this particular example L1
would also be indifferent. L1 has some
nice properties which I don't want to go
into right now. We might cover it later.
uh L1 um has some properties like a
sparityinducing
uh uh properties where if you end up
having L1's into your in your
objectives, you'll find that lots of W's
will end up being exactly zero for
reasons that we might go into later. And
uh that sometimes is like a feature
selection almost. Um and so L1 is
another alternative that we might go
into a bit more later.
Go ahead. Yeah. Doesn't the W1 on the
other slide have the nice propert isn't
it good that you're knowing some of the
um the features they're not actually
giving you a better loss. Yeah. So the
question is yeah so uh you're pointing
out that isn't it maybe a good thing
that we're ignoring features uh and just
using one of them.
Um
yeah so there's many technical reasons
why regularization is a good idea. I
wanted to give you just basic intuition.
Uh so maybe uh maybe I failed at that.
But uh yeah, I think that's a fair
point. Um
yeah, I'm not sure if I have a good
return. I would have to I might go
ahead. Couldn't you say that like
epsilon 0000 would do the exact same
thing as w1 or like would epsilon be a
really small number? So that but that
vector would do the exact same thing but
it would also have small much smaller
regularization.
Oh so you want to consider a different w
and you want it to look slightly
different from these two. I'm just
saying like
uh the previous question was like uh
isn't it good that we're ignoring
uh some value? So why why
would be Yeah. Isn't that a feature not
a bug that we're ignoring some inputs?
Yeah. Yeah. So, so I was saying that you
could just have like
01 000 as another W vector that would do
exactly the same thing as W1 in terms of
its decisions, but it
would just throw that out. I see. Okay.
Thanks. Um, yeah, I didn't want to to
dive too too much into this. There's
actually like an entire literature of
regularization and looking at the test
error and actually you know writing
theorems in in learning theory and you
saw some of that in 229 and there are
some results on why regularization is a
good case in in those areas and I don't
think I want to go into that and it's
also also beyond the scope of this
class. So for this class just uh alter
regularization will make your test error
better. Okay. So I'm going to go into
softmass classifier now which is this
generalization of logistic uh
regression.
Uh so the way the way this will work is
this is just a different functional form
for how loss is specified on top of
these scores. So in particular uh
there's this interpretation that softmax
classifier puts on top of these scores.
These are not just some arbitrary scores
and we want some margins to be met but
we have specific interpretation that is
maybe more um principled uh kind of from
a probabilistic point of view where we
actually interpret these scores not just
as these things that mean margins but
these are actually the unnormalized lock
probabilities that are assigned to
different classes. Okay, so we're going
to go into exactly what this means in a
bit. So these are unnormalized lock
probabilities of all the y's given the
image. So in other words, we are
assuming that if the scores are
unnormalized lock probabilities, then
the way to get probabilities of
different classes like class K is that
we take these the score, we exponentiate
all of them to get the um the
unnormalized probabilities and we
normalize them to get the normalized
probabilities. So we divide by the sum
over all the um exponentiated scores.
And that's how we actually get this
expression for a probability of a class
given the image. And so this function
here is called the softmax function if
you if you see it somewhere. Um it's the
e to the the element you're currently
interested in divided by the sum over
all exponentiated scores. Okay. And so
the way this will work basically is if
we're in this probabistic framework
where we are looking at we're deciding
that this is the probability of
different classes then it makes sense in
terms of what you usually want to do in
the setting. We have probability over
different classes. One of these is
correct. So we want to just maximize the
log likelihood of um for the loss
function and sorry we want to maximize
the log likelihood of the true class and
since we're writing a loss function we
want to minimize the negative log
likelihood of the true class. Okay so
you end up with a series of expressions
here. Really our loss function is we
want the log likelihood of the correct
class to be high. So negative of it want
to be low and the log likelihood is soft
max function of your scores. Let's look
at a specific example to make this more
clear. Um okay and here I've actually
like subbed in that expression so that
this is the loss negative log of that
expression. Let's look at how this
expression works and I think it will
give you a better intuition of exactly
what this is doing why what it's
computing. So suppose here we have these
scores that came out from our neural
network or from our linear classifier
and these are the unnormalized lock
probabilities. So as I mentioned we want
to exponentiate them first because under
this interpretation that gives us the
normalized probabilities and now
probabilities always sum to one. So we
have to divide by the sum of all of
these. So we add up these guys and we
divide to actually get probabilities
out. So under this interpretation we've
carried out the set of transformations
and what this is saying is that in this
interpretation the probability assigned
to this image of being a cat is 13% car
is 87% and frog is very unlikely 0%. So
these are the probabilities and now
normally in this setting you want to
maximize the lock probability because it
turns out that maximizing just the raw
probability is not as nice
mathematically. So normally you see
maximizing lock probabilities um and
then so we want to minimize the negative
log probability. So the correct class
here is cat which is only having 13% uh
chance under this interpretation. So
negative log of.13 gives
us89 and so that's the final um that's
the final loss that we would achieve for
this class here uh under this
interpretation of a of a soft softmax
classifier. So 09 for softmax. Okay, so
let's go over some examples. Uh let's go
over some questions now related to this
um to try to interpret exactly how this
works. First, what is the min and the
max possible loss with this loss
function? So that's the loss function.
What is the smallest value and the
highest
value? So I'll give you a chance to
think about this. What is the smallest
value that we can achieve?
Zero. And how would that happen?
Okay, good. So if your correct class is
getting probability of one, we're we
have a one which we're plugging into the
log and we're getting negative log of
one which is
zero and the highest possible loss
infinite. So just as with SVM we're
getting the same zero is minimum and
infinite is maximum. So infinite loss
would be achieved if you end up giving
your cat score very tiny probability and
then log of zero gives you negative
infinity. So negative that is just
infinite. Um so yeah so the same bounds
as SVM. Um and also this question
normally when we initialize W with
roughly uh small weights we end up with
all the scores that are nearly zero.
What ends up being the loss in this case
if you're doing sanity checks at the
beginning of your optimization what do
you expect to see as your first loss?
Oh yeah go ahead. log of one over number
of classes negative. Yeah, that's right.
So, it's negative log of one over number
of classes. So, you'd basically be
getting all zeros here, you get all ones
here. And so, here is one over the
number of classes and then negative log
of that ends up being your final loss.
So, actually for myself whenever I uh
run optimization, I sometimes take note
of my number of classes and I evaluate
negative log of one over number of
classes and I'm trying to see what is
the my first beginning loss that I
expect. And so when I start the
optimization, I make sure that I'm
getting roughly that. Otherwise, I know
something's maybe slightly off. I expect
to get something on that order.
Moreover, as I'm optimizing, I expect
that I go from that to zero. And if I'm
seeing negative numbers, then I know
from the functional form that something
very strange is going on, right? Because
you never actually expect to get
negative numbers out of this. Uh so
that's the softmax loss. I'll show you
one more slide and I'll take some
questions. Just to reiterate the
difference between them and really what
they look like is we have the score
function which gives us wx * b. we get
our scores vector and now the difference
is just how they interpret what these
scores coming out from this um f
function is. So either it's just random
scores no interpretation whatsoever. We
just want the large larger score the
correct score to be some margin above
the incorrect scores or we interpret it
to be these unnormalized log
probabilities and then in this framework
we first want to get the probabilities
and then we want to maximize the
probability of the correct classes or
the log of them and so that ends up
giving us the loss function for softmax.
So they start off with the same way but
they just happen to get a different
slight result. We'll go into exactly
what the differences of them are uh in a
bit. There are questions for now. So
uh these don't take significantly
different times amounts of time to
calculate right? Uh that's correct. So
they they take about the same time to
calculate for sure especially once you
have a comeet your classifier is near
instantaneous to evaluate. Most of the
work is done in doing all the
convolutions and so we'll see that the
classifier and especially the loss is
roughly the same. Of course um softmax
involves some exp and so on. So these
operations are slightly more expensive
perhaps but usually it completely washes
away compared to everything else you're
worried about which is all the
convolutions over the image.
Go ahead. What do we take uh function
even if the the final value tells us the
probability of values like 631 is the
highest number that that is more likely
to be answer
uh sorry I didn't catch your question
fully. Why do we have to take log
function at the end? Why do we want to
maximize log probabilities instead of
probabilities directly?
Um it turns out when you um so this is
partly covered in 229 when you do
logistic regressions and so on. If you
just want to maximize probability it
would it would be the exact same problem
because log is a monotonic function and
so maximizing the probability and
maximizing the log probability give you
the identical result. But in terms of
the math, everything comes out much
nicer looking when you actually put a
log there. But it's the exact same
optimization
problem. Okay, cool. Let's look at some
interpretations of these two and exactly
how they differ. So softmax versus SVM
and trying to give you an idea about one
property that actually is quite
different between the two. Um, so they
have these two different functional
forms. And now assume that we have these
three examples. all three examples and
suppose there are three classes, three
different examples and these are the
scores of these examples and for every
one of these examples the first class
here is the correct class. So 10 is the
correct class score and the other scores
are these guys either the first one,
second or third one. And now uh just
think about what these losses tell you
about how desirable these outcomes are
in terms of that w. Um and in particular
one way to think about it for example is
suppose I take this data point the third
one 10gative 100gative00 and suppose I
jiggle it like I I move it around a bit
in my input space. What is happening to
the losses um as I do that
like increases and decreases depending
on what direction you move it. Okay. Uh
do they so they increase and decrease as
I wiggle this data point around. Do they
both increase or decrease for the third
data point for example?
SVM remains uh SVM remains the same.
Correct. And why is that? It's because
the margin was met by a huge amount. So
there's this added robustness when I
take this data point and I shake it
around. The SVM is already very happy
because the margins were met by you know
we desire a margin of one and here we
have a margin of
109. So basically there's a huge amount
of margin. the SVM doesn't express a
preference over these examples where the
scores come out very negative then the
SVM adds no additional preference over
do I want these to be -20 or negative or
negative,000 the SVM won't care but the
S but the softmax could always see you
would always get an improvement for
softmax right so the softmax function
expresses preference for it wants these
to be negative 200 or 500 or thousand
all of them would give you better loss
right but the SVM at this point doesn't
care um and for the other examples. I
don't know if it's as um I mean that's
one clear distinction, right? So the SVM
has this added robustness to it wants
this margin to be met but beyond that it
doesn't micromanage your scores whereas
softmax will always want these scores to
be you know everything here nothing
there and so um that's one kind of very
clear difference between the two. Was
there a question? Go ahead. Yeah u maybe
I missed this but is there a is is the
margin that one is that a
hyperparameter? Is that something that
gets changed? Uh yes. So the margin of
one I mentioned very briefly that that's
not a hyperparameter. You can fix it to
be one. The reason for that is that
these scores they're um they kind of uh
the absolute values of those scores are
kind of uh they don't really matter
because my w I can make it larger or
smaller and I can achieve different size
scores and so um one turns out to work
better. And in the notes I have a longer
derivation where I go into details
exactly why u one is safe to choose. So
refer to that but I didn't want to spend
time on it in the lecture. So the notes
do justify not using zero there instead
of one. Oh so uh zero would be if you
wanted to use zero that would be
trouble. You can use any positive number
and that would give you an SVM. If you
use zero um that would look
different.
Um so one for example this added
constant there one property it gives you
when you actually go through the
mathematical analysis like say in the
SVM in CS229 is you'll see that it
achieves this max margin property where
uh the SVM will find that the best
margin uh when you actually have a plus
constant there combined with the L2
regularization on the weights. So you
want very small weights that meet a
specific margin and SVM will give you
this very nice max margin property that
I didn't really go into in this in this
uh lecture right now. But uh but
basically you do want the positive
number there otherwise uh things would
break.
Go ahead. Is there a reason we're
interpreting that exponential value as
like the probability? Is there a special
like reason to call it properties other
than that it's a negative?
Um yeah is there so you're saying we're
taking this exponential of these numbers
that are real numbers and we're
interpreting them as probabilities. uh
we're kind of free to so with this
you're getting these scores out and it's
up to you to to endow them with
interpretation right we can have
different losses in this specific case I
showed you multiclass SVM there's in
fact multiple versions of a multi-class
SVM you can fiddle around with exactly
the loss expression and one of the uh
one of the interpretations we can put on
this course is that there are these
unnormalized um lock probabilities they
can't be normalized because they just
can't we have to normalize them
explicitly because there's no constraint
that the output of your function will be
normalized and uh they have to be they
can't be probabilities because you're
outputting just these real numbers that
that can be positive or negative. So uh
we interpret them as lock probabilities
and and that requires us to exponentiate
them. It's a very bad kind of uh
explanation of it because um but
anyways go on to what you just said. So
that's actually pretty similar to both
my statistics. If you interpret score as
energy and then that's exactly the
probability that the energy is being
occupied. Uh yeah, that's right. So
there are really cool connections to
physics and how they actually think
about the loss functions. Um for them
energy and loss is like kind of an
equivalent as well. Go ahead. We're
talking about the SPM versus soft max.
Uh you know once it goes beyond a
certain margin you know like of two or
three and you're going to exponentiate
it the difference you will get in soft
max is going to be vanishingly small.
Uh so you're talking about um so say for
example in this case
and now you're arguing about say this
one. Yeah. Okay. If if 100 - 100 goes to
- 110, it's still not going to really
change your probabilities a lot. Uh
that's right. So what you're saying, I
think if I understand correctly, is the
softmax would already look at this and
give zero probabilities here and one
here, right? So you're saying if I
jiggle this around, not nothing is
changing. I think the difference is the
loss would definitely change for
softmax, even though it wouldn't change
a lot, but it would definitely change.
So softmax still expresses preference,
whereas SVM gets you identically zero.
Right? My question is about the
magnitude of that preference. Isn't it
just not very big? Uh yeah. Yeah. So the
preference wouldn't be very big but
there definitely is preference. But in
practice basically this distinction uh
the intuition I'm trying to give you is
that the SVM has a very
local part of the space in which you're
classifying that it cares about and
beyond it it's invariant and a softmax
kind of is a function of the full data
cloud. cares about it cares about all
the points in your data cloud not just
you know there's like a small class here
that you're trying to separate out from
everything else a softmax will kind of
consider the full data cloud when it's
fitting your uh plane and SVM will just
want to separate out that tiny piece
from the immediate part of the data
cloud uh something like that in practice
when you actually run these they kind of
give nearly identical results almost
always so uh really what I'm trying to
I'm not trying to um pitch one or the
other I'm just trying to give you this
notion that you're in charge of the loss
function. You get some scores out and
you can write down nearly any
mathematical expression as long as it's
differentiable into what you want your
scores to be like. And there are
different ways of actually formulating
this and I've shown you two two examples
that are common to see in practice. But
uh in pra and we can put down any losses
for what you want your scores to be and
that's a very nice feature because we
can optimize over all of it. Okay, let
me show you an interactive web demo at
this point. Uh
Jifer All right, let's see if
this So this is an interactive demo in
our class page. Uh you can find it at
this URL. I wrote it uh last year and I
had to show it to all of you guys to
justify uh spending one day on
developing all this. Okay, but so I'm
not sure. Last year not too many people
looked at this. So okay, but basically
this is one day of my life. You should
all look at this.
Uh so what we have here is a two
dimensional problem with three classes
and I'm showing here three classes. Each
has three examples over here in two
dimensions and I'm showing the three
classifiers. Here is the level set. So
for example, the red classifier is has
scores of zero along the line. And then
I'm showing the arrows in which the
scores increase. Right? Here's our W
matrix. So as you recall this W matrix,
the rows of that W matrix are the
different classifiers. So we have the
blue classifier, red green classifier
and red classifier. And we have both the
weights for both the X and the Y
component and also the biases. And then
here we have the data set. So we have
the X and the Y coordinate of all the
data points, their correct label and the
scores as well as the loss achieved by
all those data points right now with
this setting of W. And so you can see
that I'm taking the mean over all the
loss. So right now our data loss is
2.77. Regularization loss for this W is
3.5. And so our total loss is 6.27.
Okay. And so basically you can fiddle
around with this. So let's see. So as I
change my W, you can see that here I'm
making my W, one of the W's bigger. And
you can see what that does
in in there or the bias. You can see
that the bias basically shifts these
hyperplanes. Um okay. And then what we
can do is we can what we're going
towards this is kind of a preview of
what's going to happen. We're getting
the loss here and then we're going to do
back propagation which is giving us the
gradient over how we want to adjust
these W's in order to make the loss
smaller. And so what we're going to do
is this repeated updates where we start
off with this W but now I can improve uh
I can improve this set of W's. So when I
do a parameter
update, this is actually using these
gradients which are shown here in red
and it's actually making a tiny change
to every single parameter according to
this gradient. Right? So as I do
parameter update, you can see that the
loss here is decreasing especially the
total loss here. So the loss just keeps
getting better and better as I do
parameter update. So this is the process
of optimization that we're going to go
into in a bit.
So I can also start a repeated update
and then basically we keep improving
this W over and over until our loss it
started off was like roughly three or
something like that. So now our mean
loss over the data is 0.1 or something
like that and we're correctly
classifying all these all these points
here.
Um, so I can also
uh randomize randomize W. So it just
kind of knocks it off and then this
always converges to the exact same point
through the process of
optimization. And um you can play here
with the regularization as well. You
have different forms of a loss. So the
one I shown you right now is the Western
Watkins SVM formulation. There's a few
more SVM formulations and there's also
softmax here. Um, and you'll see that
when I switch to softmax loss, our
losses look different. And um, but the
solution ends up being roughly the same.
So when I switch back to NSVM, you know,
the hyper planes move around a tiny bit,
but really it's it's mostly the same.
Um, and so anyways, so this is the step
size. So this is um, how much how big of
steps are we making when we get the
gradient on how to improve things. So
randomized parameters, we usually start
with a very big the step size. These
scenes are jiggling trying to separate
out these data points. And then over
time, what we're going to be doing in
optimization is we're going to decrease
our update size. And this thing will
just, uh, slowly converge in on the
parameters that we want in the end. And
so uh, so you guys can play with this
and you can see how these scores jiggle
around and what the loss is. And if I
stop a repeated update, what here is,
um, you can also drag these points, but
I think on the Mac it doesn't work. So
hold on. So when I try to drag this
point, it disappears.
So but it works on a desktop. So I don't
I don't want to go in and figure out
exactly what happened there. But uh so
you can play with this. Okay,
cool. So I'm going to go into the
process optimization now uh just to give
you a sense of what this looks like.
Uh so we have this f function. We have
these two formulations that I've shown
you and the full loss is achieved as the
mean loss over data plus regularization.
This is one other diagram to show you
how what this looks like. Uh I don't
think it's a very good diagram and
there's something confusing about it
that I can't remember from last year but
basically you have this data X and Y
your images and your labels and there's
W and we're computing the scores and
getting the loss and the regularization
loss is only a function of the weights
not of the data. Um and basically what
we want to do now is we don't have uh
control over the data set right that's
given to us but we have control over
that W and as we change that W the loss
will be different. So for any W you give
me I can compute the loss and that loss
is linked to how well we're classifying
all of our examples. So wanting a low
loss means we're classifying them very
very well on the training data and then
we're crossing our fingers that that
also works on on some test data that we
haven't seen. So here's one strategy for
optimization. It's a random search. So
because we can evaluate loss for any
arbitrary W, what I can afford to do,
and I'm not sure if I don't want to go
through this in full detail, but
effectively I randomly sample W's and I
can check their loss and I can just keep
track of the W that works best. Okay, so
that's an amazing process of
optimization of guess and check. And it
turns out if you do this, I think I
tried a thousand times. If you do this
thousand times and you take the best W
you found at random and you run it on
your CR10 data test data you end up with
about 15.5% accuracy and since there are
10 classes in CR the the mean um the
baseline is at 10% that's your chance
performance so 15.5 there's some signal
actually in DW and so uh
state-of-the-art is at 95 which is a
comeet so we have some gap to close over
the next two weeks or so
uh so this is so don't use this just
because it's on the slides. Um, one
interpretation of exactly what this
looks like, this process of optimization
is that we have this loss landscape,
right? This loss landscape is in this
highdimensional W space. So here we I
guess if you're 3D and your loss is the
height. Uh, then you only have two W's
in this case and you're here and you're
blindfolded. That's your current W. You
can't see where the valleys are, but
you're trying to find low loss. And so
you're blindfolded and you have an
altitude meter and so you can tell what
your loss is at any single point and
you're trying to get to the bottom of
the valley, right? And um so that's
really the process of um optimization.
And what we've shown you what I've shown
you so far is this random uh
optimization where you teleport around
and you just check your altitude, right?
So not the best idea. So, we're going to
do instead is we're going to use what I
refer to already as a gradient or really
we're just computing the slope across in
every single uh direction. So, I'm
trying to compute the slope and then I'm
going to go downhill. Okay, so we're
following the slope. Uh I'm not going to
go into too much detail on this, but
basically there's an expression for the
gradient uh which is defined like that.
Um there's a derivative um calculus 101
um definition in multiple dimensions. If
you have a vector of derivatives that's
referred to as the gradient, right? So
because we have multiple dimensions,
multiple ws, we have a gradient vector.
Okay, so this is the expression and in
fact we can numerically evaluate this
expression before I go into the analytic
solution. I'll just show you what that
would look like to evaluate a gradient
at some W. So suppose we have some
current W and we're getting some loss.
Okay, what we want to do now is we want
to get an an idea about the slope at
this point. So we're going to basically
look at this formula and we're just
going to evaluate it. So I'm going to go
in the first dimension and I'm going and
really what this formula is telling you
to do is evaluate x plus your altitude
at x plus h subtracted from f of x and
divide by h. What that corresponds to is
me being on this landscape taking a
small step in some direction and looking
whether or not my foot went up or down.
Right? That's what the gradient is
telling me. So suppose I took a small
step and the loss there is 1.25. Then I
can use that formula with a finite
difference approximation where I've used
a small h to actually derive that the
gradient here is -2.5. The slope is
downwards. So I took a step the loss
decreased. So this is sloping downwards
in terms of the loss function. So -2.5
in that particular dimension. So now I
can do this for every single dimension
independently. Right? So I go into the
second dimension. I add a small amount.
So I step in a different direction. I
look at what happened to the loss. I use
that formula and it's telling me that
the gradient the slope is 6 and I can do
that in the third dimension and I get
the gradient there. Okay. So what I'm
referring to here is I'm basically
evaluating the nu the numerical gradient
which is using this finite difference
approximation where for every single
dimension independently I can take a
small step I can evaluate the loss and
that tells me the slope is it going
upwards or downwards for every single
one of these parameters. And so uh this
is um evaluating numerical gradient. The
way this would look like is uh Python
function here. It looks ugly because it
turns out it's slightly tricky to
iterate over all the w's. But basically
we're just looking at f of x plus h
comparing to f of x and dividing by h
and we're getting the gradient. Now the
problem with this is if you want to use
the numerical gradient then of course we
have to do this for every single
dimension to get a sense of what the
gradient is in every single dimension.
And right um when you have a comnet you
have hundreds of millions of parameters
right so we can't afford to actually
check the loss in hundreds of millions
of parameters before we do a single step
so this approach where we would try to
evaluate the gradient numerically is
first of all it's approximate because
we're using finite difference
approximations but second it's also
extremely slow because I need to do a
million checks of the loss function on
my comnet before I know what the
gradient is and I can take a parameter
update
So very slow approximate turns out that
this is also silly right because the
loss is a function of w as we've written
it out and really what we want is we
want the gradient of the loss function
with respect to w and luckily we can
just write that down thanks to these
these guys uh do you actually know who
those guys are by the way
enlighten that's right do you know which
is which because they look the
same they're just uh yeah they look
remarkably similar but basically Newton
and Lightnit uh sort of two inventors of
calculus there's actually controversy
over who really invented calculus um and
these guys fought each other over it but
basically calculus is this powerful
hammer and so what we can do is instead
of doing this silly thing where we're
evaluating numerical gradient we can
actually use calculus and we can write
down an expression for what the gradient
is of that loss function in the weight
space. So basically instead of fumbling
around and doing this is it going up or
is it going down by checking the loss I
just have an expression where I take the
gradient of this and I can s simply
evaluate what that entire vector is. So
that's the only way that you can
actually run this in practice right we
can just have an expression for here's
the gradient we could do a step and so
on. So in summary basically numerical
gradient approximate slow but very easy
to write uh because you're just uh doing
this very simple process for any
arbitrary loss function I can get the
gradient vector for analytic gradient
which is you actually do calculus it's
exact no finite uh approximations it's
very fast but it's errorprone because
you actually have to do math right so in
practice what you see is we always use
analytic gradient we do the calculus we
figure out what the gradient should be
but then you always check your implement
mentation using a numerical gradient
check as it's referred to. So I will do
all my calculus. I figure out what the
loss function should be. I write an
expression for the gradient. I evaluate
it uh in my code. So I get a an analytic
gradient and then I also evaluate a
numerical gradient on the side and that
takes a while but you enumerate your you
evaluate your numerical gradient and you
make sure that those two are the same
and then we say that you pass the
gradient check. Okay. So that's what you
see in practice whenever you try to
develop a new module for your neural
network. you write out loss, you write
the backward pass for it that computes
the gradient and then you have to make
sure to gradient check it just to make
sure that your calculus is correct. And
then I've already referred to this
process of optimization which we saw
nicely in the web demo where we have
this loop when we optimize where we
simply evaluate the gradient on your
loss function and then knowing the
gradient we can perform a parameter
update where we change this w by a tiny
amount. In particular, we want to update
with the negative step size times the
gradient. The negative is there because
the gradient tells you the direction of
the greatest increase. It tells you
which way the loss is increasing and we
want to minimize it which is where the
negative is coming from. We have to go
in the negative gradient direction. Step
size here is a hyperparameter that will
cause you a huge amount of headaches.
Step size or learning rate. This is the
most critical parameter to basically
worry about uh that uh really there's
two that you have to worry about the
most. The step size or learning rate and
there's uh the weight regularization
strength lambda that we saw already.
Those two parameters are really the two
largest headaches and that's usually
what we cross validate over. Uh was
there a question in the back by the way?
Yeah, I was just going to ask is that a
weight gradient vector a unit vector or
it's not that gradient is just gradient.
It tells you the slope in every single
direction. Um, and then we just take a
step size step of it. Um, so the process
of optimization in this weight space is
you're somewhere in your W, you get your
gradient and you march some amount in
the direction of the gradient. Um, but
you don't know how much. So that's the
step size. And you saw that when I
increased the step size in the demo,
things were jiggling jittering around
quite a lot, right? There was a lot of
energy in the system. That's because I
was taking huge jumps all over this
basin. So here the loss function is
minimal at the blue part there and it's
high in the red parts. So we want to get
to the uh lowest part of the basin. This
is actually what the loss function looks
like for an SVM or for logistic
regression. These are convex problems.
So it's really just a bowl and we're
trying to get to the bottom of it. But
this bowl is like 30,000 dimensional. So
that's why it takes a while. Um okay, so
we take a step and we reevaluate the
gradient and repeat this over and over.
In practice, uh there's this additional
uh part I wanted to mention where we
don't actually evaluate the loss for the
entire training data set. In fact, what
we do um is we only use what's called a
mini batch gradient descent where we
have this entire data set, but we sample
batches from it. So we sample say like
uh say 32 examples out of my training
data. I evaluate the loss and the
gradient on this batch of 32 and then I
do my parameter update and I keep doing
this over and over again. And basically
what ends up happening is if you only
sample very few data points from your
training data, then your estimate of the
gradient of course over the entire
training set is kind of noisy because
you're only estimating it based on a
small subset of your data. But it allows
you to step more. So you can do more
steps with approximate gradient or you
can do few steps with exact gradient.
And in practice what ends up um working
better is if you use mini batch and uh
it's much more efficient of course and
uh it's impractical to actually do full
batch gradient descent. So common mini
batch sizes 32 64 128 256. This is not
usually a hyperparameter we worry about
too much. You usually set it based on
whatever fits on your GPU. We're going
to be talking about GPUs in a bit. But
they have finite amount of memory. Say
about like 6 GB or 12 GB if you have a
good GPU. And you usually choose a batch
size such that a small mini batch of
examples fits in your memory. So that's
how usually that's determined. It's not
a hyperparameter that actually matters a
lot in in a in an optimization sense. Go
ahead. If you wanted to use momentum on
the step size, could you still do it
with the mini batch update? Yeah, for
sure. And we're going to get to momentum
in a bit. But if you wanted to use
momentum, then uh yeah, this is just
fine. We always use mini batch gradient
descent with momentum. Very common to
do. Uh so just to give you an idea about
what this looks like in practice if I'm
running optimization over time and I'm
looking at the loss evaluated on just a
small mini batch of data and you can see
that basically my loss goes down over
time on these many batches from the
training data. Uh so as I'm optimizing
I'm going downhill. Now of course if I
was doing full batch gradient descent so
this was not just mini batches sampled
from the data you wouldn't expect as
much noise. You just expect this to be a
line that just goes down. But because we
use mini batches, you get this noise in
there because some mini batches are
better than others. But over time, they
kind of all go down over time. Is there
a question?
Shouldn't the graph look like it
decreases like greatly in the beginning?
Yes. So you're wondering about the shape
of this loss function. You're used to
maybe seeing more rapid improvement
quicker. These loss functions come in
different shapes, sizes. Uh so uh it
really depends. It's not necessarily the
case that a loss function must uh look
very sharp in the beginning although
sometimes they do. They have different
shapes. For example, it also matters on
your initialization. If I'm careful with
my initialization, I would expect less
of a jump. Um but if I initialize very
incorrectly, then you would expect that
that's going to be fixed very early on
in the optimization. We're going to get
to some of those parts, I think, uh much
later. I also wanted to show you a a
plot of
um the effects of learning rate on your
loss function. And this the learning
rate is the step size. Basically, if you
have very high learning rates or step
sizes, you start thrashing around in
your W space. And so either you don't
converge or you explode. If you have a
very low learning rate, then you're
barely doing any updates at all. So it
takes a very long time to actually
converge. Um, and if you have a high
learning rate, sometimes you can
basically get kind of stuck in a bad
position of a loss. So these loss
functions kind of you need to get down
to the minimum. So if you have too much
energy and you're stepping too quickly,
then you don't have you don't allow your
problem to kind of settle in on the
smaller local minima in your objective.
In general, when you talk about neural
networks and optimization, you'll see a
lot of handwaving because that's the
only way we communicate about these
losses and basins. So just imagine like
a big basin of loss and there are these
like smaller pockets of smaller loss and
so if you're thrashing around then you
can't settle in on the smaller loss
parts and converge further. So that's
why learning rate is no good and so you
need to find the correct learning rate
which will cause you a lot of headaches
and what people do most of the time is
sometimes you start off with a high
learning rate so you get some benefits
and then you decay it over time. So you
start off with high and then we decay
this learning rate over time as we're
settling in on a good
solution. And um I also wanted to point
out we'll go into this in much more
detail but the way I'm doing the update
here which is how do you use the
gradient to actually modify your W
that's called an update parameter update
there are many different forms of doing
it this is the simplest way which we
refer to as just SGD simplest uh
stoastic gradient descent but there are
many formulas such as momentum that was
already mentioned in momentum you
basically imagine as you're doing this
optimization you imagine keeping track
of this velocity so as I'm stepping I'm
also keeping track of my velocity. So if
I keep seeing a positive gradient in
some direction, I will accumulate
velocity in that direction. So I don't
need so I'm going to go faster in that
direction. And so there are several
formulas we'll look at them shortly in
the class but ad arm prop atom all
commonly used. Um so just to show you
effect of different um what these look
like these different choices and what
they might do in your loss function.
This is a figure from uh Alec.
Um so here we have a loss
function and these are the level curves
and we start off optimization over there
and we're trying to get to the basin and
different update formulas will give you
better or worse convergence in different
problems. So you can see for example
this momentum in green it built up
momentum as it went down and then it
overshot and then it kind of go back
goes back and this SGD takes forever to
converge in red. That's what I presented
you so far. So, SGD takes forever to
converge and there are different ways of
actually performing this parameter
update that are more or less efficient
in the case of optimization. Yeah. So,
we'll see much more of this soon. Uh I
also wanted to mention at this point
slightly shifting gears uh I wanted to
go slightly into I've explained now
basically linear classification. We know
how to set up the problem. We know there
are different loss functions. We know
how to optimize them. So, we can kind of
do linear classifiers at this point in
the class. I wanted to mention that I
want to give you a sense of what
computer vision looked like before
comats came about so that you have a bit
of historical perspectives because we
used uh linear classifiers all the time
but of course you don't use linear
classifiers on the raw original image
because that's a pixel uh you don't want
to put linear classifiers on pixels we
saw all the problems with it like you
have to cover all the modes and so on.
Uh so what people used to do is they
used to compute all these different
feature types of images and then you
compute different descriptors and
different feature types and you get
these
statistical summaries of what the image
looks like, what the frequencies are
like and so on. And then we concatenated
all those into large vectors and then we
piped those into linear
classifiers. So different feature types,
all of them concatenated and then that
went into linear classifiers. That was
usually the pipeline. So just to give
you an idea of really what these feature
types were like, one very simple feature
type you might imagine is just a color
histogram. So I go over all the pixels
in the image and I bin them and to say
uh how many bins are there for different
colors depending on the hue of the
color. And so you can imagine this is
kind of like one statistical summary of
what's in the image. It's just the
number of colors in each bin. So this
would become one of my features that I
would eventually be concatenating with
many different feature types. uh another
kind of um and so basically the
classifier if you think about it the
linear classifier can use these features
to actually perform the classification
because the linear classifier can like
or dislike seeing lots of different
colors in the image with positive or
negative weights. Uh very common
features also included things like what
we call sift and hog features. Basically
these were you go in local neighborhoods
in the image and you look at whether or
not there are lots of edges of different
orientations. So are there lots of
horizontal edges or vertical edges? We
make up histograms over that. And so
then you end up with just this summary
of what kinds of edges are where in the
image and you concatenate all those
together. There was different lots of
different uh feature types that were
proposed over over the years just LBP
texton lots of different ways of
measuring what kinds of things are there
in the image and statistics of them. And
then we had these pipelines called bag
of words pipelines um where you look at
different points in your image. You
describe a little local patch with uh
some scheme that you come up with like
looking at the frequencies or looking at
the colors or whatever. And then we came
up with these dictionaries for okay
here's the stuff we see in images like
there's lots of high frequency stuff or
low frequency stuff in blue and so on.
So you end up with these centrids using
CIS of what kind of stuff do we see in
images and then we express every single
image as uh statistics over how much of
each thing we see in the image. So for
example this image has lots of high
frequency green stuff. So you might see
some feature vector that basically will
have a high value in high frequency and
in green. And then what we did is we
basically took these feature vectors we
concatenated them and put a linear
classifier on them. So really um the
context for what we were doing is as
follows. What it looked like mostly in
computer vision before roughly 2012 was
that you take your image and you have a
step of feature extraction where we
decided what are important things to you
know compute about an image different
frequencies different bins and we
decided on what are interesting features
and you'd see people take like 10
different feature types in every paper
and just concatenate all of it. Just
just dump all of it. you end up with one
giant feature vector over your image and
then you put a linear classifier on top
of it just like we saw right now and so
you train say a linear SVM on top of all
these feature types and what we're
replacing it uh since then we found that
what works much better is you start with
the raw image and you think of the whole
thing you're not designing some part of
it in isolation of what you think is a
good idea or not we come up with an
architecture that can simulate a lot of
those different features so to speak and
since everything is just a single
function we don't just train the top of
it on top of the features but we can
actually train all the way down to the
pixels and we can train our feature
extractors effectively. So that was the
big innovation in how you approach this
problem is we try to eliminate a lot of
hand engineered components and we're
trying to have a single differentiable
blob so that we can fully train the full
thing starting at the raw pixels. So
that's where historically um this is
coming from and what we'll be doing in
this
class. Uh and so next class we'll be
looking specifically at this problem of
we need to compute analytic gradients
and so we're going to go into back
propagation which is an efficient way of
computing analytic gradient and so
that's backdrop and you're going to
become good at it and then we're going
to go slightly into neural networks.
That's it.