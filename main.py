'''
Trabalho de Álgebra Linear 2019/2
Transformações de imagem utilizando operações com matrizes

Grupo:
Aline Bravin
Ana Elisa Rezende
Amanda Ferreira
'''
import matplotlib.pyplot as plt
import numpy as np
import string
import cv2

# pontos a, b, c, d
a, b, c, d = (0, 0), (0, 2), (2, 2), (2, 0)

# matriz com os vetores listados acima
A = np.array([a, b, c, d])

# matriz identidade 2x2
Id = np.eye(2)

color_lut = 'rgbc'
fig = plt.figure()
ax = plt.gca()
#lista de pontos no eixo X
xs = []
#lista de pontos no eixo Y
ys = []
# i é utilizado apenas para indicar a letra dos pontos
i = 0
for row in A:
    # o @ é um multiplicador de matrizes
    coordenadas = Id @ row
    x, y = coordenadas
    xs.append(x)
    ys.append(y)
    c = color_lut[i] # cor da letra
    plt.scatter(x, y) # marca no plano
    plt.text(x + 0.15, y + 0.10, f"{string.ascii_letters[i]}")
    i += 1
# adiciona os pontos nas listas X e Y
# pega o xs[0] para poder fechar o desenho no gráfico
xs.append(xs[0])
ys.append(ys[0])
# plota no plano 
plt.plot(xs, ys, color="blue", linestyle='solid')
ax.set_xticks(np.arange(0, 5, 0.5))
ax.set_yticks(np.arange(0, 5, 0.5))
plt.grid()
plt.show()
#salva a imagem para podermos visualizar
fig.savefig('grafico_1.png')

# "rotaciona" os pontos
M = np.array([
  [ 0,1], 
  [-1,0]
])

fig = plt.figure()
ax = plt.gca()
xs_s = []
ys_s = []
i_s = 0
for row in A:
    coordenadas = M @ row
    x, y = row
    x_s, y_s= coordenadas
    xs_s.append(x_s)
    ys_s.append(y_s)
    c_s = color_lut[i_s] 
    plt.scatter(x_s, y_s, color=c_s)
    plt.text(x_s + 0.15, y_s + 0.10, f"{string.ascii_letters[int(i_s)]}'")
    i_s += 1

xs_s.append(xs_s[0])
ys_s.append(ys_s[0])
plt.plot(xs_s, ys_s, color="red", linestyle='solid')
plt.plot(xs, ys, color="black", linestyle='dotted')
ax.set_xticks(np.arange(0, 5, 0.5))
ax.set_yticks(np.arange(-2, 5, 0.5))
plt.grid()
plt.show()
  
fig.savefig('grafico_2.png')

# cisalhamento horizontal
k = 1 
M = np.array([
  [1, k], 
  [0, 1]
])

fig = plt.figure()
ax = plt.gca()
xs_s = []
ys_s = []
i = 0
for row in A:
    coordenadas = M @ row    
    x, y = coordenadas    
    x_s, y_s = row
    xs_s.append(x)
    ys_s.append(y)
    c = color_lut[i] 
    plt.scatter(x, y, color=c)
    plt.text(x + 0.15, y + 0.10, f"{string.ascii_letters[int(i)]}")
    i += 1

xs_s.append(xs_s[0])
ys_s.append(ys_s[0])
plt.plot(xs_s, ys_s, color="red", linestyle='solid')
plt.plot(xs, ys, color="black", linestyle='dotted')
ax.set_xticks(np.arange(0, 5, 0.5))
ax.set_yticks(np.arange(0, 5, 0.5))
plt.grid()
plt.show()
  
fig.savefig('grafico_3.png')

# teste com imagem

image = cv2.imread('dog.png') # abre a imagem como array
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # corrige as cores da imagem

# cisalhamento horizontal
k = 1
M = np.float32([
  [1,-k,128],
  [0,1,0]
])

linhas, colunas, camadas = image.shape

# warpAffine realiza a transformação na imagem
# cv2.warpAffine(origem, matriz transformação, tamanho da img saída)
image = cv2.warpAffine(image,M,(colunas,linhas))

fig = plt.figure()
im = plt.imshow(image)
plt.axis("off")
plt.show

fig.savefig('cisalhamento_dog.png')

# rotaciona 

image = cv2.imread('dog.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

M = np.float32([
  [ 0,1,0], 
  [-1,0,256]
])
'''
M = np.float32([
  [np.cos(3*np.pi/2), -np.sin(3*np.pi/2), 0],
  [np.sin(3*np.pi/2), np.cos(3*np.pi/2), 256]
])
'''
linhas, colunas, camadas = image.shape

image = cv2.warpAffine(image,M,(colunas,linhas))

fig = plt.figure()
im = plt.imshow(image)
plt.axis("off")
plt.show

fig.savefig('rotaciona_dog.png')
