//Essa primeira já é padrão para se utilizar o puppeteer
const puppeteer = require('puppeteer')

//?
const fs = require('fs/promises')

async function start() {
    const browser = await puppeteer.launch({headless:false})
    const page = await browser.newPage()

    //É redirecionado para a página que queremos
    await page.goto("https://en.wikipedia.org/wiki/List_of_dog_breeds")

    //Selecionando todos os links de raças de cachorros da página inicial.
    const linksDogs = await page.evaluate(() => {
        return Array.from(document.querySelectorAll(".div-col ul li > a")).map(x => x.href)
    });

    //Percorrendo e acessando cada um dos links.
    for (const link of linksDogs) {
        await page.goto(link)

        //Selecionando todos os links de imagens dentro de cada raça de cachorro.
        const imgsDogs = await page.evaluate(() => {
            return Array.from(document.querySelectorAll("img")).map(x => x.src)
        });

        for (const img of imgsDogs) {
            const imagepage = await page.goto(img)
            await fs.writeFile('./download-imgs/' + img.split("/").pop(), await imagepage.buffer())
        }
    }

    //Aparentemnete o "await" não tem efeito nessa expressão
    browser.close()
}

start()
