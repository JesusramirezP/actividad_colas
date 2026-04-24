from collections import deque
from usuario import Usuario

class Consultorio:
    nombre: str = ''

    # Colas urgentes
    cola_urgente_particular = deque()
    cola_urgente_eps = deque()
    cola_urgente_prepagada = deque()
    
    # Colas normales
    cola_normal_particular = deque()
    cola_normal_eps = deque()
    cola_normal_prepagada = deque()

    #Punteros
    colas_urgentes_cont = 0
    colas_normales_cont = 0

    #Booleans
    grup_urgentes = True
    grup_normales = False

    def encolar_usuario(self, usuario:Usuario):
        if usuario.prioridad == "2":
            if usuario.tip_usuario == "Particular":
                self.cola_urgente_particular.append(usuario)
            elif usuario.tip_usuario == "EPS":
                self.cola_urgente_eps.append(usuario)
            elif usuario.tip_usuario == "Prepagada":
                self.cola_urgente_prepagada.append(usuario)

        elif usuario.prioridad == "1":
            if usuario.tip_usuario == "Particular":
                self.cola_normal_particular.append(usuario)
            elif usuario.tip_usuario == "EPS":
                self.cola_normal_eps.append(usuario)
            elif usuario.tip_usuario == "Prepagada":
                self.cola_normal_prepagada.append(usuario)   
        

    def atender_siguiente_usuario(self):
        colas_urgentes = [
        self.cola_urgente_particular,
        self.cola_urgente_prepagada,
        self.cola_urgente_eps,
        ]
        colas_normales = [
        self.cola_normal_particular,
        self.cola_normal_prepagada,
        self.cola_normal_eps,
        ]

    # Intentar atender urgente si aún quedan turnos urgentes
        if self.grup_urgentes:
            atendido = False
            for cola in colas_urgentes:
                if cola:
                    usuario = cola.popleft()
                    print(f"En el consultorio {self.nombre}: Se atiende al usuario: "
                        f"{usuario.nombre} con procedimiento de {usuario.tip_atencion}")
                    atendido = True
                    break

        if atendido:
            self.colas_urgentes_cont += 1
            if self.colas_urgentes_cont >= 3:
                self.colas_urgentes_cont = 0
                self.grup_urgentes = False  # Tras 3 urgentes, toca 1 normal
            return
        else:
            # No hay urgentes, pasar directo a normales
            self.colas_urgentes_cont = 0
            self.grup_urgentes = False

        # Atender 1 normal
        if not self.grup_urgentes:
            atendido = False
            for cola in colas_normales:
                if cola:
                    usuario = cola.popleft()
                    print(f"En el consultorio {self.nombre}: Se atiende al usuario: "
                        f"{usuario.nombre} con procedimiento de {usuario.tip_atencion}")
                    atendido = True
                    break

            if not atendido:
                print("No hay usuarios en ninguna cola")
            
            self.grup_urgentes = True  # Vuelve al ciclo de urgentes

        
    
    def consultar_siguiente_usuario(self):
        colas_urgentes = [
        self.cola_urgente_particular,
        self.cola_urgente_prepagada,
        self.cola_urgente_eps,
        ]
        colas_normales = [
        self.cola_normal_particular,
        self.cola_normal_prepagada,
        self.cola_normal_eps,
        ]

        hay_urgentes = any(cola for cola in colas_urgentes)
        hay_normales = any(cola for cola in colas_normales)

        # Si no hay nadie en ninguna cola
        if not hay_urgentes and not hay_normales:
            print(f"En el consultorio {self.nombre}: No hay usuarios en cola")
            return

        if self.grup_urgentes:
            if hay_urgentes:
                for cola in colas_urgentes:
                    if cola:
                        usuario = cola[0]
                        print(f"En el consultorio {self.nombre}: El siguiente usuario es: "
                            f"{usuario.nombre} con procedimiento de {usuario.tip_atencion} "
                            f"- Grupo: URGENTE")
                        return
            elif hay_normales:
                for cola in colas_normales:
                    if cola:
                        usuario = cola[0]
                        print(f"En el consultorio {self.nombre}: El siguiente usuario es: "
                            f"{usuario.nombre} con procedimiento de {usuario.tip_atencion} "
                            f"- Grupo: NORMAL (no hay urgentes en cola)")
                        return
        else:
            if hay_normales:
                for cola in colas_normales:
                    if cola:
                        usuario = cola[0]
                        print(f"En el consultorio {self.nombre}: El siguiente usuario es: "
                            f"{usuario.nombre} con procedimiento de {usuario.tip_atencion} "
                            f"- Grupo: NORMAL")
                        return
            elif hay_urgentes:
                for cola in colas_urgentes:
                    if cola:
                        usuario = cola[0]
                        print(f"En el consultorio {self.nombre}: El siguiente usuario es: "
                            f"{usuario.nombre} con procedimiento de {usuario.tip_atencion} "
                            f"- Grupo: URGENTE (no hay normales en cola)")
                        return

    def estadistica_de_usuarios(self):
        total_usuarios_pendientes = 0
        total_usuarios_urgentes_pendientes = 0
        total_usuarios_no_urgentes_pendientes = 0
        numero_de_calzas_a_realizar = 0
        numero_extracciones_dentales = 0
        numero_limpiezas_a_realizar = 0
        numero_valoraciones_a_realizar = 0
        total_valor_procedimientos_pendientes = 0

        colas_urgentes = [
            self.cola_urgente_particular,
            self.cola_urgente_prepagada,
            self.cola_urgente_eps,
        ]
        colas_normales = [
            self.cola_normal_particular,
            self.cola_normal_prepagada,
            self.cola_normal_eps,
        ]

        for cola in colas_urgentes:
            for usuario in cola:
                total_usuarios_urgentes_pendientes += 1
                if usuario.tip_atencion == "Limpieza":
                    numero_limpiezas_a_realizar += usuario.cantidad
                if usuario.tip_atencion == "Calzas":
                    numero_de_calzas_a_realizar += usuario.cantidad
                if usuario.tip_atencion == "Diagnóstico":
                    numero_valoraciones_a_realizar += usuario.cantidad
                numero_extracciones_dentales += usuario.cant_extraccion
                total_valor_procedimientos_pendientes += usuario.total

        for cola in colas_normales:
            for usuario in cola:
                total_usuarios_no_urgentes_pendientes += 1
                if usuario.tip_atencion == "Limpieza":
                    numero_limpiezas_a_realizar += usuario.cantidad
                if usuario.tip_atencion == "Calzas":
                    numero_de_calzas_a_realizar += usuario.cantidad
                if usuario.tip_atencion == "Diagnóstico":
                    numero_valoraciones_a_realizar += usuario.cantidad
                numero_extracciones_dentales += usuario.cant_extraccion
                total_valor_procedimientos_pendientes += usuario.total

        total_usuarios_pendientes = total_usuarios_urgentes_pendientes + total_usuarios_no_urgentes_pendientes
              
        print(f"Total usuarios urgentes pèndientes es: {total_usuarios_urgentes_pendientes} ")
        print(f"Total usuarios no urgentes pendientes es: {total_usuarios_no_urgentes_pendientes}")
        print(f"El total de usuarios pendientes es: {total_usuarios_pendientes}")
        print(f"El valor total de los procedimientos es: {total_valor_procedimientos_pendientes}")
        print(f"Numero de limpiezas a realizar es : {numero_limpiezas_a_realizar}")
        print(f"Numero de calzas a realizar es: {numero_de_calzas_a_realizar}")
        print(f"Numero de extracciones a realizar es: {numero_extracciones_dentales}")
        print(f"Numero de diagnosticos a realizar es: {numero_valoraciones_a_realizar}")
        


        return