const puppeteer = require("puppeteer");
const fs = require("fs");
const { exit } = require("process");
const { Agent } = require("http");

// class containing link to playlists on the page
// class="sc-list-item sc-divider item"
(async () => {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto(
        "https://nightswithalicecooper.com/last-nights-music/"
    );

    await page.waitForSelector('.sc-list-item')
    let element = await page.$('.sc-list-item')
    let value = await page.evaluate(el => el.textContent, element)




    console.log(element);


    await page.close();
    await browser.close();


})