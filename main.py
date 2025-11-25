import pyglet
from pyglet import shapes
from pyglet import text
from pyglet import clock
import math

LEBAR_JENDELA = 800
TINGGI_JENDELA = 600 
window = pyglet.window.Window(LEBAR_JENDELA, TINGGI_JENDELA, caption="LaluLintasKu", resizable=False)
batch = pyglet.graphics.Batch()

grp_bg = pyglet.graphics.Group(order=0)      
grp_objects = pyglet.graphics.Group(order=1) 
grp_sign_bg = pyglet.graphics.Group(order=2) 
grp_sign_fg = pyglet.graphics.Group(order=3) 

current_scene = 'MENU'

btn_kembali_shadow = shapes.Rectangle(680+3, 550-3, 100, 30, color=(150, 30, 30), batch=batch, group=grp_sign_fg)
btn_kembali = shapes.Rectangle(680, 550, 100, 30, color=(230, 80, 80), batch=batch, group=grp_sign_fg)
txt_kembali = text.Label('KEMBALI', x=730, y=565, anchor_x='center', anchor_y='center', batch=batch, group=grp_sign_fg)
btn_kembali_shadow.visible = False
btn_kembali.visible = False
txt_kembali.visible = False

menu_bg_sky = shapes.Rectangle(0, 0, LEBAR_JENDELA, TINGGI_JENDELA, color=(135, 206, 235), batch=batch, group=grp_bg)
menu_bg_sun = shapes.Circle(700, 530, 60, color=(255, 215, 0), batch=batch, group=grp_bg)
menu_bg_grass = shapes.Rectangle(0, 0, LEBAR_JENDELA, 150, color=(50, 205, 50), batch=batch, group=grp_bg)
menu_bg_hill = shapes.Circle(400, -100, 300, color=(34, 139, 34), batch=batch, group=grp_bg)

menu_clouds = [
    shapes.Circle(100, 530, 30, color=(255, 255, 255), batch=batch, group=grp_bg),
    shapes.Circle(140, 530, 40, color=(255, 255, 255), batch=batch, group=grp_bg),
    shapes.Circle(180, 530, 30, color=(255, 255, 255), batch=batch, group=grp_bg),
    shapes.Circle(600, 450, 30, color=(255, 255, 255), batch=batch, group=grp_bg),
    shapes.Circle(640, 460, 35, color=(255, 255, 255), batch=batch, group=grp_bg),
]

menu_judul_shadow = text.Label('BELAJAR RAMBU LALU LINTAS', font_size=28, x=403, y=503, anchor_x='center', color=(0,0,0,100), batch=batch, group=grp_objects)
menu_judul = text.Label('BELAJAR RAMBU LALU LINTAS', font_size=28, x=400, y=500, anchor_x='center', color=(255, 69, 0, 255), batch=batch, group=grp_objects)
menu_subjudul = text.Label('Pilih materi yang ingin dipelajari', font_size=16, x=400, y=450, anchor_x='center', color=(20, 20, 20, 255), batch=batch, group=grp_objects)

btn_m1_shadow = shapes.Rectangle(150, 300, 500, 70, color=(0, 0, 100), batch=batch, group=grp_objects)
btn_m1_face = shapes.Rectangle(150, 310, 500, 70, color=(30, 144, 255), batch=batch, group=grp_objects)
txt_m1 = text.Label('1. Lampu Lalu Lintas & Penyeberangan', font_size=18, x=400, y=345, anchor_x='center', anchor_y='center', batch=batch, group=grp_objects)

btn_m2_shadow = shapes.Rectangle(150, 190, 500, 70, color=(139, 69, 0), batch=batch, group=grp_objects)
btn_m2_face = shapes.Rectangle(150, 200, 500, 70, color=(255, 140, 0), batch=batch, group=grp_objects)
txt_m2 = text.Label('2. Rambu Dilarang Masuk', font_size=18, x=400, y=235, anchor_x='center', anchor_y='center', batch=batch, group=grp_objects)

deco_tiang = shapes.Rectangle(80, 150, 10, 200, color=(50, 50, 50), batch=batch, group=grp_objects)
deco_box = shapes.Rectangle(60, 280, 50, 120, color=(20, 20, 20), batch=batch, group=grp_objects)
deco_red = shapes.Circle(85, 370, 15, color=(255, 0, 0), batch=batch, group=grp_objects)
deco_yellow = shapes.Circle(85, 340, 15, color=(255, 255, 0), batch=batch, group=grp_objects)
deco_green = shapes.Circle(85, 310, 15, color=(0, 255, 0), batch=batch, group=grp_objects)

deco_car_body = shapes.Rectangle(650, 60, 100, 40, color=(255, 50, 50), batch=batch, group=grp_objects)
deco_car_top = shapes.Rectangle(670, 100, 60, 30, color=(255, 50, 50), batch=batch, group=grp_objects)
deco_car_window = shapes.Rectangle(675, 105, 50, 20, color=(200, 240, 255), batch=batch, group=grp_objects)
deco_wheel1 = shapes.Circle(670, 60, 15, color=(30, 30, 30), batch=batch, group=grp_objects)
deco_wheel2 = shapes.Circle(730, 60, 15, color=(30, 30, 30), batch=batch, group=grp_objects)

menu_objects = [
    menu_bg_sky, menu_bg_sun, menu_bg_hill, menu_bg_grass, 
    menu_judul_shadow, menu_judul, menu_subjudul,
    btn_m1_shadow, btn_m1_face, txt_m1,
    btn_m2_shadow, btn_m2_face, txt_m2,
    deco_tiang, deco_box, deco_red, deco_yellow, deco_green,
    deco_car_body, deco_car_top, deco_car_window, deco_wheel1, deco_wheel2
] + menu_clouds

s1_status_lampu = 'MOBIL_JALAN'
s1_status_anak = 'MENUNGGU'
S1_KECEPATAN_NORMAL = 350
S1_KECEPATAN_PELAN = 100
S1_KECEPATAN_ANAK = 70
S1_POS_X_ZEBRA = 500
S1_POS_ANAK_X = S1_POS_X_ZEBRA + 80
S1_POS_ANAK_Y = 180
s1_anak_y = S1_POS_ANAK_Y

s1_bg_sky = shapes.Rectangle(0, 0, LEBAR_JENDELA, TINGGI_JENDELA, color=(135, 206, 235), batch=batch, group=grp_bg)
s1_bg_sun = shapes.Circle(100, 530, 50, color=(255, 215, 0), batch=batch, group=grp_bg) 
s1_bg_grass_top = shapes.Rectangle(0, 400, 800, 300, color=(50, 205, 50), batch=batch, group=grp_bg)

s1_clouds = [
    shapes.Circle(550, 550, 30, color=(255, 255, 255), batch=batch, group=grp_bg),
    shapes.Circle(590, 550, 40, color=(255, 255, 255), batch=batch, group=grp_bg), 
    shapes.Circle(630, 550, 30, color=(255, 255, 255), batch=batch, group=grp_bg),
    shapes.Circle(300, 480, 30, color=(255, 255, 255), batch=batch, group=grp_bg),
    shapes.Circle(340, 490, 35, color=(255, 255, 255), batch=batch, group=grp_bg),
]

s1_jalan = shapes.Rectangle(0, 200, 800, 200, color=(80, 80, 80), batch=batch, group=grp_bg)
s1_trotoar_bawah = shapes.Rectangle(0, 0, 800, 200, color=(200, 200, 200), batch=batch, group=grp_bg)
s1_rumput_bawah = shapes.Rectangle(0, 0, 800, 30, color=(50, 205, 50), batch=batch, group=grp_bg)

s1_zebra_lines = []
for i in range(6):
    s1_zebra_lines.append(shapes.Rectangle(S1_POS_X_ZEBRA, 200 + (i*35), 175, 20, color=(255,255,255), batch=batch, group=grp_objects))

s1_garis_henti = shapes.Rectangle(S1_POS_X_ZEBRA - 60, 200, 5, 200, color=(255,255,255), batch=batch, group=grp_objects)

s1_tiang_school = shapes.Rectangle(200, 50, 10, 150, color=(100, 70, 20), batch=batch, group=grp_objects)
s1_rambu_school = shapes.Polygon((205, 220), (245, 180), (205, 140), (165, 180), color=(255,215,0), batch=batch, group=grp_objects)
s1_txt_school = text.Label('SCHOOL', font_size=8, x=205, y=180, anchor_x='center', anchor_y='center', color=(0,0,0,255), batch=batch, group=grp_sign_fg)

s1_tiang_lampu = shapes.Rectangle(450, 400, 15, 130, color=(30, 30, 30), batch=batch, group=grp_objects)
s1_kotak_lampu = shapes.Rectangle(430, 440, 60, 150, color=(20, 20, 20), batch=batch, group=grp_objects)
s1_l_merah = shapes.Circle(460, 550, 20, color=(40,0,0), batch=batch, group=grp_sign_fg)
s1_l_kuning = shapes.Circle(460, 510, 20, color=(40,40,0), batch=batch, group=grp_sign_fg)
s1_l_hijau = shapes.Circle(460, 470, 20, color=(0,255,0), batch=batch, group=grp_sign_fg)

s1_tiang_pb = shapes.Rectangle(450, 100, 15, 100, color=(30, 30, 30), batch=batch, group=grp_objects)
s1_kotak_pb = shapes.Rectangle(430, 180, 60, 90, color=(20, 20, 20), batch=batch, group=grp_objects)
s1_tombol = shapes.Circle(460, 140, 15, color=(0,0,200), batch=batch, group=grp_sign_fg)
s1_txt_push = text.Label('PUSH', font_size=6, x=460, y=140, anchor_x='center', anchor_y='center', batch=batch, group=grp_sign_fg)

s1_ikon_stop_head = shapes.Circle(460, 245, 7, color=(255,0,0), batch=batch, group=grp_sign_fg)
s1_ikon_stop_body = shapes.Line(460, 238, 460, 225, color=(255,0,0), batch=batch, group=grp_sign_fg)
s1_ikon_stop_body.width = 4
s1_ikon_stop_arm = shapes.Line(450, 235, 470, 235, color=(255,0,0), batch=batch, group=grp_sign_fg)
s1_ikon_stop_arm.width = 4
s1_ikon_stop_leg1 = shapes.Line(460, 225, 450, 215, color=(255,0,0), batch=batch, group=grp_sign_fg)
s1_ikon_stop_leg1.width = 4
s1_ikon_stop_leg2 = shapes.Line(460, 225, 470, 215, color=(255,0,0), batch=batch, group=grp_sign_fg)
s1_ikon_stop_leg2.width = 4
s1_ikon_stop_parts = [s1_ikon_stop_head, s1_ikon_stop_body, s1_ikon_stop_arm, s1_ikon_stop_leg1, s1_ikon_stop_leg2]

s1_ikon_jalan_head = shapes.Circle(460, 245, 7, color=(40,40,40), batch=batch, group=grp_sign_fg)
s1_ikon_jalan_body = shapes.Line(460, 238, 460, 225, color=(40,40,40), batch=batch, group=grp_sign_fg)
s1_ikon_jalan_body.width = 4
s1_ikon_jalan_arm = shapes.Line(450, 235, 470, 235, color=(40,40,40), batch=batch, group=grp_sign_fg)
s1_ikon_jalan_arm.width = 4
s1_ikon_jalan_leg1 = shapes.Line(460, 225, 450, 215, color=(40,40,40), batch=batch, group=grp_sign_fg)
s1_ikon_jalan_leg1.width = 4
s1_ikon_jalan_leg2 = shapes.Line(460, 225, 470, 215, color=(40,40,40), batch=batch, group=grp_sign_fg)
s1_ikon_jalan_leg2.width = 4
s1_ikon_jalan_parts = [s1_ikon_jalan_head, s1_ikon_jalan_body, s1_ikon_jalan_arm, s1_ikon_jalan_leg1, s1_ikon_jalan_leg2]

s1_mobil = shapes.Rectangle(0, 320, 100, 40, color=(255, 50, 50), batch=batch, group=grp_objects)
s1_mobil_top = shapes.Rectangle(20, 360, 60, 30, color=(255, 50, 50), batch=batch, group=grp_objects)
s1_mobil_window = shapes.Rectangle(25, 365, 50, 20, color=(200, 240, 255), batch=batch, group=grp_sign_fg)
s1_mobil_wheel1 = shapes.Circle(20, 320, 15, color=(30, 30, 30), batch=batch, group=grp_sign_fg)
s1_mobil_wheel2 = shapes.Circle(80, 320, 15, color=(30, 30, 30), batch=batch, group=grp_sign_fg)
s1_mobil_visuals = [s1_mobil_top, s1_mobil_window, s1_mobil_wheel1, s1_mobil_wheel2]

s1_anak_kepala = shapes.Circle(0,0,6, color=(0,100,255), batch=batch, group=grp_sign_fg)
s1_anak_badan = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch, group=grp_sign_fg)
s1_anak_badan.width = 4
s1_anak_tangan = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch, group=grp_sign_fg)
s1_anak_tangan.width = 4
s1_anak_kaki1 = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch, group=grp_sign_fg)
s1_anak_kaki1.width = 4
s1_anak_kaki2 = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch, group=grp_sign_fg)
s1_anak_kaki2.width = 4
s1_anak_parts = [s1_anak_kepala, s1_anak_badan, s1_anak_tangan, s1_anak_kaki1, s1_anak_kaki2]

scene1_objects = [
    s1_bg_sky, s1_bg_sun, s1_bg_grass_top,
    s1_jalan, s1_trotoar_bawah, s1_rumput_bawah, s1_garis_henti,
    s1_tiang_school, s1_rambu_school, s1_txt_school,
    s1_tiang_lampu, s1_kotak_lampu, s1_l_merah, s1_l_kuning, s1_l_hijau,
    s1_tiang_pb, s1_kotak_pb, s1_tombol, s1_txt_push,
    s1_mobil
] + s1_clouds + s1_zebra_lines + s1_ikon_stop_parts + s1_ikon_jalan_parts + s1_anak_parts + s1_mobil_visuals

s2_red_state = 'MOVING' 
s2_red_timer = 0
s2_red_checked = False 

s2_green_state = 'MOVING_DOWN' 
s2_green_timer = 0

s2_bg = shapes.Rectangle(0, 0, LEBAR_JENDELA, TINGGI_JENDELA, color=(50, 205, 50), batch=batch, group=grp_bg) 

s2_sidewalk_h = shapes.Rectangle(0, 230, 800, 240, color=(180, 180, 180), batch=batch, group=grp_bg)
s2_sidewalk_v = shapes.Rectangle(330, 450, 140, 250, color=(180, 180, 180), batch=batch, group=grp_bg)
s2_road_h = shapes.Rectangle(0, 250, 800, 200, color=(60, 60, 60), batch=batch, group=grp_bg)
s2_road_v = shapes.Rectangle(350, 450, 100, 250, color=(60, 60, 60), batch=batch, group=grp_bg)

s2_marka_h = []
for i in range(0, 800, 60):
    s2_marka_h.append(shapes.Rectangle(i, 350, 30, 5, color=(255, 255, 255), batch=batch, group=grp_objects))

s2_arrows_forbidden = []
for i in range(480, 700, 80):
    tri = shapes.Triangle(400, i, 380, i+30, 420, i+30, color=(200, 200, 200), batch=batch, group=grp_objects)
    s2_arrows_forbidden.append(tri)

s2_tiang_no = shapes.Rectangle(460, 460, 8, 80, color=(80, 80, 80), batch=batch, group=grp_objects) 
s2_rambu_no_bg = shapes.Circle(464, 540, 25, color=(220, 0, 0), batch=batch, group=grp_sign_bg)
s2_rambu_no_line = shapes.Rectangle(444, 537, 40, 6, color=(255, 255, 255), batch=batch, group=grp_sign_fg)

s2_tiang_left = shapes.Rectangle(340, 460, 8, 80, color=(80, 80, 80), batch=batch, group=grp_objects) 

s2_rambu_left_bg = shapes.Polygon(
    (344, 580), 
    (384, 540), 
    (344, 500), 
    (304, 540), 
    color=(255, 220, 0),
    batch=batch,
    group=grp_sign_bg 
)

s2_arrow_v = shapes.Rectangle(349, 510, 12, 35, color=(0,0,0), batch=batch, group=grp_sign_fg)
s2_arrow_h = shapes.Rectangle(325, 533, 24, 12, color=(0,0,0), batch=batch, group=grp_sign_fg)
s2_arrow_head = shapes.Triangle(310, 539, 325, 554, 325, 524, color=(0,0,0), batch=batch, group=grp_sign_fg)

s2_rambu_left_parts = [s2_arrow_v, s2_arrow_h, s2_arrow_head]

s2_msg_box = shapes.Rectangle(150, 80, 500, 80, color=(255, 255, 255), batch=batch, group=grp_sign_bg)
s2_msg_txt = text.Label("", x=400, y=120, color=(0,0,0,255), anchor_x='center', width=480, multiline=True, batch=batch, group=grp_sign_fg)

s2_mobil = shapes.Rectangle(-100, 280, 100, 40, color=(30, 144, 255), batch=batch, group=grp_objects) 
s2_mobil_top = shapes.Rectangle(-80, 320, 60, 30, color=(30, 144, 255), batch=batch, group=grp_objects)
s2_mobil_window = shapes.Rectangle(-75, 325, 50, 20, color=(200, 240, 255), batch=batch, group=grp_sign_fg)
s2_mobil_wheel1 = shapes.Circle(-80, 280, 15, color=(30, 30, 30), batch=batch, group=grp_sign_fg)
s2_mobil_wheel2 = shapes.Circle(-20, 280, 15, color=(30, 30, 30), batch=batch, group=grp_sign_fg)
s2_mobil_parts = [s2_mobil_top, s2_mobil_window, s2_mobil_wheel1, s2_mobil_wheel2]

s2_mobil_lawan = shapes.Rectangle(850, 380, 100, 40, color=(255, 50, 50), batch=batch, group=grp_objects)
s2_mobil_lawan_top = shapes.Rectangle(870, 420, 60, 30, color=(255, 50, 50), batch=batch, group=grp_objects)
s2_mobil_lawan_window = shapes.Rectangle(875, 425, 50, 20, color=(200, 240, 255), batch=batch, group=grp_sign_fg)
s2_mobil_lawan_wheel1 = shapes.Circle(870, 380, 15, color=(30, 30, 30), batch=batch, group=grp_sign_fg)
s2_mobil_lawan_wheel2 = shapes.Circle(930, 380, 15, color=(30, 30, 30), batch=batch, group=grp_sign_fg)
s2_mobil_lawan_parts = [s2_mobil_lawan_top, s2_mobil_lawan_window, s2_mobil_lawan_wheel1, s2_mobil_lawan_wheel2]

s2_mobil_green = shapes.Rectangle(360, 650, 40, 100, color=(50, 200, 50), batch=batch, group=grp_objects) 
s2_mobil_green_top = shapes.Rectangle(365, 660, 30, 40, color=(30, 150, 30), batch=batch, group=grp_objects)
s2_mobil_green_window = shapes.Rectangle(0,0,0,0, color=(200, 240, 255), batch=batch, group=grp_sign_fg) 
s2_mobil_green_wheel1 = shapes.Circle(0,0,0, color=(30,30,30), batch=batch, group=grp_sign_fg) 
s2_mobil_green_wheel2 = shapes.Circle(0,0,0, color=(30,30,30), batch=batch, group=grp_sign_fg) 
s2_mobil_green_parts = [s2_mobil_green_top, s2_mobil_green_window, s2_mobil_green_wheel1, s2_mobil_green_wheel2]

scene2_objects = [
    s2_bg] + [
    s2_sidewalk_h, s2_sidewalk_v, s2_road_h, s2_road_v,
    s2_tiang_no, s2_rambu_no_bg, s2_rambu_no_line,
    s2_tiang_left, s2_rambu_left_bg, 
    s2_mobil, s2_mobil_lawan, s2_mobil_green, 
    s2_msg_box, s2_msg_txt
] + s2_marka_h + s2_arrows_forbidden + s2_mobil_parts + s2_mobil_lawan_parts + s2_mobil_green_parts + s2_rambu_left_parts

def set_scene(scene_name):
    global current_scene, s1_status_lampu, s1_status_anak, s2_red_state, s2_red_timer, s2_red_checked, s2_green_state
    current_scene = scene_name
    
    for obj in menu_objects: obj.visible = False
    for obj in scene1_objects: obj.visible = False
    for obj in scene2_objects: obj.visible = False
    btn_kembali.visible = False
    btn_kembali_shadow.visible = False
    txt_kembali.visible = False
    
    if scene_name == 'MENU':
        for obj in menu_objects: obj.visible = True
        
    elif scene_name == 'SCENE_1':
        for obj in scene1_objects: obj.visible = True
        for part in s1_anak_parts: part.visible = False
        btn_kembali.visible = True
        btn_kembali_shadow.visible = True
        txt_kembali.visible = True
        s1_mobil.x = 0
        s1_status_lampu = 'MOBIL_JALAN'
        s1_l_merah.color = (40,0,0); s1_l_kuning.color = (40,40,0); s1_l_hijau.color = (0,255,0)
        
    elif scene_name == 'SCENE_2':
        for obj in scene2_objects: obj.visible = True
        btn_kembali.visible = True
        btn_kembali_shadow.visible = True
        txt_kembali.visible = True
        
        s2_mobil.x = -100 
        s2_mobil.y = 280
        s2_mobil_lawan.x = 850 
        
        s2_mobil_green.x = 380
        s2_mobil_green.y = 650
        s2_mobil_green.width = 40 
        s2_mobil_green.height = 100
        
        s2_msg_box.visible = False
        s2_msg_txt.visible = False
        
        s2_red_state = 'MOVING'
        s2_red_timer = 0
        s2_red_checked = False
        
        s2_green_state = 'MOVING_DOWN'

set_scene('MENU')

def s1_update_visual_anak(y):
    x = S1_POS_ANAK_X
    s1_anak_kepala.x, s1_anak_kepala.y = x, y + 15
    s1_anak_badan.x, s1_anak_badan.y, s1_anak_badan.x2, s1_anak_badan.y2 = x, y+10, x, y
    s1_anak_tangan.x, s1_anak_tangan.y, s1_anak_tangan.x2, s1_anak_tangan.y2 = x-5, y+7, x+5, y+7
    s1_anak_kaki1.x, s1_anak_kaki1.y, s1_anak_kaki1.x2, s1_anak_kaki1.y2 = x, y, x-5, y-7
    s1_anak_kaki2.x, s1_anak_kaki2.y, s1_anak_kaki2.x2, s1_anak_kaki2.y2 = x, y, x+5, y-7

def s1_atur_lampu_jalan(dt):
    global s1_status_lampu, s1_status_anak
    if current_scene != 'SCENE_1': return
    s1_status_lampu = 'MOBIL_JALAN'
    s1_l_merah.color = (40,0,0); s1_l_kuning.color = (40,40,0); s1_l_hijau.color = (0,255,0)
    for p in s1_ikon_stop_parts: p.color = (255,0,0)
    for p in s1_ikon_jalan_parts: p.color = (40,40,40)
    s1_status_anak = 'MENUNGGU'
    for p in s1_anak_parts: p.visible = False
    s1_tombol.color = (0,0,200)

def s1_atur_lampu_pejalan(dt):
    global s1_status_lampu, s1_status_anak, s1_anak_y
    if current_scene != 'SCENE_1': return
    s1_status_lampu = 'PEJALAN_JALAN'
    s1_l_merah.color = (255,0,0); s1_l_kuning.color = (40,40,0); s1_l_hijau.color = (0,40,0)
    for p in s1_ikon_stop_parts: p.color = (40,0,0)
    for p in s1_ikon_jalan_parts: p.color = (0,255,0)
    
    s1_anak_y = S1_POS_ANAK_Y
    s1_update_visual_anak(s1_anak_y)
    s1_status_anak = 'MENYEBERANG'
    for p in s1_anak_parts: p.visible = True
    clock.schedule_once(s1_atur_lampu_jalan, 5.0)

def s1_atur_kuning():
    global s1_status_lampu
    s1_status_lampu = 'MOBIL_KUNING'
    s1_l_merah.color = (40,0,0); s1_l_kuning.color = (255,255,0); s1_l_hijau.color = (0,40,0)
    clock.schedule_once(s1_atur_lampu_pejalan, 2.0)

def update(dt):
    global s1_status_lampu, s1_status_anak, s1_anak_y, s2_red_state, s2_red_timer, s2_red_checked, s2_green_state
    
    if current_scene == 'SCENE_1':
        kecepatan = S1_KECEPATAN_NORMAL if s1_mobil.x < 200 else S1_KECEPATAN_PELAN
        pos_depan = s1_mobil.x + 80
        lewat_batas = pos_depan > (S1_POS_X_ZEBRA - 60)
        
        if s1_status_lampu == 'MOBIL_JALAN':
            s1_mobil.x += kecepatan * dt
        elif s1_status_lampu in ['MOBIL_KUNING', 'PEJALAN_JALAN']:
            if lewat_batas: s1_mobil.x += kecepatan * dt
        elif s1_status_lampu == 'MOBIL_KUNING_PENDING':
            if not lewat_batas:
                s1_atur_kuning()
            else:
                s1_mobil.x += kecepatan * dt
                if s1_mobil.x > (S1_POS_X_ZEBRA + 175): s1_atur_kuning()
        
        if s1_mobil.x > LEBAR_JENDELA: s1_mobil.x = -100

        s1_mobil_top.x = s1_mobil.x + 20
        s1_mobil_window.x = s1_mobil.x + 25
        s1_mobil_wheel1.x = s1_mobil.x + 20
        s1_mobil_wheel2.x = s1_mobil.x + 80
        
        if s1_status_anak == 'MENYEBERANG':
            s1_anak_y += S1_KECEPATAN_ANAK * dt
            s1_update_visual_anak(s1_anak_y)
            if s1_anak_y > 415:
                s1_status_anak = 'MENUNGGU'
                for p in s1_anak_parts: p.visible = False

    elif current_scene == 'SCENE_2':
        s2_mobil.x += 200 * dt
        if s2_mobil.x > LEBAR_JENDELA + 50:
            s2_mobil.x = -100
        
        s2_mobil_top.x = s2_mobil.x + 20
        s2_mobil_window.x = s2_mobil.x + 25
        s2_mobil_wheel1.x = s2_mobil.x + 20
        s2_mobil_wheel2.x = s2_mobil.x + 80

        if s2_red_state == 'MOVING':
            s2_mobil_lawan.x -= 150 * dt
            
            if 480 < s2_mobil_lawan.x < 500 and not s2_red_checked:
                s2_red_state = 'STOPPED'
                s2_red_timer = 0
                s2_msg_box.visible = True
                s2_msg_txt.visible = True
                s2_msg_txt.text = "Mobil Merah berhenti: Ada rambu DILARANG MASUK ke kanan. Lanjut lurus."

        elif s2_red_state == 'STOPPED':
            s2_red_timer += dt
            if s2_red_timer > 2.5: 
                s2_red_state = 'MOVING'
                s2_red_checked = True 
                s2_msg_box.visible = False
                s2_msg_txt.visible = False

        if s2_mobil_lawan.x < -100: 
            s2_mobil_lawan.x = 900
            s2_red_checked = False
            
        s2_mobil_lawan_top.x = s2_mobil_lawan.x + 20
        s2_mobil_lawan_window.x = s2_mobil_lawan.x + 25
        s2_mobil_lawan_wheel1.x = s2_mobil_lawan.x + 20
        s2_mobil_lawan_wheel2.x = s2_mobil_lawan.x + 80

        if s2_green_state == 'MOVING_DOWN':
            s2_mobil_green.y -= 100 * dt
            
            if 420 < s2_mobil_green.y < 450:
                if 250 < s2_mobil_lawan.x < 600:
                    s2_green_state = 'WAITING'
            
            if s2_mobil_green.y <= 380: 
                s2_green_state = 'MOVING_LEFT'
                s2_mobil_green.width = 100
                s2_mobil_green.height = 40
                s2_mobil_green.x = 380 
                s2_mobil_green.y = 380 
        
        elif s2_green_state == 'WAITING':
            if s2_mobil_lawan.x < 250 or s2_mobil_lawan.x > 650:
                s2_green_state = 'MOVING_DOWN'

        elif s2_green_state == 'MOVING_LEFT':
            s2_mobil_green.x -= 150 * dt 
            if s2_mobil_green.x < -100:
                s2_green_state = 'MOVING_DOWN'
                s2_mobil_green.x = 380
                s2_mobil_green.y = 650
                s2_mobil_green.width = 40
                s2_mobil_green.height = 100

        if s2_green_state in ['MOVING_DOWN', 'WAITING']:
            s2_mobil_green_top.width = 30
            s2_mobil_green_top.height = 40
            s2_mobil_green_top.x = s2_mobil_green.x + 5
            s2_mobil_green_top.y = s2_mobil_green.y + 20
            s2_mobil_green_window.visible = False
            s2_mobil_green_wheel1.visible = False
            s2_mobil_green_wheel2.visible = False
        else:
            s2_mobil_green_window.visible = True
            s2_mobil_green_wheel1.visible = True
            s2_mobil_green_wheel2.visible = True
            
            s2_mobil_green_top.width = 60
            s2_mobil_green_top.height = 30
            s2_mobil_green_top.x = s2_mobil_green.x + 20
            s2_mobil_green_top.y = s2_mobil_green.y + 40 
            
            s2_mobil_green_window.width = 50
            s2_mobil_green_window.height = 20
            s2_mobil_green_window.x = s2_mobil_green.x + 25
            s2_mobil_green_window.y = s2_mobil_green.y + 45
            
            s2_mobil_green_wheel1.radius = 15
            s2_mobil_green_wheel1.x = s2_mobil_green.x + 20
            s2_mobil_green_wheel1.y = s2_mobil_green.y
            
            s2_mobil_green_wheel2.radius = 15
            s2_mobil_green_wheel2.x = s2_mobil_green.x + 80
            s2_mobil_green_wheel2.y = s2_mobil_green.y

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global s1_status_lampu
    
    if current_scene != 'MENU':
        if 680 < x < 780 and 550 < y < 580:
            set_scene('MENU')
            return

    if current_scene == 'MENU':
        if 150 < x < 650 and 300 < y < 370:
            set_scene('SCENE_1')
        elif 150 < x < 650 and 190 < y < 260:
            set_scene('SCENE_2')
            
    elif current_scene == 'SCENE_1':
        dx = x - 460; dy = y - 140
        if (dx*dx + dy*dy) < (15*15): 
            if s1_status_lampu == 'MOBIL_JALAN':
                s1_status_lampu = 'MOBIL_KUNING_PENDING'
                s1_tombol.color = (200, 200, 0)

clock.schedule_interval(update, 1/60.0)
pyglet.app.run()