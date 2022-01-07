###Problema 1********************************
s=250*10^6

#Segundos en una hora
h = 60 * 60
#segundos al día
d = h * 24
# segundo al año (no bisiesto)
a = 365 * d

#Pasaron 7 años se le debe quitar dos días,
# además e estamos en el año 2018+7 = 2025
diasRes = s%%a -2 * d
# han pasado 29075200 segundos a partir de que comienza 2025
dias = diasRes%/%d
# ademáss 336 dias (sin contar lo restante), es decir es 2 de diciembre
horas = (diasRes%%d)%/%h
# es la hora 12
minutos = ((diasRes%%d)%%h)%/%60
# 26 minutos (sin contar el resto), ie, estamos en el minuto 27
segundos = (((diasRes%%d)%%h)%%60)%%60
# 40 segundos
#La fecha es 2-12-2025, 12:27:40
rm(list = ls())


##Problema 2**************************************
grado1 = function(a, b){
  #ax+b=0, note que no hay control de flujo
  -b/a
}
grado1(5,3)
grado1(7,4)
grado1(1,0)

##Problema 3************************************
d=3*exp(1)-pi
round(d,3)

##Problema 4***********************************

z = Mod((2+3i)^2/(5+8i))
round(z,3)

