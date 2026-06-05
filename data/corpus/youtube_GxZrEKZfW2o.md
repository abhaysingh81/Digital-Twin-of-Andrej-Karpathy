# YouTube Transcript: GxZrEKZfW2o

3:00 let's let's get
started so um I'm going to lecture it
today give Andre a little bit of a
break so today we're so last time we
talked about uh sort of we saw all the
parts of comets we put everything
together um today we're going to see
some applications of comets uh to Spa to
actually dive inside images and talk
about spatial localization and detection
um we were we actually moved this
lecture up a little bit uh we had it
later on the schedule but we saw a lot
of you guys were interested in this
stuff for projects so we wanted to move
it earlyer to kind of give you an idea
of what what's
feasible um so first couple
administrative things um are are the
project proposals were due on Saturday
my inbox kind of exploded over the
weekend so I think most of you submitted
it but if you didn't you should probably
get on that um we're in the process of
looking through those so we'll go to
make sure that the project proposals are
reasonable and that everyone submitted
one so we'll hopefully get back to you
on your projects this week um also
homework two is due on Friday so who's
who's done
uh who's stuck on batch
Norm okay good good uh that's fewer
hands than we saw last week so we're
making progress um also keep in mind
that we're asking you to actually train
a pretty big compet on Sear for this
homework so if you're starting to train
on Thursday night that might be tough so
maybe start early on that last part um
also homework one we're in the process
of grading hopefully we'll have those
back to you this week um so you can get
feedback before homework 2 is due also
keep in mind the we actually have an
in-class midterm next week on Wednesday
um so that's a week from Wednesday so be
be ready that'll be in class it should
be a lot of
fun all right so last lecture we were
talking about convolutional networks we
kind of saw the pieces um we spent a
long time understanding how this
convolution operator Works how we're
sort of transforming feature maps from
one to another um by running inner
products over by sliding this window
over our feature map Computing inner
products and Transforming Our
representation through many layers of
processing um and if you we if you
remember these lower layers of
convolutions tend to learn things like
edges and colors and higher layers tend
to learn um more complex object parts we
talked about pooling which is used to
subsample and downsize our feature
representations inside networks um so
that's a common ingredient that we saw
uh we also did case studies on
particular Convent architectures so you
could see how these things tend to get
hooked up in practice so we talked about
Lynette which is something from '98 it's
a little five layer Comet that was used
for digit recognition uh we talked about
alexnet that kind of kicked off the big
deep Lear deep learning boom in 2012 by
winning imag net there was an eight
layer com net uh we talked about ZF net
that won imet classification in 2013
that was pretty similar to
alexnet and then we saw that uh deeper
is often better for classification we
looked at googlet and vgg that did
really well in 2014 competitions that
were much much deeper than alexnet and
zfn net and did a lot better uh and we
also saw this new fancy crazy thing from
Microsoft called resnet that won just in
December in 2015 with 150 layer
architecture um and as you'll recall
just the over the last couple years
these different architectures have been
getting deeper and getting a lot better
um but this is just for classification
so now in this lecture we're going to
talk about localization and detection
which is uh actually another really big
important problem in computer vision um
and this idea of deeper networks doing
better um hint that'll kind of we'll
revisit that a lot in these new tasks as
well so so far in the class we've really
been talking about classification um
which is sort of given an image we want
to classify which of some number of
object categories it is um that's a nice
basic problem in computer vision that
we've using that we're using to
understand componets and such um but
there's actually a lot of other tasks
that people work on too um so some of
these are classification and
localization so now instead of just um
classifying an image as one of as some
category labels we also want to draw a
bounding box in the image to say where
that class occurs um another problem
people work on is detection so here
there's again some fixed number of
object categories but we actually want
to find all instances of those
categories inside the image and draw box
around them um another more recent task
that people have started to work on a
bit is this crazy thing called instance
segmentation where again you want you
have some fixed number of object
categories you want to find all
instances of the those categories in
your image but instead of using a box
you actually want to draw a little
Contour around uh and kind of identify
all the pixels belong belonging to each
instance um instance segmentation is
kind of crazy so we're not going to talk
about that today just thought you should
be aware of it um and we're going to
really focus on this these localization
and detection tasks today and the big
difference between these is the number
of objects that we're finding so in
localization there's sort of one object
or in general a fixed number of objects
whereas in detection we might have a
multiple objects or a variable number of
objects and this seems like a small
difference but it'll turn out to
actually make a big uh be pretty
important for our
architectures so we're going to first
talk about uh classification and
localization uh because it's kind of the
simplest so just to recap what I just
said uh classification one image to a
category label uh localization is image
to a box and classification localization
means we're going to do both at the same
time uh just to give you an idea of the
kinds of data sets people use for this
um we we've talked about the imag net
classification challenge uh imet also
has run a classification plus
localization challenge so here um
similar to the classification task
there's a thousand classes um and each
training instance in those classes
actually has one class and several
bounding boxes for that class inside the
image and now at test time your
algorithm again makes five guesses where
instead of your guesses just being class
labels it's a class label together with
a bounding box and to get it right you
need to get the class label right and
the bounding box right where getting a
bounding box right just means you're
close in some thing called intersection
over Union that you don't need to care
about too much right now um so again uh
you get it for image net at least you
get it right if you one of your five
guesses is correct and this is kind of
the main data set that people work on
for classification plus
localization so uh one really
fundamental Paradigm that's really
useful when thinking about localization
is this idea of regression so I don't
know if thinking back to a machine
learning class you kind of saw like
classification like maybe with an SPM
and regression maybe with linear
regression or something fancier and when
we're talking about localization it's
really like we can really just frame
this as a regression problem where we
have an image that's coming in that
image is going to go through some some
processing and we're eventually going to
produce four real valued numbers that
parameterize this box um there's
different parameterizations people use
common is uh XY coordinates of the upper
left hand corner and the width and
height of the box but you'll see some
other variants as well but always four
numbers for a bounding box um and then
there's some ground truth bounding box
which again is just four numbers and now
we have we can compute a loss like maybe
ukian loss is a pretty pretty standard
choice between the numbers that we
produced and the correct numbers and now
we can just train this thing just like
we did our classification networks where
we sample some mini batch of data with
some ground truth boxes we propagate
forward compute a loss between our
predictions and the correct predictions
back propagate um and just update the
network so this Paradigm is is really
easy this actually makes this
localization task uh actually pretty
easy to implement so here's a really
simple recipe for how you could
Implement classification plus
localization so first you just download
uh some existing pre-trained model or
you train it yourself if you're
ambitious um something like alexnet vgg
googlet all these things we talked about
last
lecture now um we're going to take those
fully connected layers that were uh
producing our class scores we're going
to set those aside for the moment and
we're going to attach a couple new fully
connected layers to some point in the
network this will be called we'll call
this a regression head but I mean it's
basically the same thing it's a couple
fully connected layers and then it
outputs some real valued
numbers um now we train this thing just
like we trained our classification
Network the only difference is that now
instead of class scores um and ground TR
classes we use a L2 loss and ground trth
boxes other than that we train this
network exactly the same way now at test
time we just use both heads to do
classification and localization we have
an image we've trained the
classification heads we've trained the
localization heads um we pass it through
we get class scores we get boxes and and
we're done like really that's that's all
you need to do so this is kind of a
really nice simple recipe that you guys
could use for classification plus
localization on your
projects um so one slight detail with
this approach um there's sort of two
main ways that people do this regression
task um you could imagine a class
agnostic regressor or class specific
regressor um you could imagine that no
matter what class I'm going to use the
same architecture the same weights in
those fully connected layers to produce
my bounding box so that would mean
you're sort of outputting always four
numbers which are just the Box no matter
the class um and alternative you'll see
sometimes is class specific regression
where now you're going to Output C * 4
numbers that's sort of like one bounding
box per class um and different people
have found that sometimes these work
better in different cases um but I mean
intuitively it kind of makes sense that
some that the way you might think about
localizing a a cat could be a little bit
different than the way you localize a
train so maybe you want to have
different parts of your network that are
responsible for those things but uh so
then it's it's pretty easy then you just
it changes your the way you compute loss
a little bit you compute loss only using
the um the ground truth class the the
box for the ground truth class but other
than that still basically the same
idea uh another design Choice here is
where exactly you attach the regression
head um again this isn't too important
different people you'll see different
people do it in different ways some
common choices would be to attach it
right after the the the last
convolutional layer um that would just
sort of mean like you're re
reinitializing new fully connected
layers um you'll see things like
overfeat and vgg localization work this
way another common choice is to just
attach your regression head actually
after the last fully connected layers
from the classification Network um and
you'll see some other things like deep
pose and rcnn kind of work in this
flavor but either one works fine um
they'll probably you could attach it
just about anywhere and it would do
something so um as an aside you this is
we can actually generalize this
framework to multi to localizing more
than one object so normally with this uh
classification localization task that we
sort of set up on imag net we care about
producing exactly one object bounding
box for the input image but in some
cases you might know ahead of time that
you always want to localize some fixed
number of objects um so here this is
easy to generalize now your regression
head it just outputs a box for each of
those objects that you care about and
again you train the network in the same
way um and this idea of actually
localizing multiple objects at the same
time is pretty General and pretty
powerful so for example this kind of
approach has been used for human pose
estimation so the idea is we want to
input a sort of a close-up view of a
person and then we want to figure out
what's the pose of that person so well
people sort of generally have a fixed
number of joints like their wrists and
their neck and their elbows and that
sort of stuff um so we just know that we
need to I find all the joints so we
input our image we run it through a
convolutional network and we regress XY
coordinates for each joint location and
that gives us our um our that actually
lets you predict a whole human pose
using this sort of localization
framework um I mean this p and there's a
paper from Google from a year or two ago
that does this sort of approach they had
a couple other bells and whistles but
the basic idea was just regressing using
a CNN to these joint
positions so overall this idea of
localization and treating it as
regression for a fixed number of objects
is really really simple so I know some
of you guys on your projects have been
thinking that you want to actually run
detection because you want to understand
like in parts of your images or find
parts inside the image um and if you're
thinking along of a project along those
lines I'd really encourage you to think
about this localization framework
instead that if there's actually a fixed
number of objects that you know you want
to localize in every image um you should
try to frame it as a localization
problem because that's tends to be a lot
easier to set
up all right so actually the simple idea
of localization via regression actually
is really simple it'll actually work um
I would really encourage you to try it
for your projects but if you want to win
competitions like imet you need to add a
little bit of other fancy stuff so
another thing that people do for
localization is this idea of sliding
window so we'll step through this in
more detail but the idea is that um you
you still have your class
localization dual headed network but
you're actually going to run it not once
on the image but at multiple positions
on the image and you're going to
aggregate across those different
positions and you can actually do this
in an efficient way so to sort of see
more concretely how how this sliding
window localization Works we're going to
look at the overfeat architecture so
overfeat was um actually the winner of
the imag net localization challenge in
2013 it this this architect this this
sort of setup looks basically like what
we saw a couple slides ago we have um an
Alex net at the beginning then we have a
classification head we have a regression
head classification head is spitting out
class scores regression head is spitting
out bounding
boxes um and this thing because it's an
Alex net type architecture is expecting
an input of 221x
221 um but actually we can run this on
larger images and this can help
sometimes so suppose we have a lar a
larger image of uh what what did I say
257 x 257 now we could imagine taking
our classification plus localization
Network and running it just on the upper
corner of this image and that'll give us
some some class score um and also some
some regress bounding box and we're
going to repeat this um take our same
classification plus localization Network
and run it on all four corners of this
image um and after doing so we'll end up
with four regressed bounding boxes one
from each of those four locations
together with a Class A classification
score from each location um but we
actually want just a single bounding box
so then they use some thetics to merge
these bounding boxes and scores and that
part's a little bit ugly I don't want to
go into the details here they have it in
the paper but the idea is that um
probably combining aggregating these
boxes across multiple locations can help
can help the model sort of correct its
own errors and this tends to work really
well and I mean it won them the
challenge that
year but in practice they actually use
many more than four locations um oh yeah
question
so I on the previous slide so each of
those red boxes they weren't always
within the slice being looked at is that
just a design of the slide like normally
the box would be fully within the well I
mean yeah yeah that's actually a good
point so once you're doing regression
you're just predicting four numbers you
could in pract you could in theory
predict anywhere it doesn't have to be
inside the
image although although that that brings
up a good point when you're doing this
um especially when they when you're
training this network in this sliding
window way you actually need to shift
the ground truth box in a little you
need sh shift the coordinate frame for
those different slices that's kind of an
ugly detail that you have to worry
about um yeah but in practice they use
many more than four image locations and
they actually do multiple scales as well
so you can see uh this is actually a
figure from their paper on the left you
see all the different positions where
they kind of evaluated this network um
on the in the middle you see those
output regressed boxes one for each of
those positions on the bottom you see
the score map for each of those
positions and then I mean they're pretty
noisy but it's kind of conver they're
kind of generally over the bear so they
run this fancy aggregation method and
they get a final box for the bear and
they decide that this image is a bear
and they actually won the the challenge
with this but one problem you might
anticipate is it could be pretty
expensive to actually run the network on
every one of those crops but there's
actually a more efficient way thing we
could do so we normally think of these
networks as having convolutional layers
and then fully connected layers but when
you think about it a fully connected
layer is just 4096 numbers right right
it's just a vector um but instead of
thinking of it as a vector we could
think of it as just another
convolutional feature map it's kind of
crazy we've just transposed it and added
two one by one Dimensions so now the
idea is that um our we can now treat our
our fully connected layers and convert
them into convolutional layers because
if you imagine um in our fully connected
Network we had this uh convolutional
feature map and we had one weight from
each element of that convolutional
feature map to produce each element of
our 49 six dimensional Vector um but we
instead of thinking about reshaping and
having an apine layer um that's sort of
equivalent to just having a 5x5
convolution it's a little bit weird but
if you think about it it it should make
sense eventually um but right so then
then our so then we take this fully
connected layer turns into a 5x5
convolution uh then this then we
previously had um another fully
connected layer going from 4096 to 4096
um this is actually a one by one
convolution right that's that's kind of
but if you if you think hard and sort of
work out the math on paper and go sit in
a quiet room you'll figure it out um and
so we basically can turn each of these
fully connected layers in our Network
into a convolutional layer and now now
this is pretty cool because now our
network is composed entirely of just
convolutions and pooling and element
wise operations so now we can actually
run the network on images of different
sizes and this sort of will give us very
cheaply equ the equivalent of operating
the network um independent on different
locations so to kind of see how that
works um you imagine at training time
you're maybe working over a 14x 14 input
you run some convolutions and then here
are our fully connected layers that
we're now reimagining as convolutional
layers so then we had this 5x5 con block
that gets turned into these one by one
uh spatially sized elements so we' we're
sort of eliminating not showing the
depth Dimension here but these like this
1X one would be 1X one by 4096
right so we're just converting these
layers into convolutional layers and now
that we now that they're convolutions we
could actually run on an input of a
larger size and you can see that now
we've we've added a couple extra pixels
to the input and now we actually run all
these things as convolutions and get a
2x2 output um but what's really cool
here is that we're able to share
computation to make this really
efficient so now our output is four
times as big but we've done much less
than four times the compute because if
you think about the difference between
where we're doing computation here the
only extra computation happened in these
yellow parts so now we're actually very
efficiently evaluating the network at
many many different positions um without
actually spending much computation so
this is how they able to evaluate that
Network in that very very dense
multiscale way that you saw a couple
slides ago does that make sense any
questions on this okay
good right so actually we can look at
the classification plus localization
results on imag net over the last couple
years so in 2012 um Alex Alex kesy Jeff
Hinton Ilia Suk they won not only
classification but also localization but
I wasn't able to find any publish
details of exactly how they did that um
in 2013 it was the overfeat method that
we just saw actually improved on Alex's
results a little bit the year after um
we talked about vgg and their sort of
really deep 19 layer Network they got
second place on classification but they
actually won on localization and the vgg
actually used basically exactly the same
stry that overfeat did they just used a
deeper Network um and actually
interestingly vgg used fewer scales they
stamped that Network out in fewer places
and used fewer scales but they actually
decreased the error quite a bit so
basically the only difference between
overfeat and vgg here is that vgg used a
deeper Network so here we could see that
these really powerful image features
actually improve the localization
performance quite a bit um we didn't
have to change the localization
architecture at all we just swapped out
a better CNN and it improved results a
lot
and then this year in 2015 I mean
Microsoft swept everything as that'll be
a theme in this lecture as well um this
this 150 layer resnet from Microsoft
crushed localization here and Dr dropped
performance from 25 all the way down to
9 but I mean this this is a little bit
fan this is tough to really isolate the
Deep features so yes they did have
deeper features but Microsoft actually
used a different localization method
called rpns region proposal networks so
it's not really clear whether this which
part whether it's the better
localization strategy or whether the
better features but at any rate um they
did really
well so that's pretty much all I want to
say about classification localization
just consider doing it for your projects
and if there's any questions about this
task we should talk about that now
before moving on yeah um how much are
you limited by outliers in your data set
so ifet has things that are incorrectly
labeled or the boxes are in the wrong
places uh yeah that that can always hurt
performance especially with an L2 loss
right so then L2 loss when having
outliers is actually really bad um so
sometimes people don't use an L2 loss
instead you you can try an L1 loss that
can help with outliers a little bit
people also will do sometimes a smooth
L1 loss where it looks like L1 sort of
at the Tails but then near zero it'll be
quadratic so actually swapping out that
regression loss function can help a bit
with outliers sometimes but also if you
have a little bit of noise sometimes
hopefully your network will just figure
it out cross your fingers don't think
too hard
any other questions yeah when we're
using one of these pre-trained nets and
just training the regression head as you
call it do we just back into our own or
can we back all the way into
the yeah good question so people do both
actually um so for overfeat uh actually
I don't remember I don't remember
exactly which overfeat did but BGG
actually back props into the entire
network um so it'll be it'll be faster
to just it'll actually work fine if you
just train the the regression head but
but you'll tend to get a little bit
better results if you back propop into
the whole network and BGG did this
experiment and they got maybe one or two
points extra by back propping through
the whole thing but it at the expense of
a lot more computation and training time
so if so I would I would say like as a
first thing don't just try not back
propping into the network doesn't it
even generalize if if I mean the testing
data can sometimes look pretty different
from what these nets are trained on
right well yeah generally not right
because you're testing them on the same
classes that you saw at training time so
you're going to different instances
obviously but like mean you're still you
saw bears at test time you're going to
see bears at training time we're not
expecting you to generalize across
classes that would be pretty
hard yeah um if you're backing into the
whole does that mean you have to train
with the
class simane ah good question yeah so
sometimes people will do that they'll
train with both simultaneously also
sometimes people will just end up with
separate networks one that's sort of
only responsible for regression one
that's only responsible for
classification um those both
work what if you don't know the number
of objects that are going to appear in
image well pick up all them glad you
asked that's that's actually the next
thing we're going to talk about that's
that's a different task called object
detection so yeah synchronization
between the localization class and
classification
class well uh separat right yeah well so
it I mean it kind of depends on the
training strategy if you're like if you
it also kind of goes back to this idea
of class agnostic versus class specific
regression so if you're doing class
agnostic regression it doesn't matter
you just regress to the boxes to matter
the class class specific you're sort of
training separate regressors for each
class all right let's talk about object
detection so object detection is is like
much fancier much cooler but also a lot
hairier so the idea is that again we
have an input image we have some set of
classes we want to find all instances of
those classes in that in that input
image so I mean you know regression
works pretty well for localization why
don't we try it for uh for detection too
well because in this image we have uh
these These dogs and cats and we have
four things we have 16 numbers that's
looks like that looks like regression
Right image in numbers out but if we
look at another image then you know this
one only has two things coming out so it
has eight numbers if we look at this one
there's a whole bunch of cats so we need
a bunch of numbers so I mean it's it's
kind of hard to treat detection as
straight up regression because have this
problem of variable sized outputs so
we're going to have to do something
fancier although actually there is a
method we'll talk about later that sort
of does this anyway and does treat it as
as regression but we'll get to that
we'll get to that later but in general
you want to not treat this as regression
because you have variable sized
outputs so what really easy problem a
really easy way to solve this is to
think of detection not as regression but
as classification right in machine
learning regression and classification
are your two Hammers and you just want
to use those to beat all your problems
right so we regression didn't work so
we'll do classification instead um we
know how to classify image regions we
just run it through a CNN right so we're
going to do is we're going to take many
of these input regions of the image put
a classifier there and say like oh right
this region of the image is it a cat no
is it a dog no move it over a little bit
oh we found a cat that's great move it
over a little bit that's that's not
anything so then we can actually just
try out a whole bunch of different image
regions run a classifier in each one and
this will basically solve our variable
siiz output
problem um so there's there's oh yeah
question so how do you decide what's the
window size so the question of how
decide how to decide what the window
size the answer is we just try them all
right just literally try them all um so
that's that's that's actually a big
problem right because we need to try
Windows of different sizes of different
positions of different scales we need to
do this for every test image this is
going to be really expensive right
there's a whole lot of places we need to
look yeah I also he you're saying your
windows does that look like anything
usually when you're classifying you just
take whichever class has the score right
oh yeah so yeah so in practice you
usually also when you're doing this
classification you add an extra uh two
things one you you can add an extra
class to say background and say like oh
there's nothing here um another thing
you can do is um not is do actually
multi-label classification so you could
output multiple positive things um right
that's actually pretty easy to do it's
just instead of a softmax loss you have
a independent regression losses or
independent logistic regressors per
class so that can actually let you say
yes on multiple classes at one point um
but that's just swapping out a loss
function so that's that's pretty easy to
do um right so actually like like we
said a problem with this approach is
that there's a whole bunch of different
positions we need to evaluate um the
solution sort of a couple as of a couple
years ago was just use really class use
really fast classifiers and try them all
so um actually detection is this really
old problem in computer vision so you
should probably have a a little bit more
historical perspective so starting in
about 2005 um there was this really
successful approach to at the time
really successful for pedestrian
detection that used this feature
representation called histogram of
oriented gradients so if you recall back
to homework one you actually use this
feature um on the last part to actually
do classification as well so this was
actually sort of the the the best
feature that we had in computer vision
circle around 2005 so the idea is we're
just going to do linear classifiers on
top of this feature and that's going to
be our classifier so linear classifiers
are really fast so the way this works is
that we compute our histogram of
oriented gradient feature for the whole
image at multiple scales and we run this
linear classifier at every scale every
position just do it really fast just do
it everywhere because it's a linear
classifier and it's fast to evaluate um
and this worked really well in
2005 um sort of people took this idea
and worked on it a little bit more for
the next couple years so sort of the one
of the most important detection
paradigms pre- deep learning was this
thing called uh the deformable parts
model so I don't want to go too much
into the details of this but I mean the
basic idea is that we're still working
on these uh histogram of Orient gradient
features but now our model rather than
just being a linear classifier we have
this linear this linear sort of template
for the for the object and we also have
these templates for parts that are
allowed to sort of vary over spatial
positions and deform a little bit um and
they have some some fancy some fancy
thing called a latent SPM to learn these
things and a really fancy uh uh dynamic
programming algorithm to actually uh
evaluate this thing really fast at test
time um so this is actually kind of fun
if you enjoy algorithms this this thing
this part is kind of fun to to think
about but the end result is that um it's
it's a more it's a more powerful
classifier because it allows a little
bit of deformability in your in your
model and you can still evaluate it
really fast so we're still just going to
evaluate it everywhere every scale every
position every aspect ratio just do it
everywhere because it's fast um and this
actually worked really well um in 2010
uh around there so that was sort of
state-of-the-art in detection for many
problems at that time um so this is I
don't want to spend too much time on
this but there was a really cool paper
last year that argued that these DPM
models are actually just a certain Ty of
confet right so right because these
these histograms of already gradients
are like little edges we can compute
edges with convolutions and then the
histogram is kind of like pooling that
sort of thing so um if you're interested
check out this paper it's kind of fun to
think about
right but we really want to work on make
this thing work on classifiers that are
not fast to evaluate like maybe a CNN so
here this we this problem is still hard
right we have many different positions
we want to try when we probably can't
actually afford to try them all so the
solution is that we don't try them all
we have some other thing that sort of
guesses where we want to look and then
we only apply our expensive classifier
at those uh smaller number of
locations so that idea is called uh
region
proposals so we an a region proposal
method is this thing that takes in an
image and then outputs a whole bunch of
regions where maybe possibly an object
might be located so one way you can
think about region proposals is that
they're kind of like a really fast a
class agnostic object detector right
they don't care about the class um
they're not very accurate but they're
pretty fast to run and they give us a
whole bunch of boxes um and the
intuition behind behind these region
proposal methods is that they're kind of
looking for blob like structures in the
image right so like objects are gener
like the dog I mean if you kind of
squint it looks kind of like a white
blob the cat looks kind of like a white
blob these flowers are kind of Blobby
the eyes and the nose are kind of Blobby
so when you run these region proposal
methods a lot of times what you'll see
is they'll kind of put boxes around a
lot of these Blobby regions in the in
the
image um so probably the most famous
region proposal method uh is called
selective search you don't really need
to know exact in too much detail how
this works but the idea is that um you
start from your pixels and you kind of
merge adjacent pixels together if they
have similar color and and texture and
form these connected re these connected
blob likee regions and then you merge up
these blob likee regions to get bigger
and bigger Blobby Parts um and then for
each of these different scales you could
actually convert each of these Blobby
regions into a box by just drawing a box
around it so then then by doing this
over multiple scales you end up with a
whole bunch of boxes around sort of a
lot of Blobby stuff in the image and
it's reasonably fast to compute and
actually cuts down the search space
quite a
lot um but selective search really isn't
the only game in town it's just maybe
the most famous there's a whole bunch of
different uh region proposal methods
that people have developed so there was
this paper last year that actually did a
really cool thorough scientific
evaluation of all these different region
proposal methods and sort of gave you
the pros and the cons of each and all
that kind of stuff um but I mean my
takeaway from this paper was just use
Edge boxes if you have to pick one so
it's cuz it's it's really fast it you
can run it in about a third of a second
per image um compared to about 10
seconds for Selective search but um the
more stars is better and it gets a lot
of stars so it's
good right so now that we have this idea
of regent proposals and we have this
idea of a CNN classifier let's just put
everything all together um so that's and
so this this idea was was sort of first
put together in a really nice way um in
2014 in this method called rcnn the idea
is it's a region based CNN method so
it's I mean it's it's pretty simple now
that we've seen all the pieces um we
have an input image we're going to run a
region proposal method like selective
search to get about maybe 2,000 boxes of
different scales and positions I mean
2,000 is still a lot but it's a lot less
than all possible boxes in the image now
for each of those boxes we're going to
crop warp that image region um to some
fixed size and then run it forward
through a CNN to classify and then this
CNN is going to have a regression head
and a a regression head here and and a
classification head they used spms here
um so the idea is that this this
regression head can sort of correct for
region proposals that were a little bit
off right so this this actually worked
really well it's really simple um yeah
it's pretty cool but unfortunately the
so unfortunately the training pipeline
is a little bit complicated
so the way that you end up train
training this rcnn model is you know
like many like many models you first
start by downloading a model from the
internet that works well for
classification um it originally they
were using an
alexnet uh then then next we actually
want to find tune this model for
detection right because this this
classification model was probably
trained on imet for a thousand classes
but your detection data set has a
different number of classes and the
image statistics are a little bit
different so you still run this you
still train this network for
classification but you have to add a
couple new layers at the end to deal
with your classes and to help you deal
with the slightly different statistics
of uh of your image data so here um
you're just doing classification still
but you're not running it on whole
images you're running it on positive and
negative regions of your images from
your detection data
set um right so you initialize a new
layer and you and you train this thing
again for your data set um next we
actually want to cach all these features
to disk so for every image in your in
your data set you run selective search
you run that image you extract those
regions you warp them you run it through
the CNN and you cache those features to
disk um and something important for this
step is to have a large hard drive um
the Pascal data set is not too big maybe
order of a a couple tens of thousands of
images but extracting these features
actually takes hundreds of gigabytes so
that's not so great um and then next we
have this we want to train our spms to
uh actually be able to classify IM
different our different classes based on
these features so here we want to run a
bunch of we want to train a bunch of
different binary spms to classify image
regions as to whether or not they
contain or don't contain that that one
object so this goes back to a question a
little bit ago that sometimes you
actually might want to have um one
region have multiple positive be able to
Output yes on multiple classes for the
same image region and one way that they
do that is just by training separate
binary spms for each class class right
so then this is sort of an offline
process they just use libm um so you
have these features these are maybe uh
those aren't positive samples for a cad
spvm that doesn't make any sense right
but you get the idea right you have
these different image you have these
different image regions you have these
features that you've saved to dis for
those regions and then you divide them
into positive and negative samples for
each uh for each class and you just
train these these uh binary spms so you
do this for cat uh you do this the same
thing for dog and you just do this for
every class in your data
set um right and then there's another
step right so then there's this idea of
box regression so sometimes your region
proposals aren't perfect so what we
actually want to do is be able to
regress from from these cached features
to a correction onto the region proposal
um and that correction has this kind of
funny parameterized normalized
representation you can read details
about it in the paper but kind of the
intuition is that maybe for this for
this uh for this region proposal it was
pretty good we don't really need to make
any any corrections but for maybe this
one in the middle The Proposal was too
far to the left it should have like the
the correct ground truth is a little bit
to the right so we want to regress to
this correction Vector that actually
tells that we need to shift a little bit
to the right or maybe this guy is a
little bit too wide it includes too much
of the stuff outside the cat so we want
to regress to this uh correction Vector
that tells us we need to shrink the
region proposal a little bit so again
this is just a linear they just do
linear aggression which you could which
you know from 229 you have these these
features you have these targets you just
train linear aggression and that's
that um so before we look at the results
uh we should talk I want to talk a
little bit about the different data sets
that people use for detection there's
kind of three that you'll see in
practice um one is the Pascal VOC data
set uh it was pretty important I think
in the earlier 2000s but now it's a
little bit small so this one's about
this one's 20 classes and about 20,000
images and tends to have about two
objects per image so because this is a
relatively smallish data set you'll see
a lot of detection papers work on this
just cuz it's easier to handle um but
there's also an imag net detection data
set um imag net runs a whole bunch of
challenges as you've probably seen by
now we saw classification we saw
localization there's also a imag net
detection challenge um but for detection
there's only 200 classes not the
Thousand from classification but it's
it's very big uh almost half a million
images so you don't see as many papers
work on it just cuz it's kind of
annoying to handle um but there's only
about one object per image and then more
more recently there's this one from
Microsoft called Coco which has fewer
classes fewer images but actually has a
lot more objects per image so people
like to work on that now because it's
more
interesting um right there's also this
this when you're talking about detection
there's this funny evaluation metric we
use called mean average Precision I
don't really want to get too much into
the details like what you really need to
know is that it's a number between zero
and 100 and 100 is good um and it and it
also I mean kind of the intuition is
that it's um you want to have the right
you want to have true positives get high
scores and you also have want to have
some threshold on uh that your boxes you
produce need to be within some threshold
of the correct box and you can usually
this that threshold is 0.5 on
intersection over Union but you'll see
different challenges use slightly
different things for
that right so let's now that we
understand the data sets and the
evaluation let's see how rcnn did right
so this is on the Pas on two versions of
the Pascal data set like I said it's
smaller you see a lot of results on this
um the there's different versions one in
2007 2010 you'll often see people use
those just because the test data is
publicly available so it's easy to
evaluate um yeah but so in this this
deformable parts model that we saw from
2011 from a couple slides ago is getting
about 20 about 30 on mean average
Precision um there's this other method
called region LS from 2013 that was sort
of the state-of-the-art that I could
find right before deep learning but it's
it's sort of a similar flavor you have
these features and it's classifier as on
Tope of features and rcnn is this pretty
simple thing we just saw and actually
jump it actually improves the
performance quite a lot so the first
thing to see is uh we had a big
Improvement when we just switch this
pretty simple framework um using CNN um
and actually this this result here is
without the bounding box regressions
this is only using the region proposals
and the spms actually if you include
this additional bounding box proposal
step it actually helps quite a bit um
another fun thing to note is that if you
take rcnn and you do everything the same
except you use vgg16 instead of alexnet
you get another pretty big boost in
performance so this is kind of similar
to what we've seen before that just
using these more powerful image features
tends to help a lot of different
tasks right so this is really good right
we've we've done like a huge Improvement
on detection compared to 2013 that's
amazing but um rcnn is not perfect it
has some problems right so it's pretty
slow at test time right we saw that we
have maybe 2,000 regions we need to
evaluate our CNN for each region that's
kind of slow um we also had this this
slightly subtle problem where um our svm
and our regression those were sort of
trained offline using like libm and
linear aggression so actually the
weights of our of our CNN didn't really
have the chance to update in response to
what those parts of the of the network
of those objectives wanted to do um and
we also had this kind of complicated
training pipeline that was a bit of a
mess so um to fix these problems uh a
year later we had this thing called fast
rcnn
so fast rcnn was presented pretty
recently at uh in iccv just in December
but the idea is is really simple we're
just going to swap the order of uh
extracting regions and running the CNN
so this is kind of kind of related to
this sliding window idea we saw with
over feet so here the pipeline at test
time looks kind of similar we have this
input image we're going to not we're
going to take this high resolution input
image and run it through the
convolutional layers of our Network and
now we're going to get this high
resolution convolutional feature map and
now our region proposals we're going to
extract directly features for those
region proposals from this convolutional
feature map using this thing called Roi
pooling and then the regions the the
features for these the convolutional
features for those regions will be fed
into our fully connected layers and will
again have a classification head and a
regression head like we saw
before so this is really cool um it's
it's pretty great it solves a lot of the
problems that we just saw with rcnn so
rcnn is really slow at test time um we
solve this problem by just sharing this
this computation of convolutional
features across different region
proposals um RC uh rcnn also had these
problems at training time where we had
this this messy training pipeline we had
um this this problem where we're
training different parts of the network
separately and the solution is pretty
simple we just you know train it all
together all at once don't don't have
this complicated pipeline which we can
actually do now that we have this this
pretty nice function from inputs to
outputs
right so you can see that r that fast
rcnn actually solves quite a lot of the
the problems that we saw with vanilla
rcnn um sort of the really interesting
technical bit in fast rcnn was this
problem of Roi region of Interest
pooling so the idea is that we have this
input image um that's probably high
resolution and we have this region
proposal that's maybe coming out of
selective search or Edge boxes or
something like that and we can put this
region this high resolution image
through our convolutional and pooling
layers just just fine because those are
uh sort of scale invariant they scale up
to different sizes of inputs but now the
problem is that the fully connected
layers from the our pre-train Network
are expecting these uh pretty low reses
con features whereas these features from
the whole image are high reses so now we
solved this problem in a pretty
straightforward way so given this region
proposal we're going to project it onto
sort of the the spatial part of that con
feature volume now we're going to divide
that con Fe volume into a little grid um
right divide that thing into this H byw
grid that the downstream layers are
expecting and we do Max pooling um
within each of those grid cells so now
we've so now we've um through this
pretty simple strategy we've taken this
region proposal and we've shared
convolutional features now we've
extracted this uh fix size output for
that region for that uh for that region
proposal right so this is basically just
swapping the order of convolution and
warping and cropping that's one way to
think about it
and also this is a pretty nice operation
because since this thing is basically
just max pooling and we know how to back
propagate through Max pooling you can
back propagate through these these uh
region of Interest pooling layers just
fine and that's what really allows us to
train this whole thing in a joint
way right so let's see some results and
these are actually pretty cool pretty
amazing right so for training time rcnn
it had this complicated pipeline we had
save all this stuff to dis we had to do
all this stuff independently and even on
that pretty small Pascal data set it
took 84 4 hours to train fast rcnn is
much faster um you can train it in a day
as far as test time uh vanilla R CNN is
pretty slow because again we're running
these independent forward passes of the
CNN for each region proposal um whereas
for fastar CNN where we can sort of
share the computation between different
region proposals and get this gigantic
speed up at test time 146 that's great
amazing um and in in terms of
performance I mean it does a little bit
better it's not a IC difference in
performance but this could probably be
attributed to this fine-tuning property
that with fast rcnn you can actually
fine-tune all parts of the convolutional
network jointly to help with these
output tasks and that's probably why you
see a bit of an increase here right so
this is great right what's what could
possibly be wrong with fast rcnn it
looks amazing uh the big problem is that
uh these test time speeds don't include
region proposals right so now fast rcnn
is so good that actually the bottleneck
is Computing region proposals that's
pretty cool so once you factor in the
the speed of comp actually Computing
these region proposals on CPU you can
see that a lot of our speed benefits
disappear right we're only 25x faster
and we kind of lost that beautiful 100x
speed up um also now because it takes
maybe two seconds to run actually per
image end to end you can't really use
this real time it's still kind of an
offline processing
thing right so the solution of this um
should be pretty obvious right we we're
already using a convolutional work for
regression we're already using it for
classification um why not use it for
region proposals too right should work
maybe kind of crazy um so that's that's
a paper um anyone want to guess the
name yeah so it's faster
rcnn yes they were they were really
creative here right but the idea is
pretty simple right we're from Fast rcnn
we're already taking our input image and
we're Computing these big convolutional
feature Maps over the the entire input
image so then um instead of using some
external method to compute region
proposals they add this little thing
called a region proposal Network that
looks directly at these conv that looks
at these last layer convolutional
features and is able to produce region
proposals directly from that
convolutional feature map and then once
you have region proposals you just do
the same thing as fast rcnn you use this
Roi pooling and all the Upstream stuff
is the same as fast rcnn
so really the the novel bit here is this
region proposal Network it's it's really
cool right we're doing the whole thing
in one giant convolutional Network right
so the way that this region proposal
network works um is that we're sort of
we receive as input this convolutional
feature map that's maybe coming out of
the last layer of our convolutional
features and we're going to add like
like most things our region proposal
network is a convolutional network right
so actually this is a typo this is a 3X3
con I'll fix that right so we we have a
sort of a sliding window approach over
our convolutional feature map but
sliding we sliding window is just a
convolution right so we just have a 3X3
convolution on top of this feature map
and then we have this uh this familiar
this familiar two-head structure inside
the region proposal Network where um
we're doing classification where here we
just want to say whether or not um it's
an object and also regression to um
regress from this sort of position onto
an ual region proposal so the idea is
that the position of the sliding window
relative to the feature map sort of
tells us where we are in the image and
then these regression outputs sort of
give us Corrections on top of this this
position in the feature map um but
actually they make it a little bit more
complicated than that so instead of
regressing directly from this position
in the convolutional feature map they
have this notion of uh these different
anchor boxes so you could imagine taking
these different sized and shaped Anor
boxes and sort of pasting them in the
original image at the point of the image
corresponding to this point in the
feature map right like in fast RCN we
were projecting forward from the image
into the feature map um now we're doing
the opposite we're we're projecting from
the feature map back into the image for
these uh for these anchor
boxes so then for each of these anchor
boxes were they use sort of n
convolutional anchor boxes they use the
same ones at every position in the image
um and they for each of these anchor
boxes uh they produce a score as to
whether or not that Anchor Box
corresponds to an object and they also
produce four regression coordinates that
can correct that Anchor Box in similar
ways that we saw before um and now this
region proposal Network you can just
train to try to predict uh sort of as a
class agnostic object
detector so faster rcnn uh in the
original paper they train this thing in
kind of a funny way where first they
train the region proposal Network then
they train fast stcn then they do some
magic to merge together and at the end
of the day they have one network that
produces everything um so this this is a
little bit messy but in the original
paper they describe this thing but since
then they've had some unpublished work
where they actually just train the whole
thing jointly where they're sort of they
have one big Network where you have an
image coming in you have uh this in
inside the region proposal Network you
have a classification loss to classify
whether each region proposal is or is
not an object you have these bounding
box regressions ins the region proposal
Network to regress on top of your
convolutional anchors um and then from
fast then we do Roi pooling and do this
fast rcnn trick and then at the end of
the network we have this classification
loss to say which class it is and this
regression loss to correct um to have a
correction on top of the region proposal
so this is this big thing it's just one
big network with four losses yeah just
for clarification you're saying that the
um proposal works as a free by free
convolution 3x3 convolution so the
proposal scores and regression
coordinates are produced by a 3X3 3x3
and then a pair of 1ex one convolutions
off the feature map right so the idea is
that um we're looking at these different
anchor boxes of different positions and
scales and but we're actually looking at
the same position in the feature map to
classify those different anchor boxes
but you'd have different you learn
different weights for the different
anchors why is it fre by3 how does it
relate to the whole feature size um I
think it's more empirical right so the
3x the idea is just you want to have a
little bit of nonlinearity um you could
imagine just doing sort of a direct one
by one convolution directly off the
feature Maps um but I think they don't
discuss this in the paper but I'm
guessing just a 3X3 tends to work a bit
better but there's no like really deep
reason why you why you do that it could
be more it could be less it could be a
bigger kernel it's just sort of you have
this little convolutional network with
two heads that's the main
point any other questions yeah so we
were taking that map at the like after
doing all the convolution layers right
mhm so what happens if we just prune the
image just to that particular like area
before we start uh like doing all the
convolution and just keep like all the
neighboring pixels wouldn't it be like
sort of faster uh sorry I don't quite
understand because your convolutional
feature map corresponds to the whole
image the point is that um we don't
actually want to process the whole image
we want to pick out some some regions of
the image to do more processing on but
we need to choose those regions
somehow so I'm saying like what if you
just select those regions like before
doing all the previous oneu there yeah
so that's basically the that's basically
this idea of using external region
proposals right so you when you do
external region proposals you're sort of
picking it first before you do the
convolutions um but it's just sort of a
nice thing if you can do it all at once
so it's like convolutions are kind of
this General like really General process
ing uh processing that you can do to the
image so you're kind of hoping that
convolutions are good enough for
classification or good enough for
aggression the types of information that
you have in those convolutions is
probably good enough for classifying
regions as well so it's actually it's
actually a computational savings because
at the end of the day you end up using
that same convolutional feature map for
everything for the region proposals for
the downstream classification for the
down Downstream regression so that's
actually why you get the speed up
here yeah but good
question yeah so then uh we have this
big Network we train it with four losses
and now we can do object detection sort
of all at once it's pretty cool so if we
look at results um comparing the three
rcnn of various velocities then we for
original rcnn um it took about 50
seconds at test time per image this is
counting the region proposals this is
counting running the CNN separately for
each region proposal so that's pretty
slow now fast R CNN we saw it was sort
of bottlenecked by the region proposal
time but once we move to faster rcnn
then those region proposals are
basically coming for free since they're
just the way we compute region proposals
is just a tiny 3x3 convolution and a
couple 1ex one convolutions so those are
very cheap to evaluate so then at test
time faster rcnn runs in a fifth of a
second on a pretty high resolution image
so that's actually uh yeah are there any
issues with objects close to the edge of
the
image like because effectively when
you're padding or whatever you're GNA
end up
you don't gain information from those
the edge of the image well I mean all
your convolutions always have zero
padding so you're not like one of the
ideas behind zero padding is you're
hoping not to throw away information
from the edges so I think maybe you
might have a problem with uh if you
didn't do the zero padding it might be
more of a problem but I mean as we've
sort of discussed before the fact that
you're adding that zero padding might
affect the statistics of those features
so it could maybe be a bit of a problem
but in practice it seems to work just
fine um but actually that yeah that that
type of analysis of where do we have
failure cases where do we get things
wrong is a really important process when
you're developing new algorithms and
that can give you Insight onto what
might make things
better yeah any other questions yeah if
I'm only interested actually in the
classification task maybe even with like
multiple objects in the same image um do
these localization methods still um
actually help me to to boost my my
classification accuracies or scores or
can I say like actually it's not
important that for me if I'm only
interested in a classification itself so
I mean I have I have the intuition that
maybe it might help but it's actually
kind of hard to that to do that
experiment because the data sets are
different right because when you work
when you work on a classification data
set like imet that's one thing but then
when you work on detection it's this
other data set and I haven't like you
could imagine trying to classify the
detection images based on what objects
are present but I haven't really seen
any really good comparisons that try to
study that empirically but I mean that'd
be a cool experiment to have in your
project um yeah so if for example you
wanted to change your bounding boxes so
that they can also take rotation into
account you just add AA parameter to
each of the Bing boxes like their
representation and then run it through
this network and would that work in a
similar way so that that's that's
actually a very good question so then
you have this problem with Roi pooling
right because the way that the ROI
pooling worked is was by dividing that
thing into this fixed grid and doing Max
pooling once you do rotation it's
actually kind of difficult um there's
this really cool paper from Deep Mind uh
in the last over the summer called
spatial Transformer networks that
actually introduces um a a really cool
way to solve this problem um and the
idea is that instead of doing Roi
pooling we're going to do bilinear
interpolation kind of like you might use
for Textures in graphics so once you do
bilinear interpolation then you actually
can do maybe these these crazy regions
um so yeah that's definitely something
people are thinking about but it hasn't
been incorporated into the into the
whole pipeline
yet yeah couldn't you alternatively just
train on all sorts of rotations of your
data set and just learn the different
rotations of objects um you could that
would be slow then you're back in this
sort of rcnn regime right and look at
that 250 times slower do you really want
to pay that
price I mean I think another practical
concern with rotated objects is that we
don't really have that ground truth in
our data sets so for most for these most
of these detection data sets the only
ground truth information we have are
these axis align bounding boxes so it's
hard you don't really have a ground
truth position um so that's kind of a
practical concern why I think people
haven't really explored this so
much um yeah so the end end story with
faster rcnn is it's super fast and it
does about the same right that's good it
works um so actually really interesting
is um now at this point I you you can
actually understand the state-of-the-art
in object detection so this is this is
sort of the best object detector in the
world it crushed everyone the imag net
challenge in imag net and Coco
challenges in December and of like most
other things it's this deep residual
Network so the best object detector in
the world right now is 101 layer
residual Network plus faster
rcnn um plus a couple other goodies here
right so we talked about we talked about
faster rcnn we T we saw resnet last year
they have um to get an extra they always
for competitions you need to add a
couple crazy things to just get get a
little bit boost in performance right so
here this box refinement they actually
do multiple steps of refining the
bounding box cuz you you sort of saw
that in the fast rcnn framework you're
doing this a correction on top of your
region proposal so then you could
actually feed that back into the network
and reclassify and re get another
prediction so that's this box refinement
step it gives you a little bit of boost
they add context so in addition to
classifying just the just the region
they get a vector that gives you the
whole uh features for the entire image
um that sort of gives you more context
than just that little crop and that
gives you a little bit more performance
and they also do multiscale testing kind
of like we saw in overfeat how they so
they actually run the thing on images at
different sizes at test time and then
aggregate over those different sizes and
when you put all those things together
you win a lot of
competitions so this thing um one on so
Coco actually Microsoft Coco actually
runs a detection Challenge and they won
the detection Challenge on Coco we can
also look at the rapid progress on the
image net detection challenges over the
last couple years so you can see in 2013
was sort of the first time that we had
uh these deep learning uh detection
models so overfeat that we saw for
localization they actually submitted a
they had a version of their system that
works on detection as well by sort of
changing the logic with by which they
merge bounding boxes um and they did
pretty good but they were actually
outperformed by this other this other
group called U Vision that was sort of
not a deep learning approach they used a
lot of features um but then in 2014 we
actually saw both of these were deep
learning approaches and Google actually
won that one by using a Google net plus
some other detection stuff on top of
Google net and then in 2015 things went
crazy and these residual networks plus
faster rcnn just crushed everything so I
think detection especially over the last
couple years has been a really exciting
thing because we've seen this really
rapid progress over the last couple
years in detection like most other
things
and another point I think is kind of fun
to make is that actually um for all like
again to win competitions you know Andre
said you onsemble and get 2% so you
always win competitions with an ensemble
but actually sort of for fun um
Microsoft also submitted their best
single resnet model so this was not an
ensemble and just a single resnet model
actually beat all the other things from
all the other years so that's actually
pretty cool um yeah so that's that's the
best detector out
there so this is kind of a fun thing
right so this is a really so we we
talked about this idea of localization
as regression so this funny thing called
YOLO you only look once um actually
tries to pose the detection problem
directly as a regression problem so the
idea is that um we actually are going to
take our input image and we're going to
divide it into some spatial grid they
used 7 by S and then within each element
of that spatial grid we're going to make
a fixed number of Bing box predictions
um they use b equals 2 I think in most
of their experiments so then um within
each grid you're going to predict um
maybe two B bounding boxes so that's
four numbers you're also going to
predict um a a single score for how much
you believe that bounding box and you're
also going to predict a classification
score for each class in your data set so
then you can sort of take this this
detection problem and it ends up being
regression where your input is an image
and your output is this uh maybe 7x 7x 5
plus C tensor right so it's just a
regression problem and just train it end
to end with a CNN um so that's pretty
cool and it's it's sort of a neat
approach it's a little bit different
than these region proposal things that
we've seen before um of course sort of a
problem with this is that there's a
upper Bound in the number of outputs
that your model can have so that might
be a problem if your testing data has
many many more um uh ground truth boxes
than your training
data so this this YOLO detector um
actually is really fast it's actually
faster than faster rcnn um which is
pretty crazy but unfortunately it tends
to work a little bit worse so uh they
have this other thing called Fast YOLO
that I don't want to talk about
but right but ju so these are number
these are um MEAP numbers on the Pas on
one of the Pascal data sets that we saw
so you can see YOLO actually gets 64
that's pretty good and runs at 45 frames
per second so that this is obviously on
a on a powerful GPU but still that's
that's pretty much real time that's
amazing um there's also I don't want to
talk about
that right so then there's these
different versions of fast and faster
rcnn you can see that um these actually
pretty much all beat YOLO in terms of
performance but are quite a bit slower
um yeah so that's that's actually kind
of a neat Twist on the detection
problem um yeah so actually all these
all these different detection metric all
these different detection models that we
talked about today they all pretty much
have code up they're released
you should maybe consider using them for
your projects probably don't use rcnn
it's too slow fast RCN is pretty good
but requires mat lab um faster rcnn
there's actually a version of faster
rcnn that doesn't require mat lab it's
just Python and Cafe um I haven't
personally used it but it's something
you might want to try to use for your
projects I'm not sure how difficult it
is to get running um and YOLO is
actually I think maybe a good choice for
some of you for projects because it's so
fast that it might be easier to work
with if you have um not these really big
powerful gpus and they actually have
code up as
well um yeah so that's actually I got
through things a little bit faster than
I expected so is there any questions on
detection no oh yeah question so how big
are each of these models and then you
mention GPU how
big model yeah so in terms of mod like
model size it's pretty much it's about
the same as a classification model
because when when you're running on
bigger especially for faster rcnn right
CU your convolutions you don't really
introduce any more parameters the fully
connected layers are not really any more
parameters um you have a couple extra
parameters for the region proposal
network but it's basically the same
number of parameters as a classification
model all right I guess I guess we're
done a little early today
I