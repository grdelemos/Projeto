# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:26:36 2020

@author: grdel
"""

media_bedrooms =  3.06
media_bathrooms = 1.98
media_sqft_living = 1853.36
media_sqft_lot = 4979.42
media_floors = 1.528
media_waterfront = 0
media_view = 0.62
media_condition = 3.51
media_grade = 7.56
media_sqft_above = 1419.64
media_sqft_basement = 433.72
media_preco = 359.81

def preco_abaixo():
    print('A casa tem o preço abaixo da média')
    
def preco_acima():
    print('A casa tem o preço acima da média')
    
def area_porao():
    area_porao = float(input("Digite a área do porão:"))
    if area_porao <= media_sqft_basement:
        return True
    else:
        return False
 
def andares():
    andares = float(input("Digite a quantidade de andares:"))
    if andares <= media_floors:
        return True
    else:
        return False

def area_acima():
    area_acima = float(input("Digite a área da parte acima do chão:"))
    if area_acima <= media_sqft_above:
        return True
    else:
        return False

def quartos():
    quartos = float(input("Digite a quantidade de quartos:"))
    if quartos <= media_bedrooms:
      return True
    else:
        return False
    
def condicao():
    condicao = float(input("Digite a nota de condição:"))
    if condicao <= media_condition:
        return True
    else:
        return False
    
def area_terreno():
    area_terreno = float(input("Digite a área do terreno:"))
    if area_terreno <= media_sqft_lot:
         return True
    else:
        return False

def nota():
    nota = float(input("Digite a nota da casa:"))
    if nota <= media_grade:
        return True
    else:
        return False

def vista():
    vista = float(input("Digite a quantidade de vistas:"))
    if vista <= media_view:
        return True
    else:
        return False

def banheiros():
    banheiros = float(input("Digite a quantidade de vistas:"))
    if banheiros <= media_view:
        return True
    else:
        return False


p1 = area_porao()
if p1 == True:
    p2 = andares()
    if p2 == True:
        p3 = area_acima()
        if p3 == True:
            p4 = quartos()
            if p4 == True:
                p5 = condicao()
                if p5 == True:
                    p6 = area_terreno()
                    if p6 == True:
                        preco_acima()
                    else:
                        p7 = nota()
                        if p7 == True:
                            p8 = vista()
                            if p8 == True:
                                preco_acima()
                            else:
                                preco_abaixo()
                        else:
                            preco_acima()
                else:
                    preco_acima()
            else:
                preco_abaixo()
        else:
            p9 = condicao()
            if p9 == True:
                p10 = nota()
                if p10 == True:
                    preco_abaixo()
                else:
                    p11 = vista()
                    if p11 == True:
                        p12 = area_terreno()
                        if p12 == True:
                            preco_abaixo()
                        else:
                            p13 = quartos()
                            if p13 == True:
                               p14 = banheiros()
                               if p14 == True:
                                   preco_abaixo()
                               else:
                                   preco_acima()
                            else:
                                preco_acima()
                    else:
                         preco_abaixo()
            else:
                p15 = banheiros()
                if p15 == True:
                    preco_acima()
                else:
                    p16 = vista()
                    if p16 == True:
                        p17 = area_terreno()
                        if p17 == True:
                            preco_abaixo()
                        else:
                            p18 = quartos()
                            if p18 == True:
                                preco_acima()
                            else:
                                preco_abaixo()
                    else:
                        preco_acima()
    
                            
                                
                        
                    
    
        
