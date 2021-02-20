from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

# Inicializacao da estrutura de dados
class Estrutura_bonecoOlaf:
    def __init__(self):        
        self.lista_rotacao = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    def desenhar_cabeca(self):
        # Desenha a cabeca  
        glPushMatrix()  
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0, -1)
        glutSolidCone(.2, .7, 60, 100)
        glRotatef(-90, 1, 0, 0)
        glTranslatef(0, 0.05, 0)
        glutSolidSphere(0.21, 20, 20)
        glPopMatrix()
        
    def desenhar_olho(self):
        #desenhar olhos
        glPushMatrix()
        glColor3f(0, 0, 0)
        glTranslatef(0.05, 1.17, 0.18)
        glutSolidSphere(0.03, 10, 10)
        glTranslatef(-0.1, 0, 0)
        glutSolidSphere(0.03, 10, 10)
        glPopMatrix()
        
    def desenhar_nariz(self):
        # Desenha o nariz
        glPushMatrix()
        glTranslatef(0, 1.1, 0)
        glColor3f(1, 0.5, 0.5)
        glutSolidCone(0.08, 0.35, 10, 2)
        glPopMatrix()
        
    def desenhar_corpo(self):
        # Desenha o corpo
        glPushMatrix()
        glColor3f(1.0, 1.0, 1.0)
        glRotatef(90, 1, 0, 0)
        glTranslatef(0, 0, -0.30)
        glRotatef(190, 1, 0, 0)
        glutSolidTorus(.2, 0.1, 60, 60)   
        glTranslatef(0, 0, 0.30)
        glutSolidTorus(.2, 0.01, 15, 15)
        glRotatef(-190, 1, 0, 0)
        glRotatef(270, 1, 0, 0)
        
    def desenhar_braco_esquerdo(self):
        #bracos
        #ombro esquesdo
        glColor3f(0.7, 0.4, 0.4)
        glTranslatef(0, 0.1, 0)
        glRotatef(90, 0, 1, 0)
        glRotatef(10, 1, 0, 0)
        quadratic = gluNewQuadric()
        gluCylinder(quadratic, 0.02, 0.014, 0.25, 60, 60)
        
        #cotovelo esquerdo
        glTranslatef(0, 0, 0.25)
        glRotatef(50, 1, 0, 0)
        glutSolidSphere(0.015, 10, 10)
        
        #ante-braco esquerdo
        quadratic = gluNewQuadric()
        gluCylinder(quadratic, 0.013, 0.01, 0.3, 60, 60)
        
        #palma da mao
        glTranslatef(0, 0, 0.30)
        glutSolidSphere(0.02, 10, 10)
        
        #dedos
    
        #medio
        gluCylinder(quadratic, 0.005, 0.005, 0.1, 60, 60)
        
        #mindinho
        glTranslatef(0, -0.01, 0)
        glRotatef(10, 1, 0, 0)
        gluCylinder(quadratic, 0.005, 0.005, 0.08, 60, 60)
        glRotatef(-10, 1, 0, 0)
        glTranslatef(0, 0.01, 0)
    
        #indicador
        glTranslatef(0, 0.015, 0)
        glRotatef(-10, 1, 0, 0)
        gluCylinder(quadratic, 0.005, 0.005, 0.1, 60, 60)
        glRotatef(10, 1, 0, 0)
        glTranslatef(0, -0.015, 0)
    
        #polegar
        glTranslatef(0, 0.02, 0)
        glRotatef(-45, 1, 0, 0)
        gluCylinder(quadratic, 0.005, 0.005, 0.05, 60, 60)
        glRotatef(45, 1, 0, 0)
        glTranslatef(0, -0.02, 0)
    
        #desfazendo as transformacoes
        glTranslatef(0, 0, -0.30)
        glRotatef(-50, 1, 0, 0)
        glTranslatef(0, 0, -0.25)
        glRotatef(-10, 1, 0, 0)
        glRotatef(-90, 0, 1, 0)
        glTranslatef(0, -0.1, 0)
        
    def desenhar_braco_direito(self):
        #braco direito
        #ombro direito
        glTranslatef(-0.25, 0.05, 0)
        glRotatef(100, 0, 1, 0)
        glRotatef(-10, 1, 0, 0)
        quadratic = gluNewQuadric()
        gluCylinder(quadratic, 0.02, 0.014, 0.25, 60, 60)
        
        #cotovelo direito
        glTranslatef(0, 0, -0.01)
        glRotatef(125, 1, 0, 0)
        glutSolidSphere(0.015, 10, 10)
        
        #ante-braco direito
        quadratic = gluNewQuadric()
        gluCylinder(quadratic, 0.013, 0.01, 0.3, 60, 60)
        
        #palma da mao direita
        glTranslatef(0, 0, 0.25)
        glutSolidSphere(0.02, 10, 10)
        
        #dedos da mao direita
        #medio
        gluCylinder(quadratic, 0.005, 0.005, 0.1, 60, 60)
        
        #mindinho
        glTranslatef(0, 0.01, 0)
        glRotatef(-10, 1, 0, 0)
        gluCylinder(quadratic, 0.005, 0.005, 0.08, 60, 60)
        glRotatef(10, 1, 0, 0)
        glTranslatef(0, -0.01, 0)
    
        #indicador
        glTranslatef(0, -0.015, 0)
        glRotatef(10, 1, 0, 0)
        gluCylinder(quadratic, 0.005, 0.005, 0.1, 60, 60)
        glRotatef(-10, 1, 0, 0)
        glTranslatef(0, 0.015, 0)
    
        #polegar
        glTranslatef(0, -0.02, 0)
        glRotatef(45, 1, 0, 0)
        gluCylinder(quadratic, 0.005, 0.005, 0.05, 60, 60)
        glRotatef(-45, 1, 0, 0)
        glTranslatef(0, 0.02, 0)
    
        #desfazendo as transformacoes
        glTranslatef(0, 0, -0.25)
        glRotatef(-125, 1, 0, 0)
        glTranslatef(0, 0, 0.01)
        glRotatef(10, 1, 0, 0)
        glRotatef(-100, 0, 1, 0)
        glTranslatef(0.25, -0.05, 0)
        
    def desenhar_bolinha_corpo(self):
        
        #BOLINHAS DO CORPO
        glColor3f(0, 0, 0)
        
        #bolinha de cima
        glTranslatef(0, 0, 0.2)
        glutSolidSphere(0.04, 10, 10)
        
        #bolinha do meio
        glTranslatef(0, -0.2, 0)
        glutSolidSphere(0.05, 10, 10)
        
        #bolinha de baixo
        glTranslatef(0, -0.15, 0.04)
        glutSolidSphere(0.05, 10, 10)
    
        glPopMatrix()
    
    
    def desenhar_pes(self):
        
        #desenhar os pes
        glPushMatrix()
        glColor3f(1, 1, 1)
        glTranslatef(0.2, .15, 0)
        glutSolidSphere(0.1, 20, 20)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(-0.2, 0.15, 0)
        glutSolidSphere(0.1, 20, 20)
        glPopMatrix()
        
    # Metodo para chamar funções por partes para desenhar o boneco
    def desenharBonecoOlaf(self):
    
        self.desenhar_cabeca()
        self.desenhar_olho()
        self.desenhar_nariz()
        self.desenhar_corpo()
        self.desenhar_braco_esquerdo()
        self.desenhar_braco_direito()
        self.desenhar_bolinha_corpo()
        self.desenhar_pes()
        return
    
    
    
    # Metodo que permite utilizar as setas do teclado para rotacionar o boneco
    def controleSetas(self,key, x, y):
    
        # controle de rotacao vertical
        if(key == GLUT_KEY_UP):
            glRotatef(-2.0, 2.0, 0.0, 0.0)
        elif(key == GLUT_KEY_DOWN):
            glRotatef(2.0, 2.0, 0.0, 0.0)
        # controle de rotacao horizontal
        elif(key == GLUT_KEY_LEFT):
            glRotatef(-2.0, 0.0, 2.0, 0.0)
        elif(key == GLUT_KEY_RIGHT):
            glRotatef(2.0, 0.0, 2.0, 0.0)
    
        glutPostRedisplay()
        
    def display(self):
    
        # Limpa e habilita os buffers para gravacao de cores e profundidades
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
        # Chao invertido
        glPushMatrix()
        glRotate(180, 1, 0, 0)
        glBegin(GL_POLYGON)
        glColor3b(51, 51, 51)
        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(  5, 0.15, -5 )
        glVertex3f(  5, 0.15,  5 )
        glVertex3f( -5, 0.15,  5 )
        glVertex3f( -5, 0.15, -5 )
        glEnd()
        glPopMatrix()
        # Chao normal
        glPushMatrix()
        glBegin(GL_POLYGON)
        glColor3b(51, 51, 51)
        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(  5, -0.15, -5 )
        glVertex3f(  5, -0.15,  5 )
        glVertex3f( -5, -0.15,  5 )
        glVertex3f( -5, -0.15, -5 )
        glEnd()
        glPopMatrix()
    
        # Empurra a pilha de matriz atual para baixo
        glPushMatrix()
    
        # Define a posicao atual a ser rotacionado
        glRotatef(self.lista_rotacao[0], 0, 0, 1.0)
    
        #st cor default
        glColor3f(1.0, 1.0, 1.0)
        # Chama o metodo para desenhar o boneco de neve na tela
        self.desenharBonecoOlaf()
    
        # Substitui a matriz atual pela que esta abaixo dela na pilha
        glPopMatrix()
    
        # Troca de Buffers
        glutSwapBuffers()
    
        
    def vizualizar_boneco(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 800)
        glutCreateWindow('Boneco Olaf   -   Projeto de Computacao Grafica')

    def adicionar_iluminacao(self):
        # Criacao do sombreamento (suave)
        glShadeModel(GL_SMOOTH)
    
        # Habilita o face Culling (Corte de faces nao visualizadas)
        glEnable(GL_CULL_FACE)
    
        # Realiza comparacoes de profundidade para atualizar o Buffer de profundidade
        glEnable(GL_DEPTH_TEST)
    
        # Permite a renderizacao das cores com a iluminacao ativa
        glEnable(GL_COLOR_MATERIAL)
    
        # Habilita o foco de luz
        glEnable(GL_LIGHTING)
    
        # Posicionamento do foco da Luz
        lightZeroPosition = [1.0, 4.0, 15.0, 0.]
    
        # Cor da luz
        lightZeroColor = [0.8, 1.0, 0.8, 1.0]
    
        # Funcao que especifica a quantidade de focos e a posicao dela em coordenadas homogeneas
        glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition)
    
        # Especificam a intensidade RGBA difusa da luz.
        glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor)
    
        # Representa a atenuacao constante do foco
        glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1.5)
    
        # Representa a atenuacao linear do foco
        glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)
    
        # Habilita 1 foco de luz
        glEnable(GL_LIGHT1)
        
    def definir_iteracao_teclado(self):
        # Habilita as funcoes das setas do teclado
        glutSpecialFunc(self.controleSetas)
    
        # Especifica a pilha de matriz de projecao como a pilha principal
        glMatrixMode(GL_PROJECTION)
    
        # Especifica o anlgulo de visao, proporcao de visao no eixo x, distancia de visao ate o proximo plano
        gluPerspective(40.0, 1.0, 1.0, 40.0)
    
        # Define o retorno de chamada da exibicao para a janela atual.
        glutDisplayFunc(self.display)
    
        # Cria uma matriz de visualizacao derivada de um ponto ocular, um ponto de referencia indicando o centro da cena e um vetor para cima.
        gluLookAt(0, 2, 5,#camera
                  0, 1, 0,
                  0, 1, 0)
    
        # Empurra a pilha de matriz atual para baixo
        glPushMatrix()
    
        glutMainLoop()

    

if __name__ == '__main__':
    estrutura=Estrutura_bonecoOlaf()
    estrutura.vizualizar_boneco()
    estrutura.adicionar_iluminacao()
    estrutura.definir_iteracao_teclado()
