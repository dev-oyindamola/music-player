import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
from PIL import ImageTk,Image
from mutagen.mp3 import MP3
import pygame
import time


window = tk.Tk()
window.tk.call("wm","iconphoto",window._w,tk.PhotoImage(file='C:/Users/USER/Desktop/pass/music(1).png'))
# # # window.tk.call("wm","iconwindow",window._w,tk.PhotoImage(file='C:/Users/USER/Desktop/pass/song1.jpeg'))
window.geometry("500x450")
window.title("Mix Player")
pygame.mixer.init()

play_image = PhotoImage(file="C:/Users/USER/Desktop/pass/play.png")
stop_image = PhotoImage(file="C:/Users/USER/Desktop/pass/stop.png")
pause_image = PhotoImage(file="C:/Users/USER/Desktop/pass/pause.png")
unpause_image = PhotoImage(file="C:/Users/USER/Desktop/pass/play.png")
font_image = PhotoImage(file="fastforward_.png")
back_image = PhotoImage(file="fastrewind.png")
global volumeup_image
global volumedown_image
global volumemute_image

volumeup_image = PhotoImage(file="C:/Users/USER/Desktop/pass/volumeup.png")
volumedown_image = PhotoImage(file="C:/Users/USER/Desktop/pass/volumedown.png")
volumemute_image = PhotoImage(file="C:/Users/USER/Desktop/pass/volumemute.png")
def play_time():
	if stopped:
		return
	current_time = pygame.mixer.music.get_pos() / 1000
	
	converted_current_time = time.strftime("%M:%S", time.gmtime(current_time))

	song = song_box.get(ACTIVE)

	song = f"C:/Users/USER/Desktop/pass/audio/{song}.mp3"
	song_mut = MP3(song)
	global song_length
	song_length = song_mut.info.length
	converted_song_length = time.strftime("%M:%S",time.gmtime(song_length))

	current_time += 1

	if int(my_slider.get()) == int(song_length):
		status_bar.config(text=f"{converted_song_length} / {converted_song_length}")



	elif paused:
		pass	


	elif int(my_slider.get()) == int(current_time):
		slider_position = int(song_length)
		my_slider.config(to=slider_position,value=int(current_time))


	else:
		slider_position = int(song_length)
		my_slider.config(to=slider_position,value=int(my_slider.get()))
		converted_current_time = time.strftime("%M:%S",time.gmtime(int(my_slider.get())))

		status_bar.config(text=f"{converted_current_time}/{converted_song_length} ")

		next_time = int(my_slider.get()) + 1
		my_slider.config(value=next_time)

	status_bar.after(1000,play_time)

def add():
	song = filedialog.askopenfilename(initialdir='audio/',title="choose a song",filetypes=(("mp3 Files", "*.mp3"),))
	
	song = song.replace("C:/Users/USER/Desktop/pass/audio/","")	
	song = song.replace(".mp3","")
	song_box.insert(END,song)
	
global pla
pla = True
def play_a():
	global stopped
	stopped =False

	status_bar.config(text="")
	my_slider.config(value=0)
	global paused
	paused = False
	song =song_box.get(ACTIVE)
	song =f'C:/Users/USER/Desktop/pass/audio/{song}.mp3'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)


	play_time()
	
	#
def stop():
	status_bar.config(text="")
	my_slider.config(value=0)
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)
	status_bar.config(text='')
	global stopped
	stopped =True

def pause(is_paused):
	global paused
	paused = is_paused
	if paused:
		pygame.mixer.music.unpause()
		paused =False
	else:
		pygame.mixer.music.pause()
		paused=True

def forward():
	status_bar.config(text="")
	my_slider.config(value=0)
	next_one = song_box.curselection()
	next_one = next_one[0]+1
	song =song_box.get(next_one)
	song =f'C:/Users/USER/Desktop/pass/audio/{song}.mp3'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_box.selection_clear(0,END)
	song_box.activate(next_one)
	song_box.selection_set(next_one, last=None)
	
	
def backward():
	status_bar.config(text="")
	my_slider.config(value=0)
	next_one = song_box.curselection()
	next_one = next_one[0]-1
	song =song_box.get(next_one)
	song =f'C:/Users/USER/Desktop/pass/audio/{song}.mp3'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	song_box.selection_clear(0,END)
	song_box.activate(next_one)
	song_box.selection_set(next_one, last=None)
	play_time()
global paused
paused = False
def add_more():
	songs = filedialog.askopenfilenames(initialdir='audio/',title="choose a many song",filetypes=(("mp3 Files", "*.mp3"),))
	for song in songs:
		song = song.replace("C:/Users/USER/Desktop/pass/audio/","")	
		song = song.replace(".mp3","")
		song_box.insert(END,song)
		

def delete():
	song_box.delete(ANCHOR)
	pygame.mixer.music.stop()
 
def delete_all():
	song_box.delete(0,END)
	pygame.mixer.music.stop()

def save():
	file = filedialog.asksaveasfile(defaultextension=".mp3",filetypes=[("mp3 Files", ".mp3"),
						("waptt Files",".waptt"),
						("cd audio Files",".cda")])
	filetext = (song_box.get(ACTIVE))
	file.write(filetext)
	file.close()
def slider(x):
	song =song_box.get(ACTIVE)
	song =f'C:/Users/USER/Desktop/pass/audio/{song}.mp3'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0,start=int(my_slider.get()))
def volume(x):
	pygame.mixer.music.set_volume(volum_slider.get())
	current_volume = pygame.mixer.music.get_volume()
	# change volume image
	current_volume *= 100

	if int(current_volume) < 1:
		volume_meter.config(image=volumemute_image)
	elif 0 < int(current_volume) <= 50:
		volume_meter.config(image=volumedown_image)
	elif 25 < int(current_volume) <= 100:
		volume_meter.config(image=volumeup_image)

global stopped
stopped = False


men_frame = Frame()
men_frame.pack(pady=20)
controls_frame =Frame(men_frame)
controls_frame.grid(row=1,column=0,pady=10)
volume_frame = LabelFrame(men_frame,text="volume")
volume_frame.grid(row=0,column=2,padx=20)

song_box = Listbox(men_frame,bg="#950cdb",fg="#cccbbb",width=60,selectbackground="gray",selectforeground="black")
song_box.grid(row=0,column=0)
scroll = tk.Scrollbar(men_frame, orient=tk.VERTICAL, command=song_box.yview)
song_box.configure(yscrollcommand=scroll.set)
scroll.place(x=365,y=30,height=170)




back_btn =Button(controls_frame,image=back_image,borderwidth=0,command=backward)
forward_btn = Button(controls_frame,image=font_image,borderwidth=0,command=forward)
play_btn = Button(controls_frame,image=play_image,borderwidth=0,command =play_a)
pause_btn = Button(controls_frame,image=pause_image,borderwidth=0,command=lambda:pause(paused))
stop_btn = Button(controls_frame,image=stop_image,borderwidth=0,command=stop)

back_btn.grid(row=0,column=0,padx=10)
forward_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=3,padx=10)
stop_btn.grid(row=0,column=4,padx=10)
my_menu =Menu(window)
window.config(menu=my_menu)

add_song =Menu(my_menu)
my_menu.add_cascade(label="add songs",menu=add_song)
add_song.add_command(label="Add one song to playlist",command=add)
add_song.add_command(label="Add many song to playlist",command=add_more)
add_song.add_command(label="save",command=save)

remove = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs",menu=remove)
remove.add_command(label="Delete a song",command=delete)
remove.add_command(label="Delete all songs",command=delete_all)
status_bar = Label(window, text='', bd=1, relief= GROOVE,anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=2)
my_slider = ttk.Scale(window,from_=0,to=100, orient=HORIZONTAL,value=0,command=slider,length=360)
my_slider.pack(pady=30)

volume_meter = Label(men_frame,image=volumeup_image,)
volume_meter.grid(row=1,column=2,padx=10)
volum_slider = ttk.Scale(volume_frame,from_=1,to=0,orient=VERTICAL,value=1,command=volume,length=180)
volum_slider.pack(pady=10)
# volumeup_slider = Label(text="")
# volumeup_slider.pack(padx=0)

window.mainloop()