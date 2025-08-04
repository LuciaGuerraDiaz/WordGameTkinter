# import tkinter as tk
# from tkinter import messagebox
# import os
# from PIL import Image, ImageTk
# import random
# os.chdir(os.path.dirname(__file__))

# # Crear ventana principal
# root = tk.Tk()
# root.title("Juego del Ahorcado - 2 Jugadores")
# root.geometry("800x600")
# root.configure(bg="white")

# # Variables globales del juego
# palabra_secreta = ""
# letras_adivinadas = set()
# letras_correctas = set()
# vidas = 5
# palabras_secretas = []
# palabras_originales = []  # Para guardar las palabras originales
# alfabeto = "abcdefghijklmnopqrstuvwxyz"

# # Variables para widgets globales
# label_palabra = None
# label_vidas = None
# entrada_letra = None
# btn_adivinar = None
# label_alfabeto = None
# label_ahorcado = None
# instrucciones = None
# entrada = None
# btn_agregar = None
# btn_start = None
# imagen_portada = None

# def mostrar_reglas():
#     reglas = (
#         "🎯 Reglas del Juego del Ahorcado:\n\n"
#         "• El Jugador 1 ingresa 5 palabras secretas.\n"
#         "• El Jugador 2 debe adivinar la palabra letra por letra.\n"
#         "• Tiene 5 vidas (errores permitidos).\n"
#         "• El jugador 1 gana si se completa el dibujo antes de adivinar la palabra.\n"
#         "• El jugador 2 gana si adivina la palabra antes de ser ahorcado.\n\n"
#         "¡Que gane el mejor!"
#     )
#     messagebox.showinfo("Reglas del Juego", reglas)

# def cargar_imagen_portada():
#     """Carga la imagen de portada si existe"""
#     global imagen_portada
#     try:
#         script_dir = os.path.dirname(os.path.abspath(__file__))
#         # Buscar imagen de portada
#         posibles_nombres = ["portada.png", "logo.png", "hangman_logo.png", "title.png"]
        
#         for nombre in posibles_nombres:
#             image_path = os.path.join(script_dir, "assets", nombre)
#             if os.path.exists(image_path):
#                 imagen = Image.open(image_path)
#                 imagen = imagen.resize((200, 150), Image.Resampling.LANCZOS)
#                 imagen_portada = ImageTk.PhotoImage(imagen)
#                 return True
        
#         # Si no encuentra imagen, crear una con texto
#         crear_imagen_portada_texto()
#         return True
        
#     except Exception as e:
#         print(f"Error cargando imagen de portada: {e}")
#         crear_imagen_portada_texto()
#         return True

# def crear_imagen_portada_texto():
#     """Crea una imagen de portada con texto si no hay imagen disponible"""
#     global imagen_portada
#     try:
#         from PIL import Image, ImageDraw, ImageFont
        
#         # Crear imagen con fondo
#         img = Image.new('RGB', (200, 150), color='lightblue')
#         draw = ImageDraw.Draw(img)
        
#         # Intentar usar una fuente, si no está disponible usar la default
#         try:
#             font = ImageFont.truetype("arial.ttf", 20)
#         except:
#             font = ImageFont.load_default()
        
#         # Dibujar texto
#         draw.text((100, 60), "🎯", anchor="mm", font=font, fill='red')
#         draw.text((100, 90), "AHORCADO", anchor="mm", font=font, fill='black')
#         draw.text((100, 110), "2 Jugadores", anchor="mm", font=font, fill='blue')
        
#         imagen_portada = ImageTk.PhotoImage(img)
        
#     except Exception as e:
#         print(f"Error creando imagen de texto: {e}")
#         imagen_portada = None

# def agregar_palabra():
#     global palabras_secretas, palabras_originales, entrada, btn_start
    
#     palabra = entrada.get().strip().lower()
#     entrada.delete(0, tk.END)
    
#     # Validar palabra
#     if not palabra:
#         messagebox.showwarning("Entrada vacía", "⚠️ Ingresá una palabra válida.")
#         return
    
#     if not palabra.isalpha():
#         messagebox.showwarning("Entrada inválida", "⚠️ Solo se permiten letras.")
#         return
    
#     if palabra in palabras_secretas:
#         messagebox.showwarning("Palabra repetida", "⚠️ Esa palabra ya fue agregada.")
#         return
    
#     # Agregar palabra
#     palabras_secretas.append(palabra)
#     palabras_originales.append(palabra)  # Guardar copia original
    
#     # Actualizar instrucciones
#     instrucciones.config(text=f"Palabras agregadas: {len(palabras_secretas)}/5")
    
#     # Si ya hay 5 palabras, mostrar botón de inicio
#     if len(palabras_secretas) == 5:
#         # Crear botón de iniciar si no existe
#         if btn_start is None:
#             btn_start = tk.Button(root, text="🎯 ¡Iniciar Juego!", 
#                                 command=iniciar_juego,
#                                 bg="#27AE60", fg="white", 
#                                 font=("Montserrat", 12, "bold"),
#                                 padx=20, pady=10)
#             btn_start.pack(pady=20)
        
#         instrucciones.config(text="¡5 palabras listas! Presiona 'Iniciar Juego'")
#         btn_agregar.config(state="disabled")
#         entrada.config(state="disabled")

# def iniciar_juego():
#     global palabra_secreta, letras_adivinadas, letras_correctas, vidas
#     global label_palabra, label_vidas, entrada_letra, btn_adivinar, label_alfabeto, label_ahorcado
    
#     if not palabras_secretas:
#         messagebox.showwarning("Sin palabras", "⚠️ Primero agregá las palabras secretas.")
#         return
    
#     # Seleccionar palabra aleatoria SIEMPRE
#     palabra_secreta = random.choice(palabras_secretas)
#     palabras_secretas.remove(palabra_secreta) # Elimina las ya usadas
#     letras_adivinadas = set()
#     letras_correctas = set()
#     vidas = 5
    
#     print(f"🎯 Nueva palabra seleccionada: {palabra_secreta.upper()}")  # Para debug
#     print(f"🎯 Palabras restantes: {len(palabras_secretas)}")  # Para debug
    
#     # Limpiar interfaz actual completamente
#     limpiar_interfaz_completa()
    
#     # Resetear variables de widgets
#     label_palabra = None
#     label_vidas = None
#     entrada_letra = None
#     btn_adivinar = None
#     label_alfabeto = None
#     label_ahorcado = None
    
#     # Crear interfaz del juego
#     crear_interfaz_juego()

# def limpiar_interfaz_inicial():
#     """Limpia los widgets de la interfaz inicial"""
#     global instrucciones, entrada, btn_agregar, btn_start
    
#     widgets_a_limpiar = [instrucciones, entrada, btn_agregar, btn_start]
    
#     for widget in widgets_a_limpiar:
#         if widget and widget.winfo_exists():
#             widget.destroy()
    
#     # Resetear referencias
#     instrucciones = None
#     entrada = None
#     btn_agregar = None
#     btn_start = None

# def crear_interfaz_juego():
#     global label_palabra, label_vidas, entrada_letra, btn_adivinar, label_alfabeto, label_ahorcado
    
#     # Título del juego
#     titulo = tk.Label(root, text="🎯 Jugador 2: ¡Adiviná la palabra!",
#                      bg="white", font=("Montserrat", 14, "bold"))
#     titulo.pack(pady=(20, 10))
    
#     # Crear frame principal para organizar el layout
#     frame_principal = tk.Frame(root, bg="white")
#     frame_principal.pack(expand=True, fill="both", padx=20)
    
#     # Frame izquierdo para el dibujo del ahorcado
#     frame_izquierdo = tk.Frame(frame_principal, bg="white")
#     frame_izquierdo.pack(side="left", fill="y", padx=(0, 20))
    
#     # Label para el dibujo del ahorcado
#     label_ahorcado = tk.Label(frame_izquierdo, text="🎪", font=("Arial", 60), bg="white")
#     label_ahorcado.pack(pady=20)
    
#     # Frame derecho para el juego
#     frame_derecho = tk.Frame(frame_principal, bg="white")
#     frame_derecho.pack(side="right", expand=True, fill="both")
    
#     # Mostrar información del juego
#     info_juego = tk.Label(frame_derecho, 
#                          text=f"📝 Palabras disponibles: {len(palabras_secretas)} | Palabra: {'*' * len(palabra_secreta)}",
#                          bg="lightgray", font=("Montserrat", 9))
#     info_juego.pack(pady=5)
    
#     # Mostrar vidas (usar la variable global actualizada)
#     label_vidas = tk.Label(frame_derecho, text=f"❤️ Vidas: {vidas}",
#                           bg="white", font=("Montserrat", 12, "bold"), fg="red")
#     label_vidas.pack(pady=5)
    
#     # Mostrar progreso de la palabra
#     progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
#     label_palabra = tk.Label(frame_derecho, text=" ".join(progreso),
#                             bg="white", font=("Montserrat", 18, "bold"))
#     label_palabra.pack(pady=20)
    
#     # Campo para ingresar letra
#     tk.Label(frame_derecho, text="Ingresá una letra:", bg="white", 
#              font=("Montserrat", 10)).pack(pady=(10, 5))
    
#     entrada_letra = tk.Entry(frame_derecho, font=("Montserrat", 14), width=3, justify="center")
#     entrada_letra.pack(pady=5)
#     entrada_letra.focus()
    
#     # Botón para adivinar
#     btn_adivinar = tk.Button(frame_derecho, text="Adivinar", command=procesar_intento,
#                             bg="lightblue", font=("Montserrat", 12, "bold"))
#     btn_adivinar.pack(pady=10)
    
#     # Mostrar alfabeto con estados
#     label_alfabeto = tk.Text(frame_derecho, height=4, width=50, bg="white", font=("Monserrat", 12), wrap="word", bd=0)
#     label_alfabeto.pack(pady=5)
#     label_alfabeto.config(state="disabled")
    
#     # Actualizar el alfabeto inicial
#     actualizar_alfabeto()
    
#     # Actualizar el dibujo inicial
#     actualizar_dibujo_ahorcado()
    
#     # Permitir presionar Enter para adivinar
#     entrada_letra.bind('<Return>', lambda event: procesar_intento())

# def procesar_intento():
#     global vidas
    
#     if not entrada_letra:
#         return
    
#     intento = entrada_letra.get().lower().strip()
#     entrada_letra.delete(0, tk.END)
    
#     # Validar entrada
#     if len(intento) != 1 or not intento.isalpha():
#         messagebox.showwarning("Entrada inválida", "❌ Ingresá solo una letra válida.")
#         return
    
#     if intento in letras_adivinadas:
#         messagebox.showinfo("Letra repetida", "⚠️ Ya probaste esa letra.")
#         return
    
#     # Agregar letra a las adivinadas
#     letras_adivinadas.add(intento)
    
#     # Verificar si la letra está en la palabra
#     if intento in palabra_secreta:
#         letras_correctas.add(intento)
#         messagebox.showinfo("¡Bien!", "✅ ¡Bien! Esa letra está.")
#     else:
#         vidas -= 1
#         if vidas > 0:
#             messagebox.showinfo("No está", f"❌ No está. Te quedan {vidas} vida(s).")
        
#     # Actualizar interfaz
#     actualizar_interfaz()
    
#     # Verificar condiciones de victoria/derrota
#     verificar_fin_juego()

# def actualizar_interfaz():
#     if label_vidas:
#         label_vidas.config(text=f"❤️ Vidas: {vidas}")
    
#     if label_palabra:
#         progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
#         label_palabra.config(text=" ".join(progreso))
    
#     actualizar_alfabeto()
#     actualizar_dibujo_ahorcado()

# def actualizar_alfabeto():
#     if not label_alfabeto:
#         return
        
#     label_alfabeto.config(state="normal")
#     label_alfabeto.delete("1.0", tk.END)

#     for letra in alfabeto:
#         if letra in letras_correctas:
#             label_alfabeto.insert(tk.END, letra.upper() + " ", "negrita")
#         elif letra in letras_adivinadas:
#             label_alfabeto.insert(tk.END, letra.upper() + " ", "tachado")
#         else:
#             label_alfabeto.insert(tk.END, letra.upper() + " ")

#     # Configurar estilos
#     label_alfabeto.tag_config("negrita", font=("Monserrat", 12, "bold"))
#     label_alfabeto.tag_config("tachado", font=("Monserrat", 12), foreground="red")
#     label_alfabeto.config(state="disabled")
 
# def actualizar_dibujo_ahorcado():
#     if not label_ahorcado:
#         return
        
#     # Dibujos con emojis mejorados para cada estado
#     dibujos = [
#         "🎪",                    # 5 vidas - base
#         "🎪\n│",                 # 4 vidas - poste vertical
#         "🎪\n│\n│",              # 3 vidas - poste completo  
#         "🎪\n├───┐\n│",          # 2 vidas - brazo horizontal
#         "🎪\n├───┐\n│   😵",      # 1 vida - cabeza
#         "🎪\n├───┐\n│   😵\n    💀"  # 0 vidas - muerto
#     ]
    
#     # Intentar cargar imagen PNG con mejor manejo de errores
#     imagen_cargada = False
    
#     try:
#         script_dir = os.path.dirname(os.path.abspath(__file__))
#         # Probar diferentes nombres de archivo
#         posibles_nombres = [
#             f"ahorcado_{5-vidas}.png",
#             f"ahorcado{5-vidas}.png", 
#             f"hangman_{5-vidas}.png"
#         ]
        
#         for nombre in posibles_nombres:
#             image_path = os.path.join(script_dir, "assets", nombre)
            
#             if os.path.exists(image_path):
#                 imagen = Image.open(image_path)
#                 imagen = imagen.resize((150, 200), Image.Resampling.LANCZOS)
#                 foto = ImageTk.PhotoImage(imagen)
#                 label_ahorcado.config(image=foto, text="", compound="center")
#                 label_ahorcado.image = foto  # Mantener referencia
#                 imagen_cargada = True
#                 break
        
#     except Exception as e:
#         print(f"❌ Error cargando imagen: {e}")
    
#     # Si no se cargó imagen, usar dibujo ASCII
#     if not imagen_cargada:
#         label_ahorcado.config(text=dibujos[5-vidas], image="", 
#                              font=("Courier New", 12, "bold"), 
#                              justify="left")

# def verificar_fin_juego():
#     progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
    
#     # Verificar victoria
#     if "_" not in progreso:
#         messagebox.showinfo("¡Victoria!", "🎉 ¡Felicidades, adivinaste la palabra!")
#         preguntar_reinicio()
#         return
    
#     # Verificar derrota
#     if vidas <= 0:
#         messagebox.showinfo("Perdiste", f"💀 Perdiste. La palabra era: {palabra_secreta.upper()}")
#         preguntar_reinicio()
#         return

# def preguntar_reinicio():
#     print(f"🔍 Debug - Palabras restantes: {len(palabras_secretas)}")
#     print(f"🔍 Debug - Palabras originales: {len(palabras_originales)}")
    
#     # Verificar si quedan palabras para jugar
#     if len(palabras_secretas) > 0:
#         respuesta = messagebox.askyesno("Continuar", 
#             f"¿Querés continuar con la siguiente palabra?\n\n"
#             f"Palabras restantes: {len(palabras_secretas)}")
        
#         if respuesta:
#             # Continuar con la siguiente palabra
#             print("✅ Usuario eligió continuar")
#             iniciar_juego()
#             return
#         else:
#             # Preguntar si quiere empezar de nuevo
#             nuevo_juego = messagebox.askyesno("Nuevo Juego", 
#                 "¿Querés empezar un nuevo juego?\n\n"
#                 "SÍ = Crear nuevas palabras\n"
#                 "NO = Salir del juego")
            
#             if nuevo_juego:
#                 print("✅ Usuario eligió crear nuevas palabras")
#                 reiniciar_completamente()
#             else:
#                 print("✅ Usuario eligió salir")
#                 root.quit()
#             return
    
#     # Si no quedan palabras
#     print("⚠️ No quedan más palabras")
#     respuesta = messagebox.askyesno("Fin del juego", 
#         "¡Se acabaron las palabras!\n\n¿Querés jugar otra vez?")
    
#     if respuesta:
#         usar_mismas = messagebox.askyesno("Palabras", 
#             "¿Querés usar las mismas palabras secretas?\n\n"
#             "SÍ = Usar las mismas 5 palabras\n"
#             "NO = Crear nuevas palabras")
        
#         if usar_mismas:
#             # Restaurar las palabras originales
#             print("✅ Usuario eligió usar mismas palabras")
#             restaurar_palabras_originales()
#             iniciar_juego()
#         else:
#             # Crear nuevas palabras
#             print("✅ Usuario eligió crear nuevas palabras")
#             reiniciar_completamente()
#     else:
#         print("✅ Usuario eligió salir")
#         root.quit()

# def restaurar_palabras_originales():
#     """Restaura la lista de palabras originales para jugar de nuevo"""
#     global palabras_secretas
#     print(f"🔄 Restaurando palabras originales: {palabras_originales}")
#     palabras_secretas = palabras_originales.copy()
#     print(f"🔄 Palabras restauradas: {palabras_secretas}")
#     print(f"🔄 Total de palabras disponibles: {len(palabras_secretas)}")

# def reiniciar_completamente():
#     """Reinicia completamente el juego para ingresar nuevas palabras"""
#     global palabras_secretas, palabras_originales, palabra_secreta, letras_adivinadas, letras_correctas, vidas
#     global label_palabra, label_vidas, entrada_letra, btn_adivinar, label_alfabeto, label_ahorcado
#     global instrucciones, entrada, btn_agregar, btn_start  # AGREGAR btn_start aquí

#     print("🆕 Reiniciando completamente para nuevas palabras...")
    
#     # Limpiar todas las variables
#     palabras_secretas = []
#     palabras_originales = []
#     palabra_secreta = ""
#     letras_adivinadas = set()
#     letras_correctas = set()
#     vidas = 5
    
#     # Resetear variables de widgets (INCLUYENDO btn_start)
#     label_palabra = None
#     label_vidas = None
#     entrada_letra = None
#     btn_adivinar = None
#     label_alfabeto = None
#     label_ahorcado = None
#     instrucciones = None
#     entrada = None
#     btn_agregar = None
#     btn_start = None  # RESETEAR btn_start
    
#     # Limpiar interfaz
#     limpiar_interfaz_completa()
    
#     # Volver a la interfaz inicial
#     crear_interfaz_inicial()

# def limpiar_interfaz_completa():
#     """Limpia toda la interfaz excepto el botón de reglas"""
#     print("🧹 Limpiando interfaz completa...")
#     widgets_conservar = []
    
#     # Buscar el botón de reglas para conservarlo
#     for widget in root.winfo_children():
#         try:
#             if hasattr(widget, 'cget') and widget.cget('text') == "Reglas del Juego":
#                 widgets_conservar.append(widget)
#                 print("✅ Conservando botón de reglas")
#         except:
#             pass
    
#     # Destruir todos los widgets excepto los que queremos conservar
#     for widget in root.winfo_children():
#         if widget not in widgets_conservar:
#             try:
#                 widget.destroy()
#             except:
#                 pass
    
#     print("✅ Interfaz limpia")

# def crear_interfaz_inicial():
#     global instrucciones, entrada, btn_agregar, imagen_portada
    
#     print(f"🎮 Creando interfaz inicial - Palabras actuales: {len(palabras_secretas)}")
    
#     # Cargar y mostrar imagen de portada
#     if cargar_imagen_portada() and imagen_portada:
#         label_portada = tk.Label(root, image=imagen_portada, bg="white")
#         label_portada.pack(pady=(40, 20))
#     else:
#         # Si no hay imagen, mostrar título grande
#         titulo_principal = tk.Label(root, text="🎯 JUEGO DEL AHORCADO 🎯",
#                                    bg="white", font=("Montserrat", 20, "bold"),
#                                    fg="#2C3E50")
#         titulo_principal.pack(pady=(40, 10))
        
#         subtitulo = tk.Label(root, text="2 Jugadores",
#                             bg="white", font=("Montserrat", 14),
#                             fg="#7F8C8D")
#         subtitulo.pack(pady=(0, 20))
    
#     # Etiqueta de instrucciones
#     texto_instrucciones = "Jugador 1: Ingresá 5 palabras secretas"
#     if palabras_secretas:
#         texto_instrucciones = f"Palabras agregadas: {len(palabras_secretas)}/5"
    
#     instrucciones = tk.Label(root, text=texto_instrucciones,
#                             bg="white", font=("Montserrat", 12, "bold"))
#     instrucciones.pack(pady=(20, 10))

#     # Campo de entrada
#     entrada = tk.Entry(root, font=("Montserrat", 12), width=20)
#     entrada.pack(pady=10)
#     entrada.focus()

#     # Botón para agregar palabra - siempre habilitado en interfaz inicial
#     btn_agregar = tk.Button(root, text="Agregar Palabra", command=agregar_palabra, 
#                            bg="#3498DB", fg="white", font=("Montserrat", 12, "bold"),
#                            padx=20, pady=5)
#     btn_agregar.pack(pady=10)
    
#     # Permitir Enter para agregar palabra
#     entrada.bind('<Return>', lambda event: agregar_palabra())
    
#     # CORRECCIÓN: No verificar palabras aquí, el botón se creará dinámicamente en agregar_palabra()
#     # El botón "Iniciar Juego" se crea automáticamente cuando se llegue a 5 palabras
    
#     print("✅ Interfaz inicial creada")

# # Crear botón para mostrar reglas
# btn_reglas = tk.Button(root, text="Reglas del Juego", command=mostrar_reglas, 
#                       bg="#E74C3C", fg="white", font=("Montserrat", 10, "bold"),
#                       padx=15, pady=5)
# btn_reglas.place(x=10, y=10)

# # Función para verificar imágenes disponibles
# def verificar_imagenes():
#     """Verifica qué imágenes están disponibles en la carpeta assets"""
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     assets_path = os.path.join(script_dir, "assets")
    
#     print(f"📁 Buscando en: {assets_path}")
    
#     if not os.path.exists(assets_path):
#         print("❌ La carpeta 'assets' no existe")
#         return False
    
#     archivos = os.listdir(assets_path)
#     print(f"📋 Archivos encontrados: {archivos}")
    
#     imagenes_encontradas = []
#     for i in range(6):
#         nombres_posibles = [f"ahorcado_{i}.png", f"ahorcado{i}.png", f"hangman_{i}.png"]
#         for nombre in nombres_posibles:
#             if nombre in archivos:
#                 imagenes_encontradas.append(nombre)
#                 break
    
#     print(f"🖼️ Imágenes del ahorcado encontradas: {imagenes_encontradas}")
#     return len(imagenes_encontradas) > 0

# # Verificar imágenes al inicio
# verificar_imagenes()

# # Iniciar con la interfaz inicial
# crear_interfaz_inicial()

# # Iniciar el loop principal
# root.mainloop()

#Juego con conteo de victorias
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import random
os.chdir(os.path.dirname(__file__))

# Crear ventana principal
root = tk.Tk()
root.title("Juego del Ahorcado - 2 Jugadores")
root.geometry("800x600")
root.configure(bg="white")

# Variables globales del juego
palabra_secreta = ""
letras_adivinadas = set()
letras_correctas = set()
vidas = 5
palabras_secretas = []
palabras_originales = []  # Para guardar las palabras originales
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Variables de puntuación
puntos_jugador1 = 0  # Gana cuando el jugador 2 no adivina
puntos_jugador2 = 0  # Gana cuando adivina la palabra
total_palabras_jugadas = 0

# Variables para widgets globales
label_palabra = None
label_vidas = None
entrada_letra = None
btn_adivinar = None
label_alfabeto = None
label_ahorcado = None
instrucciones = None
entrada = None
btn_agregar = None
btn_start = None
imagen_portada = None
label_puntuacion = None  # Para mostrar el marcador

def mostrar_reglas():
    reglas = (
        "🎯 Reglas del Juego del Ahorcado:\n\n"
        "• El Jugador 1 ingresa 5 palabras secretas.\n"
        "• El Jugador 2 debe adivinar la palabra letra por letra.\n"
        "• Tiene 5 vidas (errores permitidos).\n"
        "• El jugador 1 gana si se completa el dibujo antes de adivinar la palabra.\n"
        "• El jugador 2 gana si adivina la palabra antes de ser ahorcado.\n\n"
        "¡Que gane el mejor!"
    )
    messagebox.showinfo("Reglas del Juego", reglas)

def cargar_imagen_portada():
    """Carga la imagen de portada si existe"""
    global imagen_portada
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Buscar imagen de portada
        posibles_nombres = ["portada.png", "logo.png", "hangman_logo.png", "title.png"]
        
        for nombre in posibles_nombres:
            image_path = os.path.join(script_dir, "assets", nombre)
            if os.path.exists(image_path):
                imagen = Image.open(image_path)
                imagen = imagen.resize((200, 150), Image.Resampling.LANCZOS)
                imagen_portada = ImageTk.PhotoImage(imagen)
                return True
        
        # Si no encuentra imagen, crear una con texto
        crear_imagen_portada_texto()
        return True
        
    except Exception as e:
        print(f"Error cargando imagen de portada: {e}")
        crear_imagen_portada_texto()
        return True

def crear_imagen_portada_texto():
    """Crea una imagen de portada con texto si no hay imagen disponible"""
    global imagen_portada
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Crear imagen con fondo
        img = Image.new('RGB', (200, 150), color='lightblue')
        draw = ImageDraw.Draw(img)
        
        # Intentar usar una fuente, si no está disponible usar la default
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        # Dibujar texto
        draw.text((100, 60), "🎯", anchor="mm", font=font, fill='red')
        draw.text((100, 90), "AHORCADO", anchor="mm", font=font, fill='black')
        draw.text((100, 110), "2 Jugadores", anchor="mm", font=font, fill='blue')
        
        imagen_portada = ImageTk.PhotoImage(img)
        
    except Exception as e:
        print(f"Error creando imagen de texto: {e}")
        imagen_portada = None

def agregar_palabra():
    global palabras_secretas, palabras_originales, entrada, btn_start
    
    palabra = entrada.get().strip().lower()
    entrada.delete(0, tk.END)
    
    # Validar palabra
    if not palabra:
        messagebox.showwarning("Entrada vacía", "⚠️ Ingresá una palabra válida.")
        return
    
    if not palabra.isalpha():
        messagebox.showwarning("Entrada inválida", "⚠️ Solo se permiten letras.")
        return
    
    if palabra in palabras_secretas:
        messagebox.showwarning("Palabra repetida", "⚠️ Esa palabra ya fue agregada.")
        return
    
    # Agregar palabra
    palabras_secretas.append(palabra)
    palabras_originales.append(palabra)  # Guardar copia original
    
    # Actualizar instrucciones
    instrucciones.config(text=f"Palabras agregadas: {len(palabras_secretas)}/5")
    
    # Si ya hay 5 palabras, mostrar botón de inicio
    if len(palabras_secretas) == 5:
        # Crear botón de iniciar si no existe
        if btn_start is None:
            btn_start = tk.Button(root, text="🎯 ¡Iniciar Juego!", 
                                command=iniciar_juego,
                                bg="#27AE60", fg="white", 
                                font=("Montserrat", 12, "bold"),
                                padx=20, pady=10)
            btn_start.pack(pady=20)
        
        instrucciones.config(text="¡5 palabras listas! Presiona 'Iniciar Juego'")
        btn_agregar.config(state="disabled")
        entrada.config(state="disabled")

def iniciar_juego():
    global palabra_secreta, letras_adivinadas, letras_correctas, vidas
    global label_palabra, label_vidas, entrada_letra, btn_adivinar, label_alfabeto, label_ahorcado
    
    if not palabras_secretas:
        messagebox.showwarning("Sin palabras", "⚠️ Primero agregá las palabras secretas.")
        return
    
    # Seleccionar palabra aleatoria SIEMPRE
    palabra_secreta = random.choice(palabras_secretas)
    palabras_secretas.remove(palabra_secreta) # Elimina las ya usadas
    letras_adivinadas = set()
    letras_correctas = set()
    vidas = 5
    
    print(f"🎯 Nueva palabra seleccionada: {palabra_secreta.upper()}")  # Para debug
    print(f"🎯 Palabras restantes: {len(palabras_secretas)}")  # Para debug
    
    # Limpiar interfaz actual completamente
    limpiar_interfaz_completa()
    
    # Resetear variables de widgets
    label_palabra = None
    label_vidas = None
    entrada_letra = None
    btn_adivinar = None
    label_alfabeto = None
    label_ahorcado = None
    
    # Crear interfaz del juego
    crear_interfaz_juego()

def limpiar_interfaz_inicial():
    """Limpia los widgets de la interfaz inicial"""
    global instrucciones, entrada, btn_agregar, btn_start
    
    widgets_a_limpiar = [instrucciones, entrada, btn_agregar, btn_start]
    
    for widget in widgets_a_limpiar:
        if widget and widget.winfo_exists():
            widget.destroy()
    
    # Resetear referencias
    instrucciones = None
    entrada = None
    btn_agregar = None
    btn_start = None

def crear_interfaz_juego():
    global label_palabra, label_vidas, entrada_letra, btn_adivinar, label_alfabeto, label_ahorcado, label_puntuacion
    
    # Título del juego
    titulo = tk.Label(root, text="🎯 Jugador 2: ¡Adiviná la palabra!",
                     bg="white", font=("Montserrat", 14, "bold"))
    titulo.pack(pady=(20, 10))
    
    # Marcador de puntuación
    label_puntuacion = tk.Label(root, 
                               text=f"🏆 Jugador 1: {puntos_jugador1} | Jugador 2: {puntos_jugador2} | Partida: {total_palabras_jugadas + 1}/5",
                               bg="lightgreen", font=("Montserrat", 11, "bold"),
                               pady=5)
    label_puntuacion.pack(pady=(0, 10), padx=20, fill="x")
    
    # Crear frame principal para organizar el layout
    frame_principal = tk.Frame(root, bg="white")
    frame_principal.pack(expand=True, fill="both", padx=20)
    
    # Frame izquierdo para el dibujo del ahorcado
    frame_izquierdo = tk.Frame(frame_principal, bg="white")
    frame_izquierdo.pack(side="left", fill="y", padx=(0, 20))
    
    # Label para el dibujo del ahorcado
    label_ahorcado = tk.Label(frame_izquierdo, text="🎪", font=("Arial", 60), bg="white")
    label_ahorcado.pack(pady=20)
    
    # Frame derecho para el juego
    frame_derecho = tk.Frame(frame_principal, bg="white")
    frame_derecho.pack(side="right", expand=True, fill="both")
    
    # Mostrar información del juego
    info_juego = tk.Label(frame_derecho, 
                         text=f"📝 Palabras disponibles: {len(palabras_secretas)} | Palabra: {'*' * len(palabra_secreta)}",
                         bg="lightgray", font=("Montserrat", 9))
    info_juego.pack(pady=5)
    
    # Mostrar vidas (usar la variable global actualizada)
    label_vidas = tk.Label(frame_derecho, text=f"❤️ Vidas: {vidas}",
                          bg="white", font=("Montserrat", 12, "bold"), fg="red")
    label_vidas.pack(pady=5)
    
    # Mostrar progreso de la palabra
    progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
    label_palabra = tk.Label(frame_derecho, text=" ".join(progreso),
                            bg="white", font=("Montserrat", 18, "bold"))
    label_palabra.pack(pady=20)
    
    # Campo para ingresar letra
    tk.Label(frame_derecho, text="Ingresá una letra:", bg="white", 
             font=("Montserrat", 10)).pack(pady=(10, 5))
    
    entrada_letra = tk.Entry(frame_derecho, font=("Montserrat", 14), width=3, justify="center")
    entrada_letra.pack(pady=5)
    entrada_letra.focus()
    
    # Botón para adivinar
    btn_adivinar = tk.Button(frame_derecho, text="Adivinar", command=procesar_intento,
                            bg="lightblue", font=("Montserrat", 12, "bold"))
    btn_adivinar.pack(pady=10)
    
    # Mostrar alfabeto con estados
    label_alfabeto = tk.Text(frame_derecho, height=4, width=50, bg="white", font=("Monserrat", 12), wrap="word", bd=0)
    label_alfabeto.pack(pady=5)
    label_alfabeto.config(state="disabled")
    
    # Actualizar el alfabeto inicial
    actualizar_alfabeto()
    
    # Actualizar el dibujo inicial
    actualizar_dibujo_ahorcado()
    
    # Permitir presionar Enter para adivinar
    entrada_letra.bind('<Return>', lambda event: procesar_intento())

def procesar_intento():
    global vidas
    
    if not entrada_letra:
        return
    
    intento = entrada_letra.get().lower().strip()
    entrada_letra.delete(0, tk.END)
    
    # Validar entrada
    if len(intento) != 1 or not intento.isalpha():
        messagebox.showwarning("Entrada inválida", "❌ Ingresá solo una letra válida.")
        return
    
    if intento in letras_adivinadas:
        messagebox.showinfo("Letra repetida", "⚠️ Ya probaste esa letra.")
        return
    
    # Agregar letra a las adivinadas
    letras_adivinadas.add(intento)
    
    # Verificar si la letra está en la palabra
    if intento in palabra_secreta:
        letras_correctas.add(intento)
        messagebox.showinfo("¡Bien!", "✅ ¡Bien! Esa letra está.")
    else:
        vidas -= 1
        if vidas > 0:
            messagebox.showinfo("No está", f"❌ No está. Te quedan {vidas} vida(s).")
        
    # Actualizar interfaz
    actualizar_interfaz()
    
    # Verificar condiciones de victoria/derrota
    verificar_fin_juego()

def actualizar_interfaz():
    if label_vidas:
        label_vidas.config(text=f"❤️ Vidas: {vidas}")
    
    if label_palabra:
        progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        label_palabra.config(text=" ".join(progreso))
    
    actualizar_alfabeto()
    actualizar_dibujo_ahorcado()

def actualizar_alfabeto():
    if not label_alfabeto:
        return
        
    label_alfabeto.config(state="normal")
    label_alfabeto.delete("1.0", tk.END)

    for letra in alfabeto:
        if letra in letras_correctas:
            label_alfabeto.insert(tk.END, letra.upper() + " ", "negrita")
        elif letra in letras_adivinadas:
            label_alfabeto.insert(tk.END, letra.upper() + " ", "tachado")
        else:
            label_alfabeto.insert(tk.END, letra.upper() + " ")

    # Configurar estilos
    label_alfabeto.tag_config("negrita", font=("Monserrat", 12, "bold"), foreground="blue",)
    label_alfabeto.tag_config("tachado", font=("Monserrat", 12), foreground="red")
    label_alfabeto.config(state="disabled")
 
def actualizar_dibujo_ahorcado():
    if not label_ahorcado:
        return
        
    # Dibujos con emojis mejorados para cada estado
    dibujos = [
        "🎪",                    # 5 vidas - base
        "🎪\n│",                 # 4 vidas - poste vertical
        "🎪\n│\n│",              # 3 vidas - poste completo  
        "🎪\n├───┐\n│",          # 2 vidas - brazo horizontal
        "🎪\n├───┐\n│   😵",      # 1 vida - cabeza
        "🎪\n├───┐\n│   😵\n    💀"  # 0 vidas - muerto
    ]
    
    # Intentar cargar imagen PNG con mejor manejo de errores
    imagen_cargada = False
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Probar diferentes nombres de archivo
        posibles_nombres = [
            f"ahorcado_{5-vidas}.png",
            f"ahorcado{5-vidas}.png", 
            f"hangman_{5-vidas}.png"
        ]
        
        for nombre in posibles_nombres:
            image_path = os.path.join(script_dir, "assets", nombre)
            
            if os.path.exists(image_path):
                imagen = Image.open(image_path)
                imagen = imagen.resize((150, 200), Image.Resampling.LANCZOS)
                foto = ImageTk.PhotoImage(imagen)
                label_ahorcado.config(image=foto, text="", compound="center")
                label_ahorcado.image = foto  # Mantener referencia
                imagen_cargada = True
                break
        
    except Exception as e:
        print(f"❌ Error cargando imagen: {e}")
    
    # Si no se cargó imagen, usar dibujo ASCII
    if not imagen_cargada:
        label_ahorcado.config(text=dibujos[5-vidas], image="", 
                             font=("Courier New", 12, "bold"), 
                             justify="left")

def verificar_fin_juego():
    global puntos_jugador1, puntos_jugador2, total_palabras_jugadas
    
    progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
    
    # Verificar victoria del Jugador 2
    if "_" not in progreso:
        puntos_jugador2 += 1
        total_palabras_jugadas += 1
        messagebox.showinfo("¡Victoria del Jugador 2!", 
                           f"🎉 ¡Felicidades Jugador 2! Adivinaste la palabra '{palabra_secreta.upper()}'!\n\n"
                           f"🏆 Marcador: Jugador 1: {puntos_jugador1} | Jugador 2: {puntos_jugador2}")
        preguntar_reinicio()
        return
    
    # Verificar victoria del Jugador 1
    if vidas <= 0:
        puntos_jugador1 += 1
        total_palabras_jugadas += 1
        messagebox.showinfo("¡Victoria del Jugador 1!", 
                           f"💀 ¡Jugador 1 gana! El Jugador 2 no adivinó la palabra: '{palabra_secreta.upper()}'\n\n"
                           f"🏆 Marcador: Jugador 1: {puntos_jugador1} | Jugador 2: {puntos_jugador2}")
        preguntar_reinicio()
        return

def preguntar_reinicio():
    print(f"🔍 Debug - Palabras restantes: {len(palabras_secretas)}")
    print(f"🔍 Debug - Palabras originales: {len(palabras_originales)}")
    print(f"🏆 Debug - Puntuación: J1={puntos_jugador1}, J2={puntos_jugador2}, Total={total_palabras_jugadas}")
    
    # Verificar si se completaron las 5 palabras
    if total_palabras_jugadas >= 5:
        mostrar_resultado_final()
        return
    
    # Verificar si quedan palabras para jugar
    if len(palabras_secretas) > 0:
        respuesta = messagebox.askyesno("Continuar", 
            f"¿Querés continuar con la siguiente palabra?\n\n"
            f"🏆 Marcador: Jugador 1: {puntos_jugador1} | Jugador 2: {puntos_jugador2}\n"
            f"📊 Partidas jugadas: {total_palabras_jugadas}/5\n"
            f"Palabras restantes: {len(palabras_secretas)}")
        
        if respuesta:
            # Continuar con la siguiente palabra
            print("✅ Usuario eligió continuar")
            iniciar_juego()
            return
        else:
            # Preguntar si quiere empezar de nuevo
            nuevo_juego = messagebox.askyesno("Nuevo Juego", 
                "¿Querés empezar un nuevo juego?\n\n"
                "SÍ = Crear nuevas palabras (se reinicia marcador)\n"
                "NO = Salir del juego")
            
            if nuevo_juego:
                print("✅ Usuario eligió crear nuevas palabras")
                reiniciar_completamente()
            else:
                print("✅ Usuario eligió salir")
                root.quit()
            return
    
    # Si no quedan palabras pero no se completaron 5 partidas
    print("⚠️ No quedan más palabras")
    respuesta = messagebox.askyesno("Fin de palabras", 
        f"¡Se acabaron las palabras!\n\n"
        f"🏆 Marcador actual: Jugador 1: {puntos_jugador1} | Jugador 2: {puntos_jugador2}\n"
        f"📊 Partidas jugadas: {total_palabras_jugadas}/5\n\n"
        f"¿Querés jugar otra vez?")
    
    if respuesta:
        usar_mismas = messagebox.askyesno("Palabras", 
            "¿Querés usar las mismas palabras secretas?\n\n"
            "SÍ = Usar las mismas 5 palabras (continuar marcador)\n"
            "NO = Crear nuevas palabras (reiniciar marcador)")
        
        if usar_mismas:
            # Restaurar las palabras originales
            print("✅ Usuario eligió usar mismas palabras")
            restaurar_palabras_originales()
            iniciar_juego()
        else:
            # Crear nuevas palabras
            print("✅ Usuario eligió crear nuevas palabras")
            reiniciar_completamente()
    else:
        print("✅ Usuario eligió salir")
        root.quit()

def mostrar_resultado_final():
    """Muestra el resultado final cuando se completan las 5 partidas"""
    if puntos_jugador1 > puntos_jugador2:
        ganador = "🏆 ¡JUGADOR 1 GANA!"
        mensaje = f"¡El Jugador 1 es el campeón!\n\nSus palabras fueron muy difíciles de adivinar."
        color = "#E74C3C"
    elif puntos_jugador2 > puntos_jugador1:
        ganador = "🏆 ¡JUGADOR 2 GANA!"
        mensaje = f"¡El Jugador 2 es el campeón!\n\n¡Excelente habilidad adivinando palabras!"
        color = "#27AE60"
    else:
        ganador = "🤝 ¡EMPATE!"
        mensaje = f"¡Ambos jugadores son igual de buenos!"
        color = "#F39C12"
    
    resultado = messagebox.showinfo("🎯 RESULTADO FINAL", 
        f"{ganador}\n\n"
        f"📊 Marcador Final:\n"
        f"Jugador 1: {puntos_jugador1} victorias\n"
        f"Jugador 2: {puntos_jugador2} victorias\n\n"
        f"{mensaje}")
    
    # Preguntar si quieren jugar de nuevo
    nuevo_juego = messagebox.askyesno("Nueva Partida", 
        "¿Querés jugar una nueva partida?\n\n"
        "SÍ = Reiniciar con nuevas palabras\n"
        "NO = Salir del juego")
    
    if nuevo_juego:
        reiniciar_completamente()
    else:
        root.quit()

def restaurar_palabras_originales():
    """Restaura la lista de palabras originales para jugar de nuevo"""
    global palabras_secretas, total_palabras_jugadas
    print(f"🔄 Restaurando palabras originales: {palabras_originales}")
    palabras_secretas = palabras_originales.copy()
    total_palabras_jugadas = 0  # Reiniciar contador de partidas
    print(f"🔄 Palabras restauradas: {palabras_secretas}")
    print(f"🔄 Total de palabras disponibles: {len(palabras_secretas)}")
    print(f"🔄 Contador de partidas reiniciado: {total_palabras_jugadas}")

def reiniciar_completamente():
    """Reinicia completamente el juego para ingresar nuevas palabras"""
    global palabras_secretas, palabras_originales, palabra_secreta, letras_adivinadas, letras_correctas, vidas
    global label_palabra, label_vidas, entrada_letra, btn_adivinar, label_alfabeto, label_ahorcado
    global instrucciones, entrada, btn_agregar, btn_start, label_puntuacion
    global puntos_jugador1, puntos_jugador2, total_palabras_jugadas  # RESETEAR puntuación

    print("🆕 Reiniciando completamente para nuevas palabras...")
    
    # Limpiar todas las variables del juego
    palabras_secretas = []
    palabras_originales = []
    palabra_secreta = ""
    letras_adivinadas = set()
    letras_correctas = set()
    vidas = 5
    
    # RESETEAR puntuación
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    total_palabras_jugadas = 0
    
    # Resetear variables de widgets (INCLUYENDO btn_start y label_puntuacion)
    label_palabra = None
    label_vidas = None
    entrada_letra = None
    btn_adivinar = None
    label_alfabeto = None
    label_ahorcado = None
    instrucciones = None
    entrada = None
    btn_agregar = None
    btn_start = None
    label_puntuacion = None
    
    # Limpiar interfaz
    limpiar_interfaz_completa()
    
    # Volver a la interfaz inicial
    crear_interfaz_inicial()

def limpiar_interfaz_completa():
    """Limpia toda la interfaz excepto el botón de reglas"""
    print("🧹 Limpiando interfaz completa...")
    widgets_conservar = []
    
    # Buscar el botón de reglas para conservarlo
    for widget in root.winfo_children():
        try:
            if hasattr(widget, 'cget') and widget.cget('text') == "Reglas del Juego":
                widgets_conservar.append(widget)
                print("✅ Conservando botón de reglas")
        except:
            pass
    
    # Destruir todos los widgets excepto los que queremos conservar
    for widget in root.winfo_children():
        if widget not in widgets_conservar:
            try:
                widget.destroy()
            except:
                pass
    
    print("✅ Interfaz limpia")

def crear_interfaz_inicial():
    global instrucciones, entrada, btn_agregar, imagen_portada
    
    print(f"🎮 Creando interfaz inicial - Palabras actuales: {len(palabras_secretas)}")
    
    # Cargar y mostrar imagen de portada
    if cargar_imagen_portada() and imagen_portada:
        label_portada = tk.Label(root, image=imagen_portada, bg="white")
        label_portada.pack(pady=(60, 60))
    else:
        # Si no hay imagen, mostrar título grande
        titulo_principal = tk.Label(root, text="🎯 JUEGO DEL AHORCADO 🎯",
                                   bg="white", font=("Montserrat", 20, "bold"),
                                   fg="#2C3E50")
        titulo_principal.pack(pady=(40, 10))
        
        subtitulo = tk.Label(root, text="2 Jugadores",
                            bg="white", font=("Montserrat", 14),
                            fg="#7F8C8D")
        subtitulo.pack(pady=(0, 20))
    
    # Etiqueta de instrucciones
    texto_instrucciones = "Jugador 1: Ingresá 5 palabras secretas"
    if palabras_secretas:
        texto_instrucciones = f"Palabras agregadas: {len(palabras_secretas)}/5"
    
    instrucciones = tk.Label(root, text=texto_instrucciones,
                            bg="white", font=("Montserrat", 12, "bold"))
    instrucciones.pack(pady=(20, 10))

    # Campo de entrada
    entrada = tk.Entry(root, font=("Montserrat", 12), width=20)
    entrada.pack(pady=10)
    entrada.focus()

    # Botón para agregar palabra - siempre habilitado en interfaz inicial
    btn_agregar = tk.Button(root, text="Agregar Palabra", command=agregar_palabra, 
                           bg="#3498DB", fg="white", font=("Montserrat", 12, "bold"),
                           padx=20, pady=5)
    btn_agregar.pack(pady=10)
    
    # Permitir Enter para agregar palabra
    entrada.bind('<Return>', lambda event: agregar_palabra())
    
    # CORRECCIÓN: No verificar palabras aquí, el botón se creará dinámicamente en agregar_palabra()
    # El botón "Iniciar Juego" se crea automáticamente cuando se llegue a 5 palabras
    
    print("✅ Interfaz inicial creada")

# Crear botón para mostrar reglas
btn_reglas = tk.Button(root, text="Reglas del Juego", command=mostrar_reglas, 
                      bg="#E74C3C", fg="white", font=("Montserrat", 10, "bold"),
                      padx=15, pady=5)
btn_reglas.place(x=10, y=10)

# Función para verificar imágenes disponibles
def verificar_imagenes():
    """Verifica qué imágenes están disponibles en la carpeta assets"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(script_dir, "assets")
    
    print(f"📁 Buscando en: {assets_path}")
    
    if not os.path.exists(assets_path):
        print("❌ La carpeta 'assets' no existe")
        return False
    
    archivos = os.listdir(assets_path)
    print(f"📋 Archivos encontrados: {archivos}")
    
    imagenes_encontradas = []
    for i in range(6):
        nombres_posibles = [f"ahorcado_{i}.png", f"ahorcado{i}.png", f"hangman_{i}.png"]
        for nombre in nombres_posibles:
            if nombre in archivos:
                imagenes_encontradas.append(nombre)
                break
    
    print(f"🖼️ Imágenes del ahorcado encontradas: {imagenes_encontradas}")
    return len(imagenes_encontradas) > 0

# Verificar imágenes al inicio
verificar_imagenes()

# Iniciar con la interfaz inicial
crear_interfaz_inicial()

# Iniciar el loop principal
root.mainloop()