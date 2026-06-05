# YouTube Transcript: hd_KFJ5ktUc

okay so let's die first
today we'll talk about training neural
networks again and then I'll give you a
bit of an intro to convolutional neural
networks before we dive into that the
material just some administrative things
first first I didn't get a chance to
actually introduce Justin last lecture
justin is your instructor also for this
class and he was missing for the first
two weeks and so you can you can ask him
anything about anything he's very
knowledgeable maybe that's an
overstatement I don't know okay
and the simon too is out as a reminder
it's quite long so I encourage you to
start earlier and it's do basically next
Friday so get started on that as soon as
possible and you'll implement neural
networks with the proper API of forward
backward passes and you'll see the
abstraction of a computational graph and
you'll implement also Bachelor Malaysian
dropout and then you'll actually
implement convolutional networks so by
the end of this assignment you'll
actually have a fairly good
understanding of all the low-level
details of how combos on your network
classifies images okay so where we are
in this class just as a reminder again
we're training neural networks and it
turns out that training neural networks
is really a four-step process you have
an entire data set of images and labels
we sample a small batch of that data set
we forward propagate it through the
network to get the loss which is telling
us how well we're currently classifying
this batch of data and then we back
propagate to compute the gradient and
all the weights and this gradient is
telling us how we should nudge every
single weight in the network so that
we're better classifying these images
and then once we have the gradient we
can use it for a parameter update where
we actually do that small nudge we last
class we looked into activation
functions and an entire zoo of
activation functions and some pros and
cons of using any of these inside your
neural network a good question came up
in Piazza so when asked why would you
even use in your activation function why
not just skip it and question was posted
and I forgot to really address this very
nicely in the last lecture but basically
if you don't use an activation function
then your entire neural network ends up
being one single linear sandwich and so
your capacity is equal to that of just a
linear classifier so those activation
functions are really critical to have in
between and they they are the ones that
give you all this wiggle
that you can use to actually fit your
data we talked briefly about data
pre-processing techniques but very
briefly we also looked at the activation
functions and their distributions
throughout the neural network and so the
problem here I see you recall is we have
to choose this initial initialization
for our weights and in particular
there's the scale of how large we want
those ways to be in the beginning and we
saw that if that if those weights are
too small then your activation in a
neural network as you have a deep
network goes all toward zero and if you
set that scale slightly too high then
all of them will explode instead and so
you end up with either supersaturated
networks or you end up with networks
that just up at all zeros and so that
scale is very very tricky thing to set
we looked into the Xavier initialization
which gives you a reasonable kind of
thing to use in that form and that gives
you basically roughly good active
activations or distributions of
activations throughout the network in
the beginning of training and then we
went into batch normalization which is
this thing that alleviates a lot of
these headaches were actually setting
that scale properly and so Bachelor
realization makes this a much more
robust choice so you don't have to
precisely get that initial scale correct
and we went to all of its pros and cons
and we talked about that for a while
and then we talked about the learning
process and so I try to show you kind of
tips and tricks for how you actually
baby set these neural networks how you
get them to train properly and also how
you run cross validations and how you
could slowly converge over time into
good hyper parameter ranges so we talked
about all of that last time so this time
we're going to go into some of the
remaining items for training in neural
networks in particular parameter update
schemes I think for the most part and
then we'll talk a bit about model
ensembles dropout and so on okay so
before I dive into that any
administrator things by the way that I'm
forgetting not necessarily okay so
parameter updates so recall that there's
this four-step process to training a
neural network and this is a pseudo code
really in what it looks like we get a
data batch evaluate the loss evaluate
the gradient and perform a parameter
update when I talk about parameter
updates we're specifically looking at
this last line in here where we are
trying to make that more complex where
so right now what we're doing is called
just gradient descent where we take that
gradient and we that we've computed and
we just multiply it scaled by the
learning rate onto our parameter vector
we can be much more elaborate with how
we perform that update and so I flashed
this image briefly in the last few
lectures where you can see different
parameter update schemes and how quickly
they actually optimize this simple loss
function here and so in particular we
can see that SPD which is what we're
using right now in the fourth line here
that's SGD in red you can see that
that's actually the slowest one of all
of them so in practice you rarely ever
use just basic STD and there are better
schemes that we can use and we're going
to go into those in this lecture so
let's look at what the problem is with
SGD why is it so slow so consider this
particular slightly contrived example
here where we have a loss function
surface so these are the level sets of
our loss and suppose that it's elongated
along one direction much more than
another direction so basically this loss
function here is very shallow
horizontally but it's very steep
vertically and we want to of course
minimize this and right now we're at the
red spot and we're trying to get to the
minimum denoted by the smiley face
that's where we're happy but think about
what the trajectory of this is in both x
and y directions of SGD if we try to
optimize this landscape what would that
look like so what would it look like
horizontally and vertically I see
someone's butt so what are you plotting
out there okay and why is it okay so why
is it going to bounce up and down like
that and why is it not making a large
progress right so the local gradient is
is basically has this form where when we
look at the gradient horizontally we see
that the gradient is very small because
this is a shallow function horizontally
but vertically we have a large gradient
because it's a very steep function and
so what's going to happen when you roll
out SGD in these kinds of cases and you
end up with this kind of pattern where
you're going way too slow in horizontal
direction but you're going way too fast
in the vertical direction okay so you
end up at this ugly juror so one way of
remedying this kind of situation is what
we call an momentum update so the
momentum update will change our update
in the following way so right now we're
just incrementing the gradient we're
taking the gradient and we're
integrating our current position by that
gradient in a momentum update instead
we're going to take the gradient that
we've computed and instead of
integrating the position directly we're
going to increment this variable V which
I call V for velocity
so we're going to and we'll see why that
is in a bit so we increment this
velocity variable B and instead instead
we're basically building up this
exponential sum of gradients in the past
and that that's what's integrating the
position this mu here is a happy
parameter and mu is kind of a number
between zero and one and what it's doing
is its decaying the previous V and
adding on this current gradient so
what's nice about the momentum update is
that you can interpret it in a very
physical terms and in the following way
basically Optima using momentum update
corresponds to interpreting this func
this as really a ball rolling allows
this round this landscape and the
gradient in this case is your force that
the particle is feeling so this particle
is feeling some force due to gradient
but instead of directly integrating the
position this force F equals MA in
physics so force is equivalent to
acceleration there and so acceleration
is what we're computing and so the
velocity gets integrated by the
acceleration here and then the MU times
V has the interpretation of friction in
that case because at every single
iteration were slightly slowing down and
intuitively if this new times V was not
there then this ball would never come to
a rest because it was just Jigar around
the last surface forever and there would
be no loss of energy where it would
settle at the end of a loss function and
so that the momentum update is taking
this physical interpretation of
optimization where we have a ball
rolling around around and it's slowing
down over time and so the way this works
is what's very nice about this update is
you end up building up this velocity and
in particular in the shallow directions
it's very easy to see that if you have a
shallow but consistent direction then
the momentum update will slowly build up
the velocity vector in that direction
you'll end up speeding up and up across
the shallow direction but in a very
steep directions what's going to happen
as you start of course during around but
then you're always being pulled up the
other direction towards the center and
with the damping you end up kind of
oscillating to the middle and so it's
kind of damping these oscillations in
the steep directions and it's kind of
encouraging these oscillate it's
encouraging process in these consistent
shallow directions and that's why it
ends up improving the convergence in
many cases so for example here in this
visualization we see the SGD update in
red momentum update as in green and so
you can see what happens with the green
one
it overshoots because it's built up all
this velocity so it overshoots the
minimum but then it eventually ends up
converging down and of course it's
overshot but once it converges there you
can see that it's converging there much
quicker than just basic STD update so
you end up building up too much velocity
but then you eventually get there
quicker than if you did not have
velocity okay so that's the momentum
update I'll go into a particular
variation of the momentum update in a
bit I just wanted to ask ours any
questions about the momentum update this
point I'll go ahead oh yeah thank you
for asking so do we use a single meu and
usually we do that's a single hyper
parameter and usually it takes some
values of roughly point five or 0.9 and
usually people sometimes this is not
super common but people sometimes and
they'll eat from point 52.99 slowly over
time but it's just a single number
good yes so you could avoid this with a
smaller learning rate but then the issue
is if you had a slower learning rate
this learning rate is applied globally
to all directions in the gradient and so
then you would basically do no progress
in the horizontal direction right you
wouldn't jitter as much but then it
would take you forever to go
horizontally if you had a small learning
rate so is this kind of trade-off there
okay so I'd like to describe a
modification on the oh sorry oh thank
you so V here the question is how do you
initialize velocity you're usually in a
slot with zero and it doesn't matter too
much because you end up building it up
in the first few steps and then you end
up with this if you expand out this
recurrence you'll see that basically
it's a exponentially decaying some of
your previous gradients and so once
you've built it up you you have certain
bandwidth so initialize at zero okay so
a particular variation of momentum is
called something called Nesterov
momentum and or Nesterov accelerated
gradient descent and the idea here is we
have the ordinary momentum equation here
and the way to think about it is that
your x is incremented by really two
parts there's a part that you've built
up some momentum in a particular
direction so that's the momentum step in
green that's the Mutants V that's where
your momentum is
currently trying to carry you and then
you have the second contribution from
the gradient so the gradient is pulling
you this way towards the decrease of a
loss function and the actual step ends
up being the vector sum of the two so
the blue is what you end up with is just
the green plus the red and the idea with
Nesterov momentum and this ends up
working better in practice is the
following we know at this point
regardless of what the current input was
to us so we haven't computed the
gradient step yet but we know that we've
built up some momentum and we know we
were definitely going to take this green
direction okay so we're definitely going
to take this green so instead of
evaluating the gradient here at our
current spot néstor of momentum does
this one step look ahead and instead
evaluates the gradient at this point at
this point at the top of the arrow so
what you end up with is the following
difference here we know we're going to
go this way anyway so why not just like
look ahead a bit to that part of the
objective and evaluate the gradient at
that point and at that point of course
your gradient is going to be slightly
different because you're in a different
position and loss function and this
one-step look-ahead gives you a slightly
better direction over there and you get
a slightly different update now you can
do you can theoretically show that this
actually enjoys better theoretical
guarantees on convergence rates but not
only is it true in theory but also in
practice Nesterov omentum almost always
works better than just standard momentum
okay so the difference roughly is the
following here I've written it in light
tech notation instead of code but we
still have this velocity vector time
equals mu times the previous velocity
vector and the gradient that you're
currently evaluating and then we do an
update here and so the Nesterov update
the only difference is we're appending
here this new plus mu times VT minus 1
when we're evaluating the gradient we
have to evaluate at a slightly different
position in this look-ahead position and
so that's really a necessarily momentum
it almost always works better and now
there's a slight technicality here which
I don't think I'm going to go into too
much but it's slightly inconvenient the
fact that normally we think about just
doing a forward pass and backward pass
so what we end up with is we have a
parameter vector theta and the gradient
at that point but here necessary off
wants us to have a gradient parameter
theta theta and a gradient at a
different point so it doesn't quite fit
in with like a simple API that you
normally have in your code and so it
turns out that there's a way and I don't
want to really probably spend too much
time on this but there's a way to
basically do a variable transform where
you denote this
beefy you do some rearrangement and then
you get something that looks much more
like a vanilla update that you can just
swap in for momentum or you can swap it
in for SGD because you end up with only
needing gradient at fee and you do
updates on fee and this fee has really
looked ahead version of the parameters
instead of just the raw parameter vector
so that's just a technicality you can go
into notes to check this out okay so
here Nestor of accelerated gradient is
in magenta and you can see the original
momentum here overshot by quite a lot
but because Nestor of accelerate
momentum has this one step look ahead
you'll see that it curls around much
more quickly and that's because all
these tiny contributions of a slightly
better gradient at where you're about to
be end up adding up and you almost
always converge faster okay so that's
necessary of accelerated momentum so
until recently SGD momentum was the
standard default way of training
convolutional networks and many people
still train using just momentum update
so this is a common thing to see in
practice and even better if you can use
necessarily accelerated momentum so mag
here stands for slurry glint okay
question you're asking about the
optimization landscape and you're
thinking about minima and whether or not
you can maybe overshoot to like a wrong
minimum or something like that so I
think it's slightly incorrect to what so
when you think about the loss functions
for neural networks usually you think
about these crazy ravines and lots of
local minima everywhere that's actually
not a correct way to look at it that's a
correct approximation to have conceptual
in your mind when you have very small
neural networks and people used to think
that local minima are an issue and
optimizing heel networks but actually it
turns out with a lot of recent even
theoretical work that as you scale up
your models these local men images
become less and less of an issue so the
the picture to have in mind is there are
lots of local minima but they're all
about the same actually loss that's a
better way to look at it so these
functions neural networks actually in
practice end up looking much more like a
like a bowl instead of the crazy ravine
landscape and you can show that as you
scale up the neural network the
difference between like the worst and
your best local minimum it actually kind
of like shrinks down over time with some
recent results so basically there's no
bad local minima
only happens in very small networks so
and in fact in practice what you find is
if you initialize with different random
initialization you almost always end up
getting the same answer like the same
loss in the end so you don't end up
there's no like bad local minima you
sometimes converge to especially when
you have bigger networks thanks for the
question
okay what's your question over there
Nesterov as an oscillating feature which
part is oscillating okay I think you're
jumping ahead maybe by by several slides
we're going to go into second-order
methods in a bit okay so let me jump
into another update that is very common
to see in practice it's called a de grad
and it was originally developed in a
convex optimization literature and then
it was kind of ported over to neural
networks and people sometimes use it so
the other grad update looks as follows
we have this update as we normally see
so this is just basic stochastic
gradient descent here learning rate
times your gradient but now we're
scaling this gradient by this additional
variable that we keep accumulating okay
note here that this cache which we're
building up and is the sum of gradients
squared this cache contains positive
numbers only and note that the cache
variable here is a giant vector of the
same size as your parameter vector and
so this cache ends up building up the
demand in every single dimension we're
keeping track of the sum of squares of
the gradients or as we like to sometimes
call it the second moment although it's
the uncentered second moment and so we
keep building up this cache and then we
divide element wise this step function
by the square root of cache and so what
ends up happening here let's see so so
that's the reason that people call it a
/ / parameter adaptive learning rate
method because every single product
every single low dimension of your
parameter space now has its own kind of
like learning rate that is scaled
dynamically based on what kinds of
ingredients you're seeing in terms of
their scale so with this interpretation
what happens with a degrade in this
particular case if we do this what
happens in the horizontal and vertical
direction
kind of dynamics okay that's correct so
what you'll see is we have a large
gradient vertically and that large
gradient will be added up to cache and
then we end up dividing by larger and
larger numbers so we'll get smaller and
smaller updates in the vertical step so
since we're seeing lots of large
gradients vertically this will decay the
learning rate and we'll make smaller and
smaller steps in the vertical direction
but in the horizontal direction it's a
very shallow direction so we end up with
smaller numbers in the denominator and
you'll see that relative to the Y
dimension we're going to end up making
faster progress so we have this
equalizing effect of accounting for this
the steepness and in shallow directions
you can actually have much larger
learning rate then instead of the
vertical directions and but so that's at
a grad one problem with a degrade is
think about what happens to this step
size as we're updating this position if
we want to train an entire deep neural
network this takes for a long time and
we're training this over a long time
what's going to happen in a de grad okay
of course so your cache ends up building
up all the time you add all these
positive numbers goes into your
denominator you're learning they just
decays towards zero and you end up
stopping learning at like completely and
so that's not so that's okay in convex
problems perhaps when you just have a
bowl and you just kind of decay down to
the optimum and you're done but in a
neural network this stuff is kind of
like shuffling around and it's trying to
pick your data and that's like a better
way to think of it and so this thing
needs continuous kind of energy to thick
your data and so you don't want it to
just decay to a halt so there's a very
simple change to an autograph that was
proposed by Geoff Hinton recently and
the idea here is that instead of keeping
it completely just the sum of squares in
every single dimension we end we make
that counter a leaky counter so instead
we end up with this decay rate hyper
parameter which we set to something like
0.99 usually and then what you're doing
is you're accumulating sum of squares
but the sum of squares is leaking slowly
but this decay rate okay so we we still
maintain this nice equalizing effect of
equalizing the step sizes in steep or
directions but we're not going to just
converge completely to zero updates so
that's called rmsprop
one nice historical fun fact about
rmsprop by the way is the way it was
introduced was you think that it would
be a paper that proposed this method but
in fact it was a slide in Jeff Hinton's
Coursera class just a few years ago and
so Jeff Fenton just was giving this
Coursera class and who flashed the slide
of life oh there's this is unpublished
but this usually works well in practice
and do this and it's basically RMS
problem and so I implemented it then I
saw like better results on my
optimization right away and I thought
that was really funny and so in fact in
my in paper it's not only my papers but
many other papers people have cited this
slide from Coursera you just slide a
lecture six this slide just there's
rmsprop since then this is actually now
an actual paper and there's more results
on exactly what it's doing and and so on
but for a while this was really funny
and so in this optimization perspective
we can see a degrade here is blue and
rmsprop is this in black and we can see
that both of them converge quite quickly
down here this way in this particular
case at a grad ends up converging
slightly faster than our miss prop but
that's not always the case
some usually what you see in practice
when you train deep neural networks is
at a grad stops too early and rmsprop
will end up usually winning out in these
in these methods any questions about
that aggressor miss prop go ahead oh
sorry where's this image
smiley face don't you want it to just go
quickly down this keep the 30 so you're
saying that in some cases you might want
to actually make faster progress in
steeper direction the issue is in this
particular case maybe that's true but in
general and there are very steep
directions you probably don't want to
this method is saying don't make very
fast updates in that direction slow
yourself down so maybe in this
particular case you'd like to go faster
but you're kind of reading into this
particular example and that's not true
kind of in general in these optimization
landscapes that neural networks are made
up of so this ends up being a good
strategy kind of to apply in those cases
good yeah but so in the beginning oh by
the way I skipped over this explanation
of 1e negative seven but you guys can
hopefully see that 1e negative seven is
there just to prevent a division by zero
it's a smoothing factor it's a hyper
parameter usually we set it to one a
negative five or six or seven or
something like that in the beginning
your cash is zero so then you increment
you're like you still need a learning
rate to you what you get is this
adaptive behavior but the scale of it is
still in your control the absolute scale
that is still in your control you still
need a learning rate for this good like
what it's doing sorry just interrupt
it's kind of doing you can look at more
like a relative thing with respect to
different parameters how are you causing
the steps but the absolute global step
is still up to you good why do we cash
from the very beginning instead of the
last hundred thank you
so our mess prop is effectively doing
what you're describing right because it
ends up for getting sort of gradients
from very long time ago and it's only
really its expression at time T is only
a function of the last few gradients but
in an exponentially decaying weighted
sum okay cool so that's our miss prop
we're going to go into last update go
ahead
using like a window with the last let's
say an x-squared values that are some of
the other so you want to have a finite
window over which you're summing up
these gradients so would it be similar
to our mess prop except uh so Armas prop
is already adding up your gradients from
the past and an exponentially weighted
way and so you want to have a finite
window on this or I don't think people
have really tried you can yeah it takes
too much memory yeah so when you once
you're optimizing neural networks you'll
see that X for example I 140 million
parameters so that's taking up quite a
lot of memory and so you don't want to
keep track of ten previous gradients and
so on
okay so last update we're going to go
into oh sure
could you combine a degrade with
momentum thank you for the question yes
you could and that's this slide so so
roughly what's happening is Adam is this
last update that was only proposed very
recently and it kind of has elements of
both as you'll notice momentum is kind
of keeping track of the first order
moment of your of your gradient it's
summing up the raw gradients and it's
keeping this exponential sum and at a
grad and so on are keeping track of the
second moment of the gradient and it's
exponential sum and what you end up with
is an Adam and Adam update as you end up
with the step that's basically take it
it's kind of like let's see what yeah
it's kind of like our mess property
momentum a bit so you end up with this
thing that looks like it's basically
keep track of this velocity in a
decaying way and that's your step but
then you're also scaling it down by this
exponentially adding up a leaky counter
of your square gradients and so you end
up with both in the same formula and
that's Adam update combining those two
okay so you're doing both momentum and
you're also doing this adaptive scaling
and let's see so here's the Armas prop
actually I should have flashed this
earlier so when you compare this
basically rmsprop in red is the same
thing as here except we've replaced DX
which there was just the previous just
agree
currently right now we're replacing this
gradient DX with M which is this running
counter of our DX so if you imagine for
example one way to look at it also is
you're in a stochastic setting you're
sampling mini-batches there's going to
be lots of randomness in a forward pass
and you get all these noisy gradients so
instead of using any gradient at every
single time step we're actually going to
be using this decaying sum of previous
gradients and it kind of stabilizes your
gradient direction a bit and that's the
function of the momentum here and the
scaling here is to make sure that the
step sizes work out relative to each
other and steep in shell directions good
thank you
beta-1 and beta-2 our hyper parameters
beta 1 usually point-9 beta 2 usually
0.995 somewhere there so it's a hyper
parameter you have to cross validate
over it in my own work I found that this
is a relatively robust settings across I
don't actually usually end up cross
validating these I just set them to
fixed values usually but you can play
with those a bit and sometimes it can
help you a tiny bit okay cool good thank
you so the question is can you combine
necessary of momentum with a degrade so
here this is like a vanilla momentum we
saw the Nostromo momentum works better
can you do that yes you can actually
just read the paper about this yesterday
and actually wasn't a paper it was a
project report from 229 someone actually
did that I'm not sure if there's a paper
about it but yeah you can play with that
certainly that's not being done here ok
now one more thing that I so I have to
make Adam slightly more complex here as
you see it's incomplete so let me just
put in the for complete version in Adam
there's one more thing where you might
be confused when you see it there's a
this thing called bias correction that
they insert there and this bias
correction the way the reason I'm
expanding out the loop is that the bias
correction depends on your absolute time
step T so T is used here and the reason
for that is what this is doing is kind
of like a minor point and I don't want
anyone to be confused about this too
much but basically it's compensated for
compensating for the fact that mmv are
initialized at zero so your statistics
are kind of incorrect in the beginning
and so what it's doing is really it's
scaling up your mmv at the first few
iterations so you don't end up with a
very kind of biased estimate of the
first and a second moment so don't worry
about
that too much this is only this is only
changing your update at the very first
few time steps as as the atom is warming
up and so it's done in the proper way in
terms of the statistics of mmv okay I
don't want to go too much into that okay
so we talked about several different
updates and we saw that all these
updates have this learning rate
parameter still there and so I just
wanted to briefly talk about the fact
that all we still require a learning
rate and we saw what happens with
different traces of learning rates for
all of these methods the question I'd
like to pose is which one of these
learning rates is best to use maybe not
a well form question I'm trying to trick
you it's a trick question so when you're
running neural networks this is a slide
about learning rate decay the trick
answer is that none of those are good
learning rates to use what you should do
is you should use the high learning rate
first because it amaz is faster than the
good learning rate you see you make very
fast progress but at some point you're
going to be too stochastic and you can't
converge into your main very nicely
because you have too much energy in your
system and you can't settle down into
like nice parts of your loss function
and so what you do then is you decay
your learning rate and then you can kind
of ride this wagon of decreasing
learning rates and do best in all of
them so there are many different ways
that people decayed the learning rates
over time and you should also decay them
in your assignment there's step decay
which is kind of like the simplest one
perhaps where after one epoch of
training data epoch is referring to
you've seen every single training
example one time so after say one epoxy
decay the learning rate to by factor of
point nine or something like that you
can also use exponential decay or one
number ttk there's several several of
them are going to notes slightly
expanding on some of the theoretical
properties that have been proven about
these different decays unfortunately not
many of them applied because I think
they're mostly from convex optimization
literature and we're dealing with very
different objectives but usually in
practice I just use exponential decay or
something like that was there a question
good
I see so you're asking about not
committing to any one of these but you
want to also like shift between them
during training yeah I don't think
that's a standard at all that's an
interesting point I'm not sure I'm not
sure when you'd want to use yeah it's
not clear to me you could try there in
your assignment that's a fun thing to
try in practice I'd like to make the
point that you almost always I find at
least in practice right now Adam is
usually the nice default choice to go
with so I use Adam for everything now
and it seems to work quite well better
than momentum or rmsprop
or a degrade or anything like that okay
cool so these are all first order
methods as we call them because they
only use your gradient information at at
your loss function so we evaluating the
gradient and we basically know the slope
in every single direction and that's the
only thing that we use there's an entire
set of second-order methods for
optimization that you should be aware of
the second-order optimization methods I
don't want to go into too much detail
but they end up forming a larger
approximation to your loss function so
they don't only approximate it with this
basically hyperplane of like which way
are we sloping but you also approximated
by this Hessian which is telling you how
your surface is curving so you don't
only need the gradient you also need the
Hessian and you need to compute that as
well and you may have seen a Newton
method say for example in 229 so in
Newton method it's basically giving you
an update that once you've formed your
bowl-like Hessian approximation to your
objective you can use this update to
dump to jump directly to the minimum of
that of that approximation and then you
can rate the scheme so what's nice about
second order methods why do people like
these or use them especially the Newton
method as presented here what's nice
about this update faster convergence
Thank You let's Hyper parameters you'll
notice no learning rate no hyper
parameter in this update okay and that's
because if you see your gradient in this
loss function in this loss function but
you also know the curvature in that
place and so if you approximate it with
this bowl you know exactly where to go
to the minimum of your approximation so
there's no need for a learning where you
can jump directly to that minimum of
that approximating Bowl so that's a very
nice feature I think those are the two
that I had in mind you have a faster
convergence because you're using second
order information as well why is it kind
of impractical to use this step update
in training neural networks yeah so the
issue of course is hashing say you have
a hundred million parameter network
you're Hessian is 100 million by 100
million matrix and then you want to
invert it so good luck with that so this
is not going to happen so there are
several kind of algorithms that I just
like you to be aware of we're not going
to use them in this class but just be
aware that there's something called BFGS
which basically lets you get away with
not inverting the Hessian it builds up
an approximation of the Hessian through
successive updates that are all Rank 1
and it kind of builds up this Hessian
but you still need to store the Hessian
in memory so still no good for large
networks and then there's something
called l-bfgs short for limited memory
BFGS which does not actually store the
full Hessian or its approximated in
inverse and that's what people use in
practice sometimes now l-bfgs
you'll see sometimes mentioned in
optimization literature especially what
it works really really well for is if
you have a single small deterministic
function like f of X there's no
stochastic noise like there's no
stochasticity in F and everything fits
in your memory then l-bfgs can usually
crush these loss functions very easily
but what's tricky is to extend l-bfgs to
basically very very large data sets and
the reason is that we're subsample in
these mini-batches because we can't fit
all the training data into memory so we
sub sample mini batches and then l-bfgs
kind of works on these mini batches and
it's approximations end up being
incorrect as you swap different mini
batches and and also the stochastic see
you have to be careful with it then you
have to make sure that you fix this
dropout you have to make sure that your
function so internally l-bfgs calls your
function many many different times is
doing all these approximations and line
search and stuff like that it's a very
heavy function and so you have to make
sure that when you use this you disable
all sources of randomness because it's
really not going to like it so basically
in practice we don't use l-bfgs because
it seems to not very not work really
well right now compared to first urban
methods it's basically too heavy too
much stuff is happening and you it's
better to just do this noisy er stuff
but do more of it that's the trade-off
so in summary use Adam as a good default
choice and if you can afford to you just
have you can afford full batch so maybe
your data set is not very large you can
afford to have it all in memory and do
all the forward and negative passes in
memory then you can look into l-bfgs but
you won't see it in practice used in any
large-scale setting right now although
it's research direction right now
alright so that concludes my discussion
of different parameter updates decay
your learning rates we're not going to
look into all BFGS in this class yeah
there's a question in the very back
um so I'm not sure if I fully understood
your question you're asking about so a
dad for example it automatically decays
your learning rate over time so would
you use also learning rate decay if
you're using at a grad so usually you
see learning rate decay very common when
you do STD or SUV momentum I actually
I'm not sure if you'd use it with at a
grad or or Adam I've used well your
learning rate to eat with Adam before it
tends to help a little bit but it kind
of breaks some of the theory but yeah
it's it's not yet yeah ah not not a very
good answer there you can certainly do
it but maybe Adam is not like Adam will
not just monotonically make your
learning rate zero at the end right
because it's a leaky gradient but if you
use data grab then certainly decaying
the learning rate probably does not make
sense because it's decayed automatically
to zero in the end all right cool okay
so we're going to go into a model
ensembles I just very briefly like to
talk about it because it's quite simple
turns out that if you train multiple
independent models on your training data
instead of just a single one and then
you average their results at test time
you always get two percent extra
performance okay so this is a not really
a theoretical result here it's kind of
like an object but just like in practice
basically this is like a good thing to
do almost always works better the
downside of course is now you have to
have all these different independent
models and you need to do forward and
forward passes of all of them and you
have trained all of them so that's not
ideal because you have a linear slowdown
test time with the number of models in
your ensemble and so there are some tips
and tricks for using ensembles but kind
of faking it a bit so one approach for
example is as you're training your
neural network you have all these
different checkpoints usually you're
saving them every single Epoque you save
a checkpoint and you figure out what
your was your validation performance so
one thing you can do for example it
turns out to actually give slight boost
sometimes is you just take some
different check points of your model and
you do an ensemble over those that
actually turns out to sometimes improve
things a bit and so that way you don't
have to train seven independent models
you just trained one but you ensemble
some different check points related to
that there's a trick of four tests ok so
what's happening here this
is your four steps that we've seen
before I'm keeping another set of
parameters here X test and this X test
is a running sum exponentially decaying
of my actual parameter vector X and when
I use X test and validation or test data
it turns out that this almost always
perform slightly better than using X
alone okay and so this is kind of doing
like a small like weighted ensemble of
last previous few parameter vectors it's
kind of a it's kind of difficult to
interpret actually but basically one way
to interpret it one way I can hand wave
about why this is actually a good thing
to do is think about optimizing your
bowl function and you're stepping too
much around your minimum then actually
taking the average of all those steps
gets you closer to the minimum okay so
that's the hand waving I can do for y
this actually ends up working slightly
better
so that's model ensembles I had to
discuss model ensembles because we're
going to look into dropout and this is a
very important technique that you will
be using and implementing and so on so
the idea for dropout is very interesting
what you do with dropout is you as
you're doing a forward pass of your
neural network you will randomly set
some neurons to zero in the forward pass
okay so just to clarify what you will do
is as you're doing a forward pass of
your data X you're computing say in this
function your first hidden layer is the
non-linearity of w1 times X plus b1 so
that's the activations of the first
inner layer and then I will compute here
a mask of binary numbers either 0 or 1
based on whether or not numbers between
0 & 1 are smaller than P which we here
see is point 5 so this u1 is a binary
mask of zeros and ones half in half and
then we multiply that onto our hidden
activations effectively dropping half of
them so we've computed all the
activations h1 the hidden layer and then
we drop half the units at random and
then we do 2nd and then we drop half of
them at random okay and of course this
is only the forward pass
the backward pass has to be
appropriately adjusted as well so these
drops have to be also back propagated
through so remember to do that when you
implement dropout so it's not only in
the forward pass you drop but in the
backward pass you have to back propagate
through multiplying by u2 and by u 1 so
you kill gradients basically in places
where you've dropped a unit
okay so you might be thinking when I
showed you this for the first time how
how does this make any sense at all and
how is this good idea why would you want
to compute your neurons and then set
them at random to zero how does that
make any sense whatsoever so I don't
know let's let's what you guys think
go ahead would it prevent overfitting in
what sense okay you're roughly getting
the right intuition so you're saying it
will prevent overfitting because if I'm
only using half of my network then
roughly I have like smaller capacity I'm
only using half of my network any one
time and with smaller networks there's
only like basically there's only so much
I can do with half a network then as a
full network so it's kind of like a
control of your of your variance in
terms of what you can represent good yep
yep okay I would like to be slightly
careful with the terms that I like
bias-variance tradeoff and so on I
haven't really we're not going to do
that too much but yeah basically have a
smaller model it's harder to overfit
good okay you're saying it's like having
many ensembles of different neural
networks we're going to go into that
point in a bit okay so you're saying
that it's forcing all the neurons to be
useful because if one of them gets
dropped out then if that if that one was
the only one that was used upstairs
okay I have a better way of rephrasing
that point in my next slide let's look
at a particular example instead of hand
waving okay suppose that we are trying
to compute the cat score in the neural
network okay and the idea here is that
you have all these different units and
what dropout is doing is it's forcing
there many ways to look at dropout but
one of them is it's forcing your code
your representation for what the image
was about to be redundant because you
need that redundancy because your
about to in a way that you can't control
get half of your network dropped off and
so you need to base your cat score on
many more features if you're going to
correctly compute the cat score because
any any one of them you can't rely on it
because it might be dropped and so
that's one way to look at it so in this
case we can still classify cat score
properly even if we don't have access to
whether or not it's very or mischievous
and so so that's one interpretation of
drop out ok another interpretation of
drop out is as was mentioned in terms of
an ensemble so drop out is effectively
can be looked at as training a large
ensemble of models that are basically
sub networks of this one large network
but they kind of share parameters in a
weird way so to understand this you have
to notice the following if we do a
forward pass and we randomly drop off
some of the units then in backward pass
think about what happens with the
gradient right so suppose we've branded
randomly dropped off these units in a
backward pass we're back propagating
through the masks that were induced by
the drop out so in particular only the
neurons that were used in the forward
pass will actually be updated or have
any gradients flowing through them
because any neuron that was shut off to
zero no gradient will flow through it
and it's weights to its previous layer
will not be updated
so effectively any neuron that was
dropped out its connections to the
previous layer will not be updated and
it'll just it's as if it wasn't there so
really with the drop out masks your sub
sampling a part of your neural network
and your only training that neural
network on that single example that you
have at that point in time so each
binary mask is one model and gets
trained on only one data point
okay I can try to repeat that it came
from somewhere here I'm onto you guys
okay but do people actually understand
this or not spur okay so when you drop a
unit you drop you drop a neuron I wish I
had the example of the neuron right but
if I drop its value I multiply its
output by zero then its effect on the
last function there's no effect right so
it's gradient will be zero because it's
Valley was not used in computing the
loss and so its weights will not get an
update and so it's as if we've sampled a
part of the network and we only trained
that single data point that currently
came to the network we only trained on
it and every time we do a forward pass
we subsampled a different part of your
neural network but they all share
parameters so it's kind of like a weird
ensemble of lots of different models
altering the one data point but they all
share parameters so that's kind of
roughly the the idea here does that make
sense okay cool go ahead question
usually say 50% is a very rough
approximation you can use
yeah the weight array is the same size
so in this in this forward pass you'll
notice we actually compute all the
neurons H we compute them just as we did
before all the neurons get computed but
then half of the values will get drops
to zero so nothing changes there oops oh
yes I will see that in a bit good would
you be making the matrix sparse so can
you take advantage of some sparse matrix
computations so instead of computing all
the HS you want to only compute the
neurons that are not being dropped and
in that case you want to do sparse
updates so you could in theory but I
don't think that's done usually in
practice we don't worry too much
oh I see so in every single forward pass
we sample these right we sample the
masks at every single forward pass and
so you always get a different like sub
network that you're training so every
single iteration we get a mini batch we
sample our noise pattern for what we're
going to drop out and we do a forward
and backward pass and update the
gradient and we keep iterating this over
and over again oh I see so your question
is can we add like some how cleverly
choose the binary mask in like a way
that best optimizes the model or
something like that not really I don't
think that's done or anyone has looked
into it too much good sorry
oh yes so I'm going to get into that in
one slide in next slide we're going to
look at this time I'll take up one last
question good so two questions one is
can you use drop out to different
amounts in different layers you can
there's nothing stopping you I it's
intuitively you want to apply stronger
drop out if you need more regularization
so there's a layer that has a huge
amount of parameters will see that
income that's in one example you want to
apply stronger drop out there
conversely there might be some layers
that we'll see what convolution networks
early on the convolutional layers are
very small you don't we usually apply as
much drop out there so it's quite common
for example in the commercial Network
and I'll go into this in a bit you start
off with low dropout and then you scale
that up over time so the answer to that
is yes and I forgot your second question
was it oh can you instead of units drop
out just individual weights you can and
that's called something called drop
connect we won't go into too much in
this class but there's a way to do that
as well okay now at test time a test
time ideally what you want to do is
we've introduced all this noise right
into the forward pass and so what we'd
like to do now at test time is we'd like
to integrate out all that noise and a
Monte Carlo approximation to that would
be something like you have a test image
that you'd like to classify you can do
many forward passes with many different
settings of your binary masks and you're
only using the sub networks and then you
can average across all those probability
distributions so that would be great but
unfortunately it's not very efficient so
it turns out that you can actually
approximate this process to some degree
as Jeff Fenton pointed out and when they
first introduced dropout and the way
we'll do this intuitively you want to
take advantage of all your neurons you
don't want to be dropping them out at
random so we're going to try to come up
with a way where we can leave all the
neurons turned on so do no dropout in a
forward pass on a test image but we have
to actually be careful with how we do
this so we can so in a for pass for test
images we're not going to drop any units
but we have to be careful with something
and basically one way to get at what the
issue is is suppose that this was a
neuron and it's got two inputs and
suppose that with all these inputs press
at test time so we're not dropping unit
so we're a test time these two have some
activations and the output of this
neuron gets computed to be some value of
x you have to compare this value of x to
what the neurons output would be during
training time in expectation okay
because in in training time this dropout
masks vary randomly and so there's many
different cases that could have happened
and in different in those cases the
outputs of this neuron would be possibly
in a different scale and you have to
worry about this so let me show you
exactly what this means I think so
during test this neuron computes say
there's no non-linearity we're only
looking at a linear neuron during Tres
test this activation becomes w0 which is
the weight here times X plus W 1 times y
ok so that's what we want to compute at
test time and the reason we have to be
careful is that during training time the
expected output of a in this particular
case would have been quite different so
we have four possibilities we could have
dropped one or the other or both or none
so in those four possibilities we would
have computed different values and if
you actually crunch through this math
you'll see that when you reduce it you
end up with 1/2 of w0 X plus w1 times y
so in expectation at training time the
output of this neuron was actually a
half of what it is at test time okay and
so when you want to use all the neurons
at test time you have to compensate for
this additional half and that's half by
the way is coming from the fact that
we've dropped units with probability of
1/2 and so that's why this ends up being
1/2 and so with probability point 5 all
inputs in a forward pass so basically if
we did not do this then we end up having
too large of an output compared to what
we had in expectation during training
time and your output distribution would
change and basically things in the
neural network would break because
they're not used to seeing such large
outputs from all the neurons and so you
have to compensate for that and you have
to squish down so now you're using all
your things instead of just half of the
things but you have to squash down the
activations to get back the to recover
your expected output ok this is actually
a tricky point but I think I was told
once the story that when Geoff Hinton
came up with dropout in the beginning he
actually didn't fully come up with this
part so we tried dropout
it didn't work and actually the reason
it didn't work is he he missed out on
this tricky point actually admittedly
and so you have to scale your
activations at test time down because of
this effect and then everything works
much better
so at test time just to show you what
this looks like
we basically compute these neural nets
as normal so we compute the first layer
second layer but now at test time we
have to multiply by P so for example at
P is 1/2 we're dropping out with 1/2
probability that were scaling down the
activation so that the expectation the
expected output now is the same as
expected output in the training time and
so at this time you actually recover
full dropout and the expected outputs
are matching and this actually works
really well good so in training we're
half the time dropping these inputs and
so you end up with some some expected
output from this neuron I don't think
there's an issue at train time basically
it's just the discrepancy between train
and test like if you're using all your
neurons instead of dropping them there's
discrepancy so either you can correct it
at test time or you can use what we call
inverted dropout which I'll show you in
a bit so let me just get to that in a
bit
so dropout summary if you want to use
dropout drop your units with probability
of with keeping the probability of P and
then at test time don't forget to scale
them so if you do this your neural
networks will do will work better ok and
don't forget to also back propagate the
masks which I'm not showing here an
inverted dropout by the way to is to
take care of this discrepancy between
the train and test distribution in a
slightly different way in particular
what we'll do is we're changing this
step here so before you one was a binary
mask of zeros and ones what we're now
going to do is we're going to do the
scaling here at training time so we're
going to scale down the activations at
training time or rather scale them up
because if P is 0.5 then we're boosting
activations at train time by 1/2 and
then at test time we can leave our code
untouched right so we're doing the
boosting of the activations at train
time we're making everything
artificially greater by 2x and then a
test time we're supposed to have but now
we're just going
recover the clean expressions because
we've done the scaling a training time
so now you'll be you'll be properly
calibrated in expectations between the
train and test of every neuron in the
network
okay so let's wrap it so use inverted
dropout that's the most common one to
use in practice so in fact it really
comes down to a few lines and then the
backward pass changes a bit but the
network's almost always work better with
this good unless you're severely
underfitting
good thank you for the question does
that depend on you having a linear
response activation function it does so
once you have nonlinearities in there
then these expectations aren't actually
exact and that's why this is an as I
mentioned here approximation it's an
approximation to valuing the fallen
sample and one of the reasons in
approximation is because once you
actually have nonlinearities in the
picture then these expected outputs are
all kind of screwed up because of the
nonlinear effects on top of these so
yeah that's a good question thank you
for pointing that I'll go ahead
I see you're saying that the inverted
drop and drop out are not equivalent so
doing a very rapid or not is not
equivalent because of the Denali Ortiz
um I'd have to think about it maybe
maybe you're right ah yeah maybe you're
right
yeah yeah good
so we're P here is 0.5 right so it's
probably a point 5 or dropping I see so
sometimes you have more dropped and less
drop then you have an entire
distribution like in some forward passes
you'll have fewer neurons than half or
more neurons and a half but I think all
of this is just about expectations in
expectation you're dropping a half and
so that's the correct thing to use even
though there's some randomness on
exactly the amount that actually end up
being dropped okay great
oh yeah this is a placeholder slide to
tell you guys a fun story about drop out
so I was in a deep learning summer
school in 2012 and Geoff Hinton was for
the first time or at least the first
time I saw it presenting dropout and so
he's basically just saying okay set your
neurons to zero at random and the test
time just boost the activations and this
always works better better and we're
like wow that's interesting and so a
friend of mine sitting next to me he
just pulled up his laptop right there he
has a station of his university machines
and implemented right there during the
talk and by the time geoff hinton
finished the talk he was getting better
results and getting actually
state-of-the-art report her like
accuracies on his data said that he was
working with so that's the that's the
fastest I've seen someone go like get an
extra few boos percent it was right
there and then horology fintan was
getting to talk so I thought that was
really funny there's very few times that
actually this something like this
happens and so drop out is a great thing
because it's one of those few advances
that is very simple and it always works
just better and there's very few of
those kinds of tips and tricks that
we've picked up and I guess the question
is how many more simple things like
dropout are there that just give you 2%
boost
always so we don't know okay so I was
going to go on at this point into
gradient checking ah but I think I
actually I decided that I'm going to
skip this because I'm tired of all the
neural network like we've been talking
about lots of details of training neural
networks and I think you guys are tired
as well and so I'm going to skip
gradient checking because it's quite
well described here in notes so I
encourage you to go through it
gradient checking is kind of a tricky
process it takes a bit of time to
appreciate all the difficulties with the
process and so just read through it I
don't think there's anything I can hand
wave around to make it more interesting
to you and so I would encourage you to
just check it out
meanwhile we're going to jump right
ahead and going to commercial networks
and look at pictures okay so couple
neural networks look like this this is a
leanette five from 1980 roughly and so
we're going to go into details of how
commercial neural networks work and in
this class we're not actually going to
going to do any of the low-level details
I'm just going to try to give you
intuition about how this field came
about some of the historical context and
just complex all networks in general so
if you'd like to talk about the history
of convolutional networks you have to go
back to roughly 1960s to experiments of
hooble and Wiesel
so in particular they were studying the
prime of the visual cortex in a cat and
they were studying an early visual area
in the cat brain as the cat was looking
at patterns on the screen and they ended
up actually winning a Nobel Prize for
this sometime later for these
experiments and so I'd like to show you
what these experiments look like just so
they're really fun to look at so I
pulled up a YouTube video here and so
what's going on here is the cat is fixed
in position and we're recording from its
cortex somewhere in the first visual
area of processing which is in the back
of your brain called v1 and now we're
showing different light patterns to the
cat and we're recording and hearing the
neurons fire for different stimuli so
let's look at how this experiment looked
like
I don't know if you guys can hear
so nothing happens when it goes this way
and then he's going to make it go that
way okay I don't if you guys can hear it
all the way back okay so this is one
neuron in the v1 cortex and through
experiments like this they basically
figured out that there are these cells
and they seem to turn on four edges in a
particular orientation and they get
excited about edges in one orientation
any other norian tation does not excite
them okay and so like this through a
long process this is like a ten minute
video so we're not gonna go to basically
for a long time they experimented and
they came up with a model of how the
visual cortex processes information in
the brain and so they found several
things the gate that ended up leading to
their nobel prize for example they
figured out that the cortex is arranged
retina topically the visual cortex and
what that means is that let's see
where's my printer basically nearby
cells in the cortex so this is cortical
tissue unfolded nearby cells in your
cortex are actually processing nearby
areas in your visual field so your
whatever is mapping onto your recognized
process nearby in your brain this
locality is preserved in your processing
and they also figured out that there was
an entire hierarchy of these rows what's
called simple cells and they responded
to a particular orientation of an edge
and then there were all these other
cells that had more complex system
responses so for example some cells
would be turning off for a specific
orientation but we're slightly
translationally invariant so they don't
care about the specific position of the
edge but they only cared about the
orientation and so they hypothesized
through all these experiments that the
original cortex has this kind of
hierarchical organization where you end
up with simple cells that are feeding to
other cells called complex cells and etc
and these cells are building on top of
each other and these simple cells in
particular have these relatively local
receptive fields and then we're building
up more more complex kind of
representations in the brain through
successive layers of representation and
so these were experiment by hobo and
easel and of course they some people are
trying to reproduce this in in computers
and try to model the visual cortex with
code and so one of the first examples of
this was the neurocognitive trial
Fukushima and he basically uh ended up
setting up a layered architecture with
these local receptive sales that
basically these are neurons that look at
a small region of the input and then he
stacked up layers and layers of these
and so he had these simple cells and
then complex cells simple cells complex
cells in the sandwich of simple and
complex cells building up into a
hierarchy now back then though in 1980s
back propagation was still not really
around and so Fukushima had an
unsupervised learning procedure for
training these networks with like a
clustering scheme but this was not back
propagate at the time but it had this
idea of successive layers small cells
building up on top of each other and
then Yela come to call this experiments
further and he kind of built on top of
who she must work and he kept the
architecture and layout but what he did
was actually trained these networks with
back propagation and so for example he
trained different classifiers for digits
or letters and so on and so trained all
of it with backdrop and they actually
ended up using this in complex systems
that read check they read off like
digits from postal mail service and so
on and so common let's actually go back
to quite a long time ago to 1990s and so
on when Jana Kuhn was using them back
then but they were quite small okay
and so in 2012 is when the comment
started to get quite a bit bigger so
this was the paper from that I keep
referring to from Alex Khrushchev's key
Ilya sutskever and Jeff Fenton they took
all of image net image net as the data
set that comes actually from a face lab
from our lab so it's a million images
with thousand classes huge amount of
data you take this model which is
roughly 60 million parameters and it's
called an Alex net based on the first
name of Alex Khrushchev ski these
networks were going to see that they
have names so this is Alex net there's a
vgg net a Zenith net Google net
there's several nets so just like this
one is Linnet and so we give them names
so this was Alex net and it was the one
that actually outperformed by quite a
bit all the other algorithms what's
interesting to note historically is the
difference between Alex net in 2012 and
the Linnet in 1990s there's basically
very very little differences when you
look at these two different these two
networks this one used I think sigmoids
or 10 H 10 H probably and this one used
relu
and it was bigger and deeper and he was
training GPU and it had more data and
that's basically it that's the only like
that's roughly the difference and so
really what we've done is we figured out
better ways of course initializing them
and it works better with batch norm and
rel lose work much better but other than
that it was just scaling up both the
data and the compute uh but for the most
part the architecture was quite similar
and we've done a few more tricks like
for example they used big filters we'll
see that we use much smaller filters we
also now this is only a few tens of
layers we now have 150 layer commnets so
we really just scale this up quite a bit
in some respects but otherwise the basic
concept of how you process information
is similar okay so comments are now
basically everywhere ah so they can do
all kinds of things like classify things
of course they're very good at retrieval
so if you show them an image they can
retrieve other images like it they can
also do detection so here they're
detecting dogs or horses or people and
so on you'll this might be used for
example in self-driving cars I'll have
this on the next slide they can also do
semantic segmentation so every single
pixel is labeled for example as a person
or a road or tree or sky or building so
that segmentation so they're used in
cars for example here's an nvidia tegra
which is a small embedded GPU we can run
commnets on these and for example this
might be useful in the self-driving car
where you can identify all the you can
basically do perception of around you of
things around you come that's are
identifying faces probably if you some
of your friends are tagged on facebook
automatically it's almost certainly I
would guess at this point come that
they're used on video classification on
YouTube identifying what's inside
YouTube videos they're used in this is a
project from Google that was very
successful where basically Google is
really interested in taking Street view
images and automatically reading out
house numbers from them okay and turns
out this is a perfect task for a ComNet
so they had lots of human laborers
annotate huge amounts of this data and
then put a giant comment on it and it
ended up working almost as well as a
human and that's a thing that will see
throughout that this this stuff works
really really well they can estimate
poses
they can play computer games they detect
all kinds of cancer or something like
that and bye-bye-bye images they can
read Chinese characters recognize street
size this is I think segmentation of
neural tissue they can also do things
that are not visual so for example they
can recognize speech so contents have
been used for speech processing they've
been used also for text documents so you
can feed text into commnets as well
they've been used for to recognize
different types of galaxies they've been
used to in recent cattle competition to
recognize different whales so this is a
particular whale there was like hundred
whales or something like that and you
have to just use a color to recognize
specific individual whales so this whale
by the pattern of its you know white
spots on its head is a particular whale
that become that has to recognize so
it's amazing that that works at all
they're using satellite images quite a
bit because now there are several
companies that have lots of satellite
data so this is all analyzed with large
commnets in this case it's finding roads
but you can also look at agriculture
applications and so on they can also do
image captioning so you might have seen
some some of these results my work
included as well where you take images
and you caption them with sentences
instead of just a single category and
they can also be used for various
artistic endeavors so this is something
called deep dream and we're going to go
into how this works you'll actually
implement anything in your third
assignment maybe okay maybe you will
implement this on your third assignment
you give it an image and using ComNet
you can make it do weird stuff in
particular you'll notice there are lots
of hallucinations of dogs and we're
going to go into why dogs appear it has
to do with the fact that imagenet which
is where these networks get trained they
end up they have a lot of dogs and so
the so these networks end up
hallucinating dogs it's kind of like
they're used to some patterns and then
when you show them a different image you
can make them put them in the loop of
the image and they'll hallucinate things
so we'll see how this works in a bit I'm
not going to explain the slide but it
looks cool so you can imagine that a
calm that is probably involved somewhere
I also wanted to point out that what's
interesting there's this paper called
Deakin neural networks rival
representation of primate ID cortex call
for a core visual recognition what they
did here is
they are basically looking at I think
this was a macaque monkey and they're
recording from the IT from the from the
iit cortex here and they're recording
neural activations as a monkey is
looking at images and then they fed the
same images to a convolutional neural
network and what they're trying to do is
from the popul from the convolutional
neural network code or from the
population of neurons that are is only a
sparse population of neurons in the IP
cortex they're trying to perform a
classification of some concepts and what
you see is that decoding from the i.t
cortex and classifying images is almost
as good as using this neural network
from 2013 so in terms of the information
that's there about the image you can do
almost equal in performance for
classification perhaps even more
striking results here where they were
comparing they fed a lot of images
through the convolutional Network and
they got this monkey to look at lots of
images and then you look at how these
images are represented in the brain or
in the content so these are two spaces
of representation of how images are
arranged in the space by the comment and
you can compare the similarity matrices
and statistics and you'll see that the
i.t cortex and the cognate commnets are
basically very very similar
representation there's a mapping between
them it almost seems like similar things
are being computed the way they arrange
the visual space of different concepts
and what's close and what's far is very
very remarkably similar to what you see
in the in the brain and so some people
think that this is just some evidence
that comments are doing something brain
like and that is very interesting so the
only question that remains then in that
case is how do you come that's work and
we'll find out in the next class so
that's it