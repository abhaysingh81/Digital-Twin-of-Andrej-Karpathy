# YouTube Transcript: NfnWJUyUJYU

There is more seats on the side for people walking in late.
So just to make sure you are in CS231n
The deep learning on neural network class for visual recognition
Anybody in the wrong class? Okay, good.
Alright, so welcome and happy new year, happy first day of the winter break
the second offering of this class when
we have literally doubled our enrollment
and from a hundred eighty people last
time we offered to about 350 of you
signed up just a couple of words to do
to make us all legally covered we are
video recording this class so um you
know if you're uncomfortable about this
for today just go behind the camera or
go to a corner that the camera is not
gonna turn but we are going to send out
forms for you to fill out in terms of
allowing a video recording so so that's
that's just one bit of housekeeping so
um all right um my name is Faye Faye Lee
I'm a professor at the computer science
department so this class I'm co-teaching
with two senior graduate students and
one of them is here is Andre capaci
and ray can you just say hi to everybody
we have well I don't think Andre needs
too much introduction a lot of you
probably know his work follow his blog
his Twitter follower Andre has way more
followers than I do
he's very popular and also Justin
Johnson who is still traveling
internationally but will be back in a
few days so Andre and Justin will be
picking up the bulk of the lecture
teaching
and today I'll be giving the first
lecture but as you probably can see that
I'm expecting a newborn ratio
speaking of weeks so you'll see more of
Andra and Justin in lecture time we will
also introduce a whole team of TAS
towards the end of this lecture again
people who are looking for seats if you
go out of that door and come back there
is a whole bunch of seats on this side
okay so let's so this for this lecture
we're going to give an introduction of
the class the kind of problems we work
on and the tools we'll be learning so
again welcome to CS 231n this is a
vision class it's based on a very
specific modeling architecture called
neural network and even more
specifically mostly on convolution on
your network and a lot of you hear this
term maybe through a popular press an
article we or coverage we tend to call
this the deep learning network vision is
one of the fastest growing field of
artificial intelligence in fact cisco
has estimated and and we are on day four
of this by 2016 which we already have
arrived more than 85% of the internet
cyberspace data is in the form of pixels
or what they call multimedia so so we
basically have entered an age of vision
of images and videos and why why is it
so well partially and to a large extent
is because of the explosion of both the
internet as a carrier of data as well as
sensors we have more sensors than the
number of people on earth these days
every one of you is carrying some kind
of smartphones digital cameras and and
and and you know cars are running on the
street with cameras so so the sensors
have really enabled the explosion of
visual data in the on the internet but
visual data or pixel data is also the
hardest data to harness so if you have
heard my previous talks and some other
um talks by computer vision professors
we call this the dark matter of the
internet why is this the dark matter
just like the universe is consisted of
85% dark matter dark energy is these
matters energy that is very hard to
observe we can we can infer it by
mathematical models in the universe on
the Internet
these are the matters pixel data other
the data that we don't know we have a
hard time grasping the contents here's
one very very simple aspects for you to
consider
so today YouTube servers every 60
seconds we have more than 150 hours of
videos uploaded onto YouTube servers for
every 60 seconds think about the amount
of data there's no way that human eyes
can sift through this massive amount of
data and and make annotations labeling
it and and and and describe the contents
so think from the perspective of the
YouTube team or Google company if they
want to help us to search index manage
and of course for their purpose put
advertisement or whatever manipulate the
content of the data were at loss because
nobody can hand annotate this the only
hope we can do this is through vision
technology to be able to label the
objects find the things find the frames
you know locate where that basketball
video were Kobe Bryant's making like
that awesome shot and so so these are
the problems that we are facing today
that the massive amount of data and the
the challenges of the dark matter so
computer vision is a field that touches
upon many other fields of studies so I'm
sure that even sitting here sitting here
many of you come from computer science
but many of you come from
biology psychology are specializing
natural language processing or graphics
or robotics or you know medical imaging
and so on so as a field computer vision
is really a truly interdisciplinary
field what the problems we work on the
models we use touches on engineering
physics biology psychology computer
science and mathematics so just a little
bit of a more personal touch I am the
director of the computer vision lab at
Stanford in our lab we I work with
graduate students and postdocs and and
and even undergraduate students on a
number of topics and most dear to our
own research who some of them you know
that Andre just didn't come from my lab
a number of TAS come from my lab we work
on machine learning which is part a
percent of deep learning we work a lot
cognitive science and neuroscience as
well as the intersection between NLP and
speech so that's that's the kind of
landscape of computer vision research
that my lab works in so also to put
things in a little more perspective what
are the computer vision classes that we
offer here at Stanford through the
computer science department
clearly you're in this class yes 21 n
and so you some of you who have never
taken computer vision probably have
heard of comparison for the first time I
probably should have already done CS 131
that's an intro class of previous
quarter we offered and then and then
next quarter which normally is offer
this quarter but this year is a little
shifted there's an important graduate
level computer vision class called CS
231 a offered by Professor Silvio subber
si who works in robotics and 3d vision
and a lot of you asked us the question
that are these you know do these replace
each other this class CS 231n vs. CS
231 a and the answer is no and if you're
interested in a broader coverage of
tools and topics of computer vision as
well as some of the fundamental
fundamental topics that comes that
relates you to 3d vision robotic vision
and visual recognition you should
consider taking 231 a that is the more
general class 231 n which will go into
starting today more deeply focuses on a
specific angle of both problem and model
the model is your network and the angle
is visual recognition mostly but of
course they have a little bit of overlap
but that's the major difference and next
next quarter we also have possibly a
couple of a couple of advanced
seven-hour level class but you that's
still in the formation stage so you just
have to check the syllabus so that's the
the kind of computer vision curriculum
we offer this
you're at Stanford any questions so far
yes 131 is not a strict requirement for
this class but you'll soon see that if
you've never heard of computer vision
for the first time I suggest you find a
way to catch up because this class
assumes a basic level of understanding
of of of computer vision you can browse
the notes and so on all right okay so
the rest of today is that I will give a
very brief broad stroke history of
computer vision and then we'll talk
about 231n a little bit in terms of
the organization of the class actually
really care about sharing with you this
brief history of computer vision because
you know you might be here primarily
because of your interesting this really
interesting tool called deep learning
and this is the purpose of this class
we're offering you an in-depth look in
them and just journey through the the
what this deep learning model is but
without understanding the problem domain
without thinking deeply about what this
problem is it's very hard for you to to
go on to be an inventor of the next
model that really solves a big problem
in vision or to be you know developing
developing making impactful work in
solving a heart problem and also in
general problem domain and model the
modeling tools themselves are never
never fully decoupled they inform each
other and you see through the history of
deep learning a little bit that the
convolutional neural network
architecture come from the need to solve
a vision problem and
then vision problem helps the the deep
learning algorithm to evolve and back
and forth so it's really important to to
you know I want you to finish this
course and feel proud that your student
of computer vision and of deep learning
so you have this boost tool set and the
in-depth understanding of how to use the
tools that to to to to tackle important
problems so it's a brief history but
doesn't mean it's a short history so
we're gonna go all the way back to two
hundred thirty five hundred forty
million years ago so why why did I pick
this you know on the scale of the the
earth history this is a fairly specific
range of years well so I don't know if
you have heard of this but this is a
very very curious period of the Earth's
history and biologists call this the Big
Bang of evolution before five hundred
three four five hundred forty million
years ago the earth is a very peaceful
pot of water I mean it's pretty big pot
of water so we have very simple
organisms these are like animals that
just floats in the water and the way
they eat and now on a daily basis is you
know they just float and if some kind of
food comes by near their mouths or
whatever they just open the mouth and
grab it and we don't have too many
different types of animals but something
really strange happened around five
hundred forty million years suddenly
from the fossils we study there's a huge
explosion of species the biologists call
speciation like suddenly for some reason
something hit the earth that animals
start to diversify
get really complex and they they start
to yellow to to you start to have
predators and praise and then they have
all kind of tools to to survive and what
was the triggering force of this was a
huge question because people were saying
oh did you know another set of whatever
a meteoroid hit the earth or or you know
the environment change it turned out one
of the most convincing theory is that by
this guy called Andrew Parker of his a
modern zoologist in Australia from
Australia he studied a lot of fossils
and his theory is that it was the onset
of the ice so one one of the first
trilobite developed and I a really
really simple I it's almost like a
pinhole camera that just catches light
and make some projections and register
some information from the environment
suddenly life is no longer so mellow
because once you have the eye the first
thing you can do is you can go catch
food you actually know where food is
you're not just like blind and and
floating the water and once you can go
catch food guess what the food better
develop eyes and to run away from you
otherwise they'll be gone you know
you're you're so the first element we
had had eyes were like in a in a
unlimited buffet it's like working at
Google and it just like it has the best
time you know eating everything they can
but because of this onset of the eyes
what we whether the geologists realized
is that the the biological arms race
began every single animal needs to needs
to learn to develop things to survive or
to you know you you you suddenly have
praise and predators and and all this
and the speciation begin so that's when
vision become 540 million
years and not only vision began vision
was one of the major driving force of
the speciation or the the big ban of
evolution alright so so we're not going
to follow evolution for with too much
detail another big important work that
focus on in engineering of vision
happened around the Renaissance and of
course it's attributed to this amazing
guy
Leonardo da Vinci so before Renaissance
you know throughout human civilization
from Asia to Europe to India to Arabic
world we have seen models of cameras so
Aristotle has proposed the camera
through the leaves Chinese philosopher
Moses have proposed the camera through a
box with a hole but if you look at the
first documentation of really a modern
looking camera
it's called camera obscura obscura and
that is documented by Leonardo da Vinci
I'm not going to get into the details
but this is you know you get the idea
that there is some kind of lens or at
least a hole to capture lights reflected
from the real world and then there is
some kind of projection to capture the
information of the of the of the real
world image so that's the beginning of
the modern you know of engineering of
vision
it started with wanting to copy the
world and wanting to make a copy of the
visual world it hasn't got anywhere
close to wanting to engineer the
understanding of the visual world right
now we're just talking about duplicating
the visual world so that's one important
work to remember and of course after a
camera obscura that we we start to see
a whole series of successful you know
some film gets developed um you know
like kodak was one of the first
companies developing commercial cameras
and then we start to have camcorders and
all this another very important
important piece of work that i want you
to be aware of as vision student is
actually not an engineering work but a
sign science piece of science work that
starting to ask the question is how does
vision work in our biological brain no
we we now know that it took 540 million
years of evolution to get a really
fantastic visual system in mammals in
humans but what did evolution do during
this time what kind of architecture did
it develop from that simple trilobite
eye to today yours and mine well a very
important piece of work happened at
harvard by 2:00 at that time young to
very young ambitious postdoc Cuba and
visa what they did is that they used
awake but Anna sized cats and then there
was enough technology to build this
little needle called electrode to push
the electrode through into the the wall
that the skull is open into the brain of
the cat into an area what we already
know primary visual cortex primary
visual cortex is an area that neurons do
a lot of things for for visual
processing but before you go visa we
don't really know what primary visual
cortex is doing we just know it's one of
the earliest state other than your eyes
of course but earliest stage for visual
processing and there's tons and tons of
neurons working on vision and we really
ought to ought to know what this is
because
that's the beginning of vision visual
process in the brain so they they put
this electrode into the primary visual
cortex and interestingly this is another
interesting fact if I don't drop all my
stuff I'll show you
primary visual cortex the first stage or
second dependent where he come from I'm
being very very rough rough here first
state of your cortical visual processing
stage is in a back of your brain not
near your eye okay it's very interesting
because your olfactory cortical
processing is right behind your nose
your auditory is right behind your a
year but your primary visual cortex is
the farthest from your eye and another
very interesting fact in fact not only
the primary there's a huge area working
on vision almost 50% of your brain is
involved in vision vision is the hardest
and most important sensory perceptual
cognitive system in the brain you know
I'm not saying anything else does it
it's not useful clearly but you know it
takes nature this long to develop this
this sensory system and it takes later
this much real estate space to be used
for this system why because it's so
important and it's so damn hard that's
why we need to use this much place I'll
get back to human reason they were
really ambitious they want to know what
primary visual cortex is doing because
this is the beginning of our knowledge
for deep learning your network ah so
they were showing cats so they put the
cats in this room and they were
recording your activities and when I say
recording your activity they're tall
they're basically trying to see you know
if I put the the neural electrode here
like to the neurons to the neurons fire
when they see something so for example
if they show ah if they show cat
their ideas if I show this kind of fish
you know apparently at that time cats
eat fish rather than these beings um
with the cats new are like yellow you're
happy and start sending spikes and and
the funny thing here is a story of
scientific discovery a scientific
discovery takes both luck and care and
thoughtfulness they were shown as
catfish whatever Mouse flower it just
doesn't work the catch neuron in the
primary visual cortex was silent there
was no spiking are very little spiking
and they were really frustrated but the
good news is that there was no computer
at that time so what they have to do
when they show this cats these stimuli
is they have to use a slight projector
so they put a put a slide of a fish and
then wait till the neuron spike if the
neuron doesn't spike they take the slide
out and put in another slide and then
they notice every time they change slide
like this dislike you know the squarish
film I don't even remember if they use
glass or film but whatever the neural
spikes that's weird you know like the
actual mouse and fish and flower didn't
drive then you're excite the neuron but
the the movement of taking a slide out
or putting a sliding dip excite the nor
I can be the cat is thinking or finally
they're changing the new you know a new
object for me so it turned out there's
an edge that's created by this slide
that they're changing right the slide
whatever it's a square rectangular plate
and that moving edge drove or excited
the neurons so they're really chased
after that observation you know if they
were too frustrated or too careless they
would have missed that but they were not
they really they chase
after that and realize neurons in the
primary visual cortex are organized in
columns and for every column of the
neurons they like to see a specific
orientation of the of the of a stimuli
simple oriented bars rather than the
fish or Mouse you know I'm making this a
little bit of a simple story because
there are still numerous in primary
visual cortex we don't know what they
like they don't like simple oriented
bars but by large we human visual found
that the beginning of visual processing
is not a holistic fish or Mouse the
beginning of visual processing is simple
structures of the world edges oriented
edges and this is a very deep deep
implication to both neurophysiology and
neuroscience as well as engineering
modeling it's if later when we visualize
our deep neural network features will
see that simple simple of edge like
structure emerging from our from our
model and even though the discovery was
in a later 50s and early 60s they won a
Nobel a medical price for this work in
1981 so that was another very important
piece of work related to vision and
visual processing and so when did
computer vision begin that's another
interesting um that's another
interesting story his history the
precursor of computer vision as a modern
field was this particular dissertation
by Larry Roberts in 1963 it's called
block world he just as Hubel and Visa
were discovering that the visual world
in our brain is organized
by simple edge like structures Larry
Roberts as an early piece Commerce
science PhD students were trying to
extract these edge like structures in
images and and and and as a as a piece
of engineering work and in this
particular case his goal is that you
know bow you and I as humans can
recognize blocks no matter how it's
turned right like we know it's the same
block these two are the same block even
though the lighting changed and the
orientation changed and his conjuncture
is that just like people told us it's
the edges that define is the structure
the edges the edges define the shape and
they don't change rather than all these
interior things so Larry Roberts wrote a
PhD dissertation to just extract these
edges it's you know if you work as a PhD
student computer vision this is like you
know this is like undergraduate computer
vision we don't have being a PhD thesis
but that was the first precursor
computer vision PhD thesis on Larry
Roberts is interesting he kind of gave
up he's he's a working computer vision
afterwards and and went to DARPA and was
one of the inventors of the Internet so
you know he didn't do too badly by
giving up computer vision but we always
like to say that the birthday of
computer vision as a modern field is in
the summer of 1966 the summer of 1966
MIT artificial intelligence lab was
established before that actually for one
piece of history you should feel proud
as a Stanford student this there are two
pioneering artificial intelligence lab
established in the world in the early
1960s one by Marvin Minsky
at MIT one by John McCarthy at Stanford
at Stanford the compel the artificial
intelligence lab was established before
the computer science department and
professor John McCarthy who founded AI
lab is the one who is responsible for
the term artificial intelligence so
that's a little bit of a proud stanford
history but anyway we have to give MIT
this credit for starting the field of
computer vision because in the summer of
1966 a professor at MIT AI lab decided
it's time to solve vision you know so AI
was established we start to understand
you know first of all the logic and all
this and I think Lisp was probably
invented at that time but anyway vision
is so easy you open your eyes you see
the world how hard can this be let's
solve it in one summer
so especially MIT students are smart
right so the summer vision project is an
attempt to use our summer workers
effectively in a construction of a
significant part of a visual system this
was the proposal for that summer and
maybe they didn't use their summer work
effectively but in any case Kumbi
computer vision was not solved in that
summer since then they become the
fastest growing field of comparison and
AI if you go to today's premium computer
vision conferences CS call cvpr or icc v
we have like 2,000 to 2,500 researchers
worldwide attending this conference and
a very practical note for for students
if you are a good computer vision slash
machine learning students you will not
worry about jobs in Silicon Valley or
anywhere else so so it's it's actually
one of the most exciting field but that
was the birthday of computer vision
which means this year is the 50th
versary of computer vision that's a very
exciting year in computer vision I we
have come a long long way
okay so continue on the history of
computer vision this is a person to
remember David Marr he he was also at
MIT at that time working with a number
of a very influential computer vision
scientist Shimon Ullman Thomas Tommy
Poggio and David Marr himself died early
in 70s and he wrote a very influential
book called vision it's a very thin book
and David Marsh
thinking about vision he took a lot of
insights from neuroscience we already
said that Hubel and Wiesel give us the
concept of simple structure vision
starts with simple structure it didn't
start with a holistic fish or holistic
Mouse David Marr give us the next
important insight and these two insight
together is the beginning of deep
learning architecture is that vision is
hierarchical you know so human and Visa
said okay we start simple but human visa
didn't say we're any simple this visual
world is extremely complex in fact I
take a picture a regular picture today
with my iPhone there is I don't know my
iPhone's resolution let's suppose it's
like 10 mega megapixels the potential
combination of pixels to form a picture
in that is bigger than the total number
of atoms in the universe that's how
complex vision can be is it's it's
really really complex so human visit
oldest are simple David Marr told us
build a hierarchical model of course
David mark didn't tell us to build it in
a convolution on your network which we
will cover for the rest of the quarter
but his idea is
is this to represent or to think about
an image we think about it in several
layers the first one he thinks we should
think about the edge image which is
clearly an inspiration
it took the inspiration from human visa
and he personally call this the primal
sketch it's you know the name is
self-explanatory and then you think
about two and half D this is where you
start to reconcile your 2d image with a
3d world you recognize there is layers
right on you know I look at you right
now
I don't think half of you only has a
head and a neck even though even though
that's all I see but there is I know
you're included by the row in front of
you and this is the fundamental
challenge of vision we have an ill-posed
problem to solve nature had a ill-posed
problem to solve because the world is 3d
but the imagery on our retina is 2d
Nature solved it by first a hardware
trick which is to ice it did I use one
eye but then there's going to be a whole
bunch of software trick to merge the
information of the two eyes and all this
so the same thing with computer vision
we have to solve that two and half the
problem and then eventually we have to
put everything together so that we
actually have a good 3d model of the
world why do we have to have a 3d model
of the world because we have to survive
navigate manipulate the world when I
shake your hand I really need to know
how to you know extend out my hand and
grab your hand in the right way that is
a 3d modeling of the world otherwise I
won't be able to grab your hand in the
right way when I pick up a mug the same
thing so so that's a that's a that's
David Marsh architecture for visual it's
a very high-level abstract architecture
it doesn't really inform us exactly what
of mathematical modeling we should use
it doesn't inform us of the learning
procedure and it really doesn't inform
as of the the inference procedure which
we were getting to through the deep
learning network architecture but that's
the that's the high-level view and it's
an important it's an important concept
to learn in in vision and we call this
the representation um a couple of really
important work and this is a little bit
Stanford centric to just show you as
soon as David Marr are laid out this
important way of thinking about vision
the first wave of visual recognition
algorithms went after that 3d model
because that's the goal right like no
matter how you represent the the stages
the goal here here is to reconstruct a
3d model so that we can recognize object
and this is really sensible because
that's what we go to the world and do so
both of these two influential work comes
from Palo Alto one is from Stanford one
is from SR I so uh Tom Binford was a
professor at Stanford AI lab and he had
his student Rodney Brooks proposed one
one of the first so-called generalized
cylinder model I'm not going to get into
the details but the idea is that the
world is composed of simple shapes like
cylinders blocks and then any real-world
object is just a combination of these
simple shapes given a particular viewing
angle and that was a very influential
visual recognition model in the 70s and Romney Brook went on to become a
director of MIT's AI lab and he was
also a founding member of the irobot
company and
Roomba and all this so he continued very
influential of AI work
another interesting model coming from
local uh Stanford Research Institute I
think SR I is a across the street from
El Camino is this pictorial structure
model is very similar it focused it has
less of a 3d flavor but more of a
probabilistic flavor is that the objects
are made of still simple parts like a
person's head is made of eyes and nose
and mouth and the parts were connected
by Springs allowing for some deformation
so this is getting a sense of okay we
recognize the world not every one of you
have exactly the same eyes in the
distance between the eyes we allow for
some kind of variability so this concept
of variability start to get introduced
in a model like this and using models
like this you know the the reason I want
to show you this is to see how simple
that the work was in 80s this is one of
the most influential model in the 80s
are recognizing real world object and the
entire paper of real world object is
these shaving razors and but using the
edges and and simple shapes formed by
the edges to to recognize this by by
develop another another Stanford
Graduate so that's that's a that's kind
of the ancient world of computer vision
we have been seen black and white or
even synthetic images starting the 90s
we finally start to move into like
colorful images of real world it was a
big change again a very very influential
work
here it's not particularly about
recognizing an object is about how
only like carve out an image into
sensible parts right so if you enter
this room there's no way your visual
system is telling you oh my god I see so
many pixels right you immediately have
group things you see heads heads heads
chair chair chair a stage platform piece
of furniture and all this this is called
perceptual grouping perceptual grouping
is one of the most important problem in
vision biological or artificial if we
don't know how to how to solve the
perceptual grouping problem we're going
to have a really hard time to deeply
understand the visual world and and you
will learn towards the end of this this
class this course a problem is
fundamental as this it's still not
solved in computer vision even though we
have made a lot of progress before deep
learning and after deep learning we're
still grasping the final solution of a
problem like this so so this is again
why I want to give you this introduction
to for you to be aware of the deep
problems in vision and also the the
current state in the the challenges in
vision we did not solve all the problem
in vision despite whatever the news says
you know like we're far from developing
terminators who can do everything yet so
this piece of work is called normalized
cut is one of the first computer vision
work that takes real-world images and
tries to solve a very fundamental
difficult problem and titania Malick is
a senior computer vision researcher
now professor at Berkeley also Stanford
Graduate and you can see the results are
not that great um are we going to cover
any segmentation in this class for me
when we might right you see we are
making progress but this is the
beginning of that another very
influential work that I want to
I want to bring out and pay tribute so
for even though these work were not
covering them in the rest of the course
but I think it as a vision student it's
really important for you to be aware of
this because not only introduces the
important problem we want to solve it
also gives you a perspective on the
development of the field this work is
called village owns face detector and
it's very dear to my heart because as a
graduate student fresh graduate student
at Cal Tech it's the full of the first
papers I read as a graduate student when
I enter the lab and I didn't know
anything that my advisor said read this
amazing piece of work that you know
we're all trying to understand and then
P by the time I graduated from Cal Tech
this very work is transferred to the
first smart digital camera by Fujifilm
in 2006 as the first digital camera that
has a face detector so from a transfer
point point a technology transfer point
of view it was extremely fast and it was
one of the first successful high-level
visual recognition algorithm that's
being used by consumer product so this
work just learns to detect faces and
faces in a wild it's no longer you know
simulation data or very contrived data
these are any pictures and and again
even though it didn't use a deep
Learning Network it has a lot of the
deep learning flavor the features were
learned you know the algorithm learns to
find features simple features like these
black and white filter features that can
give us the best localization of faces
so this is a very influential piece of
work it's also one of the first computer
vision work that is deployed on a a
computer and can run real time before
that compare vision
algorithms were very slow the paper
actually is called real-time face
detection it was granted
Pentium 2 chips I don't know if anybody
remember that kind of chip but it was on
a slow chip but nevertheless it run real
time so that was another very important
bit of work and also one more thing to
point out around this time this is not
the only work but this is a really good
representation around this time computer
the focus of computer vision is shifting
remember that David Marr and the early
Stanford work was trying to model the 3d
shape of the object now we're shifting
to recognizing what the object is we
lost a little bit about can we really
reconstruct these faces or not there is
a whole branch of computer vision
graphics that continue to work on that
but a big part of computer vision is not
at this time around the turn of the
century is focusing on recognition
that's bringing computer vision back to
AI and today the most important part of
the computer vision work is focused on
these cognitive questions like
recognition and AI questions um another
very important piece of work is starting
to focus on features so around the time
of face recognition people start to
realize it's really really hard to
recognize an object by describing the
whole thing like I just said you know I
see you guys
heavily included I don't see the rest of
your torso I really don't see any of
your legs other than the first row but I
recognize you and I can infer you as an
object so so people start to realize gee
it's not necessarily that global
shape that we have to go after in order
to recognize an object maybe it's the
features if we recognize the important
features on an object we can go a long
way and it makes a lot of sense think
about evolution right if you're out
hunting you don't need to recognize that
Tigers full body and shape to decide you
need to run away you know just a few
patches of the fur of the tiger through
the leaves probably can alarm you enough
so so we need to vision as quick
decision-making based on vision is
really quick a lot of this happens on
important features so this work cost
sift by devil Oh again you saw that name
again is about learning important
important features on an object and once
you learn these important features just
a few of them on an object you can
actually recognize this object in a
totally different angle on a totally
cluttered scene so up to deep learnings
resurrection in that 2010 or 2012 for
about 10 years the entire field of
computer vision was focusing on using
these features to build models to
recognize objects and things and we've
done a great job we've gone a long way
one of the reasons deep learning network
uh was became more more convincing to a
lot of people is we will see that the
features that a deep learning network
learns is very similar to these
engineered features by brilliant
engineers so it's kind of confirmed even
though you know in needed we need a
develope to first tell us this features
work and then we start to develop better
mathematical models to learn these
features by itself but they confirmed
each other so so the historical you know
importance of this work should not be
diminished
they this work is the intellectual
foundation for us one of the
intellectual foundation for us
to realize that how critical or how
useful these deep learning features are
when we learn them uh I'm going to skip
this work and just briefly say because
of the features that they will owe and
meaning other researchers taught us we
can use that to to learn that Scene
Recognition and around that time the
machine learning tools we use mostly is
either graphical models or support
vector machine and this is one
influential work on using support vector
machine and kernel models to recognize
the sink but I'll I'll be brief here and
then one almost one last model before
deep learning model is this feature or
feature based model called deformable
part model is where we learn parts of an
object like parts of a person and we
learn how to configure each other well
they come they configure in space and
use a support vector machine kind of
model to recognize objects like humans
and bottles around this time that's 2009
2010 the field of computer vision is
matured enough that we're working on
these important and hard problem like
recognizing pedestrians and recognizing
cars they're no longer contrived problem
something else was needed its
benchmarking because as a field advanced
enough if we don't have good benchmark
then everybody's just published in
papers on a few set of images and it's
really hard to really set global
standard so one of the most important
benchmark is called Pascal vo C object
recognition benchmark it's by a European
it's a European effort that researchers
put together at tens of thousands of
images from 20 classes of objects and
these are
one example per per object like Cat
Scouts cows maybe no cats dogs cows
airplanes bottles you know horses trains
and all this and then we used and then
annually our computer vision researchers
and labs come to compete on the object
recognition task for a Pascal object
recognition challenge and in over the
past you know like through the years the
the performance just keeps increasing
and that was when we start to feel
excited about the progress of the field
at that time here's a little bit of more
a closer story close to us is that my
lab and my students were thinking you
know the real world is not about twenty
objects the with real world is a little
more than twenty objects so following
the work of Pascal visual object
recognition challenge we put together
this massive massive project or imagenet
some of you might have heard of image
net in this class you will be using a
tiny portion of image that in some of
your assignments that image that is a
data set of 50 million images all
clinged by hands and annotated over
20,000 object classes door it's not
graduate student who cleaned it it's
that that would be very scary it's
Amazon Mechanical Turk platform the
crowdsourcing platform and having said
that graduate student also suffered for
from you know putting together this this
platform but it's a very exciting data
set and we started we started to put
together competitions annually called
image that competition for object
recognition and for example a standard
competition of image classification by
image that is a thousand object classes
over almost 1.5 million images and
algorithms compete on the performance so
actually I just heard somebody was on
the social media was referring image
that challenge as the Olympics of
computer vision I was very flattering
but um but here is something that here's
bringing as close to the history making
of deep learning so in in a so the image
step challenge started in 2010 that's
actually around the time Pascal you know
we're colleagues they told us they're
going to start to phase out their
challenge of twenty objects so we faced
in the thousand object image the
challenge and y-axis is error rate and
we start to we started with very
significant error and of course you know
every year the error decreased but
there's a particular year that error
really decreased it was cutting half or
almost is 2012 2012 is the year that the
winning architecture of image that
challenge was a convolutional neural
network model and we'll talk about it
convolutional neural network was not
invented in 2012 despite how all the
news make it sound like it's the newest
thing around the block it's not it was
invented back in the 70s or 80s
but having a convergence of things we'll
talk about convolutional neural network
showed its massive power as a high
capacity end to end training
architecture and won the image they're
challenged by a huge margin and that was
you know a quite a historical moment
from a math mathematical point of view
nothing it wasn't that new but from an
engineering and an solving real-world
point of view this was a historical
moment that that piece of work was
covered by you know New York Times and
all this this is the onset this is the
beginning of the deep learning
revolution if you call it
and this is the premise of this class so
at this point I'm gonna switch so we
went through a bit of brief history of
computer vision for 540 million years
and now I'm going to switch to the
overview of this class is there any
other questions ok all right so um we've
talked about even though it was kind of
overwhelming we talked a lot about many
different tasks in computer vision CS
231 n is going to focus on the visual
recognition problem also by enlarge
especially through most of the
foundation lecture we're going to talk
about the image classification problem
but now you know everything we talked
about is going to be based on that image
that classification setup we will we
were getting to other visual recognition
scenarios but the image classification
problem is the main problem we will
focus on in this class which means
please keep in mind visual recognition
is not just the image classification
right there was 3d modeling there was
perceptual grouping and segmentation and
all this but that's that's what we'll
focus on and I don't need to convince
you that just even application wise
image classification is extremely useful
problem in
you know big big commercial internet
companies a point of view to start up
ideas you know you want to recognize
objects you want to recognize food you
want to do online shop mobile shopping
you want to sort your albums so image
classification is is is can be a bread
and butter a task for many many
important problems um there is a lot of
problem that's related to image
classification and today I don't expect
you to understand the differences but I
want you to hear that throughout this
class we'll make sure you learn to
understand the neurons in the the
details of different flavours of visual
recognition what is image classification
what's object detection
what's image captioning and these have
different flavors for example you know
while image classification my focus on
the whole big image object detection by
tell you where things exactly are like
where the car is the pedestrian or the
hammer and and where the the
relationship between objects and so on
so there are nuances and and details
that you will be learning about in this
class and I already said CNN or
convolutional neural network is one type
of deep learning architecture but it's
the overwhelmingly successful deep
learning architecture and this is the
architecture we will be focusing on and
to just go back to the image that
challenge ah so I said the historical
year is 2012 this is the year that Alex
Khrushchev ski and his advisor geoff
hinton proposed this this convolutional
neural network I think it's a seven
layer convolutional neural network to
win the image that challenge model
before this year it was a shift feature
plus
a support vector machine architecture
it's still hierarchical but it doesn't
have that flavor of end to end learning
and fast forward to 2015 the winning
architecture is still a convolutional
neural network it's a hundred fifty one
layers by by Microsoft Asia research
researchers and it's covering the
residual net right is that could the
residual net so I'm not so sure if we're
going to cover that definitely don't
expect to know every single layer what
they do actually they repeat so it's not
that hard but but but every year since
2012 the winning architecture of image
net challenge is a deep learning based
architecture so like I said I also want
you to respect history um
CNN is not invented overnight there is a
lot of influential players today but you
know there are a lot of people who build
the foundation I actually I don't have
the slides one important name to
remember is kunihiko fukushima kunihiko
fukushima it was a Japanese computer
scientist who build a model Konya
cognitum and that was the beginning of
the the neural network architecture and
yellow kun is also a very influential
person and he's really his the the
groundbreaking work in my opinion of
young ku was published in the 1990s so
that's when mathematicians and which
geoff hinton Yellen Cruz PhD advisor was
involved worked out the back propagation
learning strategy which if this work
didn't mean anything
Andrei will tell you in a couple of
weeks so but but the the mathematical
model was worked out in the 80s and the
90s and this was a yellow Coon was
working for Bell
laughs at AT&T which is a amazing place
at that time there's no Bell Labs today
anymore
that they were working on really
ambitious projects and he needed to
recognize digits because eventually that
product was shipped to banks in the u.s.
post office to recognize zip codes and
checks and he constructed this
convolutional neural network and this is
where he he's inspired by Hubel and
Wiesel he starts by looking as simple
edge like structures of an image it's
not like the whole letter a it's really
nice just edges and then layer by layer
he he you know he filters these edges
pull them together filters pool and then
the build this architecture 2012 when
Alex Khrushchev ski and geoff hinton
used almost exactly the same
architecture to participate in a in the
in the image net challenge almost there's
very few changes but that become the
winning architecture of this so what I
will tell you more about the detail
changes there is the capacity that the
model did grow a little bit because
Moore's Law helped us there's also a
very a very detailed function that
changed a little bit of a shape from a
sigmoid row to a more rectified linear
shape but whatever there's a couple of
small changes but really by enlarge
nothing had changed mathematically but
two important things did change and that
Grove the deep learning architecture
back into into its Renaissance one is
like I said Moore's law and hardware
hardware made a huge difference because
these are high extremely high capacity
models when Gallagher was doing this
it's just painfully slow because of the
the bottleneck of computation he
couldn't build this model too big
at once you cannot build it too big it
cannot fully realize its potential you
know the from machine learning
standpoint there's overfitting and all
these problems you cannot solve but now
we have a much faster and bigger
transistor not transistors bigger
capacity microchips and GPUs from Nvidia
Nvidia made a huge difference in deep
learning history that we can now train
these models in a reasonable amount of
time even if they're huge another thing
I think we do need to take credit for is
data the availability of data that was
the big data data itself is just you
know it doesn't mean anything if you
don't know how to use it but in this
deep learning architecture data become
the driving force for a high capacity
model to enable the end-to-end training
and to help avoid overfitting when you
have enough data so you know so you if
you look at the number of pixels that
machine learning people had in 2012
versus yellow ku had in 1998 it's a huge
difference orders of magnitude so so
that was that's so this is the focus of
231 n but we'll also go
it's also important one last time I'm
gonna drilling this idea that visual
intelligence does go beyond object
recognition I don't want any of you
coming out of this course thinking we've
done everything you know we've saw
vision and if it's the challenge defined
the entire space of visual recognition
it's not true there are still a lot of
cool problems to solve for example you
know dense labeling of an entire scene
with perceptual groupings I know where
every single pixel belong to that's
still an ongoing problem combining
recognition with 3d is a really there's
a lot of excitement happening at the
intersection of vision and robotics and
this is this is definitely one area of
that and then anything to do with motion
affordance and and and this is another
big open area of research there is a I
put this here because Justin is heavily
involved in this in this work you know
beyond just putting labels on a sink you
actually want to deeply understand a
picture what people are doing what are
the relationship between objects and we
start getting into the the relation
between objects and this is the ongoing
project called visual genome in my lab
that justin and a number of my students
are involved and this goes far beyond
image classification we we talked about
and what is one of our Holy Grails well
one of the Holy Grails of computer
vision is to be able to tell a story of
a scene right so think about you as a
human you open your eyes the moment you
open your eyes you're able to describe
what you see and in fact in psychology
experiments we find that even if you
show people this picture for only 500
milliseconds that's literally half of a
second people can write essays about it
we pay them $10 an hour so they did
every it wasn't that long but you know I
figure if we took a little longer a
little more money they'd probably write
longer essays but the point is that our
visual system is extremely powerful we
can tell stories and I would dream this
is my challenge to undress a
dissertation that can we give you give a
computer one picture and outcomes a
description like this you know and we're
getting there you'll see work that you
give the computer one picture it gives
you one sentence or you give the little
computer one picture it gives you a
bunch of short sentences but we're not
here yet but
that's one of the Holy Grail and another
Holy Grail is continuing this continuing
this Atlas I think is summarized really
well by Audrey's blog is you know take a
picture like this right
there's the stories are so refined
there's so much nuance in this picture
that you get to enjoy not only you
recognize the global sea it would be
very boring if all computer can tell you
is man man man room
you know room scale mirror whatever
cabinet Locker that's it you know here
you recognize who they are you recognize
the trick Obama is doing you recognize
the kind of interaction you recognize
the humor you recognize there's just so
much nuance that this is what visual
world is about we use our ability to of
visual understanding to not only survive
navigate manipulate but we use it to
socialise to entertain to understand to
learn the world and this is where vision
you know the grand goals of vision is so
and and I don't need to convince you
that computer vision technology will
make our world a better place
despite some scary talks out there you
know even going on today in industry as
well as research world we're using
computer vision to build better robots
to save lives to go deep exploring and
all this now ok so I have like what two
minutes three minutes five minutes left
great time let me introduce the team and
Andre and Justin are the co instructors
with me TAS please stand up when to say
hi to everybody can you like to say your
name quickly and you're like what year
and just don't give a speech but yeah
start start with you your name
what so so these are the heroes behind
the thing and so please stay in touch
with us there two really the best way
and almost I almost wanted to say the
only way and I'll tell you what's the
exception is stay in touch through
Piazza as well as the staff meeting list
anything course related please please do
not send any of us personal email
because I'm just gonna say this
if you don't hear replies or your issue
is not taken care of because you send a
personal email I'm really sorry because
this is a 300 plus people class hour
this mailing list actually tags our
email and and and and help us to process
the only time I respect you to send a
personal email mostly to me and Andre
and Justin is confidential personal
issues you know and I understand if you
don't want that to be broadcasted to a
team of 10 TAS that's okay
but that should be really really minimal
at the only time that you send us an
email and also you know just again I'm
going on my turn to leave for a few
weeks starting the end of January so so
please if you decide you just want to
send an email to me and it's my like
due day for her baby
I'm not likely going to reply you
promptly sorry about that
priorities so a couple words about our
philosophy out this is we're not going
to get into the details we really want
this to be a very hands-on project and
this is really I give a lot of credit to
Justin and Andre they are extremely good
at walking through these hands-on
details with you so that when you come
out of this class you not only have a
high level understanding but you have a
thorough you have a really good ability
to to build your own deep learning code
we want you to be exposed to
state-of-the-art material you're going
to be learning things really that's as
fresh as 2015 and it'll be fun
you get to do things like this now not
all the time but you know like turn a
picture into Van Gogh or or this weird
and kin thing so it will be a fun class
in addition to all the important tasks
you are you you learn uh we do have
grading policies these are all on our
website I'm not going to eat to rate
this again one thing I want to be very
clear I'm actually two things what is
late policy you are grownups we treat
you like grown-ups we do not take
anything at the end of the courses who
my professors want me to go to this
conference and I have to have like three
more late days no you are responsible
for using your total late days you have
seven late days you can use them in
whatever way you want with zero penalty
beyond those you have to take a penalty
again if there's like really really
exceptional medical family emergency
talk to us on an individual basis but
anything else conference deadlines other
final exams
you know like missing cat
or whatever is we we we budgeted that
into the seven days
another thing is honor code this is one
thing I have to say with a really
straight face you are enough such a
privileged institution you're you are
grownups
I want you to be responsible for honor
code every single Stanford student
taking this class should know the honor
code if you don't there's no excuse you
should go back
we take collaboration extremely
seriously I almost hate to say that's
statistically given a class this big
we're going to have a few cases but I
also want you to be an exceptional class
even with the size this big we do not
want to see anything that infringes on
academic honor code so read the
collaboration policies and respect that
this this is really respecting yourself
ah I think I'm done with you know these
pre-requisite you can you can read it I'm done
with anything I want to say is there any
burning questions that you feel it's
worth asking yes a good question Andre
do you have
midterm move a bit of everything which
means they haven't figured it out
yeah we will give you sample meters okay
all right
thank you welcome to the class
the water's going