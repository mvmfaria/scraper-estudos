//Essa primeira já é padrão para se utilizar o puppeteer
const puppeteer = require('puppeteer')

//Variáveis utilizadas para alterar entre páginas
const allDogs = "List_of_dog_breeds"

//Ferramenta do node para conseguirmos escrever no arquivo.
const fs = require('fs/promises')

//Função principal.
async function start() {
    const browser = await puppeteer.launch()
    const page = await browser.newPage()

    //É redirecionado para a página que queremos
    await page.goto("https://learnwebcode.github.io/practice-requests/")

    
    /*const names = await page.evaluate(() => {
        //A parte do map é para restringir qual parte do Selector queremos extrair.
        return Array.from(document.querySelectorAll(".div-col ul li a[title]")).map(x => x.textContent)
    })

    await fs.writeFile("names.txt", names.join("\r\n"))*/

    //Criada especificamente para selecionar múltiplos elementos. O primeiro parâmetro é um "selector" do CSS e o segundo é uma função.
    const photos = await page.$$eval("img", (imgs) => {

        //Aparentemente nos iremos selecionar a fonte da imagem.
        return imgs.map(x => x.src)
    })

    //Criando um loop para fazer dowload?
    for (const photo of photos) {
        const imagepage = await page.goto(photo)
        //photo.split("/") vai nos retornar o último item do endereço? / Segundo parâmetro é conteúdo que queremos salvar.
        await fs.writeFile(photo.split("/").pop(), await imagepage.buffer())
    }

    //Aparentemnete o "await" não tem efeito nessa expressão
    browser.close()
}

//Chamando função.
start()