## Scraping Ted Talks using Scrapy


Setup environment on OSX:

```
conda create -n scrapyenv python=2.7 scrapy service_identity pillow
source activate scrapyenv
```

Scrapy requires python 2.7.  `pillow` and `service_identity` are not absolutely necessary but could save some trouble down the road.

Start a new project:

```
scrapy startproject tedtalk
```
