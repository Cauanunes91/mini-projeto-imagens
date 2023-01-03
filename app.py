from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#Quais palavras sobrepor na imagem
palavras = ['Notebok gamer',' Notebook Office', 'Notebook Bonito', 'Notebook Zero Bala']
contador = 1
for palavra in palavras:
    #abrir a imagem
    imagem = Image.open('laptop.jpg')
    #abrir a sobreposição
    draw = ImageDraw.Draw(imagem)
    # setar qual fonte quero usar
    fonte = ImageFont.truetype('BRADHITC.TTF',60)
    #sobrepor (escrever por cima) da imagem
    draw.text((300,77),palavra,font=fonte)
    #salvar essa imagem
    imagem.save(f'imagem{contador}.jpg')
    contador += 1