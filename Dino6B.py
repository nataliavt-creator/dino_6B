# 🦖 Biblioteca de dinosaurios 🦕

#Lista prellenada de dinosaurios con su información
dinosaurios = [
     ("Tiranosaurio Rex","Carnívoro","12 metros","cretásico","Tenía brazos muy cortos pero mandibulas poderosas"),
    ("Triceratops","Herbívoro","9 metros","Cretásico","Tenía 3 cuernos y un gran volante oséo"),
    ("Velociraptor","Carnívoro","2 metros","Cretácico","Tenía una garra en forma de hoz en cada pata"),
    ("Brachiosaurio","Herbívoro","25 metros","Jurásico","Tenía un cuello larguísimo para alcanzar hojas altas"),
    ("Stegosaurio","Herbívoro","9 metros","Jurásico","Tenía placas en la espalda y púas en la cola"),
    ("Spinosaurus","Carnívoro","15 metros","Cretácico","Tenía una vela en la espalda y púas en la cola"),
    ("Ankylosaurus","Hervivoro","8 metros","Cretácico","Estaba acorazado y tenía una maza en la cola"),
    ("Pteranodon","Carnívoro","7 metros de ala a ala","Cretácico","Era un reptil volador, pero no era un dinosaurio"),
    ("Diplodocus","Herbívoro","10 metros","Jurásico","Uno de los dinosaurios más largos que existieron"),
    ("Parasaurolophus","Herbívoro","10 metros","Cretácico","Tenía una cresta hueca para hacer sonidos"),
]
   
print("=" * 60)
print("🦖 Bienvenido a la biblioteca de dinosaurios 🦕")
print("=" * 60)
print("Pregunta por cualquier dinosaurio y te daré su información")
print("Escribe ´lista´ para ver todos los dinosaurios disponibles. ")
print("Escribe ´salir´ para terminar./n")

while True:
    consulta=input("¿Que dinosaurio quieres consultar?").strip().lower()
    
    if consulta =="salir":
          print("👋 ¡Hasta luego, explorador de dinosaurios!")
          break
      
      if consulta =="lista":
          print("/n📑 Dinosaurios disponibles:")
          for i, (nombre, _,_,_,_) in enumerate(dinosaurios, 1):
              print(f"{i}. {nombre}")
          print()
          continue
      
      # Buscar el dinosaurio en la lista
      encontrado=False
      for nombre, dieta, tamaño, periodo, daro_curioso in dinosaurio:
          if consulta in nombre.lower():
              print("/n" + "=" * 60)
              print(f"🦕 {nombre}")
              print("=" * 60)
              print(f"🍖 Dieta: {dieta}")
              print(f"🧻 Tamaño: {tamaño}")
              print(f"⏰ Periodo: {periodo}")
              print(f"💡 Dato curioso {dato_curioso}")
              print("=" * 60 + "/n")
              encontrado=True
              break
              
    if not encontrado:
        print(f"✖️ No encontré la información sobre ¨{consulta}¨.")
        print("💡 Intenta escribir "lista" para ver los dinosaurios disponibles. /n")