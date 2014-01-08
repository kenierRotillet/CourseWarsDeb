#!/usr/bin/python
# -*- coding: latin-1 -*-
import time
def escribir(texto):
    arch = open("log.log", 'a')
    arch.write(texto+"\n")
    arch.close()
    return


