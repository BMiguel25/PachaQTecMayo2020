//Suma de n n�meros : RPC
Proceso suma_n_numeros 

	Escribir "Ingrese un N�mero (0 para Calcular)";
	Leer a;
	tot<-0
	Mientras a<>0 Hacer
		tot<-tot+a;
		Escribir "Ingrese otro Numero (0 para Calcular)";
		Leer a;
	FinMientras
	Escribir "Total: ",tot;
FinProceso
