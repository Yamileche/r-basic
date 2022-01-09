#Variables
x = pi/2
x
y <- cos(pi/4)
y
19 -> z

#Funciones
x = 4
doble = function(x){x*2}
doble(x)
product = function(x,y){
  x*y
}
product(9,4)


ls()#lista de variables y funciones
rm(porduct) #remover cosas
rm(list = ls()) #Remover todo

#Ejercicio

opBasic = function(a, b){
  print(paste(sprintf("%0.2f+%0.2f = %0.2f", a, b, a+b)))
}
opBasic(5.5, 6)

