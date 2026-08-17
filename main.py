from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

LUGARES = [
    {"nombre": "Parque Nacional Podocarpus", "ciudad": "Loja", "desc": "Bosque nublado, caminatas y aves."},
    {"nombre": "Valle de Vilcabamba", "ciudad": "Loja", "desc": "Valle de la longevidad y clima cálido."},
    {"nombre": "Centro Histórico", "ciudad": "Quito", "desc": "Iglesias coloniales y plazas históricas."},
    {"nombre": "Ciudad Mitad del Mundo", "ciudad": "Quito", "desc": "Monumento ecuatorial y museos."},
    {"nombre": "Parque Nacional Cajas", "ciudad": "Cuenca", "desc": "Páramo andino con más de 200 lagunas."}
]

def buscar(consulta):
    consulta = consulta.lower()
    res = []
    for l in LUGARES:
        texto = f"{l['nombre']} {l['ciudad']} {l['desc']}".lower()
        if consulta in texto or any(p in texto for p in consulta.split()):
            res.append(f"📍 {l['nombre']} ({l['ciudad']})\n{l['desc']}")
    if res:
        return "\n\n".join(res)
    return "❌ No encontré coincidencias. Prueba con 'Loja', 'Quito' o 'lagunas'."

class EcuBotApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#111827')
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.scroll = ScrollView(size_hint=(1, 0.88))
        self.chat = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.chat.bind(minimum_height=self.chat.setter('height'))
        
        self.add_msg("🤖 ¡Hola! Soy EcuBot 🇪🇨\n¿Qué lugar de Ecuador deseas explorar?", "#1E40AF")
        self.scroll.add_widget(self.chat)
        layout.add_widget(self.scroll)
        
        box = BoxLayout(orientation='horizontal', size_hint=(1, 0.12), spacing=10)
        self.txt = TextInput(hint_text="Escribe aquí...", multiline=False, size_hint=(0.75, 1))
        self.txt.bind(on_text_validate=self.enviar)
        
        btn = Button(text="Enviar", size_hint=(0.25, 1), background_color=get_color_from_hex('#2563EB'))
        btn.bind(on_release=self.enviar)
        
        box.add_widget(self.txt)
        box.add_widget(btn)
        layout.add_widget(box)
        return layout

    def enviar(self, *args):
        t = self.txt.text.strip()
        if t:
            self.txt.text = ""
            self.add_msg(f"👤 {t}", "#374151")
            resp = buscar(t)
            self.add_msg(f"🤖 {resp}", "#1E40AF")

    def add_msg(self, text, color):
        lbl = Label(text=text, size_hint_y=None, color=(1,1,1,1), padding=(10,10))
        lbl.bind(texture_size=lbl.setter('size'))
        self.chat.add_widget(lbl)
        self.scroll.scroll_y = 0

if __name__ == '__main__':
    EcuBotApp().run()
