import tkinter as tk
import time
import Botones as Botones
import threading
from tkinter import messagebox

class Interfaz(tk.Tk):
	def __init__(self):
		super().__init__()
		self.iniciar_gui()
		

		
	def iniciar_gui(self):
		self.title("JUEGO DE MEMORIA")
		self.config(background="RoyalBLue1")
		self.geometry("900x700")
		self.resizable(0,0)
		self.frame=tk.Frame(self,background="blue")
		self.frame.pack()
		
		self.identificador_btn_primero=""
		self.identificador_btn_segundo=""
		self.configurar_btn_primero=""
		self.configurar_btn_segundo=""
		self.verificar=0
		
		self.construccion_botones()
	def construccion_botones(self):
		self.btn_1=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_1.grid(row=0,column=0,padx=5,pady=5)

		self.btn_2=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_2.grid(row=0,column=1,padx=5,pady=5)

		self.btn_3=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_3.grid(row=0,column=2,padx=5,pady=5)

		self.btn_4=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_4.grid(row=1,column=0,padx=5,pady=5)

		self.btn_5=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_5.grid(row=1,column=1,padx=5,pady=5)

		self.btn_6=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_6.grid(row=1,column=2,padx=5,pady=5)

		self.btn_7=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_7.grid(row=2,column=0,padx=5,pady=5)

		self.btn_8=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_8.grid(row=2,column=1,padx=5,pady=5)

		self.btn_9=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_9.grid(row=2,column=2,padx=5,pady=5)

		self.btn_10=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_10.grid(row=3,column=0,padx=5,pady=5)

		self.btn_11=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_11.grid(row=3,column=1,padx=5,pady=5)

		self.btn_12=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_12.grid(row=3,column=2,padx=5,pady=5)

		self.btn_13=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_13.grid(row=4,column=0,padx=5,pady=5)

		self.btn_14=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_14.grid(row=4,column=1,padx=5,pady=5)

		self.btn_15=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_15.grid(row=4,column=2,padx=5,pady=5)

		self.btn_16=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_16.grid(row=5,column=0,padx=5,pady=5)

		self.btn_17=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_17.grid(row=5,column=1,padx=5,pady=5)

		self.btn_18=tk.Button(self.frame,text="MOSTRAR",background="sienna3",font=("Courier",14,"bold"),width=12,height=4)
		self.btn_18.grid(row=5,column=2,padx=5,pady=5)
		self.instrucciones_botones()

	def instrucciones_botones(self):
		self.lista_datos_botones=Botones.Lista_Datos()
		self.btn_1['command']=lambda:self.Numero_btn(1)
		self.btn_2['command']=lambda:self.Numero_btn(2)
		self.btn_3['command']=lambda:self.Numero_btn(3)
		self.btn_4['command']=lambda:self.Numero_btn(4)
		self.btn_5['command']=lambda:self.Numero_btn(5)
		self.btn_6['command']=lambda:self.Numero_btn(6)
		self.btn_7['command']=lambda:self.Numero_btn(7)
		self.btn_8['command']=lambda:self.Numero_btn(8)
		self.btn_9['command']=lambda:self.Numero_btn(9)

		self.btn_10['command']=lambda:self.Numero_btn(10)
		self.btn_11['command']=lambda:self.Numero_btn(11)
		self.btn_12['command']=lambda:self.Numero_btn(12)
		self.btn_13['command']=lambda:self.Numero_btn(13)
		self.btn_14['command']=lambda:self.Numero_btn(14)
		self.btn_15['command']=lambda:self.Numero_btn(15)
		self.btn_16['command']=lambda:self.Numero_btn(16)
		self.btn_17['command']=lambda:self.Numero_btn(17)
		self.btn_18['command']=lambda:self.Numero_btn(18)
		


	def Numero_btn(self,numero_btn):
		
		
		
		if numero_btn==1:

			self.btn_1.config(text=self.lista_datos_botones[0])
			thread_btn_1=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_1.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_1.cget('text')
				self.configurar_btn_primero=self.btn_1

				
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_1.cget('text')
				self.configurar_btn_segundo=self.btn_1
	
			
		elif numero_btn==2:
		
			self.btn_2.config(text=self.lista_datos_botones[1])
			thread_btn_2=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_2.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_2.cget('text')
				self.configurar_btn_primero=self.btn_2
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_2.cget('text')
				self.configurar_btn_segundo=self.btn_2
		if numero_btn==3:	
			self.btn_3.config(text=self.lista_datos_botones[2])
			thread_btn_3=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_3.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_3.cget('text')
				self.configurar_btn_primero=self.btn_3
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_3.cget('text')
				self.configurar_btn_segundo=self.btn_3
			
		elif numero_btn==4:	
			self.btn_4.config(text=self.lista_datos_botones[3])
			thread_btn_4=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_4.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_4.cget('text')
				self.configurar_btn_primero=self.btn_4
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_4.cget('text')
				self.configurar_btn_segundo=self.btn_4
		
		elif numero_btn==5:
			self.btn_5.config(text=self.lista_datos_botones[4])
			thread_btn_5=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_5.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_5.cget('text')
				self.configurar_btn_primero=self.btn_5
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_5.cget('text')
				self.configurar_btn_segundo=self.btn_5
		
		elif numero_btn==6:	
			self.btn_6.config(text=self.lista_datos_botones[5])
			thread_btn_6=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_6.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_6.cget('text')
				self.configurar_btn_primero=self.btn_6
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_6.cget('text')
				self.configurar_btn_segundo=self.btn_6
			
		elif numero_btn==7:	
			self.btn_7.config(text=self.lista_datos_botones[6])
			thread_btn_7=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_7.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_7.cget('text')
				self.configurar_btn_primero=self.btn_7
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_7.cget('text')
				self.configurar_btn_segundo=self.btn_7
		
		elif numero_btn==8:	
			self.btn_8.config(text=self.lista_datos_botones[7])
			thread_btn_8=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_8.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_8.cget('text')
				self.configurar_btn_primero=self.btn_8
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_8.cget('text')
				self.configurar_btn_segundo=self.btn_8
	
		elif numero_btn==9:	
			self.btn_9.config(text=self.lista_datos_botones[8])
			thread_btn_9=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_9.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_9.cget('text')
				self.configurar_btn_primero=self.btn_9
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_9.cget('text')
				self.configurar_btn_segundo=self.btn_9
			
		elif numero_btn==10:
			self.btn_10.config(text=self.lista_datos_botones[9])
			thread_btn_10=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_10.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_10.cget('text')
				self.configurar_btn_primero=self.btn_10
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_10.cget('text')
				self.configurar_btn_segundo=self.btn_10
			
		elif numero_btn==11:	
			self.btn_11.config(text=self.lista_datos_botones[10])
			thread_btn_11=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_11.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_11.cget('text')
				self.configurar_btn_primero=self.btn_11
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_11.cget('text')
				self.configurar_btn_segundo=self.btn_11
		
		elif numero_btn==12:
			self.btn_12.config(text=self.lista_datos_botones[11])
			thread_btn_12=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_12.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_12.cget('text')
				self.configurar_btn_primero=self.btn_12
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_12.cget('text')
				self.configurar_btn_segundo=self.btn_12
		
		elif numero_btn==13:
			self.btn_13.config(text=self.lista_datos_botones[12])
			thread_btn_13=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_13.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_13.cget('text')
				self.configurar_btn_primero=self.btn_13
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_13.cget('text')
				self.configurar_btn_segundo=self.btn_13
			
		elif numero_btn==14:	
			self.btn_14.config(text=self.lista_datos_botones[13])
			thread_btn_14=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_14.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_14.cget('text')
				self.configurar_btn_primero=self.btn_14
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_14.cget('text')
				self.configurar_btn_segundo=self.btn_14
		
		elif numero_btn==15:	
			self.btn_15.config(text=self.lista_datos_botones[14])
			thread_btn_15=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_15.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_15.cget('text')
				self.configurar_btn_primero=self.btn_15
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_15.cget('text')
				self.configurar_btn_segundo=self.btn_15
		
		elif numero_btn==16:	
			self.btn_16.config(text=self.lista_datos_botones[15])
			thread_btn_16=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_16.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_16.cget('text')
				self.configurar_btn_primero=self.btn_16
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_16.cget('text')
				self.configurar_btn_segundo=self.btn_16
			
		elif numero_btn==17:
			self.btn_17.config(text=self.lista_datos_botones[16])
			thread_btn_17=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_17.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_17.cget('text')
				self.configurar_btn_primero=self.btn_17
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_17.cget('text')
				self.configurar_btn_segundo=self.btn_17
		
		elif numero_btn==18:
			self.btn_18.config(text=self.lista_datos_botones[17])
			thread_btn_18=threading.Thread(target=self.retardo_mostrar,args=(numero_btn,))
			thread_btn_18.start()
			if self.identificador_btn_primero=="":
				self.identificador_btn_primero=self.btn_18.cget('text')
				self.configurar_btn_primero=self.btn_18
			elif self.identificador_btn_segundo=="":
				self.identificador_btn_segundo=self.btn_18.cget('text')
				self.configurar_btn_segundo=self.btn_18
		
		app=practica(self,self.identificador_btn_primero,self.identificador_btn_segundo,self.verificar)
		app1= app.guardar_numero_pulsado(self.identificador_btn_primero,self.identificador_btn_segundo,self.verificar)
		if app1==True:
			self.verificar+=1
			
			app.configurar_btn_color(self.configurar_btn_primero,self.configurar_btn_segundo)
		if self.verificar==9:
			app=practica(self,self.identificador_btn_primero,self.identificador_btn_segundo,self.verificar)
		if self.identificador_btn_primero!="" :
			if self.identificador_btn_segundo!="":
				self.identificador_btn_primero=""
				self.identificador_btn_segundo=""



	def retardo_mostrar(self,numero_btn_mostrar):
		if numero_btn_mostrar==1:
			self.btn_1['state']=tk.DISABLED
			time.sleep(3)
			self.btn_1['state']=tk.NORMAL
			self.btn_1.config(text="MOSTRAR")
		elif numero_btn_mostrar==2:
			self.btn_2['state']=tk.DISABLED
			time.sleep(3)

			self.btn_2['state']=tk.NORMAL
			
			self.btn_2.config(text="MOSTRAR")
		elif numero_btn_mostrar==3:
			self.btn_3['state']=tk.DISABLED
			time.sleep(3)
			self.btn_3['state']=tk.NORMAL
			self.btn_3.config(text="MOSTRAR")
		elif numero_btn_mostrar==4:
			self.btn_4['state']=tk.DISABLED
			time.sleep(3)
			self.btn_4['state']=tk.NORMAL
			self.btn_4.config(text="MOSTRAR")
		elif numero_btn_mostrar==5:
			self.btn_5['state']=tk.DISABLED
			time.sleep(3)
			self.btn_5['state']=tk.NORMAL
			self.btn_5.config(text="MOSTRAR")
		elif numero_btn_mostrar==6:
			self.btn_6['state']=tk.DISABLED
			time.sleep(3)
			self.btn_6['state']=tk.NORMAL
			self.btn_6.config(text="MOSTRAR")
		elif numero_btn_mostrar==7:
			self.btn_7['state']=tk.DISABLED
			time.sleep(3)
			self.btn_7['state']=tk.NORMAL
			self.btn_7.config(text="MOSTRAR")
		elif numero_btn_mostrar==8:
			self.btn_8['state']=tk.DISABLED
			time.sleep(3)
			self.btn_8['state']=tk.NORMAL
			self.btn_8.config(text="MOSTRAR")
		elif numero_btn_mostrar==9:
			self.btn_9['state']=tk.DISABLED
			time.sleep(3)
			self.btn_9['state']=tk.NORMAL
			self.btn_9.config(text="MOSTRAR")
		elif numero_btn_mostrar==10:
			self.btn_10['state']=tk.DISABLED
			time.sleep(3)
			self.btn_10['state']=tk.NORMAL
			self.btn_10.config(text="MOSTRAR")
		elif numero_btn_mostrar==11:
			self.btn_11['state']=tk.DISABLED
			time.sleep(3)
			self.btn_11['state']=tk.NORMAL
			self.btn_11.config(text="MOSTRAR")
		elif numero_btn_mostrar==12:
			self.btn_12['state']=tk.DISABLED
			time.sleep(3)
			self.btn_12['state']=tk.NORMAL
			self.btn_12.config(text="MOSTRAR")
		elif numero_btn_mostrar==13:
			self.btn_13['state']=tk.DISABLED
			time.sleep(3)
			self.btn_13['state']=tk.NORMAL
			self.btn_13.config(text="MOSTRAR")					
		elif numero_btn_mostrar==14:
			self.btn_14['state']=tk.DISABLED
			time.sleep(3)
			self.btn_14['state']=tk.NORMAL
			self.btn_14.config(text="MOSTRAR")
		elif numero_btn_mostrar==15:
			self.btn_15['state']=tk.DISABLED
			time.sleep(3)
			self.btn_15['state']=tk.NORMAL
			self.btn_15.config(text="MOSTRAR")
		elif numero_btn_mostrar==16:
			self.btn_16['state']=tk.DISABLED
			time.sleep(3)
			self.btn_16['state']=tk.NORMAL
			self.btn_16.config(text="MOSTRAR")
		elif numero_btn_mostrar==17:
			self.btn_17['state']=tk.DISABLED
			time.sleep(3)
			self.btn_17['state']=tk.NORMAL
			self.btn_17.config(text="MOSTRAR")		
		elif numero_btn_mostrar==18:
			self.btn_18['state']=tk.DISABLED
			time.sleep(3)
			self.btn_18['state']=tk.NORMAL
			self.btn_18.config(text="MOSTRAR")			
		
		
		
class practica():
	def __init__(self,frame,btn1,btn_2,verificar):

		self.boton_prueba=tk.Button(frame,text="OK",font=("Verdana",12,"bold"),background="#1162ac",bd=12)
		self.boton_prueba.place(x=780,y=280,width=65,height=65)
		self.boton_prueba['command']=lambda:self.guardar_numero_pulsado(btn1,btn_2,verificar)
		
		

	def guardar_numero_pulsado(self,btn1,btn2,verificar):

		

			
		if verificar==9:
			
			messagebox.showinfo("INFORMACIÓN",'TERMINASTE, FELICITACIONES')

		if btn1==btn2:
			
			
			return True
		
	def configurar_btn_color(self,btn1,btn2):
		btn1.config(background="dark green")
		btn2.config(background="dark green")

	

def main():
	app=Interfaz()
	app.mainloop()

if __name__ == '__main__':
	main()