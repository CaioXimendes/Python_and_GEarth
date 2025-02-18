from g_python.hmessage import Direction, HMessage
from g_python.hpacket import HPacket
from g_python import hparsers
from g_python import htools
import sys
from g_python.gextension import Extension

extension_info = {
    "title": "Extension stuff",
    "description": "g_python test",
    "version": "1.0",
    "author": "caiofsx"
}

ext = Extension(extension_info, sys.argv)   # sys.argv are the commandline arguments, for example ['-p', '9092'] (G-Earth's extensions port)
ext.start()

"""def falar_no_chat(p):           
    comando = "falar"
    comando2 = ":iniciar"
    jogador = int
    id_usuario, text = p.packet.read('is')
    if text == comando:
        jogador = id_usuario
        talk("mensagem enviada")
        talk(f'{jogador}')
    if text == comando2:
        talk("Planta carnivora iniciado!!")"""

contador = int
def falar_no_chat(p):
    comando = ":iniciar"
    id_usuario, text = p.packet.read('is')
    if text == comando:
        talk("Quanto é 1+2")
    if text == "3":
        jogador = id_usuario
        talk("voce acertou!")
    else:
        talk(f"{text}")
    

def talk(message):
    ext.send_to_server(HPacket("Shout", message, 24))

ext.intercept(Direction.TO_CLIENT, falar_no_chat, "Chat")