from collections import deque
from usuario import Usuario
from display import fmt_cop, titulo_a_mostrar
from datetime import datetime

class Consultorio:                          #Se crea la clase Consultorio (el molde)
    nombre: str = ''                        #Se inicializa

    # Colas de atencion urgente
    cola_usuario_urgente = deque()
    cola_usuario_extracciones = deque()
    cola_usuario_general = deque()
    

    def ordenar_cola(self, cola: deque) -> deque:
        return deque(sorted(cola, key=lambda x: datetime.strptime(x.fecha, "%d/%m/%Y")))


    def encolar_usuario(self, usuario:Usuario):                         
        if usuario.prioridad == "2"                                         :                       #Se verifica que sea urgente(2) y ademas si tiene extraccion, el usuario se almacene en esta cola
            self.cola_usuario_urgente.append(usuario)                                               #Se agrega usuario a la cola urgente
            self.cola_usuario_urgente = self.ordenar_cola(self.cola_usuario_urgente)
            return

        elif usuario.tip_atencion == "Extracción":                                                  #Se verifica si el usuario tiene extracciones
            self.cola_usuario_extracciones.append(usuario)                                          #Se agrega usuario a la cola extraccion
            self.cola_usuario_extracciones = self.ordenar_cola(self.cola_usuario_extracciones)
            return
        else:
            self.cola_usuario_general.append(usuario)                                               #Se agrega usuario a la cola general
            self.cola_usuario_general = self.ordenar_cola(self.cola_usuario_general)
            return
    

    def mostrar_usuarios_pendientes_ordenados(self):
        titulo_a_mostrar("  LISTA DE USUARIOS.")

        todos_los_usuarios = []

        # Recorre cola urgente
        for usuario in self.cola_usuario_urgente:
            todos_los_usuarios.append((usuario, "URGENTE"))

        # Recorre cola extracciones
        for usuario in self.cola_usuario_extracciones:
            todos_los_usuarios.append((usuario, "EXTRACCIÓN"))

        # Recorre cola general
        for usuario in self.cola_usuario_general:
            todos_los_usuarios.append((usuario, "GENERAL"))

        # Verifica si hay usuarios
        if not todos_los_usuarios:
            print(f"\n** La lista de usuarios está vacía.")
            return

        # Ordena por fecha de más cercana a más lejana
        todos_los_usuarios.sort(key=lambda x: datetime.strptime(x[0].fecha, "%d/%m/%Y"))

        # Encabezado de la tabla
        print(f"{'#':<4} {'Cédula':<12} {'Nombre':<22} {'Telefono':<11} {'Tipo cliente':<15} {'Tipo atencion':<15} "
            f"{'Cant':>6} {'Prioridad':>12}  {'Fecha':<12} {'Valor cita':>10} {'Valor atencion':>16} {'Total':>12} {'Cola':>12}")

        # Muestra cada usuario en la tabla
        for i, (usuario, grupo) in enumerate(todos_los_usuarios, start=1):
            print(f"{i:<4} {usuario.cedula:<12} {usuario.nombre:<22} {usuario.telefono:<11} {usuario.tip_usuario:<15} {usuario.tip_atencion:<15} "
                f"{usuario.cantidad:>6} {usuario.prioridad:>12}  {usuario.fecha:<12} {fmt_cop(usuario.valor_cita):>10} {fmt_cop(usuario.valor_atencion):>16} "
                f"{fmt_cop(usuario.total):>12} {grupo:>12}")


    def atender_usuario_urgente(self):
        print("ok")
        if self.cola_usuario_urgente:
            usuario = self.cola_usuario_urgente.popleft()
            print(f"En el consultorio se atiende al usuario: {usuario.nombre} "                 #Muestra en en el terminal el usuario que se esta atendiendo
                  f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
            return 
        else:
            print(f"** No hay usuarios urgentes en cola.")                                                        #Mustra mensaje
            return
        
    def atender_usuario_extraccion(self):
        if self.cola_usuario_extracciones:
            usuario = self.cola_usuario_extracciones.popleft()
            print(f"En el consultorio se atiende al usuario: {usuario.nombre} "                 #Muestra en en el terminal el usuario que se esta atendiendo
                  f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
            return 
        else:
            print(f"** No hay usuarios urgentes en cola.")                                                        #Mustra mensaje
            return
        
    def atender_usuario_general(self):
        if self.cola_usuario_general:
            usuario = self.cola_usuario_general.popleft()
            print(f"En el consultorio se atiende al usuario: {usuario.nombre} "                 #Muestra en en el terminal el usuario que se esta atendiendo
                  f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
            return 
        else:
            print(f"** No hay usuarios urgentes en cola.")                                                        #Mustra mensaje
            return
        

    def consultar_siguiente_usuario_urgente(self):
        if self.cola_usuario_urgente:
            usuario = self.cola_usuario_urgente[0]
            print(f"** El siguiente usuario es: {usuario.nombre} "                          #Muestra en en el terminal el usuario que se va a atender
                f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
            return 
        else:
            print(f"** No hay usuarios urgentes en cola.")                                                        #Mustra mensaje
            return

    
    def consultar_siguiente_usuario_extraccion(self):
        if self.cola_usuario_extracciones:
            usuario = self.cola_usuario_extracciones[0]
            print(f"** El siguiente usuario es: {usuario.nombre} "                          #Muestra en en el terminal el usuario que se va a atender
                f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
            return 
        else:
            print(f"** No hay usuarios para extracción en cola.")                                                        #Mustra mensaje
            return
    
    def consultar_siguiente_usuario_general(self):
        if self.cola_usuario_general:
            usuario = self.cola_usuario_general[0]
            print(f"** El siguiente usuario es: {usuario.nombre} "                          #Muestra en en el terminal el usuario que se va a atender
                f"con procedimiento de {usuario.tip_atencion} por {usuario.tip_usuario}") 
            return 
        else:
            print(f"** No hay usuarios general en cola.")                                                        #Mustra mensaje
            return

    def estadistica_de_usuarios(self):
        #Variables para crear la estadistica
        total_usuarios_urgentes_pendientes = 0
        total_usuarios_extracciones_pendientes = 0
        total_usuarios_general_pendientes = 0
        total_usuarios_pendientes = 0
        numero_de_calzas_a_realizar = 0
        numero_extracciones_dentales = 0
        numero_limpiezas_a_realizar = 0
        numero_valoraciones_a_realizar = 0
        total_valor_procedimientos_pendientes = 0

        
        for usuario in self.cola_usuario_urgente:                           #Ciclo for para recorrer la cola 
            total_usuarios_urgentes_pendientes += 1                         #Contabiliza usuarios
            if usuario.tip_atencion == "Limpieza":                          #Consulta el tipo de atencion del usuario
                numero_limpiezas_a_realizar += usuario.cantidad             #Si es "Limpieza" incrementa la variable para la estadistica
            if usuario.tip_atencion == "Calzas":                            #Consulta el tipo de atencion del usuario
                numero_de_calzas_a_realizar += usuario.cantidad             #Si es "Calzas" incrementa la variable para la estadistica
            if usuario.tip_atencion == "Diagnóstico":                       #Consulta el tipo de atencion del usuario
                numero_valoraciones_a_realizar += usuario.cantidad          #Si es "Diagnostico" incrementa la variable para la estadistica
            numero_extracciones_dentales += usuario.cant_extraccion         #realiza conteo de extracciones dentales para la estadistica
            total_valor_procedimientos_pendientes += usuario.total          #Suma el valor total de cada usuario para la estadistica


        for usuario in self.cola_usuario_extracciones:                      #Recorre la cola y suma el atributo deseado
            total_usuarios_extracciones_pendientes += 1                     #Contabiliza usuarios
            numero_extracciones_dentales += usuario.cant_extraccion         #realiza conteo de extracciones dentales para la estadistica
            total_valor_procedimientos_pendientes += usuario.total          #Suma el valor total de cada usuario para la estadistica

        for usuario in self.cola_usuario_general:                           #Ciclo for para recorrer la cola 
            total_usuarios_general_pendientes += 1                          #Contabiliza usuarios
            if usuario.tip_atencion == "Limpieza":                          #Consulta el tipo de atencion del usuario
                numero_limpiezas_a_realizar += usuario.cantidad             #Si es "Limpieza" incrementa la variable para la estadistica
            if usuario.tip_atencion == "Calzas":                            #Consulta el tipo de atencion del usuario
                numero_de_calzas_a_realizar += usuario.cantidad             #Si es "Calzas" incrementa la variable para la estadistica
            if usuario.tip_atencion == "Diagnóstico":                       #Consulta el tipo de atencion del usuario
                numero_valoraciones_a_realizar += usuario.cantidad          #Si es "Diagnostico" incrementa la variable para la estadistica
            numero_extracciones_dentales += usuario.cant_extraccion         #realiza conteo de extracciones dentales para la estadistica
            total_valor_procedimientos_pendientes += usuario.total          #Suma el valor total de cada usuario para la estadistica
        
        total_usuarios_pendientes = total_usuarios_urgentes_pendientes + total_usuarios_extracciones_pendientes  #Suma para saber la cantidad de usuarios pendientes
        total_usuarios_pendientes = total_usuarios_pendientes + total_usuarios_general_pendientes

        titulo_a_mostrar("  ESTADISTICAS.")         #Muestrar titulo en terminal desde el modulo display.py 
        #Mustra la tabla de estadisticas del consultorio                                                       
        print(f"{'- Total usuarios urgentes pendientes es: ':<44}{total_usuarios_urgentes_pendientes :>10}")
        print(f"{'- Total usuarios por extrac pendientes es: ':<40}{total_usuarios_extracciones_pendientes:>11}")
        print(f"{'- Total usuarios general es: ':<44}{total_usuarios_extracciones_pendientes:>10}")
        print(f"{'- El total de usuarios pendientes es: ':<44}{total_usuarios_pendientes:>10}")
        print(f"{'- Numero de limpiezas a realizar es : ':<44}{numero_limpiezas_a_realizar:>10}")
        print(f"{'- Numero de calzas a realizar es: ':<44}{numero_de_calzas_a_realizar:>10}")
        print(f"{'- Numero de extracciones a realizar es: ':<44}{numero_extracciones_dentales:>10}")
        print(f"{'- Numero de diagnosticos a realizar es: ':<44}{numero_valoraciones_a_realizar:>10}")
        print(f"{'- El valor total de los procedimientos es: ':<44}{fmt_cop(total_valor_procedimientos_pendientes):>10}")
        return  #Sale de la funcion