[Sitemap](/sitemap/sitemap.xml)

[Open in
app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page
---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign
in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkarpathy.medium.com%2Ficml-
accepted-papers-institution-stats-bad8d2943f5d&source=post_page---
top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---
top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=---top_nav_layout_nav-----------------------
new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---
top_nav_layout_nav-----------------------------------------)

Sign up

[Sign
in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fkarpathy.medium.com%2Ficml-
accepted-papers-institution-stats-bad8d2943f5d&source=post_page---
top_nav_layout_nav-----------------------global_nav------------------)

![Unknown
user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# ICML accepted papers institution stats

[![Andrej
Karpathy](https://miro.medium.com/v2/resize:fill:64:64/0*8ldFdx9B6FhSkQmV.jpeg)](/?source=post_page
---byline--bad8d2943f5d---------------------------------------)

[Andrej Karpathy](/?source=post_page---byline--
bad8d2943f5d---------------------------------------)

2 min read

·

May 24, 2017

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fbad8d2943f5d&operation=register&redirect=https%3A%2F%2Fkarpathy.medium.com%2Ficml-
accepted-papers-institution-stats-
bad8d2943f5d&user=Andrej+Karpathy&userId=ac9d9a35533e&source=---header_actions
--bad8d2943f5d---------------------clap_footer------------------)

\--

8

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbad8d2943f5d&operation=register&redirect=https%3A%2F%2Fkarpathy.medium.com%2Ficml-
accepted-papers-institution-stats-bad8d2943f5d&source=---header_actions--
bad8d2943f5d---------------------bookmark_footer------------------)

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dbad8d2943f5d&operation=register&redirect=https%3A%2F%2Fkarpathy.medium.com%2Ficml-
accepted-papers-institution-stats-bad8d2943f5d&source=---header_actions--
bad8d2943f5d---------------------post_audio_button------------------)

Share

The accepted papers at ICML have been
[published](https://2017.icml.cc/Conferences/2017/AcceptedPapersInitial). ICML
is a top Machine Learning conference, and one of the most relevant to Deep
Learning, although NIPS has a longer DL tradition and ICLR, being more
focused, has a much higher DL density.

### Most mentioned institutions

I thought it would be fun to compute some stats on institutions. Armed with
Jupyter Notebook and regex, we look for all of the institution mentions, add
up their counts and sort. Modulo a few annoyances:

  * I manually collapse e.g. “Google”, “Google Inc.”, “Google Brain”, “Google Research” into one category, or “Stanford” and “Stanford University”.
  * I only count up one unique mention of an institution on each paper, so if a paper has 20 people from a single institution this gets collapsed to a single mention. This way we get a better understanding of which institutions are involved on each paper in the conference.

In total we get 961 institution mentions, 420 unique. The top 30 are:

    
    
    #mentions institution  
    ---------------------  
           44 Google  
           33 Microsoft  
           32 CMU  
           25 DeepMind  
           23 MIT  
           22 Berkeley  
           22 Stanford  
           16 Cambridge  
           16 Princeton  
           15 None  
           14 Georgia Tech  
           13 Oxford  
           11 UT Austin  
           10 Duke  
           10 Facebook  
            9 ETH Zurich  
            9 EPFL  
            8 Columbia  
            8 Harvard  
            8 Michigan  
            7 UCSD  
            7 IBM  
            7 New York  
            7 Peking  
            6 Cornell  
            6 Washington  
            6 Minnesota  
            5 Virginia  
            5 Weizmann Institute of Science  
            5 Microsoft / Princeton / IAS

I’m not quite sure about “None” (15) in there. It’s listed as an institution
on the ICML page and I can’t tell if they have a bug or if that’s a real cool
new AI institution we don’t yet know about.

### Industry vs. Academia

To get an idea of how much of the research is done at industry, I took the
counts for the largest industry labs (DeepMind, Google, Microsoft, Facebook,
IBM, Disney, Amazon, Adobe) and divide by the total. We get 14%, but this
doesn’t capture the looong tail. Looking through the tail, I think it’s fair
to say that

> about 20–25% of papers have an industry involvement.

or rather, approximately three quarters of all papers at ICML have come
entirely out of Academia. Also, since DeepMind/Google are both Alphabet, we
can put them together (giving 60 total), and see that

> 6.3% of ICML papers have a Google/DeepMind author.

It would be fun to run this analysis over time. Back when I started my PhD
(~2011), industry research was not as prevalent. It was common to see in
Graphics (e.g. Adobe / Disney / etc), but not as much in AI / Machine
Learning. A lot of that has changed and from purely subjective observation,
the industry involvement has increased dramatically. However, Academia is
still doing really well and contributes a large fraction (~75%) of the papers.

cool!

**_EDIT 1_** _: fixed an error where previously the Alphabet stat above read
10% because I incorrectly added the numbers of DM and Google, instead of
properly collapsing them to a single Alphabet entity.  
_**_EDIT 2_** _: some more discussion and numbers on_[
_r/ML_](https://www.reddit.com/r/MachineLearning/comments/6d2zco/r_icml_2017_accepted_papers/)
_thread too._

[ Machine Learning](https://medium.com/tag/machine-learning?source=post_page
-----bad8d2943f5d---------------------------------------)

[![Andrej
Karpathy](https://miro.medium.com/v2/resize:fill:96:96/0*8ldFdx9B6FhSkQmV.jpeg)](/?source=post_page
---post_author_info--bad8d2943f5d---------------------------------------)

[![Andrej
Karpathy](https://miro.medium.com/v2/resize:fill:128:128/0*8ldFdx9B6FhSkQmV.jpeg)](/?source=post_page
---post_author_info--bad8d2943f5d---------------------------------------)

## [Written by Andrej Karpathy](/?source=post_page---post_author_info--
bad8d2943f5d---------------------------------------)

[60K followers](/followers?source=post_page---post_author_info--
bad8d2943f5d---------------------------------------)

·[186 following](/following?source=post_page---post_author_info--
bad8d2943f5d---------------------------------------)

I like to train deep neural nets on large datasets.

[Help](https://help.medium.com/hc/en-us?source=post_page-----
bad8d2943f5d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----
bad8d2943f5d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
bad8d2943f5d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-
medium-959d1a85284e?source=post_page-----
bad8d2943f5d---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----
bad8d2943f5d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-
policy-f03bf92035c9?source=post_page-----
bad8d2943f5d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page
-----bad8d2943f5d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-
service-9db0094a1e0f?source=post_page-----
bad8d2943f5d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----
bad8d2943f5d---------------------------------------)

