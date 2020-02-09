#Lo primero que tenemos que hacer es importar el módulo para trabajar con sockets
import socket

#Creamos un objeto socket para el servidor. 
#1er param:socket_family: es la familia de protocolos que es usada como mecanismo de transporte. 
#2do param: socket_type: tipo de comunicación entre los 2 extremos de la conexion.
#protocolos orientados a conexiones. 
#el protocolo determinado es TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Para mejorar el servicio, obtenemos el nombre del equipo para que luego sepamos la dirección, sin tener 
#que cambiarla cada vez que se cambie de red, todo esto con las funciones que nos trae el módulo de sockets.
nombre_equipo = socket.gethostname()
localhost = socket.gethostbyname(nombre_equipo)


#Con el metodo bind vincula una dirección,
#le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind((localhost, 9999))

#Con el método listen aceptamos conexiones entrantes, y ademas aplicamos como parametro
#el numero de conexiones entrantes que vamos a aceptar.
s.listen(1)

#Instanciamos un objeto sc (socket cliente) esta función acepta una conexión de cliente 
#TCP esperando hasta que la conexión llegue.
sc, addr= s.accept()



while True:

    #El método recv lo usamos para recibir el mensaje que nos esta llegando del cliente, es decir, 
    #la respuesta del mismo, con el parámetro 1024, que es máximo de bit que puede recibir o enviar.
    
    recibido = sc.recv(1024)
    resp='Peticion recibida'
    #Si el mensaje recibido es la palabra close se cierra la aplicacion

    #Si se reciben los datos nos muestra la IP, puerto y el mensaje recibido
    print ("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1])+"dice:",recibido)
    #Devolvemos el mensaje al cliente
    sc.sendall(resp.encode('utf-8'))
 
print ("Adios.")

#Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()