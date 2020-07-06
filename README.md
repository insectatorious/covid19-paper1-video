# COVID-19 Mathematical Modelling Paper Video

![video_sample.gif](media/gifs/video_optimised.gif)

This work-in-progress repository contains code to create a series of videos that explain the mathematical
modelling in our paper [Simulating human interactions in supermarkets to measure the risk of COVID-19 contagion at scale](https://arxiv.org/abs/2006.15213).

The final version will be hosted on YouTube.
Until then, all videos and gifs will live here.

 MP4 | GIF
-----|----
[Link](media/videos/basket_distributions/1440p60/BasketDistributions.mp4) | [Link](media/gifs/video_optimised.gif)

Video produced using the [`Manim`](https://github.com/3b1b/manim) library made popular by the videos on the YouTube channel [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw).

## Dependencies

Python dependencies are listed under `requirements.txt`.
Additional requirements like LaTeX and associated packages are to be installed separately (see below).

### Mac OS 

#### Install LaTeX

To install the minimal version (using `brew`)
```commandline
brew cask install basictex
```

Note that LaTeX is only needed when text is used (via `TextMobject`).
If the video only has shapes then it is not required.

#### Install LaTeX Packages
```commandline  
sudo tlmgr install collection-fontsrecommended standalone preview dsfont doublestroke relsize calligra dvisvgm fontaxes fontawesome lato # collection-fontsextra
```

If there are issues with the `calligra` package, edit `tex_template.tex` (located inside `manim` lib) and comment out the line  `\usepackage{calligra}`.

## Usage

### Create MP4

#### Low Quality Render
This is useful when developing as it is significantly faster than the high quality render (seconds vs minutes). 

```commandline
manim covid19-paper1-video/basket_distributions.py -apl
```

#### Render Video Subset
Also useful when developing as it allows for a quick preview of a subset of all the animations.

```commandline
manim covid19-paper1-video/basket_distributions.py -apl -n 23,30
```
Here the preview only renders animations 23 to 30.
`-n 23` can also be used to render from animation 23 onward.

#### High Quality Render

```commandline
manim covid19-paper1-video/basket_distributions.py -a
```

### Create GIF
First create MP4 then convert using `ffmpeg`. 
Directly exporting to GIF was part of the library, but [this has been removed](https://github.com/3b1b/manim/commit/61bb4944fad2ee889145bbf8a3253fb07c71bf7d#comments).

```commandline
ffmpeg -i video.mp4 -vf scale=600:-1 -r 20 -f image2pipe -vcodec ppm - | convert -delay 5 -loop 0 - video.gif
```

### Optimise GIF 

The GIF may be extremely large and can usually be optimised heavily.
In some cases the optimised file can be 20% of the original file size. 
 
```commandline
gifsicle --colour 256 -O3 video.gif -o video_optimised.gif
```

## Things to keep in mind

`manim` is not a video editor. [According to Grant himself,](https://www.reddit.com/r/3Blue1Brown/comments/c1omxg/euler_wave_requires_a_lot_more_chiseling_and/ereqrub/) `manim` should only be used for mathematical animations. 
>  don't try to do everything in manim; use a video editor for as much as possible, and manim for the math things.
