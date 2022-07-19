import subprocess
import sys
import time
import os
import pyautogui
import webbrowser
import ctypes

from setuptools import find_namespace_packages

#Colores
red = '\033[31m'
green = '\033[32m'
reset = '\033[0m'
bold = '\033[01m'

PATH_TO_FOLDER=os.getcwd()

os.system("cls")

reset

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def _header_():
    print ("""
    cccc   i   bbbb    eeeeee   rrrrrrr
   cc      i   b   b   eeeeee   rr   rrr
   cc      i   b b     eee      rrrrrr      ------   P3d1A
   cc      i   b   b   eeeeee   rr rrrr
    cccc   i   bbbb    eeeeee   rr  rrr                                                                   """)

_header_()
print("\n")

if is_admin():
    def main():
            print("Bienvenido a la herramienta configuradora del servidor Blockdash + Laser Tracer + Lavaland de Stumble Guys.\n")
            time.sleep(6)
            os.system("cls")

    def ask_input():
        os.system("cls")
        print("¿Qué quieres hacer?\n")
        print("\t[1] Configurar el server\n")
        print("\t[2] Encender el server\n")
        print("\t[3] Apagar el server\n")
        print("\t[4] Iniciar Stumble Guys\n")
        print("\t[5] Comprobar el estado del server (apagado/encendido)\n")
        print("\t[q] Salir\n\n")
        time.sleep(0.5)
        accion=input(">>>")
        accion=str(accion)
        if accion == "1":
            opcion1()
        elif accion == "2":
            opcion2()
        elif accion == "3":
            opcion3()
        elif accion == "4":
            opcion4()
        elif accion == "5":
            check_estado_server()
        elif accion == "q":
            os.system("cls")
            print("[-] Saliendo.")
            time.sleep(0.5)
            os.system("cls")
            print("[-] Saliendo..")
            time.sleep(0.5)
            os.system("cls")
            print("[-] Saliendo...")
            time.sleep(0.5)
            os.system("cls")
            sys.exit(0)
        else:
            print("[!] Intruduzca un valor válido")
            ask_input()


    def opcion1():
        try:
            PATH=PATH_TO_FOLDER+"\\StumbleFakeServer\\InstalarCertificadoAtualizado.pfx"
            os.system('start "" "' + PATH + '"')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('enter')
            pyautogui.press('down')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.press('down')
            pyautogui.press('enter')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.press('enter')
            ask_input()
        except Exception:
            print("[!] Hubo un error durante el proceso")
            sys.exit(1)        

    def opcion2():
        try:
            PATH=PATH_TO_FOLDER+"\\StumbleFakeServer\\TrocaFakeStumble-3-TorneiosAmigos.bat"
            subprocess.check_output([PATH])
            with open("status_of_server.txt", "w") as file:
                file.write("1")
                file.close()
            print("[+] Server encendido correctamente")
            time.sleep(1.5)
            ask_input()
        except Exception:
            print("[!] Hubo un error durante el proceso")
            sys.exit(1)


    def opcion3():
        try:
            PATH=PATH_TO_FOLDER+"\\StumbleFakeServer\\TrocaFakeStumble-0-VoltaOriginal.bat"
            subprocess.check_output([PATH])
            with open("status_of_server.txt", "w") as file:
                file.write("0")
                file.close()
            print("[+] Server apagado correctamente")
            time.sleep(1.5)
            ask_input()
        except Exception:
            print("[!] Hubo un error durante el proceso")
            sys.exit(1)

    def opcion4():
        os.system("cls")
        time.sleep(0.5)
        try:
            print("[+] Abriendo Stumble Guys...")
            webbrowser.open_new("steam://rungameid/1677740")
        except Exception:
            os.system("cls")
            print("[-] No se pudo abrir el programa. ¿Lo tienes instalado?")
        sys.exit(0)

    def check_estado_server():
        with open("status_of_server.txt", "r") as file:
            server_status=file.read()
            file.close()
            if server_status == "0":
                os.system("cls")
                print("[" + red + bold + "X" + reset + "] Actualmente el servidor está " + red + bold + "apagado" + reset)
                time.sleep(3)
                ask_input()
            elif server_status == "1":
                os.system("cls")
                print("[" + green + bold + "V" + reset + "] Actualmente el servidor está " + green + bold + "encendido" + reset)
                time.sleep(3)
                ask_input()
            else:
                os.system("cls")
                print("[!]" + red + bold + " Advertencia" + reset + ": Los valores del archivo <status_of_server.txt> han sido modificados.")
                time.sleep(2)
                os.system("cls")
                try:
                    os.system("cls")
                    print("[!] Reseteando el servidor...")
                    time.sleep(1)
                    PATH=PATH_TO_FOLDER+"\\StumbleFakeServer\\TrocaFakeStumble-3-TorneiosAmigos.bat"
                    subprocess.check_output([PATH])
                    print("[+] Server encendido correctamente")
                    time.sleep(1)
                    PATH=PATH_TO_FOLDER+"\\StumbleFakeServer\\TrocaFakeStumble-0-VoltaOriginal.bat"
                    subprocess.check_output([PATH])
                    print("[+] Server apagado correctamente")
                    time.sleep(2.5)
                    os.system("cls")
                    with open("status_of_server.txt", "w") as file:
                        file.write("0")
                        file.close()
                    print("[" + green + bold + "V" + reset + "] Server reseteado correctamente")
                    ask_input()
                except OSError:
                    print("[" + red + bold + "X" + reset + "] Error durante la ejecución")
                    time.sleep(2.5)
                    sys.exit(1)
                

    main()
    ask_input()
else:
    print("[-] Debes ejecutar el programa como" + red + bold + " Administrador" + reset)
    input("\nPulse enter para terminar...")
    sys.exit(1)