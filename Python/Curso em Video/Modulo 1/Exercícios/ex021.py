import pygame
print('')
print(' '*25+'=====DESAFIO 21=====')
print('-'*74)
print('Faça um programa em python que abra e reproduza o áudio de um arquivo mp3')
print('-'*74)

pygame.mixer.init()
pygame.mixer.music.load(f"file.mp3")
pygame.mixer.music.play()