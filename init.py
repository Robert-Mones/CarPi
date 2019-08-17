import subprocess, os, sys, pygame, datetime

pygameClock = pygame.time.Clock()

NAV,MUSIC,CAMERA,XXX,SETTINGS = 0,1,2,3,4
MUSIC_DIR = "/home/pi/Music/"
f = open("/home/pi/MUSIC_DIR","r")
if f.mode == "r":
        x = f.read().strip()
        if "/" not in x:
                x = MUSIC_DIR
        if x[-1] != "/":
                x += "/"
        MUSIC_DIR = x

# init
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
pygame.init()
pygame.mixer.quit()
pygame.mouse.set_visible(False)

music = None

# display
size = width, height = 800, 480
screen = pygame.display.set_mode(flags=pygame.NOFRAME)
font32 = pygame.font.SysFont("arial", 32)
f32_pad = 8
font24 = pygame.font.SysFont("arial", 24)
f24_pad = 6
font16 = pygame.font.SysFont("arial", 16)
f16_pad = 4
cur = (0, (0,0), False)

# colors
white = 255,255,255
black = 0,0,0
blue = 0,0,255
back_color = white
fore_color = black

# gui
left_ui = pygame.Surface((88,440))
right_ui = pygame.Surface((712,440))
top_ui = pygame.Surface((800,40))

wifi_logo = pygame.image.load("wifi.jpeg")
wifi_logo = pygame.transform.scale(wifi_logo,(32,32))
wifi_r = wifi_logo.get_rect()
wifi_r.right = 795
wifi_r.centery = 20

left_labels = ("Nav","Mus","Cam","??","Set")
state = MUSIC

wifi_con = False
wifi_en = False

music_dirs = os.listdir(MUSIC_DIR)
music_files = []
for d in music_dirs:
        music_files.append(os.listdir(MUSIC_DIR + d))
selected_music_dir = None if len(music_dirs)==0 else 0
playing_song = (None,None)

def play_music(file):
        global music
        if music != None:
                stop_music()
        music = subprocess.Popen(["mplayer",MUSIC_DIR+file])

def stop_music():
        global music, playing_song
        if music == None:
                return
        else:
                music.terminate()
                music = None
                playing_song = (None,None)

def text(text, x, y, color=fore_color, center=False, dest=screen, font=font32):
        text = font.render(text, True, color)
        text_r = text.get_rect()
        if center:
                text_r.center = (x,y)
        else:
                text_r.x = x
                text_r.y = y
        dest.blit(text, text_r)

def rect(x,y,w,h,t=0,dest=screen):
        pygame.draw.rect(dest, fore_color, pygame.Rect(x,y,w,h),t)


# left_ui
left_ui.fill(back_color)
pygame.draw.line(left_ui,fore_color,(0,0),(88,0),4)
pygame.draw.line(right_ui,fore_color,(0,0),(0,440),1)
for i in range(0,5):
        rect(-1,(i*88)+1,88,88,2,dest=left_ui)
        text(left_labels[i],43,(i*88)+45,center=True,dest=left_ui)


while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        stop_music()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN: cur = (True, (event.pos[0]-10,event.pos[1]-15))

        if cur[0]: # if there's a new click
                x,y = cur[1]
                
                # narrow down by region
                if y < 40: # top_ui
                        print("top")
                elif x < 88: # left_ui
                        for i in range(5):
                                if y < (120+(80*i)):
                                        state=i
                                        break
                else: # right_ui
                        if state == NAV:
                                stop_music()
                        elif state == MUSIC:
                                i = 0
                                current_y = 3 + 40 # to account for the top UI
                                for d in music_dirs:
                                        done = False
                                        current_y += 24+(2*f24_pad)
                                        if y < current_y:
                                                selected_music_dir = (None if i == selected_music_dir else i)
                                                break
                                        if i == selected_music_dir:
                                                j = 0
                                                for file in music_files[i]:
                                                        current_y += 16+(2*f16_pad)
                                                        if y < current_y:
                                                                play_music(d+"/"+file)
                                                                playing_song = (i,j)
                                                                done = True
                                                                break
                                                        j += 1
                                        if done:
                                                break
                                        i += 1
                        elif state == SETTINGS:
                                if y<(40+3+f32_pad+32+f32_pad):
                                        if wifi_en:
                                                subprocess.run(["sudo","rfkill","block","0"])
                                        else:
                                                subprocess.run(["sudo","rfkill","unblock","0"])
                                elif y>(480-(f32_pad+32+f32_pad)):
                                        if x<190:
                                                subprocess.Popen(["sudo","reboot","now"])
                                                exit()
                                        elif x>640:
                                                subprocess.Popen(["sudo","shutdown","now"])
                                                exit()
                
                cur = (False,(x,y))
        
        # check to see if song is over
        if music != None and music.poll() == 0:
                next_song = (playing_song[0],playing_song[1]+1)
                if len(music_files[next_song[0]]) > next_song[1]:
                        play_music(music_dirs[next_song[0]] + "/" + music_files[next_song[0]][next_song[1]])
                        playing_song = (next_song[0],next_song[1])
                else:
                        stop_music()
        
        # background
        right_ui.fill(back_color)
        top_ui.fill(back_color)
        
        # top ui
        time = datetime.datetime.now()
        text((str(time.hour) if time.hour <= 12 else str(time.hour-12)) + ":" + (str(time.minute) if time.minute>9 else "0"+str(time.minute)),
                f24_pad, f24_pad, font=font24, dest=top_ui)
        
        wifi_con = "RUNNING" in os.popen("ifconfig wlan0").read().split("\n")[0]
        if wifi_con:
                top_ui.blit(wifi_logo,wifi_r)
        
        # right ui
        pygame.draw.line(right_ui,fore_color,(0,0),(712,0),4)
        ### NOTE: Top corner pixel of ui_right i(1,3)
        if state == MUSIC:
                i = 0
                current_y = 3 + f32_pad
                for d in music_dirs:
                        text(d, 1+f24_pad, current_y, dest=right_ui, font=font24,
                             color=(blue if (i==playing_song[0] and i!=selected_music_dir) and playing_song[0]!=None else fore_color))
                        current_y += 24+(2*f24_pad)
                        if i == selected_music_dir:
                                j = 0
                                for file in music_files[i]:
                                        text(file.split(".")[0], 40, current_y, dest=right_ui, font=font16,
                                             color=(blue if i==playing_song[0] and j==playing_song[1] else fore_color))
                                        current_y += 16+(2*f16_pad)
                                        j += 1
                        i += 1
        elif state == SETTINGS:
                wifi_en = "UP" in os.popen("ifconfig wlan0").read().split("\n")[0]
                text("WiFi - " + ("On" if wifi_en else "Off") + (", Connected" if wifi_con else ""),
                     1+f32_pad, 3+f32_pad, dest=right_ui)
                text(str(round(pygameClock.get_fps()))+" fps", 600, 3+f32_pad, dest=right_ui)
                text("Reboot", 1+f32_pad, (440-(32+f32_pad)), dest=right_ui)
                text("Shutdown", 560, (440-(32+f32_pad)), dest=right_ui)
        
        screen.blit(left_ui, (0,40))
        screen.blit(right_ui, (88,40))
        screen.blit(top_ui, (0,0))
        pygame.display.flip()
        pygameClock.tick()
