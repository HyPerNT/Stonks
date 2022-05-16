# $tonks
> Nobody knows if a stock's going up, down or f***ing sideways, least of all stockbrokers. But we have to pretend we know. - Jordan Belfort

## About this Project
![stonks.jpg](stonks.jpg)
This is a ~~poor~~ attempt at writing a stock trading bot from scratch.

The idea behind it is to pick out stocks that are expected to make *some* return within the next few days and sell them within the window that *should* generate the most profit. Rinse and repeat to expand your capital.

That being said, any APIs and libraries used to interface with brokerages will *not* be conducting any real trades. This will be a "paper money" bot to test the feasibility of this approach.

In the future, I might include some way to act on those trades with a connected account for personal use, but I'm not very good at writing secure software, so use that at your own risk

### Approach
Two pronged: Python and C, my favorite.

Python will handle most of the work I'm too lazy to implement in C. It will grab symbols and their prices and (hopefully) interface with some C code that will handle all of the analysis and calculation (for speed). Then based on what C thinks, python will act on it and throw $hitloads of more data at it.

Then, python will handle the portfolio tracking and "trading". I might even have some matplotlib shenanigans going on to show how your portfolio evolves over time.

Maybe I'll even throw some ML in if I'm bored.

It'd also be neat to have a Discord bot or something that would notify users of particularly good picks.

Don't hold me to any of this. This repo is likely to end up dead before the month ends.

## Installation

Nothing to install (yet)


## TODO
- [ ] Scrape current value of symbols
- [ ] Figure out how to get Python to talk to C
- [ ] Git gud at stonks
- [ ] Build a UI?
- [ ] Profit
