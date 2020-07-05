# COVID-19 Mathematical Modelling Paper Video

![video_sample.gif](media/gifs/video_optimised.gif)

This work-in-progress repository contains code to create a series of videos that explain the mathematicall
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

If there are issues with the `calligra` package, edit `tex_template.tex` and comment out the line  `\usepackage{calligra}`.

## Usage

### Create MP4

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