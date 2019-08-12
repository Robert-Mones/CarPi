import subprocess, os, sys, pygame

NAV,MUSIC,CAMERA,XXX,SETTINGS = 0,1,2,3,4
MUSIC_DIR = "/home/pi/Music/"

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

def play_music(file):
        global music
        if music != None:
                kill_music()
        print("play")
        music = subprocess.Popen(["mplayer",MUSIC_DIR+file])

def kill_music():
        global music
        print("kill")
        if music == None:
                return
        else:
                music.kill()
                music = None

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

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN: cur = (True, (event.pos[0]-10,event.pos[1]-15))

        if cur[0]: # if there's a new click
                x,y = cur[1]
                
                # narrow down by region
                if y < 40:
                        print("top")
                elif x < 88:
                        for i in range(5):
                                if y < (120+(80*i)):
                                        state=i
                                        break
                else:
                        if state == NAV:
                                kill_music()
                        elif state == MUSIC:
                                i = 0
                                current_y = 3 + 40 # to account for the top UI
                                for d in music_dirs:
                                        current_y += 24+(2*f24_pad)
                                        if y < current_y:
                                                break
                                        for file in music_files[i]:
                                                current_y += 16+(2*f16_pad)
                                                if y < current_y:
                                                        play_music(d+"/"+file)
                                                        break
                                        i += 1
                        elif state == SETTINGS:
                                if y<(40+3+f32_pad+32+f32_pad):
                                        if wifi_en:
                                                subprocess.run(["sudo","rfkill","block","0"])
                                        else:
                                                subprocess.run(["sudo","rfkill","unblock","0"])
                                elif y>(480-(f32_pad+32+f32_pad)):
                                        print(x,y)
                                        if x<190:
                                                subprocess.Popen(["sudo","reboot","now"])
                                                exit()
                                        elif x>640:
                                                subprocess.Popen(["sudo","shutdown","now"])
                                                exit()
                
                cur = (False,(x,y))
        
        # background
        screen.fill(back_color)
        left_ui.fill(back_color)
        right_ui.fill(back_color)
        top_ui.fill(back_color)
        
        # top ui
        wifi_con = "RUNNING" in os.popen("ifconfig wlan0").read().split("\n")[0]
        if wifi_con:
                top_ui.blit(wifi_logo,wifi_r)
        
        # left ui
        pygame.draw.line(left_ui,fore_color,(0,0),(88,0),4)
        pygame.draw.line(right_ui,fore_color,(0,0),(0,440),1)
        for i in range(0,5):
                rect(-1,(i*88)+1,88,88,2,dest=left_ui)
                text(left_labels[i],43,(i*88)+45,center=True,dest=left_ui)

        # right ui
        #text(left_labels[right_state],2,2,dest=right_ui)
        pygame.draw.line(right_ui,fore_color,(0,0),(712,0),4)
        ### NOTE: Top corner pixel of ui_right i(1,3)
        if state == MUSIC:
                i = 0
                current_y = 3 + f32_pad
                for d in music_dirs:
                        text(d, 1+f24_pad, current_y, dest=right_ui, font=font24)
                        current_y += 24+(2*f24_pad)
                        for file in music_files[i]:
                                text(file.split(".")[0], 40, current_y, dest=right_ui, font=font16)
                                current_y += 16+(2*f16_pad)
                        i += 1
        elif state == SETTINGS:
                wifi_en = "UP" in os.popen("ifconfig wlan0").read().split("\n")[0]
                text("WiFi - " + ("On" if wifi_en else "Off") + (", Connected" if wifi_con else ""),
                     1+f32_pad, 3+f32_pad, dest=right_ui)
                text("Reboot", 1+f32_pad, (440-(32+f32_pad)), dest=right_ui)
                text("Shutdown", 560, (440-(32+f32_pad)), dest=right_ui)
        
        screen.blit(left_ui, (0,40))
        screen.blit(right_ui, (88,40))
        screen.blit(top_ui, (0,0))
        pygame.display.flip()
