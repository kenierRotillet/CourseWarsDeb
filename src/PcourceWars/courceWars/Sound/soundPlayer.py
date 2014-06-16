#!/usr/bin/python
# -*- coding: latin-1 -*-
"""módulo que se encarga de la reproducción de sonidos"""
import pygame
import Tools
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=64)
pygame.mixer.set_num_channels(64)

bgVolume =0.3



def playSounds(personaje):
    """método qque reproduce la cola de sonidos del personaje entregado, en el frame actual."""
    #log.escribir("en cola hay " + str(len(personaje.currentSounds)))

    if len(personaje.currentSounds) >= 0:
        for snd in personaje.currentSounds:
            #log.escribir(str(snd))
            if snd == "":
                continue
            if Tools.FastMethods.usingPyAl==False:

                snd.play()
            else:
                wic = personaje.topWidth/2
                pos = (personaje.rect.centerx-wic)

                if personaje.player==1:
                    reproducir(sourcep1,snd,[pos,0,0],120)
                else:
                    reproducir(sourcep2,snd,[pos,0,0],120)
                    
                    
                    
                    



            


    personaje.currentSounds = []




def simpleplay(sfx):
    if Tools.FastMethods.usingPyAl==False:

        sonido = pygame.mixer.Sound(sfx)
        sonido.play()
    else:
        source = Sound.openal.audio.SoundSource(position=[0, 0, 0])
        data = Sound.openal.loaders.load_wav_file(sfx)
        reproducir(source,data,source.position)
        






def bgmPlay(bgm,vol=bgVolume):
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(-1)


def stopbgm():
    pygame.mixer.music.stop()

def playSysSound(sound,player=0):
    if comonSounds.has_key(sound):
        if Tools.FastMethods.usingPyAl==False:
            comonSounds[sound][0][1].play()
        else:
            if player==1:
                data=comonSounds[sound][0][1]
                reproducir(sourcep1,data,[-1,0,0])
                

            elif player==2:
                data=comonSounds[sound][0][1]
                reproducir(sourcep2,data,[1,0,0])
            else:
                data=comonSounds[sound][0][1]
                reproducir(sourcep1,data,[0,0,0])
                
                








def reproducir(source,data,pos,gain=1):
    global soundSinkEngine
    global sourcep1
    global sourcep2
        
    try:
        source.position = pos
        source.gain=gain
        source.queue(data)
        
        soundSinkEngine.play(source)
        soundSinkEngine.update()
        sourcep1=Sound.openal.audio.SoundSource(position=pos)
        sourcep2=Sound.openal.audio.SoundSource(position=pos)
    except Exception:
        Tools.Logger.escribir("error en openal, reiniciando sistema")
        Tools.Logger.excepcion("error con openal, reiniciando")
        soundSinkEngine=Sound.openal.audio.SoundSink()
        soundSinkEngine.activate()
        sourcep1=Sound.openal.audio.SoundSource()
        sourcep2=Sound.openal.audio.SoundSource()






try:
    import Sound.openal
    import Sound.openal.audio as opaudio
    import Sound.openal.loaders
    Tools.FastMethods.usingPyAl=True
    soundSinkEngine = opaudio.SoundSink()
    listener = opaudio.SoundListener()
    listener.position=[0,0,0]
    listener.velocity=[0,0,0]
    listener.orientation=[0,0,-1,0,1,0]
    soundSinkEngine.listener=listener
    sourcep1=opaudio.SoundSource(position=[0,0,0])
    sourcep2=opaudio.SoundSource(position=[0,0,0])
    soundSinkEngine.activate()
except Exception, mes:
    Tools.Logger.escribir("No se pudo cargar pyAl")
    Tools.Logger.excepcion("detalles del error")
    Tools.FastMethods.usingPyAl=False
    simpleplay("sfx/error.wav")




    
comonSounds = Tools.FastMethods.LoadSounds("cfg/sfx.snd")
