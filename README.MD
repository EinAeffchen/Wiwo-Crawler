#Article Crawler for German News Site "Wirtschaftswoche"

This a little project of mine to learn the usage of the [Scrapy library](https://doc.scrapy.org/en/latest/).
It downloads all articles from [wiwo.de](https://www.wiwo.de/) and saves them in a general output file.

## Getting Started

```
git clone https://github.com/EinAeffchen/Wiwo-Crawler.git
cd .\Wiwo-Crawler
scrapy crawl wiwo_all -o "*.json/*.csv"
```

### Prerequisites

Install Anaconda - [Installation guide](https://conda.io/docs/user-guide/install/index.html)
Install scrapy: 
```
pip install scrapy
```
Alternatively
```
conda install -c conda-forge scrapy
```

That's it!

### Usage

#### Run the Crawler
A simple method to crawl all articles would be to run:
```
scrapy crawl wiwo_all -o "output.json"
```
This will crawl all articles and the option '-o "filename"' creates an output file with crawled data in the format:
url, topic, author, time, title, leadtext, body

If you want to add additional information to the output, you can create new css requests in the yield from line 17.

The topic is the little text above the heading, the time is the publishing date with time in hh:mm:ss+nn:nn format. The leadtext is the bold text above the social buttons. 
The Script automatically creates raw data entries for every article in the folder raws, if you don't want this just comment the lines 26-29 like this:
```
    #RAWS = Path("Raws/")
    #RAWS.mkdir(exist_ok=True)
    #with open(RAWS/filename, "wb") as f:
    #    f.write(response.body)
```

The fetching of new articles happens through the lines 31-35.
```
    next_articles = response.css("div.c-teaser div.u-lastchild a::attr(href)").extract()
    next_pages = response.css("div.u-flex__item a.c-button::attr(href)").extract()
    new_authors = response.css("div.c-metadata a::attr(href)").extract()
```
fetches authors, additional pages on author sites and linked articles. Lines 35-35 iterate through those fetched data and crawl all articles from every found author. 
If you want to restrict the articles to certain authors you could just change line 16 to
```
        author = response.css("a span.u-font-bold::text").extract_first()
        if author != None and author == "firstname lastname" and article != None:
```
This way just articles with a certain author will be written to the output file. Usually it is enough to set the start-urls (line 6-8) to the author page (e.g. [https://www.wiwo.de/melanie-bergermann/6828194.html](https://www.wiwo.de/melanie-bergermann/6828194.html)) and comment out lines 43-45.

#### Usage of extracted data

The extracted output file can e.g. be used to learn a language model and use it for transfer learning. [More information](http://nlp.fast.ai/).
A model I created can be found in the "model" folder together with the voccabulary in a zip file.
Also analysis on the raw articles could be performed, like David Kriesel did in [this CCC Talk](https://www.youtube.com/watch?v=-YpwsdRKt8Q&t=1s).

If you have any new ideas or projects based on this data I'd appreciate it if you share those with me!

Enjoy!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


#### Example output of text generation

> xbos  aus der schweiz, der türkei, österreich und schweden, aber nicht mit der schweiz und deutschland zusammen, um das zu ändern und das wachstum in der euro zu verbessern, sondern die zahl seiner beschäftigten i diesem land auf rund 20 prozent steigern. das heißt aber, sie würden die zahl von derzeit knapp fünf prozent i diesem vergleich erhöhen, wenn es zu einem weiteren rückgang der nachfrage kommen könnte, wenn sich der markt für den gesamten markt in deutschland weiter erholen wird, so die studie der t_up oecd, der die zeitung in seiner „ zeit " veröffentlicht. 
> 
>
> der europäische markt ist i diesem vergleich zu 2012 um ein drittel gewachsen, während der umsatz in den letzten drei monaten von knapp zehn prozent um zwei drittel gestiegen war, und die zahl auf rund 50 prozent der wirtschaftsleistung steigen soll, so dass es in der vergangenheit auch auf den deutschen mittelstand nicht ankommt : so stieg der durchschnittliche durchschnittliche haushalt der bundesrepublik 2011 in den vergangenen jahren von knapp unter 20 prozent i vergangenen monat. i deutschland sind das sogar vier millionen. die deutsche industrie ist in diesem zeitraum um fast 30 prozentpunkte auf rund 40 milliarden dollar geklettert, was einem rückgang i der globalen nachfrage bedeutet : die einnahmen werden i der vergangenen woche in deutschland von rund zwei auf vier prozent gesenkt, während sie in der vergangenheit deutlich über den höchsten wert lag - vor allem i deutschland, österreich oder österreich, in der t_up oecd sogar über zwei prozentpunkte und in italien mit einem anteil vom vorjahr. 
> 
>
>  die wichtigsten punkte für deutsche firmen 
>
>
>  das handelsblatt und das magazin " report 2016 2016 “ stellen sie auf den neuen seiten des internationalen netzwerks ( facebook - gruppe, kurz : die unternehmen, das institut, die deutsche telekom und der deutsche maschinenbau ), in den niederlanden, österreich und der niederlanden sowie der türkei, österreich und österreich - schweiz, aber noch aus den anderen eu. 