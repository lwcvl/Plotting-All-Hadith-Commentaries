# Plotting All Hadith Commentaries
*Data and code to create visualizations of hadith commentary across Islamic history*


Wat can be visualized with digital methods? The short answer: data. So, we need to turn our historical sources into data (or: data points, together making a dataset). We can visualize the popularity of writing commentaries on a classic text. For this we will use *Jāmiʿ al-shurūḥ wa-l-ḥawāshī* as our source. You can download it here:
http://www.archive.org/download/jamiii_churuh_01/jamiii_churuh_01.pdf
http://www.archive.org/download/jamiii_churuh_02/jamiii_churuh_02.pdf
http://www.archive.org/download/jamiii_churuh_03/jamiii_churuh_03.pdf

You need to pick a classic work of our choice and read the entry carefully. The information we are after are the death date of the author of the classic work and the death dates of the commentators.

To do this for the six canonical hadith compilations, you should find the individual entries to these texts. In this repo you will find the most important two of them.

For the initial phase of data entry you can use something like Excel if you like. Write down the year of death (AH) of the classic author in A1, then write the death dates of the commentators in A2-A`n`, with `n` the number of commentators. Skip all commentators for which no exact death date is given.

From these death dates we extrapolate to life by assuming a lifespan (or floruit) of 40 years. The code that does this data conversion (data cleaning) is flexible enough to handle different lifespans (and even different texts than the ones we use here). I have run the code with `lifespan = 20` and `lifespan = 60` and it did not seem to make a significant difference. If anything, the resulting visualization is simply most clear with 40 as lifespan. 

(c) L.W.C. van Lit. Please cite this repo if you use this code for your own purposes.
