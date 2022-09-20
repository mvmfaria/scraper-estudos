//Essa primeira já é padrão para se utilizar o puppeteer
const puppeteer = require('puppeteer')

async function start() {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()

    for 