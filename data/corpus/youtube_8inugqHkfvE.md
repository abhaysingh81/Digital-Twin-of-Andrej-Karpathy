# YouTube Transcript: 8inugqHkfvE

and we're recording as well okay great
just to remind you again hello uh we're
recording the classes so if you're
uncomfortable speaking in in the camera
you're not in the picture but your voice
might be uh on the on the uh recording
okay great uh as you can see also the
screen is uh wider than it should be and
I'm not sure how to fix it so we'll have
to live with it luckily your visual
cortex is very good it's very invariant
to stretching so this is not a problem
okay so we'll start out with some
administrative things before we dive
into the class
um the first assignment will come out
tonight or early tomorrow uh it is due
on January 20 so you have exactly two
weeks you will be writing a kous neigh
classifier a linear classifier and a
small two layer neural network and
you'll be writing the entirety of back
propagation algorithm for a two two
layer neural network we'll cover all
that material in the next two weeks and
um Warning by the way there are
assignments from last year as well and
we're changing the assignments so they
will please do not complete a 2015
assignment that's something to be aware
of and uh for your computation by the
way we'll be using Python and numpy uh
and we'll also be offering terminal.com
which is uh which is basically these
virtual machines in the cloud that you
can use if you don't have a very good
laptop and so on I'll go into detail of
that in a bit I just like to point out
that for the first assignment we assume
that you'll be relatively familiar with
python and you'll be writing these
optimized numpy Expressions where you're
manipulating these matrices and vectors
in very efficient forms so for example
if you're seeing this code and it's
doesn't mean anything to you then please
have a look at our python NPI tutorial
that is up on the website as well it's
written by Justin and it's very good and
uh so go through that and familiarize
yourself with the notation because
you'll be seeing you'll be writing a lot
of code that looks like this uh where
we're doing all these optimized
operations so they're fast enough to run
on a CPU now in terms of terminal
basically what this amounts to is that
we'll give you a link to the assignment
you'll go to a web page and you'll see
something like this this is a virtual
machine in the cloud that has been set
up with all the dependencies off the
assignment they're all installed already
all the data is already there and so you
click on launch a machine and this will
basically bring you to something like
this this is running in your browser and
this is basically a a thin layer on top
of an AWS uh machine a UI layer here and
so you have an iPad to notebook and a
little terminal and you can go around
and this is just like a machine in the
cloud and so they have some CPU
offerings and they also have some GPU
machines that you can use and so on uh
you normally have to pay for terminal
but we'll be Distributing credits to you
so you just uh email us to a specific ta
that will decide in a bit you email to a
TA and you ask for money we'll send you
money and we keep track of how much
money we've sent to all the people so
you have to be responsible with the
funds uh so this is also an option for
you to use if you
like uh okay any details about this y go
a quick question you said that they have
GP units does that mean we can write
Huda code or is that not acceptable uh
you can you can write it if you like
it's not required for the assignment but
you can probably get that to run yeah
okay great so I'm just going to dive
into the lecture now today we'll be
talking about uh image classification
and especially uh we'll start off on
linear classifiers so when we talk about
image classification um the basic task
is that we have some number of fixed
categories say a dog cat truck plane or
so on we get to decide what these are
and then the task really is to take an
image which is a giant grid of numbers
and we have to transform it to one of
these labels we have to bin it into one
of the categories this is the image
classification problem we'll spend most
of our time talking about this one
specifically but if you'd like to do any
other task in computer vision such as
object detection image captioning
segmentation or whatever else you'll
find that once you know about image
classification and how that's done
everything else is just a tiny Delta on
top of it so you'll be in a great
position to do any of the other tasks so
it's really good for conceptual
understanding and we'll work through
that as a specific example uh to
simplify things in the beginning now why
is this problem hard just to give you an
idea the problem is what we refer to as
a semantic Gap this image here is a
giant grid of numbers the way images are
represented in the computer is that this
is basically say roughly a 300X 100x 3
pixel array so threedimensional array
and the three is for the three color
channels red green and blue and so when
you zoom in on a part of that image it's
basically a giant grid of numbers
between 0 and 255 uh so that's what we
have to work with these numbers indicate
the amount of brightness in all the
three color channels at every single
position in the image and so the reason
that image classification is difficult
is when you think about what we have to
work with these like millions of numbers
of that form and having to classify
things like cats it quickly becomes
apparent the complexity of the task so
for example the camera can be rotated
around this cat and it can be Zoomed In
and Out and rotated shifted the focal
properties intrinsics of that camera can
be different and think about what
happens to the brightness values in this
grid as you actually do all these
Transformations with a camera they'll
completely shift all the patterns are
changing and we have to be robust to all
of this there's also many other
challenges for example challenges of
Illumination here we have have a long
cat uh long cat we actually have two of
them but you almost even can't see the
other one um and so one cat is basically
illuminated quite a bit and the other is
not but you can still recognize two cats
and so think about again the brightness
valys on the level of the grid and what
happens to them as you change all the
different lightings and all the possible
lighting schemes that we can have in the
world we have to be robust to all of
that there's issues of um deformation
many
classes lots of uh strange uh
Arrangements of all these objects we'd
like to recognize so cats coming in very
different uh poses by the way the slides
when I create them they're quite dry
there's a lot of math and so on so this
is the only time I get to have fun so uh
that's why I just pile everything with
cat pictures uh so we have to be robust
to all of these deformations you can
still recognize that there's a cat in
all of these images despite its
Arrangement there's problems of
occlusion so sometimes we might not see
the full object but you still recognize
that that's a cat behind a curtain
that's a cat behind a water bottle and
there's a also a cat there inside a
couch even though you're seeing just
tiny pieces pieces of this uh class
basically there's problems of background
clutter so things can blend into the
environment we have to be robust to that
and there's also what we refer to as
intraclass variation so cat actually
there's a huge amount of cats uh just
species uh and so they can look
different ways we have to be robust to
all of that so I just like you to
appreciate the complexity of the task
when you consider any one of these
independently is difficult but when you
consider the full cross product of all
these different things and the fact that
our algorithms have to work across all
of that it's actually quite amazing that
anything works at all uh in fact not
only does it work but it works really
really well almost at human accuracy we
can recognize thousands of categories
like this and we can do that in a few
dozen milliseconds uh with the current
technology and so that's what you'll
learn about in this class um so what
does an image classifier look like
basically we're taking this 3D array of
pixel values we'd like to produce a
class label and what I'd like you to
notice is that there's no obvious way of
actually encoding any of this of these
classifiers right there's no simple
algorithm like say you're taking an
algorithm class in your early computer
science curriculum you're writing bubble
swort or you're writing something else
to do any particular task you can Intuit
all the possible steps and you can
enumerate them and list them and play
with it and analyze it but here there's
no algorithm for detecting a cat under
all these variations or it's extremely
difficult to think about how you'd
actually write that up what is the
sequence of operations you would do or
an arbitrary image to detect a cat
that's not to say that people haven't
tried especially in the early days of
computer vision uh there were these
explicit approaches as I'd like to call
them where you think about okay a cat
say is a we' like to maybe look for um
little earpieces so what we'll do is
we'll detect all the edges we'll Trace
out edges we'll classify the different
shapes of edges and their Junctions
we'll create you know libraries of these
and we'll try to find their arrangements
and if we ever see anything earlike then
we'll detect a cat or if we see any
particular texture of some particular
frequencies we'll detect a cat and so
you can come up with some
rules but the problem is that once I
tell you okay I'd like to actually
recognize a boat now or a person then
you have to go back to the drawing board
and you have to be like okay what makes
a boat exactly what's the arrangement of
edges right it's completely unscalable
approach to the to classification and so
the approach we're adopting in this
class and the approach that works much
better is uh the data driven approach
that we like in the framework of machine
learning and uh just to point out that
in these days actually in the early days
they did not have the luxury of using
data because at this point in time
you're taking you know great scale
images of very low resolution you have
five images and you're trying to
recognize things it's obvious not going
to work but with the availability of
Internet huge amount of data I can
search for example for cat on uh Google
and I get lots of cats everywhere and we
know that these are cats based on the
surrounding text in the web pages and so
that gives us lots of data so the way
that this now looks like is that we have
a training phase where you give me lots
of training examples of cats and you
tell me that they're cats and you give
me lots of examples of any type of other
category you're interested in I do I go
away and I train a Model A model is a
class and I can then use that model to
actually classify new test data so when
I'm given a new image I can look at my
training data and I can do something
with this based on just a pattern
matching um and statistics and so on so
as a simple uh first example we'll work
with in this framework consider the
nearest neighbor classifier the way
nearest neighbor classifier works is
that effectively we're given this giant
training set what we'll do at training
time is we'll just remember all of the
training data so I have all the train
data I just put it here and I remember
it now when you give me a test image
what we'll do is we'll compare that test
image to every single one of the images
we saw in the training data and we'll
just transfer the label over so I'll
just look through all the images um
we'll work with specific case as I go
through this I'd like to be as concrete
as possible so we'll work with a
specific case of something called cart
10 data set the C4 10 data set has 10
labels these are the labels there are
50,000 training images that you have
access to and then there's a test set of
10 10,000 images where we're going to
evaluate how well the classifier is
working and these images are quite tiny
they're just little toy data set of
32x32 little thumbnail images so the way
nearest neighbor classifier would work
is we take all this training data that's
given to us 50,000 images now at test
time suppose we have these 10 different
examples here these are test images
along the First Column here what we'll
do is we'll look up nearest Neighbors in
the training set of things that are most
similar to every one of those images
independently so there you see a ranked
list of images that are most similar to
uh in the training data to any one of
those 10 uh to every one of those test
images over there so in the first row we
see that there's a truck I think as a
test image and there's quite a few
images that look similar to it uh we'll
see how exactly we Define similarity in
a bit but you can see that the first
Retreat result is in fact a horse uh not
a truck and that's because of just the
arrangement of the blue sky that was
throwing that off so you can see that
this will not probably work very well
now how do we Define the distance metric
how do we actually do the comparison
there's several ways one of the simplest
ways might be uh a Manhattan distance so
an L1 distance or Manhattan distance
I'll use the two terms interchangeably
simply what it does is you have a test
image you're interested in classifying
and consider one single training image
that we want to compare this image too
basically what we'll do is we'll
elementwise compare all the pixel values
so we'll form the absolute value
differences and then we just add all of
it up so we're just looking at every
single Pixel position we're subtracting
it off uh and seeing what the
differences are at every single spatial
position adding it all up and that's our
similarity so these two images are
456 different okay so we'll get a zero
if we have identical images here just to
show you code specifically uh the way
this would look like this is a full
implementation of a nearest neighbor
classifier in numpy and
python um where I filled in the actual
body of the two methods that I talked
about and basically what we do here at
training time is we're given this data
set X the images and Y which usually
denote the labels so we're giving images
and labels all we do is just just
assigned to the class instance methods
so we just remember the data nothing is
being done at predict time though uh
what we're doing here is uh we're
getting new um test set of images X and
I'm not going to go through full details
but you can see that there's a for Loop
over every single test image
independently we're getting the
distances to every single training image
and notice that that's only a single
line of vectorized python code so in a
single line of code we're comparing that
test image to every single training
image in the database and we're
Computing this distance in a previous
slide in a single line okay so that's
vectorized code we didn't have to expand
out all those four Loops that are
involved in processing this distance and
then we compute the instance that is
closest so we're getting the Min index
so that's the index of the training
example that is has the lowest distance
and then we're just predicting for this
image the label of whatever was nearest
okay so here's a question for you in
terms of the nearest neighbor classifier
How does its speed depend on the
training data size what happens is I
scale up the training
data
it's slower
okay yes it's actually it's in fact
linearly slower right because if I have
I just have to I have to compare to
every single training example
independently so it's a linear slowdown
and you'll notice actually as you go as
we go through the class is that this is
actually backwards because what we
really care about in most practical
applications is we care about the test
time performance of these classifiers
that means that we want this classifier
to be very efficient at test time and so
there's this tradeoff between really how
much compute do we put in the train
method and how much Compu do we put in a
test method a nearest neighbor is
instant at train but then it's expensive
at test and as we'll see soon comets
actually flip this completely the other
way around we'll see that we do a huge
amount of compute at train time we'll be
training a convolutional neural network
but the test Time Performance will be
super efficient in fact it will be
constant amount of compute uh for every
single test image we do constant amount
of computation no matter if you have a
million billion or trillion training
images i' I'd like to have a trillion
tril trillion training images no matter
how large your training data set is we
do a constant compute to classify any
single testing example so that's very
nice uh practically speaking now I'll
just like to point out that uh there are
ways of speeding up nearest neighbor
classifiers there's these approximate
nearest neighbor methods flan is an
example library that people use often in
practice that allows you to speed up uh
this process of nearest neighbor
matching but uh that's just a side note
okay so let's go back to the design of
the nearest neb classifier we saw that
we've defined this uh distance and I've
arbitrarily chosen to show you the
Manhattan distance which compares the
difference of the absolute values
there's in fact many ways you can
formulate a distance metric and so
there's many different choices of
exactly how we do this comparison
another simp another choice that people
like to use in practice is what we call
the ukian or L2 distance which instead
sums up the differences in the sums of
squares of these differences between
images and so this
Choice what happened there did someone
push a button over there in the
back
okay thank you so this choice of what
how exactly we compute a distance it's a
discrete choice that we have control
over that's something we call the
hyperparameter it's not really obvious
how you set it it's a hyperparameter we
have to decide later on exactly how to
set this somehow another sort of hyper
parameter that I'll talk about in
context of nearest neighbor classifier
is when we generalize nearest neighbor
to what we call a canor neighbor
classifier so in a canor neighbor
classifier instead of retrieving for
every test image the single nearest
Training example will in fact retrieve
several nearest examples and we'll have
them do a majority vote over the classes
to actually classify every test instance
so say a five nearest neighbor we would
be retrieving the five most similar
images in the training data and doing a
majority vote of the labels here's a
simple two-dimensional data set to
illustrate the point so here we have a
three class data set in 2D and here I'm
drawing what we call decision regions of
this nearest neighbor classifier here
what this refers to is we're showing the
training data over there and we're
coloring the entire 2D plane by what uh
class this nearest neighbor classifier
would assign at every single point
suppose you suppose you had a test
example somewhere here then this is just
saying that that this would have been
classified as blue class based on the
nearest neighbor you can for example
note that here is a point that is a
Green Point inside the blue cluster and
it has its own little region of
influence where it would have classified
a lot of test points around it as green
because if any point fell there then
that Green Point would have been the
nearest neighbor now when you move to
higher numbers for K such as five
nearest neighbor class classifier what
you find is that the boundaries start to
smooth out it's kind of this uh nice uh
effect where even if there's this one
point um kind of randomly as a noise and
outlier in the blue cluster it's
actually not influencing the predictions
too much because we're always retrieving
five nearest neighbors and so they get
to overwhelm the green point so uh in
practice you'll find that usually kers
neighbor classifiers offer better uh
better performance at test time now but
again the choice of K is again a hyper
parameter right so I'll come back to
this in a bit just to show you an
example of what this would look like
here I'm retrieving 10 most similar
examples they're ranked by their
distance and I would actually do a
majority vote over these training
examples here to classify every Test
example
here
okay so let's do a bit of uh questions
here just for fun uh consider what is
the accuracy of the neural classifier on
the training data when we're using ukian
distance so suppose our test set is
exactly the training data and we're
trying to find the accuracy in other
words how many how often would we get
the correct answer 100% 100% good
why okay among the murmur um yeah that's
correct so we're always find a training
example exactly on top of that test
which has zero distance and then it St
will be transferred over good uh What if
we're using the Manhattan distance
instead
so Manhattan distance doesn't use sum of
squares it uses sum of absolute values
of differences would it be the same it
would it's just a trick question it
would be
so okay good uh so we're we're keeping
paying attention here uh okay what is
the accuracy of the K nearest neighbor
classifier in a training data then it
say k was 5 is it 100% no not
necessarily right good because basically
the points around you could overwhelm
you even if you're uh best example is
actually of the of a different class
okay good so we've discussed two choices
of different uh here hyper parameters we
have the distance metric it's a hyper
parameter and this K we're not sure how
to set it should be 1 2 3 10 and so on
so we're not exactly sure how to set
these in fact they're problem dependent
you'll find that you can't find a
consistently best choice for these hyper
parameters in some applications some
case might look might work better than
other applications so we're not really
sure how to set this so here's an idea
uh we have to basically try out lots of
different type parameters so what I'm
going to do is I'm going to take my um
train data and then I'm just going to
try out lots of different type
parameters so I have my test data and I
try out k equal 1 2 3 4 5 6 20 100 I try
out all the different distance metrics
and whatever works best that's what I'll
take so that will work very well right
no it won't work very well why is it not
going to why is this not a good idea uh
because you will fail to generalize on
on unseen data okay so basically correct
so basically um yes so test data is your
proxy for your generalization of your
algorithm you should not touch the test
data in fact you should forget that you
ever have test data so when once you're
given your data set always set aside the
test data pretend you don't have it
that's telling you how well your
algorithm is generalizing to unseen data
points and this is important because
you're trying to develop your algorithm
and then you're hoping to eventually
deploy it in in some setting and you'd
like to have an understanding of exactly
how well do I expect this to work in
practice
right and so uh you'll see that for
example sometimes you can perform very
very well on train data but not
generalize very well to test data when
you're overfitting and so on a lot of
this by the way 229 is a requirement for
this class so you should be quite
familiar with this this is to most
extent a um this is kind of more more of
r view for you but basically this test
data is use it very sparingly forget
that you have it instead what we do is
we separate our training data into what
we call folds so uh we separate say we
use a fivefold validation so we use % of
the training data as a imagine test set
data and then we only train on part of
it and we test on we test out the
choices of hyp parameters on this
validation set so I'm going to train on
my fourfolds and try out all the
different case and all the different
zance metrics and whatever else if
you're using approximate nearest
neighbor you have many other choices you
try it out see what works best on that
validation data if you're feeling
uncomfortable because you have very few
training data points people also
sometimes use cross validation where you
actually iterate the choice of your test
or validation fold across these choice
es so I'll first use four one to four
for my training and try out on five and
then I cycle the choice of the
validation fold across all the five
choices and I look at what works best
across all the possible choices of my
test fold and then I just take whatever
works best across all the possible
scenarios okay that's referred to as a
cross validation set as cross validation
so in practice the way this would look
like say we're cross validating for k
for a nearest neighbor classifier is we
are trying out different values of K and
this is our performance um across five
choices of a fold so you can see that
for every single K we have five data
points there and then this is the
accuracy so high is good and I'm
plotting a line through the mean and I'm
also showing the bars for the standard
deviations so what we see here is that
the performance goes up on the across
these validation folds um as you go up
but at some point it starts to Decay so
for this particular data set it seems
that k equal to 7 is the best choice so
that's what I'll use I'll do this for
all my hyper parameters also for thism
metric and so on I do my cross
validation I find the best high
parameters I set them I fix them then I
evaluate a single time on the test set
and whatever number I get that's what I
report as a accuracy of a K classifier
on this data set that's what goes into a
paper that's what goes into a final
report and so on that's the final
generalization result of what you've
done um okay any questions about this
yep so the reason that happens with K is
that is that because large K gives you
high
bias um
I would be careful with that terminology
but
basically it's about the statistics of
the distribution of these data points in
your label in your data space and so
sometimes it's it's basically hard to
say like you get where is this
picture you see roughly what's happening
is you get more clunkiness in more case
and it just depends on how clunky your
data set is that's really what it comes
down to is uh how how Blobby is it or
how specific is it
I know that's a very handwavy answer but
that's roughly what what that comes down
to uh so different data sets will have
different
clunkiness Y how do you deal with skewed
data sets skewed data sets uh so what is
that a lot more of one class than other
class uh so that's a technical question
that I maybe want to get into right now
but we will address that later in the
class
probably oh yeah go ahead shoulding
hyper parameters uh data specifically
consider
aching uh no not at all because your
hyper parameters are just choices you're
not sure how to set them and different
uh different data sets will require
different choices and you need to see
what works best in fact when you try out
different algorithms because you're not
sure what's going to work best on your
data the choice of your algorithm is
also kind of like a hyper parameter so
you're just not sure what works you're
not
different um approaches will give you
different generalization boundaries they
look different and some data sets have
different structure than others so some
things work better than others and you
have to just train try it
out okay cool I just like to point out
that K neighbors is no one basically
uses this so I'm just going through this
just to get you uh used to this approach
of really how this works with training
test splits and so on um the reason this
is never used is because first of all
it's very inefficient but second of all
distance metrics on images which are
very high dimensional objects they act
in very unnatural unintuitive ways so
here what I've done is we're taking an
or image and I change it in three
different ways but all these three
different images here have actually the
exact same distance to this one in an L2
ukian sense and so just think about it
this one here is slightly shifted to the
left it's basically cropped slightly and
its distances here are completely
different because these pixels are not
matching up exactly and it's all
introducing all these errors and you're
getting a distance this one is slightly
darkened so you get a small Delta across
all spatial locations and this one is
untouched so you get zero distance
errors across everywhere except for in
those positions over there and that is
taking out critical pieces of the image
and it doesn't the nearest the nearest
nebor classifier would not be able to
really tell a difference between these
settings because it's based on these
distances that don't really work very
well in this case so uh very unintuitive
things happen when you try to throw
distances on very high dimensional
objects that's partly why we don't use
this okay so in summary so far uh we're
looking at image classification as a
specific case and we'll go into
different settings later in the class
I've introduced enable classifier and
the idea of having different splits of
your data and we have these
hyperparameters that we need to pick uh
and we use cross validation for this
usually most of the time people don't
actually use entire cross validation
they just have a single validation set
and they try out on the validation set
whatever works best in terms of the
hyper parameters and once youve get the
best high parameters you evalate the
single time on a test set okay so I'm
going to go into linear classification
bit any questions at this point
otherwise great okay
so we're going to look at linear
classification um this is a point where
we are starting to work towards
convolutional Lal networks so there will
be a series of lectures we'll start with
linear classification that will build up
to an entire convolutional network
analyzing an
image now I just like to say that we've
motivated the class yesterday from a
task specific uh view so this class is
computer vision class we're interested
in you know uh giving machines site
another way to motivate this class would
be from a modelbased point of view in a
sense that we're um giving you guys uh
we're teaching you guys about deep
learning and neural networks these are
wonderful algorithms that you can apply
to many different data domains not just
Vision so in particular over the last
few years we saw that neural networks
can not only see that's what you'll
learn a lot about in this class but they
can also hear they're used quite a bit
in uh speech recognition now so when you
talk to your phone that's now a deep
neural network they can also uh do
machine translation so here you're
feeding um a neural network a set of
words one by one in English and the
neural network produces the translation
in French or whatever else target
language you have they can also perform
control so we've seen neural network
applications in um manipul in robots
manipulation in playing of Atari games
so these neural networks learn how to
play Atari games uh just by seeing the
raw pixels of the screen and we've seen
neur networks be very successful in a
variety of domains and even more than uh
I put here and we're uncertain exactly
where this will take us and then I'd
like to also say that we're exploring
ways for neural networks to think but
this is very handwavy it's just a
wishful thinking but uh there's some
hints that maybe uh they can do that as
well now neural networks are very nice
because they're just a fun modular
things to play with when I think about
working with neural networks I kind of
this picture comes to mind for me here
we have a neural networks practitioner
and she's building what looks to be a
roughly 10 layer convolutional neural
network at this point and so these are
very fun really the best way to think
about playing with neural networks is
like Lego blocks you'll see that we're
building these little function pieces
these Lego blocks that we can stack
together to create entire architectures
and they very easily talk to each other
and so we can just create these modules
and stack them together and play with
this very easily um one work that I
think exemplifies this is uh my own work
on image captioning from roughly a year
ago uh so here the task was you take an
image and you're trying to get the
neural network to produce a sentence
description of the image so for example
in the top left these are test set
results the neural network would say
that this is a man in black shirt is
playing a guitar or a constructure
worker in Orange safety West is working
on the road and so on so the neural
network can look at the image and create
this description of every single image
and when you go to the details of this
model the way this works is we're taking
a convolutional neural network which we
know so there's two modules here in this
uh system diagram for image captioning
model we're taking a convolutional
neural network which we know can see and
we're taking a recurrent neural network
which we know is very good at modeling
sequences in this case sequences of
words that will be describing the image
and then just as if we were playing with
Legos we take those two pieces and we
stick them together that's corresponding
to this Arrow here in between the two
modules and these networks learn to talk
to each other and in the process of
trying to describe the images these
gradients will be flowing through the
convolutional network and the full
system will be adjusting itself to
better see the images in order to
describe them at the end and so this
whole system will work uh together as
one uh so we'll be working towards this
model we'll actually cover this in class
so you'll have full understanding
exactly of both this part and this part
about half halfway through the course
roughly and you'll see how that image
captioning model works but that's just a
motivation for really what we're
building up to and these are like really
nice models to work with Okay but for
now back to uh c41 and linear
classification um so again just to
remind you we're working with this data
set 50,000 images 10 labels and the way
we're going to approach linear
classification is from what we call a
parametric approach K neighbor that we
just discussed now is something an
instance of what we call non-parametric
approach there's no parameters that
we're going to be optimizing over this
distinction will become clear in a few
minutes uh so in the parametric approach
what we're doing is we're thinking about
constructing a function that takes an
image and produces the scores for your
classes right this is what we want to do
we want to take an image and we'd like
to figure out which one of the 10
classes it is so we'd like to write down
a function an expression that takes an
image and gives your do 10 numbers but
the expression is not only a function of
that image but critically it will be
also a function of these parameters that
I'll call W sence also called the
weights and so really it's a function
that goes from 372 numbers which make up
this image to 10 numbers that's what
we're doing we're defining a
function and we'll go through several
choices of this function in this in the
first case we'll look at linear
functions and then we'll extend that to
get neural networks and then we'll
extend that to get convolutional neural
networks but intuitively what we're
building up to is that what we'd like is
when we pipe this image through our
function we'd like the 10 numbers that
correspond to the scores of the 10
classes we'd like the number that
corresponds to the cat class to be high
and all the other numbers to be low and
we'll have we don't have a choice over X
that X is our image that's given but
we'll have Choice over W so we'll be
free to set this in whatever way we want
and we want we'll want to set it so that
this function gives us the correct
answers for every single image in our
training data okay that's roughly the
approach we're building up towards so
suppose that we use the simplest uh
function arguably the simplest just a
linear classification here so X is our
image in this case what I'm doing is I'm
taking this array this image that makes
up uh the cat and I'm stretching out um
all the pixels in that image into a
giant column Vector so that X there is a
column Vector of 372
numbers okay and so um if you know your
Matrix uh
Vector operations which you should
that's a prerequisite for this class
that there is just a matrix
multiplication which you should be
familiar with and basically we're taking
X which is a 300 72 dimensional column
Vector we're trying to get 10 numbers
out and it's a linear function so you
can go backwards and figure out that the
dimensions of this W are basically 10 by
372 so there are 30,7
7200 numbers that goes into W and that's
what we have control over that's what we
have to tweak and find what works best
on our data so those are the parameters
in this particular case uh what I'm
leaving out is there's also an appended
plus b sometimes so you have a bias
these biases are again 10 more par
and um we have to also find those so
usually in your linear classifier you
have a w and a b we have to find exactly
what works best and this B is not a
function of the image that's just
independent weights on the on How likely
any one of those um images might be so
to go back to your question if you have
a very unbalanced data set for uh so
maybe you have mostly cats but some dogs
or something like that then you might
expect that the cat the bias for the cat
class might be slightly higher because
by default the classifier wants uh to
predict the cat class unless something
convinces it
otherwise something in the image would
convince it otherwise okay so to make
this more concrete uh I just like to
break it down but of course I can't
visualize it very explicitly with 372
numbers so imagine that our input image
only had four pixels and imagine so four
pixels are stretched out in the column X
and imagine that we have three classes
so red green and blue class or a cat dog
ship class okay so in this case W will
be only a 3x4 Matrix and what we're
doing here is we're trying to compute
the score of this um image X so this is
matrix multiplication going on here to
give us the output of f which is the
scores we get the three scores for three
different classes so this is an random
setting of w just random weights here
and we're carrying out the matrix
multiplication to get some scores so in
particular you can see that with this
this setting of w is not very good right
because with this setting of w our cat
score 96 is much less than any of the
other classes right so this was not
correctly classified for this training
image so that's not it's not a very good
classifier so we want to change a
different we want to use a different W
so that that score comes out higher than
the other ones okay but we have to do
that consistently across the entire
training set of examples but uh but one
thing to notice here as well is that
basically W it's um this function is in
parallel evaluating all the 10
classifiers but really there are 10
independent classif iers uh to some
extent here and every one of these
classifiers like say the cat classifier
is just the first row of w here right so
the first row and the first bias gives
you the cat score and the dog classifier
is the second row of w and the ship
score the ship classifier the third row
W so basically this W Matrix has all
these different classifiers stacked in
rows and they're all being dot producted
with the image to give you the scores
okay so here's a question for you uh
what does a linear classifier do in
English uh we saw the functional form
it's taking these images it's doing this
funny operation there but what how do we
really
interpret in English somehow what this
is
doing what is this functional form
really
doing yeah good Ahad if you just think
of it as a a single binary classifier
it's basically drawing a line that will
tell you based on the um obser
observations in your data if the point
is below the line and it's not class
Dimensions okay good so you're thinking
about it uh in a spatial domain of X
being a high dimensional data point and
W is really putting uh planes through
this High dimensional data point I'll
come back to that interpretation in a
bit uh what other way can we think about
this uh for each class it has like sort
of a template image that it basically
multiplies with every image in which
everyone comes through the brightest
that's okay so you're thinking about it
more in kind of like a template way
where every single one of these rows of
w effectively is like this template that
we're do producting with the image and a
do product is really a way of like
matching up seeing what what aligns uh
good um what otherwis yeah I guess it's
same as what you said but putting a
different words uh it's just saying that
this part of the image is important
attribute to be a cat this part of the
image uh is not an important not an
important part as
to things like those those kind of yep
so what you're referring to is that W
basically has the capacity to to care or
not care about different spatial
positions in the image right because
what we can do is some of the spatial
positions in X if we have zero weights
then the classifier would be doesn't
care what's in part of image so if I
have zero weights for this part here
then nothing affects it but for some
other parts of the image if you have
positive or negative weights something's
going to happen there and this is going
to contribute to the score any other
ways of describing it yeah it's taking
something that exists in image space and
projecting it into a space of
labels uh yeah so taking yeah so you can
think about it that also is like a nice
interpretation it's like a mapping from
image space to a label space yep good
how do you come up with the with each of
the numbers in the column Vector oh I
made that up sorry how do you get them
from the red and blue values sorry how
do you get them from the red green and
blue Valu
uh yeah thank you so uh good question so
this image is a threedimensional uh
array where we have all these channels
you just uh stretch it out so all the
you just stretch it out in whatever way
you like say you stack the red green and
blue portions side by side that's one
way you just stretch it out in whatever
way you like but in a consistent way
across all the images you figure out a
way to serialize in which way you want
to read off the pixels and you stretch
them out into a column so then when you
have 12
values uh for four pixel image yeah okay
good Point um okay yeah so let's say we
have a four pixel grayscale image which
is this is a terrible example thank you
you're right thank you I didn't want to
confuse people especially because
someone pointed out to me later after I
made this figure that red green and blue
are the color channels but here the red
green and blue correspond to classes so
this is a complete uh screw up on my
part so I apologize not color channels
nothing to do with color channels just
three different colored classes sorry
about that okay go ahead so uh we have a
different size of image like 40 * 600
time something like that do you put a
sort of zero inside
or yeah thank you so your question is
what if my images have different sizes
in my data set some could be small some
could be large exactly how do we make
this all be a single sized column Vector
uh the answer is you always we always
resize images to be basically the same
size we can't easily deal with different
sized images uh or we can and we might
go into that in a in later but but the
simplest thing to think of is just
resize every single image to the exact
same uh size is the simplest thing
because we want to ensure that all of
them are kind of uh comparable of the
same stuff so that we can make these
columns and we can analyze statistical
patterns that are aligned in the image
space um yeah uh in fact
state-of-the-art methods the way they
actually work on this is they always
work on Square images so if you have a
very long image these methods will
actually work worse because many of them
what they do is just squash it that's
what we do still works fairly well
uh so yeah if you have very long like
panr images and you try to put that
somewhere on like some online service
chances are it might work worse because
they'll probably when they put it
through a compet they will make it a
square because these componets always
work on
squares uh you can make them work on
anything but that's just in practice
what happens
usually uh any other questions or yeah
it's like assigning a score to each test
image for each class uh yep so you're
interpreting the W the classifier yeah
yeah so each image gets mapped through
this uh setting okay anyone anyone else
would like to interpret this or okay
great so another way to actually put it
one way that I didn't hear but it's also
a relatively nice way of looking at it
is that basically every single score is
just a weighted sum of all the pixel
values in the image and these weights
are we get to choose those eventually
but it's just a giant weighted sum it's
really all it's doing is it's counting
up colors right it's counting up colors
at different spatial positions so uh one
way to one way that was brought up in
terms of how we can inter interpret this
W classifier to make it concrete is that
it's kind of like a bit like a template
matching thing so here what I've done is
I've trained a classifier and I haven't
shown you how to do that yet but I
trained my weight Matrix W and then I'll
come back to this in a second I'm taking
out every single one of those rows that
we've learned every single classifier
and I'm reshaping it back to an image so
that I can visualize it okay so I'm
taking it originally just a giant row of
372 numbers I reshape it back to the
image to undo the Distortion I've done
and then I have all these templates
and so for example what you see here is
that plane it's like a blue blob here
the reason you see blue blob is that if
you looked at the color channels of this
plain template you'll see that in the
blue Channel you'll have lots of
positive weights because those positive
weights if they see blue values then
they interact with those and they get a
little contribution to the score so this
PL classifier is really just counting up
the amount of blue stuff in the image
across all these spatial locations and
if you look at the red and the green
channel for the plane classifier you
might find zero values or even negative
values right so that's the plain
classifier and then we have classifiers
for all these other images so say a frog
you can almost see the template of the
Frog there right we're looking for some
green stuff is green stuff has positive
weights in here and then we see some
brown stuff is things on the side right
so if that gets put over an image and do
producted you'll get a high
score um one thing to note here is that
look at this the car classifier that's
not a very like nice template of a car
also here the horse look looks a bit
weird what's up with that why is the car
looking weird and why is the horse
looking
weird yeah some horses are facing left
and some are facing right we end up with
this where it looks like a horse is two
heads both basically that's what's going
on in the data the horses some are
facing left somewh right and this
classifier really it's not very powerful
classifier and it has to combine the two
modes it has to do both things at the
same time so you end up with this
two-headed horse in there and you can in
fact say that just from this result
there's probably more left facing horses
in far than right because it's stronger
there uh also for car right we can have
a car like 45° tilted left or right or
front and this classifier here is the
optimal way of mixing across like
merging all those modes into a single
template because that's what we're
forcing it to do once we're actually
doing com nuts and neural networks they
don't have this downside they can
actually have in principle they can have
a template for this car or that car or
that car and combine across them we're
giving them more power to actually carry
out this classification more properly
but for now we're constrained by this
question if you only have one image of a
horse or only a couple you rotate it
yourself bu different ways and in
certain ways so thatass would over to
one
orientation uh yes what you're referring
to I think is something we call data
augmentation so at training time we
would not be taking just uh exact images
but we'll be jittering them stretching
them spewing them and we'll be piping
all of that in that's going to become a
huge part of getting comat to work very
well uh so yeah so we'll be doing a huge
amount of that stuff
uh for every single training example
we're going to hallucinate many other
training examples of shifts and rotates
and SKS and that works much better go
ahead uh how do these templates differ
from just taking the average pixel value
for each
class uh how do these templates uh
change taking the average pixel value
took all the images for a plane took the
average all the I see so you want to uh
explicitly set a template and the way
you'll set the temp is you'll take the
average across all the images and that
becomes your template sure I'm just
wondering
yeah how those two approaches would
differ um so this classifier it finds it
would do something similar I would guess
it would work worse uh because the
linear classifier when you look at its
mathematical form and really what it
optimizes for I don't think it would
have a minimum at what you described and
just the mean of the images uh but that
would be like a intuitively decent
heuristic to perhaps set the weights in
the initialization or something like
that classier that does that like
something yeah there's something related
to it uh yeah yeah but we might even go
into that LDA probably is what you're
referring to there's several several
things okay yeah uh don't you think it
would be much better if we do it with
gray scale images because let's say we
got a car that was like yellowish right
but our template image highlights red
right so wouldn't it be better if you
race yeah so that's a good point so
there are cars have many different
colors and here this happened to pick up
on red which is saying that there's
probably more red cars in the data set
and uh it might not work for yellow in
fact yellow cars might be frog for this
classifier right um so this thing just
does not have capacity to do all of that
which is why it's not powerful enough it
can't capture all these different modes
correctly and so this will just go after
the numbers there's more red cars that's
where it will
go uh if this was grayscale I'm not sure
if that would work better I'll come back
to that actually in a bit go ahead if
you have a training set with more
examples for cash would that affect the
buyas higher and if so would that affect
the the
test uh yeah so you might expect as I
mentioned for unbalanced data sets what
you might expect um not
exactly you what you might expect if you
have lots of cats is that the cat bias
would be higher because this class this
this classifier is just used to spewing
out large numbers uh based on the loss
but uh we have to go into loss fun to
exactly see how that will play out uh so
it's hard to say right now um okay uh
another interpretation of the linear
classifier that also someone else
pointed out that I'd like to point out
is uh you can think of these images as
very high dimensional points in a 372
dimensional space right in the 372 pixel
space dimensional pixel space every
image is a point and these linear
classifiers are describing these
gradients across the 372 dimensional
space these scores are this uh gradient
of negative to positive along some
linear Direction across the space and so
for example here for a car classifier
I'm taking the first row of w which is
the car class and the line here is
indicating the zero level set of that
classifier in other words that along
that line the car classifier has zero
score so the car classifier there has
zero and then the arrow is indicating
the direction along which it will color
the space uh with more and more carness
of score similar we have these three
different classifiers in this example
they will correspond to these gradients
with a particular level set and they're
basically trying to go in you have all
these points they are in the space and
these linear classifiers we initialize
them randomly so this car classifier
would have its level set at random and
then you'll see when we actually do the
optimization as we optimize this will
start to shift turn and it will try to
isolate the car class and we like it's
really fun to watch these classifiers
train because it will it will rotate it
will snap in for the car class and it'll
start to jiggle and it will try to like
separate out all the cars from all the
we got all the non cars it's really
amusing to watch so that's another way
of interpreting that someone has brought
up okay so here's a question for you
given all these interpretations what
would be a very hard test set given how
the linear classifier Works what would
you expect to work really just really
not well with a linear
classifier concurrent circles sorry
concurrent circles concurrent circles so
your classes are what are your CL
classes exactly so you have a red class
in the middle that's like Circle or like
a blob of red classes and then around it
you have a blob of blue classes oh I see
so you're in okay so what you're
describing is in this interpretation of
space if your images in one class would
be in a blob and then your other class
is like around it so I'm not sure
exactly what that would look like if you
actually visualize it in in a pixel
space uh but yes you're right in that
case linear classifier would not be able
to separate out those but what about in
terms of like uh what would the images
look like you would look at this data
set of images and you clearly say that
linear classifier will probably not do
very well
here yeah go ahead you want to separate
like scooters for
motorcycles basically or something like
that because I think somebody else was
asking about the averaging of the
pictures and that that made me think if
you're doing like ordinary Le squares
what you're basically doing is
maximizing projections of of all the X's
onto your row space so if you look at
training X's of scooters and training
X's of motorcycles they're going to
effectively yield the same like centroid
for the template and then you're going
to get the same situation describing
where you have concentric circles in
yourens space mhm yep yep so that's a
pretty good one yeah good maybe the
negative images like uh CH you know
subtracting 255 whatever the color is
you know
like so you want one Clause to be say
you take all the airplanes and then you
you want to switch like an airplane to a
human if it were the negative like film
negative image of a oh I see it would it
would be actually the lowest scoring oh
I see I see so you're you're pointing
out that if I took that image of an
airplane class and I have a trained
classifier and then I do a negative of
it negative image of that classifier
you'd still see the edges and you you'll
say okay that's an airplane obviously by
the shape but for linear classifier all
the colors would be exactly wrong and so
the linear classifier would hate that
airplane so yeah good example good you
take the same exact image and you
translate it or scale it differently and
you move it to different places are
rotated for each class you have several
of these I'd expect that to perform I
see so uh you're saying that we take one
thing say like dogs but then so what
you're referring to is say you have dogs
one class is dogs in the center and one
class is dogs in the on the right and
you think that that would be uh yeah I'm
saying even if it's a picture of the
same exact dog same pose and everything
you just move it to the right up down or
you scale it to different sizes and move
it around so would that be a problem if
so one class is dogs in the center and
one class is dogs in the right but
otherwise white background or something
like that would that be a
problem it wouldn't be a problem why
wouldn't it be a problem
transformation uh it's an aine
transformation a linear transformation
what you areel I guess that the problem
would be if you work an image you have a
set of images like dogs and dogs work or
ex skewed in some nonlinear way I
see right so you're saying that maybe a
more difficult thing would be if you
have dogs that are warped in some funny
ways according to class why wouldn't it
be a problem if you actually could a
linear classifier do something in the
center and something on the right does
it actually have an understanding of a
spatial layout that' actually be fine
right that would be relatively easy
because you would have positive weights
in the middle oh Sor suggesting oh sorry
okay maybe I'm misunderstood I'm sorry
okay another one classifying different
types of P names the author be hard
because they use Bunch different colors
and different Set uh yeah possibly yeah
so I think many of you are kind of
understanding the the main point is uh
yeah so this is really really what it's
doing well I'm skipping ahead here
really what this is doing is it's
counting up uh counting up colors in
spatial positions anything that messes
with this will be really hard actually
to go back to your point if you had a
grayscale data set by the way that would
work not very well with L linear
classifiers would probably not work if
you took CFR 10 and you make it all
grayscale then doing the exact cartan
classification but on grayscale images
would probably work really terribly
because you can't pick up on the colors
you have to pick up on these textures
and fine details now and you just can't
localize them because they could be at
arbitrary positions you can't
consistently count across it um so yeah
that would be kind of a disaster uh
another example would be different
textures if you have say all of your
textures are blue but these textures
could be uh different types then this
doesn't really like say these textures
could be different types but they can be
spatially invariant and that would be
terrible terrible for all your
classifier as well okay
good uh so just to remind you I think uh
nearly there um we defin this linear
function so with a specific case of w
we're looking at some test images we're
getting some scores out and just looking
forward where we're headed now is with
some setting of W's we're getting some
scores for all these images and so for
example with this setting of w in this
image we're seeing that the cat score is
2.9 but there are some classes that got
a higher score like dog so that's not
very good right but some classes have
negative scores which is uh good for
this image
so this is a kind of a medium result for
this weights for this image and here we
see that the car class which is correct
for there has the highest score which is
good right so this setting of w worked
well on this image here we see that the
for class is a very low score so w
worked terribly on that image so where
we're headed now is we're going to
Define what we call a loss function and
this loss function will quantify this
intuition of what we consider good or
bad right now we're just eye boiling
these numbers and saying what's good
what's bad we have to actually write
down a mathematical expression that
tells us exactly like this setting of w
across our test set is 12.5 bad or 12
whatever bad or 1.0 bad because then
once we have it defined specifically
we're going to be looking for W's that
minimize the loss and it will be set up
in such a way that when you have a loss
of very low numbers like say even zero
then you're correctly classifying all
your
images um but if you have a very high
loss then everything is messed up and W
is not good at all so we're going to
Define a loss function and then we're
going to look for different W's that
actually do very well across all of it
so that's roughly what's coming up we'll
Define loss function which is a quantify
a way to quantify how bad each W is on
our data set the loss function is a
function of your entire training set and
your weights we don't have um control
over the training set but we have
control over the weights then we're
going to look at the process of
optimization how do we efficiently find
the set of Weights W that works across
all the images and gives us a very low
loss and then eventually what we'll do
is we'll go back and we'll look at this
expression the linear classifier that we
saw and we're going to start meddling
with the function f here so we're going
to extend F to not be that simple in
your expression but we're going to make
it slightly more complex we'll get a
neural network out and then we'll make
it slightly more complex and we'll get a
convolutional network out but otherwise
the entire framework will stay unchanged
all the time we'll be Computing these
scores this functional form will be
changing but we're going from image to
some set of scores uh through some
function and we'll make it more
elaborate over time and then we're
identifying some loss function and we're
looking at what weights what parameters
are giving us very low loss and that's
the setup will we working with uh going
forward so next class we'll look into
loss functions and then we'll go towards
neural networks and comets so um I guess
this is my last slide so I can take uh
any last questions and then can you
explain the advantage of this itative
approach uh sorry sorry uh sorry I
didn't hear so I was saying why are we
doing why are we doing alterative
approach in the
optimization so sometimes in
optimization settings you can have for
um these iterative approaches are
basically the way this will work we'll
we'll always start off with a random W
uh so that will give us some loss and
then we we don't have a process of
finding right away the best set of
Weights what we do have a process for is
iterative slightly improving the weights
so what we'll see is we'll look at the L
function and we'll find the gradient in
in the parameter space and we'll March
down so what we do know how to do is how
do we slightly improve a set of Weights
we don't know how to do the problem of
just find the best set of weights right
away we don't know how to do that
because especially when these functions
are very complex like say entire comets
it's a huge landscape of it's just a
very uh intractable problem is that your
question I'm not sure I okay thank you
um
yeah so how do you deal with that uh
color problem how do we deal with the
color problem
yeah since we had a high bias of red
cars oh so okay so uh so here we saw
that the linear classifier for a car was
this red template for a car a neural
network basically what we'll do is we'll
be will you can look at it as stacking
linear classifiers to some degree so
what it'll end up doing is it will have
all these little templates really for
red cars yellow cars green cars whatever
cars going this way or that way or that
way there will be a neuron assigned to
detecting every one of these different
modes and then they will be combined
across them on a second layer so
basically you'll have these neurons
looking for different types of cars and
then the next neuron will be just like
okay I just take a wait at some of you
guys and I'm just doing an or operation
over you and then we can detect cars in
all of their modes and all of their
positions if that makes sense uh so
that's roughly how it will
work makes sense okay awesome
okay
this