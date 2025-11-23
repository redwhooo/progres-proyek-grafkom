import pyglet
from pyglet import shapes
from pyglet import text
from pyglet import clock
from pyglet import graphics

LEBAR_JENDELA = 800
TINGGI_JENDELA = 700
window = pyglet.window.Window(LEBAR_JENDELA, TINGGI_JENDELA, caption="Aplikasi Edukasi Rambu Lalu Lintas", resizable=True)
batch = pyglet.graphics.Batch()

current_scene = 'MENU'

btn_kembali = shapes.Rectangle(680, 650, 100, 30, color=(200, 50, 50), batch=batch)
txt_kembali = text.Label('KEMBALI', x=730, y=665, anchor_x='center', anchor_y='center', batch=batch)
btn_kembali.visible = False
txt_kembali.visible = False

menu_judul = text.Label('BELAJAR RAMBU LALU LINTAS', font_size=24, x=400, y=550, anchor_x='center', batch=batch)
menu_subjudul = text.Label('Pilih materi yang ingin kamu pelajari:', font_size=14, x=400, y=500, anchor_x='center', batch=batch)

btn_menu_1 = shapes.Rectangle(200, 350, 400, 60, color=(50, 150, 200), batch=batch)
txt_menu_1 = text.Label('1. Lampu Lalu Lintas & Penyeberangan', font_size=16, x=400, y=380, anchor_x='center', anchor_y='center', batch=batch)

btn_menu_2 = shapes.Rectangle(200, 250, 400, 60, color=(50, 200, 100), batch=batch)
txt_menu_2 = text.Label('2. Rambu Dilarang Masuk', font_size=16, x=400, y=280, anchor_x='center', anchor_y='center', batch=batch)

menu_objects = [menu_judul, menu_subjudul, btn_menu_1, txt_menu_1, btn_menu_2, txt_menu_2]

s1_status_lampu = 'MOBIL_JALAN'
s1_status_anak = 'MENUNGGU'
S1_KECEPATAN_NORMAL = 350
S1_KECEPATAN_PELAN = 100
S1_KECEPATAN_ANAK = 70
S1_POS_X_ZEBRA = 500
S1_POS_ANAK_X = S1_POS_X_ZEBRA + 80
S1_POS_ANAK_Y = 200
s1_anak_y = S1_POS_ANAK_Y

s1_jalan = shapes.Rectangle(0, 200, 800, 200, color=(60, 60, 60), batch=batch)
s1_trotoar_atas = shapes.Rectangle(0, 400, 800, 300, color=(180, 180, 180), batch=batch)
s1_trotoar_bawah = shapes.Rectangle(0, 0, 800, 200, color=(180, 180, 180), batch=batch)

s1_zebra_lines = []
for i in range(6):
    s1_zebra_lines.append(shapes.Rectangle(S1_POS_X_ZEBRA, 200 + (i*35), 175, 20, color=(255,255,255), batch=batch))

s1_garis_henti = shapes.Rectangle(S1_POS_X_ZEBRA - 60, 200, 5, 200, color=(255,255,255), batch=batch)

s1_tiang_school = shapes.Rectangle(200, 50, 10, 100, color=(50,50,50), batch=batch)
s1_rambu_school = shapes.Polygon((205, 220), (245, 180), (205, 140), (165, 180), color=(255,215,0), batch=batch)
s1_txt_school = text.Label('SCHOOL', font_size=8, x=205, y=180, anchor_x='center', anchor_y='center', color=(0,0,0,255), batch=batch)

s1_tiang_lampu = shapes.Rectangle(450, 400, 15, 130, color=(50,50,50), batch=batch)
s1_kotak_lampu = shapes.Rectangle(430, 490, 60, 150, color=(20,20,20), batch=batch)
s1_l_merah = shapes.Circle(460, 600, 20, color=(40,0,0), batch=batch)
s1_l_kuning = shapes.Circle(460, 560, 20, color=(40,40,0), batch=batch)
s1_l_hijau = shapes.Circle(460, 520, 20, color=(0,255,0), batch=batch)

s1_tiang_pb = shapes.Rectangle(450, 100, 15, 80, color=(50,50,50), batch=batch)
s1_kotak_pb = shapes.Rectangle(430, 180, 60, 90, color=(20,20,20), batch=batch)
s1_tombol = shapes.Circle(460, 140, 15, color=(0,0,200), batch=batch)
s1_txt_push = text.Label('PUSH', font_size=6, x=460, y=140, anchor_x='center', anchor_y='center', batch=batch)

s1_ikon_stop_head = shapes.Circle(460, 245, 7, color=(255,0,0), batch=batch)
s1_ikon_stop_body = shapes.Line(460, 238, 460, 225, color=(255,0,0), batch=batch)
s1_ikon_stop_body.width = 4
s1_ikon_stop_arm = shapes.Line(450, 235, 470, 235, color=(255,0,0), batch=batch)
s1_ikon_stop_arm.width = 4
s1_ikon_stop_leg1 = shapes.Line(460, 225, 450, 215, color=(255,0,0), batch=batch)
s1_ikon_stop_leg1.width = 4
s1_ikon_stop_leg2 = shapes.Line(460, 225, 470, 215, color=(255,0,0), batch=batch)
s1_ikon_stop_leg2.width = 4
s1_ikon_stop_parts = [s1_ikon_stop_head, s1_ikon_stop_body, s1_ikon_stop_arm, s1_ikon_stop_leg1, s1_ikon_stop_leg2]

s1_ikon_jalan_head = shapes.Circle(460, 245, 7, color=(40,40,40), batch=batch)
s1_ikon_jalan_body = shapes.Line(460, 238, 460, 225, color=(40,40,40), batch=batch)
s1_ikon_jalan_body.width = 4
s1_ikon_jalan_arm = shapes.Line(450, 235, 470, 235, color=(40,40,40), batch=batch)
s1_ikon_jalan_arm.width = 4
s1_ikon_jalan_leg1 = shapes.Line(460, 225, 450, 215, color=(40,40,40), batch=batch)
s1_ikon_jalan_leg1.width = 4
s1_ikon_jalan_leg2 = shapes.Line(460, 225, 470, 215, color=(40,40,40), batch=batch)
s1_ikon_jalan_leg2.width = 4
s1_ikon_jalan_parts = [s1_ikon_jalan_head, s1_ikon_jalan_body, s1_ikon_jalan_arm, s1_ikon_jalan_leg1, s1_ikon_jalan_leg2]

s1_mobil = shapes.Rectangle(0, 300, 80, 40, color=(200, 50, 50), batch=batch)

s1_anak_kepala = shapes.Circle(0,0,5, color=(0,100,255), batch=batch)
s1_anak_badan = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch)
s1_anak_badan.width = 3
s1_anak_tangan = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch)
s1_anak_tangan.width = 3
s1_anak_kaki1 = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch)
s1_anak_kaki1.width = 3
s1_anak_kaki2 = shapes.Line(0,0,0,0, color=(0,100,255), batch=batch)
s1_anak_kaki2.width = 3
s1_anak_parts = [s1_anak_kepala, s1_anak_badan, s1_anak_tangan, s1_anak_kaki1, s1_anak_kaki2]

scene1_objects = [
    s1_jalan, s1_trotoar_atas, s1_trotoar_bawah, s1_garis_henti,
    s1_tiang_school, s1_rambu_school, s1_txt_school,
    s1_tiang_lampu, s1_kotak_lampu, s1_l_merah, s1_l_kuning, s1_l_hijau,
    s1_tiang_pb, s1_kotak_pb, s1_tombol, s1_txt_push, s1_mobil
] + s1_zebra_lines + s1_ikon_stop_parts + s1_ikon_jalan_parts + s1_anak_parts

s2_mobil_dx = 350 
s2_msg_timer = 0  

s2_jalan = shapes.Rectangle(0, 200, 800, 200, color=(60, 60, 60), batch=batch)
s2_trotoar_atas = shapes.Rectangle(0, 400, 800, 300, color=(180, 180, 180), batch=batch)
s2_trotoar_bawah = shapes.Rectangle(0, 0, 800, 200, color=(180, 180, 180), batch=batch)

POSISI_RAMBU_NO_ENTRY_X = 600
s2_tiang = shapes.Rectangle(POSISI_RAMBU_NO_ENTRY_X, 410, 10, 130, color=(50,50,50), batch=batch)
s2_rambu_bg = shapes.Circle(POSISI_RAMBU_NO_ENTRY_X + 5, 560, 30, color=(220,0,0), batch=batch)
s2_rambu_line = shapes.Rectangle(POSISI_RAMBU_NO_ENTRY_X + 5 - 25, 560 - 5, 50, 10, color=(255,255,255), batch=batch)

s2_mobil = shapes.Rectangle(0, 300, 80, 40, color=(200, 50, 50), batch=batch)

s2_warning_bg = shapes.Rectangle(200, 500, 400, 80, color=(255, 255, 255), batch=batch)
s2_warning_txt = text.Label('DILARANG MASUK!', font_size=20, x=400, y=540, color=(255,0,0,255), anchor_x='center', anchor_y='center', batch=batch)
s2_warning_sub = text.Label('Mobil harus putar balik.', font_size=12, x=400, y=515, color=(0,0,0,255), anchor_x='center', anchor_y='center', batch=batch)

scene2_objects = [
    s2_jalan, s2_trotoar_atas, s2_trotoar_bawah, 
    s2_tiang, s2_rambu_bg, s2_rambu_line, 
    s2_mobil, s2_warning_bg, s2_warning_txt, s2_warning_sub
]

def set_scene(scene_name):
    global current_scene, s1_status_lampu, s1_status_anak, s2_msg_timer
    current_scene = scene_name
    
    for obj in menu_objects: obj.visible = False
    for obj in scene1_objects: obj.visible = False
    for obj in scene2_objects: obj.visible = False
    btn_kembali.visible = False
    txt_kembali.visible = False
    
    if scene_name == 'MENU':
        for obj in menu_objects: obj.visible = True
        
    elif scene_name == 'SCENE_1':
        for obj in scene1_objects: obj.visible = True
        for part in s1_anak_parts: part.visible = False
        btn_kembali.visible = True
        txt_kembali.visible = True
        s1_mobil.x = 0
        s1_status_lampu = 'MOBIL_JALAN'
        s1_l_merah.color = (40,0,0)
        s1_l_kuning.color = (40,40,0)
        s1_l_hijau.color = (0,255,0)
        
    elif scene_name == 'SCENE_2':
        for obj in scene2_objects: obj.visible = True
        s2_warning_bg.visible = False
        s2_warning_txt.visible = False
        s2_warning_sub.visible = False
        btn_kembali.visible = True
        txt_kembali.visible = True
        s2_mobil.x = 0
        s2_msg_timer = 0

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
    global s1_status_lampu, s1_status_anak, s1_anak_y, s2_msg_timer
    
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
        
        if s1_mobil.x > LEBAR_JENDELA: s1_mobil.x = -80
        
        if s1_status_anak == 'MENYEBERANG':
            s1_anak_y += S1_KECEPATAN_ANAK * dt
            s1_update_visual_anak(s1_anak_y)
            if s1_anak_y > 415:
                s1_status_anak = 'MENUNGGU'
                for p in s1_anak_parts: p.visible = False

    elif current_scene == 'SCENE_2':
        BATAS_BERHENTI = POSISI_RAMBU_NO_ENTRY_X - 90 
        
        if s2_mobil.x < BATAS_BERHENTI and s2_msg_timer == 0:
            s2_mobil.x += 200 * dt 
            
        elif s2_mobil.x >= BATAS_BERHENTI:
            s2_warning_bg.visible = True
            s2_warning_txt.visible = True
            s2_warning_sub.visible = True
            s2_msg_timer += dt
            
            if s2_msg_timer > 3.0:
                s2_mobil.x = -100
                s2_msg_timer = 0
                s2_warning_bg.visible = False
                s2_warning_txt.visible = False
                s2_warning_sub.visible = False

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global s1_status_lampu
    
    if current_scene != 'MENU':
        if 680 < x < 780 and 650 < y < 680:
            set_scene('MENU')
            return

    if current_scene == 'MENU':
        if 200 < x < 600 and 350 < y < 410:
            set_scene('SCENE_1')
        elif 200 < x < 600 and 250 < y < 310:
            set_scene('SCENE_2')
            
    elif current_scene == 'SCENE_1':
        dx = x - 460; dy = y - 140
        if (dx*dx + dy*dy) < (15*15): 
            if s1_status_lampu == 'MOBIL_JALAN':
                print("Tombol PUSH ditekan!")
                s1_status_lampu = 'MOBIL_KUNING_PENDING'
                s1_tombol.color = (200, 200, 0)

clock.schedule_interval(update, 1/60.0)
pyglet.app.run()