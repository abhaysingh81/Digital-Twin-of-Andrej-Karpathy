# YouTube Transcript: gYpoJMlgyXA

um how are you guys doing by the way
with the assignment our most have you
finished anyone finished put up your
hands okay good so we're doing decent
okay good I'll be holding up make up
office hours right after this class
assignment two will be released tomorrow
or day after tomorrow we haven't fully
finalized the date we're still working
on it and we're changing it from last
year and so we're in process of
developing it and we are hope to have it
as soon as possible it's meaty but
educational so you do want to get
started on it ASAP once it's released
we might be adjusting the due date for
some into because it is slightly larger
and yeah so so we'll be shuffling some
of the these things around and also the
grading scheme all this stuff is kind of
just tentative and subject to change
because we're still trying to figure out
the course it's still relatively new and
a lot of it is changing so those are
just some heads-up items before we start
now in terms of your project proposal by
the way which is due in roughly ten days
I wanted to just bring up a few points
because you'll be thinking about your
project and some of you might have some
misconceptions about what makes a good
or bad project so just to point out a
few of them the most common one probably
is that people are hesitant to work with
datasets that are small because they
think that commnets require a huge
amount of data to Train and this is true
there's hundreds of millions of
parameters in a continent and they need
training but actually for your purposes
in the project this is kind of a myth
this is not something you have to worry
about a lot you can work with smaller
datasets and it's okay the reason it's
okay is that we have this process that
we'll go into much more detail down the
later in the class called fine-tuning
and the thing is that in practice you
rarely ever train these giant
convolutional networks from scratch you
almost always do this pre training and
fine-tuning process so the way this will
look like is you almost always take a
convolutional network you trained on
some large data set of say images like
say on image net huge amount of data and
then you're interested in some other
data set right there and you can't train
your comment on your small data set so
we'll train it here and then we'll
transfer it over there and the way this
transfer works like is so here's a
schematic of a convolutional neural
network we start with the image on top
and we'll go through a series of layers
down to a classifier so you're used to
this but we haven't of course talked
about the specific layers here but we
take that image net
pre-trained network we trained on
imagenet and then we chop off the top
layer the classifier we chop that off
take it away and we train the entire
convolutional network is a fixed feature
extractor and so you can put that
feature extractor on top of your new
data set and you're just going to swap
in a different layer that performs the
classification on top and so depending
on how much data you have you're only
going to train the last layer of your
convolutional network or you can do fine
tuning where we actually back propagate
through some portions of the comment and
if you have more data you're going to do
back propagation deeper through the
network and in particular this
pre-training step on image net people do
this for you so there's a huge amount of
people who've trained convolutional
networks over long periods of time weeks
on different data sets and then they
upload the weights of the ComNet online
so there's something called the cafe
model Zoo for example and these are all
these convolutional net works that have
been pre trained on large data sets they
already have lots of the parameters
learned and so you just take this around
then you swap in your data set and you
fine-tune through the network so
basically if you don't have a lot of
data that's okay and you just take a
preacher in combat and you just
fine-tune it and so don't be afraid to
work with smaller data set that's going
to work out ok the second thing that we
solve some problems with last time is
that people think they have infinite
compute and this is also a myth I just
like to point out don't be overly
ambitious in what you propose these
things take a while to train you don't
have too many GPUs you're going to have
to do hyper air optimization there's a
few things you have to worry about here
so we had some projects last year where
people proposed projects of training on
very large data sets and you just won't
have the time so be mindful of that and
yeah you'll get a better sense as we go
through the class and what is or is not
possible given your computer constraints
ok so we're going to dive into lectures
are there any administrative things that
I may be left out that you'd like to ask
about ok good so we're going to dive
into the material we have quite a bit of
it today so just a reminder we're
working in this framework of many bad
stochastic gradient descent for training
of neural networks and basically it's a
four-step process training a neural
network is as simple as 1 2 3 4 you
sample your data so a batch of your data
from a data set you forward it through
your network to compute the loss you
back propagate to compute your grade
ian's and then you do a parameter update
where you tweak your weights slightly in
the direction of the gradient and so
when you end up repeating this process
then really what this comes down to is
an optimization problem where in the
weight space we're converging into areas
of the weight space where you have low
loss and that means you're correctly
classifying your training center and we
saw that these neural networks can get
very large and I flash this image of a
neural Turing machine basically these
are huge computational graphs and we
need to do back propagation through them
and so we talked about intuitions of
back propagation and the fact that it's
really just a recursive application of
chain rule from back of the circuit to
the front where we're changing gradients
through all the local operations we
looked at some implementations of this
concretely with the forward-backward api
on both a copy to a computational graph
and also in terms of its nodes which
also implement the same api and do
forward propagation and back propagation
we looked at specific examples in torch
and cafe and I drew this analogy that
these are kind of like your little
blocks these layers or gates are your
little blocks from which you build out
the entire combinational networks then
we talked about neural networks first
without the brain stuff and basically
what that amounts to as we're making
this F which goes from your image to
class course more complex and then we
looked at neural networks from the brain
stuff perspective where this is a crude
analogy of a neuron and what we're doing
is we're stacking these URLs in layers
okay so that's roughly what we're doing
right now and we're going to talk in
this class about this process of
training neural networks effectively
okay so we're going to go into that
before I dive into the details of it I
just wanted to kind of pull out and give
you a zoomed out view of a bit of a
history of how this field evolved over
time so if you try to find where this
field where it comes from when were the
personal networks proposed and so on you
probably will go back to roughly 1960
where Frank Rosenblatt in 1957 was
playing around with something called
perceptron and the perceptron basically
it ended up being this implementation in
hardware so they all had to like they
didn't just write code right they
actually had to build these things out
from circuits and electronics in these
times for the most part and so basically
the perceptron roughly was this funk
here and it looks very similar to what
we're familiar with it's just a W X plus
B but then the activation function which
were used to as a sigmoid that
activation function was actually a step
function it was either 1 or 0 it was a
binary step function and so since this
is a binary step function you'll notice
that this is non differentiable
operation so they were not able to back
propagate through this in fact the
concept of back propagation for training
neural networks had to come much later
and so they came up with these binary
stepwise functions perceptron and they
came up with these learning rules and so
this is an kind of an ad hoc specified
learning rule that tweaked the weights
to make the desired outcome from the
perceptron match the true of the true
desired values but there was no concept
of a loss function there was no concept
of back propagation is these ad hoc
rules which when you look at them they
kind of almost do background but it's
kind of funny because of the step
function which is not differentiable and
then people started to stack these so in
roughly 1960 with the advent of Adeline
and Madeline by Woodrow and Huff they
started to take these perceptron like
things and stack them into the first
multi-layer perceptron networks and this
was still all done in this electronics
analogy and actually building out from
hardware and but still there's no back
propagation at this time this was all
these rules that they've come up with in
terms of like thinking about trying to
flip bits and seeing if it works better
or not and it was kind of a there was no
view of back propagation at this time
and so roughly in 1960 people got very
excited and building out these circuits
and they thought that you know this
could go really far we can have these
circuits that learn you have to remember
that back then the concept of
programming was very explicit you write
a series of instructions for a computer
and this is the first time that people
who are thinking about this kind of
data-driven approach where you have some
kind of a circuit that can learn and so
this was at the time a huge conceptual
leap that people are very excited about
unfortunately these networks would not
actually end up working very well right
away
so in terms of 1960 for example they got
slightly overexcited
and over-promised and then slightly
under delivered and so throughout the
period of 1970s actually the field of
neural networks was very quiet and not
much research has been done the next
boost actually came about roughly in
1986 and in 1980
people there was this influential paper
that basically is the first time that
you see back propagation like rules in a
nicely presented format and so this is
real hard Hinton and Wilson and they
were playing with multi-layer
perceptrons and this is the first time
when you go to the paper where you
actually see something that looks like
back propagation and so at this point
they already discarded this idea of ad
hoc rules and they formulate the lochs
function and talked about back
replication and gradient descent and so
on and so this time people got excited
again in 1986 because they felt that
they now had a principled nice credit
assignment kind of scheme by back
propagation and they could train
multi-layer networks the problem
unfortunately was that when they tried
to scale up these networks to make them
deeper or larger they didn't work very
well compared to some of the other
things that might be in your machine
learning toolkits and so they just did
not give very good results at this time
and training would get stuck and that
propagation was basically not working
very well especially if you wanted to
have large deep networks and this was
the case for actually roughly 20 years
where again there was less research on
your own networks because somehow it
wasn't working very well enough and you
couldn't train deep nets and in 2006 the
research was research was again
reinvigorated with a paper in science by
Hinton and Ann Russell ocarina select
enough I can't say his name sorry but
basically what they found here was this
was roughly the first time where you can
actually have like say a 10 layer neural
network that trains properly and what
they did was instead of training all the
layers like ten layers by
backpropagation at a single pass they
came up with this unsupervised pre
training scheme using what's called
restricted Boltzmann machine and so what
this amounts to is you train your first
layer using an unsupervised objective
and then you train your second layer on
top of it and then third and fourth and
so on and then once all of these are
trained then you put them all together
and then you start back propagation then
you start the fine-tuning step so it was
a two step process of first we do the
Spree training stepwise through the
layers and then we plug them in and then
back propagation works and so this was
the first time where back propagation it
needed basically this initialization
from the unsupervised retraining
otherwise they would not work out of
like from scratch and we're going to see
why in this lecture it's kind of tricky
to get these deep networks to train from
scratch using just back wrap and you
have to really think about it
and so it turned out later that you
actually don't need this a surprise
process you can just train with backdrop
right away but you have to be very
careful with initialization and they
used sigmoid networks at this point and
sigmoid are just not a great activation
function to use and so basically
backdrop works but you have to be
careful in how you use it and so this
was in 2006 so a bit more researchers
kind of came back to the area and it was
rebranded as deep learning but really
it's still neural networks synonymous
but it's a better word for uh PR and so
basically at this point things started
to work relatively well and people could
actually train these deeper networks now
still not too many people paid attention
and when people started to really pay
attention was roughly I think around
2010 and 2012 so specifically in 2010
there were the first really big results
where neural networks really worked
really well compared to everything else
that you had in your machine learning
toolkit like say uh kernels or SVM's and
so on and this was specifically in the
speech recognition area where they took
this on G mm-hmm framework and they
swapped at one part and subbed in the
neural network and that neural network
gave them huge improvements in 2010 and
this was worked on Microsoft and so
people start to pay attention because
this was the first time neural networks
really gave a large improvements and
then we saw that again in 2012 where it
played out even more dramatically in in
the domain of visual recognition in
computer vision where basically we took
this 2012 Network by Alice kuchizuke
Ilya sutskever and Geoff Hinton and
basically it crushed all the competition
from all the features and there was a
really large improvement from these
neural networks that we witnessed and
that's when people really start to pay
attention and that's since then the
field has kind of exploded and there's a
lot of area done in this field now and
so we'll go into details I think a bit
later in a classroom why it started to
work really in 2010 it's a combination
of things but I think it's we got we
figured out better ways of initializing
of getting these things to work of
activation functions and we had GPUs and
we had much more data and so really a
lot of the stuff before didn't quite
work because it was just not there in
terms of compute data
and some of the ideas just needed a
tweaking okay
and so that's rough a historical setting
so we basically went through
over-promising under the luring
over-promising under the reloading and
now it seems like things are actually
starting to work really well and so
that's where we are at this point okay
so I'm going to no doubt into the
specifics and we'll see exactly we'll
actually dive into neural networks and
how you train them properly so the
overview of what we're going to cover
over the course of next two lectures is
a whole bunch of independent things so
I'll just be kind of peppering you with
all these little areas that we have to
understand and see what people do in
each case and we'll go through them the
pros and cons of all choice is how you
actually properly train these neural
networks in our real-world data sets so
the first thing we're going to talk
about is activation functions as I
promised I think a lecture so ago so
activation function is this function f
at the top of the neuron and we saw that
it can have many different forms so
sigmoid 10h relu these are all different
proposals for what these activation
functions can look like we're going
through go through some pros and cons
and how you think about what an
activation what are good desirable
properties of an activation function so
historically the one that has been used
the most is the sigmoid non-linearity
which looks like this
so it's basically squashing function it
takes a real-valued number squashes it
to be between 0 & 1 and so the first
problem with the sigmoid is that as was
pointed out a few lectures ago there's a
problem that saturated neurons which are
neurons that output either very close to
0 or very close to 1 those neurons kill
gradients during back propagation and so
I'd like to expand on this and show you
exactly what this means and this
contributes to something that will go
into called the vanishing gradient
problem so let's look at a sigmoid gate
in the back in the circuit it received
some value X and Sigma of X comes out
and then in backprop we have DL by D
Sigma and we'd like to back drop it
through the sigmoid gate to using chain
rule so that we have DL by DX at the end
and you can see that through chain rule
basically tells us to multiply those two
quantities and so think about what
happens when this sigmoid gate receives
input of either negative 10 or 0 or 10
it computes some value and
and it's getting some gradient from the
top and what happens to that gradient as
you backdrop through the circuit in any
of these cases what is the possible
problem in some of these cases so okay
so you're saying that the gradient is
very low when X is negative 10 or 10 and
the way to see this is basically we have
this local gradient here that we'll be
multiplying with this gradient there's
local gradient defy the Sigma by DX when
you're at negative 10 you can see that
the gradient is basically zero because
the slope at this point is zero and
gradient at 10 will also be near zero
and so the issue is that your gradient
will drop in from here but if your
neuron is saturated so it basically
either output it zero or I'd put it 1
then the gradient will be killed it'll
just be multiplied by a very tiny number
and gradient flow will stop through them
through the sigmoid neuron so you can
imagine if you have a large network of
sigmoid neurons and many of them are in
a saturated regime where they're either
0 or 1 then gradients can't back
propagate through the network because
they'll be stopped if your Sigma neurons
are in these saturated regimes the
gradients only flow if you're kind of in
a safer zone and what we call an active
region of a sigmoid and so that's kind
of a problem we'll see a bit more about
this soon another problem with sigmoids
is that their outputs are not 0 centered
so we'll talk about data pre-processing
soon but you always want to when you pre
process your data you want to make sure
that it's 0 centered right and in this
cases suppose you have a big network of
several layers of Sigma your neurons
they're outputting these non zero
centered values between 0 & 1 and we're
putting more basically linear
classifiers that we're stacking on top
of each other and the problem roughly
with non 0 centered outputs I'll just
try to give you a bit of an intuition on
what goes wrong
so consider a neuron that computes this
function right so it's a sigmoid neuron
looking at its just computing WX plus B
and what can we say about think about
what you can say about the gradients on
W during back propagation if your axis
are all positive in this
between zero and one so maybe you're a
neuron somewhere deep in the network
what can you say about the weights if
all the XS are positive numbers they're
kind of constrained in a way go ahead
right so what you said is all the
gradients with W are either all positive
or all negative and that is because
gradient flows in from the top and if
you think about the expression for all
the W gradients
they're basically x times the gradient
on F and so the gradient of on at the
output of the neuron is positive then
all your W gradients will be positive
and vice versa so basically you end up
with this case where it's suppose you
have just two weights so you have the
first weight in a second weight what
ends up happening is either all your
gradient for that for that as this as
this input goes through and you compute
your radiant in the weights they're
either all positive or they're all
negative and so the issue is that you're
constrained in the kind of update you
can make and you end up with this
undesirable zigzagging path if you want
to get to some parts that are outside of
these regions so it's kind of like a
slightly hand wavy reason here but just
to give you intuition and you can see
this empirically when you train with
things that are not zero centered you'll
observe slower convergence and this is a
bit of a hand wavy reason for why that
might happen but I think if you actually
wanted to go much deeper into that you
can and there are papers written about
this but you have to then reason about
mathematics of Fisher matrices and
natural gradients and it gets a bit more
complex than this
but I just wanted to give you intuition
for you want to have zero centered
things in the input you want to have
zero central things throughout other Y
thinks things don't converge as nicely
and so that is a downside of a sigma on
your own and the last one is that X
function inside this expression is kind
of expensive to compute compared to some
of the alternatives of other
nonlinearities and so it's just a small
detail I suppose when you actually train
these large convolutional networks most
of the compute time is in convolutions
and these dot products it's not in this
X operation and so it's kind of
vanishingly small contribution but it's
still something that is a bit of a
downside compared to the other parts so
I'll go into 10h and I'll ask a few
I'll take a few questions then so 10h is
an attempt to fix one of these problems
in particular the fact that it's non
zero centered sigmoid so yell Hakuna in
1991 right I wrote a very nice paper on
how you optimize neural networks and
I've linked to it from the syllabus and
he recommended that people use a 10 H of
X instead of sigmoid and 10 H of X
basically is kind of like two signals
put together you end up with being
between negative 1 and 1 and so your
outputs are 0 centered but otherwise you
have still some some of the other
problems like for example you have these
regions where if your neurons get
saturated no gradients flow and so we
haven't really fixed that at this point
but so 10 ages I think strictly prefer
to sigmoid because it has all the same
problems except for one ok
I'll continue and then maybe we can take
more questions so around 2012 in the
paper by oskar jerski this is the first
convolutional net worths paper they
proposed that actually they noticed that
this non-linearity where you use max of
0 and X instead of sigmoid or 10h just
makes your networks converge much
quicker and in their experiments almost
by a factor of 6 and so we can go back
and try to think about why is this and
we're kind of reading into it like you
can see that it works better in practice
but explaining it is not always as easy
so here's some hand wavy reasons I think
for why people are thinking that this
works much better so one thing is that
this this railway neuron it does not
saturate at least in a positive region
so at least in this region you don't
have this vanishing gradient problem
where your gradients will just kind of
die and you have this issue where the
neurons are only active in a small area
that is bounded from both sides but
these neurons are actually active in a
sense of a back propagate correctly or
not correctly but at least they don't
not back propagate all zeroes at least
in half of their regions there are much
more computationally efficient because
doing you're just being Thresh holding
and experimental you can see that this
converge is much much faster so this is
called the rel-nei on or the rectified
linear unit and it was pointed out in
this paper for the first time that this
works much better and this is kind of
like the default recommendation of what
you should use
this point at the same time there are
several problems with this rail in Iran
so one thing again notice that it's not
zero centered outputs so not completely
ideal perhaps and a slight annoyance of
the rail in Iran that we can talk about
and think about is what happens when
this rail in rural outputs are zero what
happens during back propagation if
irelia neuron does not become active so
in the forecast area URL stays inactive
then during backdrop what does it do it
kills right it kills the gradient and so
the way to see this of course is that
with the same picture and if you're at
negative site 10 then your local
gradient here will just be zero because
there's no there's just 0 gradient
identically it's not just you squish the
gradient down you actually kill it
completely so any neuron that does not
activate will not back propagate
downwards its weights will not be
updated and nothing happens below it at
least for its contribution and at x
equals 10 what is the local gradient
it's just one so a relativist passes
through gradients just a gate if if if
it's if during the forward pass its
output was positive then it just passes
gradient through otherwise it kills it
it's kind of like a gradient gate and by
the way what happens when x is zero what
is your gradient at that point it's
actually undefined that's right the
gradient does not exist at that point we
only talk about whenever I talk about
gradient just assume that I always mean
sub gradient which is a generalization
of gradients to functions that are
sometimes non differentiable so here the
limit does not exist but there's a whole
bunch of sub gradients that could be 0
or 1 and so that's what we use usually
in practice this this distinction
doesn't really matter too much but I
wanted to also point this out in the
case of the binary max gate max of X and
Y and someone asked the question what
happens if x and y are equal then in
that case you you kind of also have a
kink in the function and makes it not
differentiable but in practice these
things don't really matter just pick one
so you can have a gradient of 0 or 1
there and things will work just fine and
that's roughly because these are very
unlikely cases that you end up right
there ok so the issue with relu roughly
here's the problem
happens in practice you try to Israel
units and one thing that you have to be
aware of is you have these neurons that
if they don't output anything they won't
get any gradient they'll kill it and
they won't update and so let's see so
the issue is suppose you have a
sometimes what can happen is when you
initialize your rail in your owns you
can initialize them in a not very lucky
way and what ends up happening is
suppose this is your data cloud of
inputs to your revenue rounds but you
can end up with is a what we call it
dead rail a dead rail in your own so if
this neuron only activates in the region
outside of your data cloud then this
dead rail you will never become
activated and then it will never update
and so this can happen in one of two
ways either during initialization you
are really really unlucky and you happen
to sample weights for the rail in Iran
in such a way that that neuron will
never turn on in that case the neuron
will not train but more often what
happens is during training if your
learning rate is high then think about
these neurons it's kind of like
jittering around and what can happen
sometimes by chances they just get
knocked off the data manifold and when
that happens then they will never get
activated again and they they will not
come back to the data manifold and you
can see this actually in practice like
sometimes you can train a big neural net
with rail units and you train it and it
seems to work fine and then what you do
you stop the training and you pass your
entire training data set through your
network and you look at the statistics
of every single neuron and what what can
happen is that as much as like 10 or 20
percent of your network is dead these
are neurons that never turn down for
anything in the training data and this
can actually happen usually it's because
your learning rate was high and so those
are just like dead parts of your network
and you can come up with hacky schemes
for reinitializing these things and so
on people don't usually do it as much
but that's something to be aware of and
it's a problem with this non-linearity
and so especially for initialization
because of this dead rail loop problem
what people like to do is normally
initialize the biases with 0 instead
people initialize with slightly positive
numbers like say 0.01 because that makes
it more likely that initialization these
Relan neurons will output positive
numbers and they'll get
dates so it makes it less likely that
the neuron will just never become
activated ever throughout training but I
don't actually I think this is slightly
of a controversial point I've seen
people claim that it helps I've seen
some people say that it actually doesn't
help at all
and so just something to think about
okay any questions at this point we had
sigmoid 10h and relu I'm going to go
into some other ones okay good so let's
look at things like people trying to fix
Rea loose so one issue with Ray loose as
these dead neurons are not ideal so
here's one proposal which is called the
leaky relu and the idea with leaky relu
is basically we want this kink and we
want this piecewise linear T and we want
this efficiency of relu but the issue is
that in these this region your
ingredients die so instead let's make
this slightly negatively sloped here or
slightly positively sloped I suppose in
this region and so you end up with this
function and that's called a leaky relu
and so some people there are papers
showing that this works slightly better
you don't have this issue of neurons
dying but I think it's not completely
established that this works always
better and then some people play with
this even more so right now this is 0.01
but that can actually be an arbitrary
parameter and then you get something
that's called a parametric rectifier or
P relu and basically the idea here is to
introduce this is 0.01 that can be an
arbitrary alpha which is a parameter in
your network and this alpha can be
learned
you can back propagate into it and so
these neurons basically can choose what
slope to have in this negative region
okay and so they can become a rail if
they want to or they can become a leaky
rail or they can be they have the choice
roughly for every neuron and so this is
the kinds of things that people play
with when they try to design better
nonlinearities good so alpha here would
be a parameter that you back propagate
to in just a very normal way in your
computational graph there's every neuron
will have its alpha just like it has its
own bias okay go ahead
yeah I'm not sure if they worry about
this lots of alpha is one then you're
going to get an identity so that's
probably not something that that
propagation will want in a sense that if
that was an identity then that shouldn't
be very computationally useful so you
might expect that maybe back propagation
should not actually get you to those
regions of the space and wavy reason
perhaps I don't actually think if I
remember correctly there's no specific
things where people really worry about
that too much but I could be wrong I had
I read the paper a while ago now and I
don't use these too much in my own work
okay and then so one issue still is as
we saw so these are different schemes
for fixing the the dead relevant ons
there's another people that only came
out for example roughly two months ago
so this just gives you a sense of how
new this field is there are papers
coming out just two months ago trying to
propose new activation functions one of
them is exponential in your units or
Allu so just give you an idea about what
people play with it tries to have all
the benefits of relu but it tries to get
rid of this downside of being nonzero
centered and so they end up with is this
blue function here that looks like a
reloj but in the negative region it
doesn't just go to zero or it doesn't
just go down as a leaky relu but it has
this funny shape and there are two pages
of math in that paper justifying partly
why you want that and roughly when you
do this then you end up with 0 mean
outputs and they claim that this trains
better and I think there's some
controversy about this and and and so
we're basically trying to figure all of
this out active area of research and
we're not sure what to do yet but Ray
Lewis right now are like a safe
recommendation if you if you're careful
with it ok so that's a loose and one
more I would like to note mention
because it's relatively common and
you'll see it if you read about neural
networks is this max at neuron from
Inglot fellow at all and basically it's
a very different form of a neuron it's
not just an activation function that
looks different it actually changes what
a neuron computes or how it computes so
it doesn't just have this form of F of W
transpose X it actually has two weights
and then it computes max of W transpose
X plus B and another set of W transpose
X plus B so you end up with these like
two hyperplanes that you take a max over
and that's what the neuron computes so
you can see that there are many way
playing with these activation functions
so this doesn't have some of the
downsides of
relu this won't die and it's still
piecewise-linear it's still efficient
but now every single neuron has two
weights and so you've kind of double the
number of parameters per neuron and so
maybe that's not as ideal so some people
use this but I think it's it's not super
common I would say that robots are still
most common good at the end of the
that's right so what's your question
that's right so the weights will end up
yeah based on what the activation
functions are the dynamics of the back
drop into those weights will be
different and so you end up with
different weights for sure yeah I think
it's it's complicated
the reason it's complicated is a lot of
the optimization process is not just
about the loss function but just like
about the dynamics of the backward flow
of gradients and we'll see a bit about
that in the next few slides you have to
really think about it dynamically more
than just a lost landscape and how it's
so it's a complex and also we use
specifically stochastic gradient descent
and it has a particular form and some
things play nicer some nonlinearities
play nicer with the fact like the
optimization is tied the update is tied
into all of this as well and it's kind
of all interacting together and the
choice of these activation functions and
the choice of your updates are kind of
coupled and it's kind of very unclear
when you actually optimize this kind of
a complex thing okay
so TL DR here is that use relu you can
try out these guys you can try out ten
eight but you shouldn't expect too much
I don't think people use it too much
right now and don't use sigmoid because
basically 10 H is strictly better and
you won't see people use sigmoid now
anymore of course we use it in things
like long short-term memory units LS DMS
and so on and we'll go into the
in a bit in recurrent neural networks
but there are specific reasons why we
use them there and that we'll see later
in the class and they are they're used
differently than what we have covered so
far and like this just a fully connected
sandwich of matrix multiply
non-linearity and so on just having a
basic neural network okay
so that's everything I wanted to say
about activation functions it's
basically this one hyper parameter in
our functions that we worry about
there's research about it and we haven't
fully figured it out and there's some
pros and cons and many of them come down
to thinking about how the gradient flows
through your network and these these
issues like dead ray loose and you have
to really know about the gradient flow
if you try to debug your networks and to
understand what's going on okay so let's
look at data pros be processing very
briefly how many time okay so data
pre-processing just very briefly
normally suppose you just have a cloud
of original data in two dimensions here
very common to 0 Center your data so
that just means that along every single
feature we subtract the mean people
sometimes also when you go through
machine learning literature try to
normalize the data so in every single
dimension you normalize say by standard
deviation call standardizing or you can
make sure that the min and the max are
within say negative 1 or 1 and so on
there are several schemes for doing so
in images it's not as common because you
don't have separate different features
that could be at different units
everything is just pixels and they're
all bounded between 0 and 255 so it's
not as common to normalize the data but
it's very common to 0 Center your data
you can go further
normally in machine learning you can go
ahead and your data has some covariance
structure by default you can go ahead
and make that covariance structure be
diagonal say for example by applying PCA
or you can go even further and you can
whiten your data and what that means is
you kind of even squish after you
performed PCA you also squish your data
so that your covariance matrix becomes
just a diagonal and so that's another
form of pre-processing you might see
people talk about and these are both I
go much more detail in the class notes
on these I don't want to go into too
many details on them because it turns
out that in images we don't actually end
up using these even though there are
common in machine learning so in images
specifically what's common is just a
mean centering and then a particular
variant of mean centering that is
slightly more convenient in practice
so in means centering we say have a 32
by 32 by three images of CFR if you want
to Center your data then for every
single pixel you compute that's mean
value over the training set and you
subtract that out so what you end up
with is this mean image that has
basically dimension of 32 by 32 by 3 so
I think the mean image for example for
image net is just this orange blob so
you end up subtracting that from every
single image to Center your data to have
better training dynamics and one other
form that is likely more convenient is
subtracting just a per channel mean so
you go in red green and blue channel and
you compute to the mean across all of
space so you just end up with basically
three numbers of the means in red green
and blue channel and just subtract those
out and so some networks use that
instead so those are the two common
schemes this one is likely more
convenient because you only have to
worry about those three numbers you
don't have to worry about a giant array
of mean image that you have to ship
around everywhere when you're actually
coding this up okay so not too much more
I want to say about this just basically
subtract the mean in computer vision
applications things don't get much more
complex than that in particular doing
PCA and so on this used to be slightly
common the issues you can't apply it on
full images because your images are very
high dimensional objects with lots of
pixels and so these various matrices
would be huge and people try to do
things like only doing whitening locally
so you would slide a whitening filter
through your images spatially and that
used to be done several years ago but
it's not as common now it doesn't seem
to matter too much okay good so we will
dive into weight initialization a very
very important topic one of the reasons
that I think early neural networks
didn't quite work but as well is because
people are just not careful enough with
this so one of the first things will we
can look at is first of all how not to
do weight initialization so in
particular you might be tempted to just
say okay let's start off at all the
weights are equal to zero and you use
that in your neural network so suppose
you have like a ten layer neural network
and you set all the ways to zero why
doesn't that work why isn't that a good
idea
I sorry go ahead yeah so basically just
all your neurons output the same thing
in backdrop they will behave the same
way and so there's nothing as we call
now as well actually call it symmetry
breaking so all the neurons are
computing same stuff and so in backdrop
they will all look the same they will
compute the same gradients and so on so
not the best thing
so instead people use small numbers
small random numbers so one way you can
do that for example that is a relatively
common thing to do is you sample from a
unit Gaussian with 0.01 standard
deviation so small random numbers
so that's your W matrix how you would
initialize it now the issue with this
initialization is that it works ok but
you'll find that it only works ok if you
have small networks but as you start to
go deeper and deeper with neural
networks you have to be much more
careful about the initialization and I'd
like to go into exactly what breaks and
how it breaks and why it breaks when you
try to do these naive initialization
strategies and try to have deep networks
so let's look at what goes wrong so what
I've written here is a small ipython
notebook so what we're doing here is I'm
going to step through this just briefly
I'm sampling a data set of 1,000 points
that are 500 dimensional and then I'm
creating a whole bunch of hidden layers
and nonlinearities so say right now we
have 10 layers of 500 units and we're
using 10 H and then what I'm doing here
is I'm just basically taking unit
Gaussian data and I'm forwarding it
through the network and with this
particular initialization strategy we're
right now that initialization strategy
is what I described in the previous
slide so example from unit Gaussian and
scale it by 0.01 so what I'm doing here
in this for loop is I'm forward
propagating this network which is right
now made up of just a series of layers
of the same size so with 10 layers of
500 neurons on each layer and I'm
forward propagating with this
initialization strategy for a unit
Gaussian data and what I want to look at
is what happens to the statistics of the
hidden of the neurons activations
throughout the network with this
initialization so we're going to look
specifically at the mean and a standard
deviation and we're going to plot the
mean standard deviation and we're going
to plot the histograms so we take all
this data
and then say at the fifth player we're
going to look at what the what value is
the neurons take on and say the fifth or
sixth or seventh layer and we're going
to make histograms of those so with this
initialization if you run this
experiment you end up it ends up looking
as follows so here I'm printing it out
we start off with a mean of zero and
standard deviation of one that's our
data and now I'm forward propagating and
as I go to tenth player look at it what
happens to the mean we're using ten H so
10 H is symmetric so as you might expect
the mean stays around zero but the
standard deviation look at what happens
to it it started off at one and some of
the standard deviation goes to point two
then point zero four and it just
plummets down to zero so the standard
deviation of these neurons just goes
down to zero
looking at the histograms here at every
single layer at the first layer the
histogram is reasonable so we have a
spread of numbers between negative 1 and
1 and then what ends up happening to it
this just collapses to a tight
distribution at exactly zero so it ends
up happening with this initialization
for this ten layer Network is all the 10
H neurons just end up outputting just
zero so at the last layer these are tiny
numbers of like near zero values and so
all activations basically become zero
and why is this an issue okay so think
about what happens to the dynamics of
the backward pass to the gradients when
you have tiny numbers in the activations
your X's are tiny numbers on the last
few layers what what do these gradients
look like on the weights in these layers
and what happens to the backward pass so
first of all suppose my so there is a
layer here that looks at some layer
before it and almost all the inputs are
tiny numbers that's the X X is a tiny
number what is the gradient what do you
what might you expect the gradients for
the W to be in that case for those
layers sorry you said very small so why
would they be very small
that's right so the gradient for W will
be equal to x times the gradient from
the top okay and so if X are tiny
numbers then your gradients for W are
tiny numbers as well and so these guys
will basically have almost no gradient
accumulated now we can also look at what
happens with these matrices again we we
took data that was distributed as a unit
Gaussian at the beginning and then we
ended up multiplying it by W and
activation function and we saw that
basically everything goes to zero this
just collapses over time and think about
the backward pass as we change the
gradient through these layers and back
propagation what we were doing
effectively is some of the gradient kind
of Forks off and to our gradient W and
we saw that those are tiny numbers but
then throwing back propagation we're
going through gradients of X and so we
end up doing when we back drop through
here is we again end up multiplying by W
again and again at every single layer
and if you take unit Gaussian data and
you multiply it by W at this scale you
can see that everything goes to zero and
the same thing will happen in backward
pass we're successively multiplying by W
as we've back propagated into X on every
single layer and we're as we do that
this gradient which started off with
reasonable numbers from your loss
function will end up just going towards
zero as you keep doing this process and
you end up with gradients here that are
basically just tiny tiny numbers and so
you basically end up with very very low
gradients throughout this network
because of this reason and this is
something that we refer to as vanishing
gradient as this gradient travels
through with this particular
initialization you can see that the grip
the magnitude of the gradient will just
go down when we used this initialization
for W of 1e negative 2 okay so we can
try a different extreme instead of
scaling here as we scaled with one
negative two we can try a different
scale of the W matrix at initialization
so suppose I try one point zero instead
of 0.01
we'll see another funny thing happen
because now we've overshot the other way
in a sense that you can see that well
maybe it's best to look at the
distributions here you can see that
everything is completely saturated these
ten H neurons are either all negative
one or all
one I mean the distribution is really
just everything is supersaturated your
entire network all the neurons
throughout the network are either
negative one or one because the weights
are too large and they keep over
saturating 10h neurons because this
course that end up going through the
non-linearity are just very large
because the weights are large and so
everything is supersaturated so what are
the gradients flowing through your
network it's just terrible it's complete
disaster right it's just zeros forever
just exponentially zero and you die so
you can train for a very long time at
what you'll see when this happens is
your loss is just not moving at all
because nothing is back propagate in
because all the neurons are saturated
and nothing is being updated okay so
this initialization as you might expect
actually is like super tricky to set and
it needs to be kind of in this
particular case it needs to be somewhere
between one and zero point zero one okay
and so you can be slightly more
principled instead of trying different
values and there are some papers written
on this so for example in 2010 there was
a proposal for what we now call the
Xavier initialization from Glu out at
hall and they kind of went through and
they looked at the expression for the
variance of your neurons and you can
write this out and you can basically
propose a specific initialization
strategy for how you scale your
gradients so I don't have to try a 0.01
I don't have to try one or whatever else
so they recommend this kind of
initialization where you divide by the
square root of the number of inputs for
every single neuron so if you have lots
of inputs then you end up with lower
weights and intuitively that makes sense
because you're doing more weight you
have more stuff that goes into your
weighted sum so you want less of an
interaction to all of them and if you
have smaller number of units that are
feeding into your lair then you want
larger weights because then there's only
a few of them and you want to have a
variance of one so just to back up a bit
the idea here is they were looking at a
single neuron no activation functions
included it's just a linear neuron and
all they're saying is if you want if
you're getting unit Gaussian data as
input and you'd like this linear neuron
to have a variance of 1 then you should
initialize your weights with this amount
and in the notes I go into exactly how
this is derived is just some math with
standard deviations and basically this
is a reasonable initialization so I can
use that
instead and you can see that if I use it
here
the distributions end up being more
sensible so we're again looking at the
histogram between negative one and one
of these 10h units and you get a more
sensible number here and you actually
have your within the active region of
all these ten HS and so you can expect
that this will be a much better
initialization because things are in the
active regions and things will train
from the start nothing is super
saturated in the beginning the reason
that this doesn't just end up being very
nice and the reason we still have
conversions down here is because this
paper doesn't take into account the
nonlinearities in this case the 10 H and
so the 10 H non-linearity ends up like
kind of deforming your statistics of the
variance throughout and so if you stack
this up it ends up still you know doing
something to distribution in this case
it seems that the standard deviation
goes down but it's not as dramatic as if
you were to set this by by just trial
and error and so this is like a
reasonable initialization to use in your
neural networks compared to just setting
it to 0.01 and so people end up using
this in practice sometimes but so this
works in the case of 10 H does something
reasonable it turns out if you try to
put it into a rectified linear unit
Network it doesn't work as well and the
decrease in the standard deviations will
be much more rapid so looking at irelia
on and the first layer it has some
distribution and then this distribution
as you can see just gets more and more
peaky at 0 so more and more neurons are
not activating with this initialization
so using the Xavier initialization in a
rectified layer layer net does not do
good things and so again thinking about
this paper they don't actually talk
about nonlinearities and the relevant
ons they compute this weighted sum which
is within their domain here but now
after the weighted sum you do a relly so
you kill half of the distribution you
set it to zero and intuitively what that
does to your distribution of your
outputs is it basically halves your
variance and so it turns out as was
proposed in this paper just last year in
fact someone said basically look there's
a factor of two you're not accounting
for because these relevant neurons they
effectively have your variance each time
because you take everything like say you
have unit Gaussian inputs you take them
through your non-linearity you have unit
Gaussian stuff out
now you relieve that and so you end up
having the variance so you need to
account for it with an extra two and
when you do that then you get proper
distributions specifically for the
relevant on and so in this
initialization where if you're using
relative Nets you have to worry about
that extra factor of two and everything
will come out nicely and you won't get
this factor of two that keeps building
up and it screws up your activations
exponentially okay so basically this is
tricky tricky stuff and it really
matters in practice in practice in their
paper for example they compare having
the factor of two or not having that
factor of two and it matters when you
have really deep networks in this case I
think they had a few dozen layers if you
account for the factor of two you
converge if you don't account for that
factor of two you there's nothing it's
just zero lots okay so very important
stuff you need really need to think it
through you have to be careful with the
initialization if it's incorrectly set
are bad things happen and so
specifically in the case if you have
neural networks with railway units
there's a correct answer to use and
that's the this initialization from
coming coming okay so tricky stuff this
is partly this is partly why you let
worse even work for a long time as we
just I think people didn't then fully
maybe appreciate just how how difficult
this was to get right and tricky and so
I just like to point out that proper
neutralization basically active area of
research you can see that papers are
still being published on this a large
number of papers just proposing
different ways of initializing your
networks these last few are interesting
as well because they don't give you a
formula for initializing they have these
data-driven ways of initializing
networks and so you take a batch of data
you forward the through your network
which is now an arbitrary network and
you look at the variances at every
single point in your network and
intuitively you don't want your
variances to go to zero you don't want
them to explode you want everything to
have roughly say like be a unit Gaussian
throughout your network and so they
iteratively scale these weights in your
network so that you have roughly unit
Gaussian activations everywhere or on
the order of that basically and so there
are some data-driven techniques and a
line of work on how to properly
initialize okay so I'm going to go into
some I'm going to go into a technique
that alleviates a lot of these problems
but
right now I could take some questions if
there are any at this point good would
it make sense to standardize the
gradient coming in by dividing by the
variance possibly but then you're not
doing back propagation because if you
meddle with the gradient then it's not
clear what your objective is anymore and
so you're not getting necessarily
gradient so that's maybe the only
concern I'm not sure what would happen
you can you can try to normalize the
gradient I think the method I'm going to
propose in a bit is actually doing
something to the effect of that but in a
clean way okay cool so let's go into
something that actually fixes a lot of
these problems in practice it's called
batch normalization and it was only
proposed last year and so I couldn't
even cover this last year in this class
but now I can and so this actually helps
a lot okay and the basic idea in bash
normalization paper is okay you want
roughly unit Gaussian activations in
every single part of your network and so
just just do that just just make them
unit Gaussian okay you can do that
because making something unit Gaussian
is a completely differentiable function
and so it's okay you can back propagate
through it and so what they do is you're
taking a mini batch of your data and
you're taking it through your network
we're going to be inserting these batch
normalization layers into your network
and the batch normalization layers they
take your input X and they make sure
then every single feature dimension
across the batch you have unit Gaussian
activations so say you have a batch of
100 examples going through the network
maybe this is a good example here so
your batch of activations so you have n
things in your mini batch and you have D
features or D activations of neurons
that are at some point some part and
this is an inputs to your Bachelor
Malaysian layer so this is a matrix of X
of activations and bash normalization
effectively it evaluates the empirical
mean and variance along every single
feature and it just divides by it so
whatever your X was it just makes sure
that every single column here has unit
as a unit Gaussian and so that's a
perfectly differentiable function and it
just applies it at every single feature
or activation independently across the
okay so you can do that and that's it
turns out to be a very good idea now one
problem with this scheme so this is the
way this will work is we'll have
normally we have fully connected
followed by non-linearity fully
connected how about non-linearity and we
have a deep network of this now we're
going to be inserting these batch
normalization layers right after fuller
connected layers or equivalently after
convolutional layers as well see soon in
with convolutional networks and
basically we insert them there and they
make sure that everything is roughly
unit gaussian at every single step of
the network because we just make it so
and one problem you might think of with
this with this is that that seems like a
unnecessary constraint so when you put a
Bachelor normalization here after fuller
connected the outputs will definitely be
unit gushin because you normalize them
but it's not clear that 10h actually
wants to receive unit gaussian inputs so
if you think about the form of 10h it
has a specific scale to it it's not
clear that a neural network wants to
have this hard constraint of making sure
that Batchelor outputs are exactly unit
Gaussian before the 10h because you if
you'd like the network to pick if it
wants your 10h outputs to be more or
less diffuse more or less saturated and
right now it wouldn't be able to that so
a small patch on top of it this is the
second part of batch normalization is
not only do you normalize X but after
normalization you allow the network to
shift by gamma and add a B for every
single feature input and so what this
allows the network to do and these are
all parameters so gamma and B here are
parameters that we're going to back drop
back wrap into and they just allow the
network to to shift after you've
normalized to unit Gaussian they allow
this bump to shift and scale if the
network won't stick and so we initialize
though presumably with 1 and 0 or
something like that and then we can the
network can choose to adjust them and by
adjusting these you can imagine that
once we feed into 10h the network can
choose through the backdrop signal to
make the 10 age more or less picky or
saturate it in whatever way it wants but
you're not going to get into this
trouble where things just completely die
or explode in the beginning of
optimization and so things will train
right away and then back propagation can
take over and can find
over time and note one more important
feature by the way is that if you set
these gamma and B if you train them if
my back propagation it happens that they
end up taking the empirical variance and
the mean then you can see that basically
the network has the capacity to undo the
batch normalization so this part can
learn to undo that part and so that's
why back normalization and can act as an
identity function or it can learn to be
an identity whereas before it couldn't
and so when you have these bachelor
layers in there the network can through
back propagation learn to take it out or
it can learn to take advantage of it if
it finds it helpful through the back
prop this will kind of work out so
that's just a nice point to have and so
basically there are several nice
properties to bachelor so this is the
algorithm as I described nice properties
are that it improves the gradient flow
through the network it allows for higher
learning rates so your network can learn
faster it reduces this is an important
one it reduces the strong dependence on
initialization as you sweep through
different choices of your initialization
scale you'll see that with and without
batch norm you'll see a huge difference
with batch norm you'll see a much more
things will just work for much larger
settings of the initial scale and so you
don't have to worry about it as much it
really helps out with this point and one
kind of more subtle thing to point out
here is it kind of acts as a funny form
of regularization and it reduces need
for dropout which we'll go into in a bit
later in the class but the way it acts
as a funny regularization is with batch
norm when you have some kind of an input
X and it goes through the network then
it's representation at some layer in the
network is basically not only a function
of it but it's also a function of
whatever other examples happen to be in
your batch so because whatever other
examples are with you in that batch
normally these are processed completely
independently in peril but Batchelor
actually ties them together and so your
representation that say like the fifth
layer of network is actually a function
of whatever back you happen to be
sampled in and what this does is it
jitters your place in the representation
space on that layer and this actually
has a nice regularizing effect
and so this jittering sarcastically
through this batch that you happen to be
in has this effect and so I realize it's
hand wavy but actually seems to actually
help out a bit okay and that test time
bachelor layer by the way functions a
bit differently you don't want that test
time you want this to be a deterministic
function so just a quick point that at
test time when you're using a bachelor
layer it functions differently in
particularly you have this mu and a
Sigma that you keep normalizing by so at
test time you just remember your mu and
Sigma across the data set you can either
compute it like what is the mean and
Sigma at every single point in the
network you can compute that once over
your entire training set or you can just
have a running sum of news and Sigma's
while you're training and then make sure
to remember that in the bachelor layer
because that test time you don't want to
actually estimate the empirical mean and
variance across your batch you want to
just use those directly okay so because
this gives you an idea terminus function
forward at test time so there's just a
small detail okay and so that's a batch
norm any any questions about fashion by
the way so this is a good thing use it
and you'll implement it actually in your
assignment good thank you so the
question is does it slow down things at
all it does so there is a runtime
penalty that you have to pay for it
unfortunately I don't know exactly how
expensive it is I heard someone say
value of like 30% even and so I don't
know actually I haven't fully checked
this but basically there is a penalty
because you have to do this at every
normally you it's very common to
basically have a bachelor after every
convolution layer and when you have to
say hundred and fifty calm like layers
you end up having all this stuff build
up any other questions that's the price
we pay I suppose good
your day is not going so well so yeah so
when can you tell that you maybe need
Bosch norm I think I'll come back to
that in a few slides we'll see like how
can you detect that your network is not
healthy and then maybe you want to try
bathroom okay so the learning process I
have 20 minutes I think I can do this
yeah where it's like 70 out of 100 so I
think we're fine okay so we've
pre-processed our data we've decided
let's try let's decide on some for these
purposes of these experiments I'm going
to work with C for 10 and I'm going to
use a two layer neural network with say
50 hit in neurons and I'd like to give
you an idea about like how this looks
like in practice when you're training
neural networks like how do you play
with it where some of the how do you
actually converge to good hyper
parameters what does this process of
playing with the data and getting things
to work look like in practice and so I
decided to try out a small neural
network
I've pre-processed my data and so the
first kinds of things that I would look
at if I want to make sure that my
implementation is correct and things are
working first of all um so I'm going to
be initializing here a two layer neural
network so weights and biases
initialized with just naive
initialization here because this is just
a very small network so I can afford to
maybe do just a naive sample from a
Gaussian and then this is a function
that basically is going to train a
neural network and I'm not showing you
the implementation obviously but just
one thing basically it returns your loss
and returns your gradients on your model
parameters and so the first thing I
might try for example is I disable the
regularization that's passed in the and
and I make sure that my loss comes out
correct right so I've mentioned this in
previous slides
so say I have ten classes in C for 10
I'm using softmax classifier so I know
that I'm expecting a loss of negative
log of one over ten because that's the
that's just the expression for the loss
and that turns out to be 2.3 and so I
put this in I get a loss of 2.3 so I
know that basically the neural network
is currently giving you a diffuse
distribution over the classes because it
doesn't know anything
we've just initialized it so that checks
out the next thing that my check is that
for example I cranked up the
regularization and I of course expect my
loss to go up right because now we have
this additional term in the objective
and so that checks out so that's nice
the next thing I would usually try to do
it's a very good sanity check when
you're working with neural networks is
try to take a small piece of your data
and try to make sure you can over fit
your training data just that small piece
so I'm going to take like say a sample
of like 20 training examples and 28
labels and I just make sure that I train
on that small piece and I just make sure
that I can get a loss of basically near
zero I can fully over fit that because
if I can't over fit a tiny piece of my
data then things are definitely broken
and so here I'm starting the training
and I'm starting with a random number of
parameters here I'm not going to go into
full details there but basically I make
sure that my cost can go down to zero
and that I'm getting accuracy of 100% on
this tiny piece of data and so that
gives me confidence that probably
backprop is working probably the update
is working the learning rate is set
somehow reasonably and so I can over fit
a small data set and I'm happy at this
point and I maybe I'm thinking about now
scaling up to larger a data good then
sometime ie so you should be able to
overfit sometimes I even try like say
like one or two or three examples you
can really crank this down and you
should be able to over fit even with
smaller networks and so that's a very
good sanity check because you can afford
to have small networks and you just make
sure you can over fit if you can't over
fit your implementation is probably
incorrect something is very funky is
wrong so you should not be scaling up to
your full data set before you can pass
the sanity check um so let's see so so
basically the way I try to approach this
is take your small piece of data and now
we're scaling it up we've over fitted so
now I'm scaling up to like the bigger
data set and I'm trying to find the
learning rate that works and you have to
really play with this right you can't
just eyeball the learning rate you have
to find the scale roughly so I'm trying
first a small learning rate like one e-
six and i see that the loss is bate
barely barely going down so this lost
this learning rate of 1 e negative 6 is
probably aa too small right nothing is
changing of course there could be many
other things wrong because your loss
could be constant for like a million
reasons but we've passed a small sanity
check so I'm thinking that this is proud
the loss is too low and I need you to
knit by the way this is a fun example
here of something funky going on that is
fun to think about my loss
just barely went down but actually my
training accuracy shot up to 20 percent
from the default 10 percent how does
that make any sense
how can I be by loss just barely change
but my costs my accuracy is so good well
much much better than 10% how's that
even possible
the regularization term is still yeah
yeah maybe not quote me either not quite
I think my mother per good okay
on okay a bit maybe not quite so think
about how accuracy is computed and how
this cost is computed right go ahead
right right so you you start out with a
fuse losses the diffuse sorry scores and
now what's happening is your training so
these scores are tiny shifting your loss
is still roughly diffused so you end up
at the same loss but now your correct
answers are now tiny bit more probable
and so when you're actually computing
the accuracy the art maxy class is
actually ends up being the correct one
so these are some of the fun things you
run into when you actually train some of
this stuff you have to you have to think
about the expressions okay so now I
start I tried very low learning rate
things are barely happening so now I'm
going to go to the other extreme and I'm
going to try out a learning rate of a
million what could possibly go wrong
so what happens in that case you get
some weird errors and things explode you
get Nan's
really fun stuff happens so okay 1 1
million is probably too high is what I'm
thinking at this point so then I try to
narrow in on rough region that actually
gives me a decrease in my costs right
that's what I'm trying to do with my
binary search here and so at some point
I get some idea about you know roughly
where should I be cross validating ok
like the hyper arm optimization at this
point I'm trying to find the best high
parameters for my network what I really
like to do in practice is go from course
to find strategy so first I just have a
rough idea by playing with it where the
learning rate should be then I do a
course search our learning rates of like
a bigger segment and then I repeat this
process so I look at what works and then
I narrow in on the regions that work
well ok do this here are quickly and in
your code for example detect explosions
and break out early that's like a nice
tip in terms of the implementation so
what I'm doing effectively here is I
have a loop where I sample my hyper
parameters say in this case the
regularization and the learning rate I
sample them I train I get some results
here so these are the accuracies in the
validation data and these are the hyper
parameters that produce them and some of
the accuracies you can see that they
work quite well so fifty percent forty
percent some of them don't work well at
all so this gives me an idea about what
range of learning rates and
regularization are working relatively
well and when you do this type RAM
my zation you can start out first with
just a small number of epochs you don't
to run for a very long time just run for
a few minutes you can already get a
sense of what's working better than than
some other things and also one note when
you're optimizing over regularization of
the learning rate it's best to sample
flow malach space you don't just want to
sample from a uniform distribution
because these are learning rates and
regularization they act multiplicatively
on the dynamics of your back propagation
and so that's why you want to do this in
locked space so you can see that I'm
sampling from negative 3 to negative 6
the exponent for the learning rate and
then I'm raising it to the power of 10
I'm raising ten to the power of it and
so you don't want to just be sampling
from a uniform of 0.01 to like 100
because then most of your samples are
kind of in a bad region right because
the learning rate is a multiplicative
interaction so something to be aware of
now once I found what works relatively
well of course doing a second pass where
I'm kind of going in and I'm changing
these again a bit and I'm looking at
what works so I find that I can now get
to 53 so some of these work really well
one thing to be aware of sometimes you
get a result like this so 53 is working
quite well and this is actually where if
I see this I'm actually worried at this
point because I'm so through this
cross-validation here I have a result
here and there's something actually
wrong about this result that hints at
some issue there's an unsettling problem
with this result
looks like necessarily Baltimore a local
Optima is not necessarily global optimum
so what makes you say that exactly oh I
see so you're saying that actually
they're quite a defuse in a sense like
there's not they're not consistent too
much yeah perhaps okay so an interest of
time what's happening here look I'm
optimizing learning rate between
negative three negative four ten to the
and I end up with a very good result
that is just at the boundary of what I'm
hiper I'm optimizing over so this is
almost 1 a negative 3 it's almost zero
point zero zero one which ends which is
really a boundary of what I'm searching
over so I'm getting a really good result
at an edge of what I'm looking for and
that's not good because maybe this edge
here the way I've defined it is not
actually optimal and so I want to make
sure that I spot these things and I
adjust my ranges because there might be
even better results going slightly this
way so maybe I want to change negative 3
to negative 2 or 2.5 and but for
regularization I see that a 1 a negative
4 is working quite well so maybe I'm in
a slightly better spot and so on so
worried about this one thing also I'd
like to point out is you'll see me
sample these randomly so 10 to the
uniform of this so I'm sampling random
regularization and learning rates when
I'm doing this what you might see
sometimes people do is what's called a
grid search so really the difference
here is instead of sampling randomly
people like to go in steps of fixed
amounts in both the learning rate and
the regularization and so you hand up
with this double loop here over some
settings of learning rate and some
settings of regularization because
you're trying to be exhaustive and this
is actually a bad idea it doesn't
actually work as well as if you sample
randomly and it's unintuitive but you
actually always want to sample randomly
you don't want to go in fixed steps and
here's the reason for that it's kind of
you think about it a bit but this is the
grid search way so I've sampled at set
intervals and I kind of have confidence
that I've you know sweep out this this
entire space and as opposed to random
sampling where I've just randomly
sampled from the to the issue is that in
hyper parameter optimization in training
neural networks what often happens is
that one of the parameters can be much
much more important than the other
parameter
okay so say that this is an unimportant
parameter it's performance the
performance of your loss function is not
really a function of the Y dimension but
it's really a function of the X
dimension you get much better result in
a specific range along the x axis and if
this is true then which is often the
case then in this case you're actually
going to end up sampling lots of
different X's and you end up with a
better spot then here where you've
sampled at exact spots and you're not
getting any kind of information across
the X if that makes sense so always use
random because in these cases which are
common the random will actually give you
more bang for the buck okay so there are
several high programs you want to play
with the most common ones are probably
the learning rate the update type maybe
we're going to we're going to go into
this in a bit the regularization and the
dropout amounts which we're going to go
into so this is really a it's so much
fun so in practice the way what this
looks like as we have it for example a
computer vision cluster we have 70
machines so I can just distribute my
training across 70 machines and I've
written myself for example a command
center interface where these are all the
loss functions on all the different
machines in our computer vision cluster
these are all here hyper parameters I'm
searching over and I can see basically
what's working well and what isn't and I
can send commands to my workers and I
can say okay this isn't working at all
so just resample you're not doing well
at all and some of these are doing very
well and I look at what's exactly
working well and I'm adjusting it's a
dynamic process that I have to go
through to actually get this stuff to
work well because you just have too much
stuff to optimize over and you can't
afford to just a spray and pray you have
to work with it okay so you're
optimizing and you're looking at loss
functions these loss functions can take
various different forms and you need to
be able to read into what that means so
you'll be you'll get quite good at
looking at loss functions and intuiting
what happens so this one for example I
was pointing out in the previous lecture
it's not as exponential as I may be used
to my loss functions I'd like it to you
know it looks a little too linear and so
that maybe tells me that the learning
rate is maybe slightly too low so that
doesn't mean the learning rate is too
low it just means that I might want to
consider trying a higher learning
right sometimes you get all kinds of
funny things so you can have a plateau
where at some point the network decides
that it's now ready to optimize usually
so what is the prime suspect in these
kinds of cases just a guess maybe sorry
yeah sure so weights initialization I
think is the prime suspect you've
initialized them incorrectly the
gradients are barely flowing but at some
point they add up and it just suddenly
starts training so lots of fun in fact
it's so much fun that I've started an
entire tumblr a while ago on loss
functions so you can go through these so
people contribute these which is nice
and so this is I think someone training
a spatial transformer network we're
going to go into that this is a all
kinds of exotic shapes
I'm not even you know at some point
you're not really sure how what any of
this means
it's going so well
yeah so here this this is again like
several tasks that are training at the
same time and just this by the way I
know what happened here it's this is
actually training a reinforcement
learning agent the problem in
reinforcement learning is you don't have
a stationary data distribution you don't
have a fixed data set in reinforcement
learning you're an agent interacting
with the environment if your policy
changes and you end up like staring at
the wall or you end up looking at
different parts of your space you end up
with different data distributions and so
suddenly I'm looking at something very
different than what I used to be looking
at and I'm training my agent and the
loss goes up because the agent is
unfamiliar with that kind of inputs and
so you have all kinds of fun stuff
happening there and then so this one is
one of my favorites I have no idea what
basically happened here this loss
oscillates but roughly does and then it
kind of just explodes
I clearly something was not fully right
in this case and also here it just kind
of some point decides to converge I have
no idea what was wrong so you get all
kinds of funny things if you end up with
funny plots in your assignments and
please do send them to loss functions
that some will post them so during
training don't only look at the loss
function another thing to look at is
your accuracy especially accuracies for
example so you sometimes prefer looking
at accuracies over loss functions
because accuracies are interpretable i
know what these classification
accuracies mean in absolute terms
whereas for loss function is maybe not
as interpretable and so in particular I
have a loss I have an accuracy curve for
my validation data and my training data
and so for example in this case I'm
saying that my training data accuracy is
getting much much better and my
validation accuracy has stopped
improving and so based on this gap that
can give you hints on what might be
going on under the hood in this
particular case there's a huge gap here
so maybe I'm thinking I'm overfitting
I'm not a hundred percent sure but I
might be overfitting I might want to try
to regularize strongly more strongly one
of the things you might also be looking
at is tracking the difference between
the scale of your parameters and the
scale of your updates to those
parameters so say your your suppose that
your weights are on the order of unit
in distributed then intuitively the
updates that you're incrementing your
weights by in backpropagation you don't
want those updates to be much larger
than the weights obviously or you don't
want them to be tiny like you don't want
your updates to be on the order of one
in negative seven when your weights are
on the order of one negative two and so
look at the update that you're about to
increment onto your weights
and just look at its norm for example
the sum of squares and compare it to the
update the scale of your parameters and
usually a good rule of thumb is this
should be roughly one in negative three
so basically every single update you're
modifying on the order of like a third
significant digit for every single
parameter right you're not making huge
updates you're not making very small
updates so that's one thing to look at
roughly one a negative three usually
works okay if this is too high I want to
maybe decrease my learning rate if it's
way too low like say it's money negative
seven maybe I want to increase my
learning rate and so in summary today we
looked at a whole bunch of things to do
with training neural networks the TLDR s
of all of them are basically use values
for images subtract mean use the heavier
initialization or if you think you have
a smaller network you can maybe get away
with just choosing your scale to be 0.01
or maybe you want to play with that a
bit there's no strong recommendation
here I think a batch normalization just
use and when you're doing high parameter
optimization make sure to sample your
head REMS and do it in lock space when
appropriate and that's something to be
aware of and this is what we still have
to cover and that will be next class we
do have two more minutes so I will take
questions if there are any but
the way to like know how they're gonna
like poorly with each other's reunited
like randomly yes oh you're asking about
the correlation between regularization
and the learning rate you you optimize
over both of them during half the
parameter optimization right and you try
to decouple them but maybe the yeah I
don't think there's any obvious thing I
can recommend there you have to guess
and check a bit I don't think that
anything jumps out at me that's obvious
or not to decouple them okay great no
more questions or them
have a quick question regarding sign