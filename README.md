# SciHub Downloader Workflow for Alfred (MacOS)

SciHub article retrieval made easy. Simply paste a DOI link (multiple formats acceptable) into the Alfred command line, and instantly have the file downloaded to your Downloads folder.

If the searched article is somehow unavailable in one domain of SciHub, the script will look for it on multiple domains.

![Preview GIF](preview.gif)

<hr>

## Installation

```
pip install beautifulsoup4
pip install requests
```

## Usage

Just paste the target DOI link or index.

Below are all acceptable input formats:

```
https://doi.org/10.1016/j.socscimed.2017.03.024
doi.org/10.1016/j.socscimed.2017.03.024
/10.1016/j.socscimed.2017.03.024
10.1016/j.socscimed.2017.03.024
```

Then hit `Enter` to download the retrieved article straight away (if it is found), or `CMD + Enter` to go to the SciHub page instead.

## Two Different Modes

As you notice in the workflow, there are two versions of the command, `sci` and `quicksci`.

`sci` will search for the article and wait till it returns a result via the Alfred Script Filter object, meaning you have to wait for the result (but it usually should not take more than a few seconds).

`quicksci` will allow you to simply enter a DOI and enter. Everything else will happen in the background and you will not need to wait for a result. The drawback of using this is that sometimes you might want to see the returned result as confirmation that you are retrieving the right article.
