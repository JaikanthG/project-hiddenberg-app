from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang.builder import Builder
import speech_recognition as sr
from kivy.core.window import Window
from transformers import pipeline


screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>:
    Screen:
        Image:
            source: "app-rt.jpeg"
            size_hint: None, None
            width: "360dp"
            height: "640dp"
            pos_hint: {'center_x':.5, 'center_y':.2}
        MDLabel:
            text: 'WELCOME'
            font_name: 'Georgia'
            font_size: "48dp"
            halign: "center"
            color: "#ffcc00"
            pos_hint: {'center_y':.8}
        MDTextField:
            hint_text: "Username"
            icon_right: 'account'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {'center_x':.5, 'center_y':.65}
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        MDTextField:
            id: psswd
            hint_text: "Password"
            password: True
            icon_right: 'eye-off'
            font_size: "20dp"
            size_hint_x: .85
            pos_hint: {'center_x':.5, 'center_y':.5}
            on_text: self.text = self.text.replace(" ", "")
            write_tab: False
        BoxLayout:
            size_hint: .85, None
            height: "30dp"
            pos_hint: {'center_x':.5, 'center_y':.4}
            spacing: "5dp"
            MDCheckbox:
                id: cb
                size_hint: None, None
                width: "30dp"
                height: "30dp"
                pos_hint: {'center_x':.5, 'center_y':.5}
                on_press:
                    psswd.password = False if psswd.password == True else True
            MDLabel:
                text: "[ref=Show Password]Show Password[/ref]"
                markup: True
                pos_hint: {'center_x':.5, 'center_y':.5}
                on_ref_press:
                    cb.active = False if cb.active == True else True
                    psswd.password = False if psswd.password == True else True
            BoxLayout:
                size_hint: .6, None
                height: "30dp"
                pos_hint: {'center_x':.5, 'center_y':.3}
                spacing: "5dp"
            MDRectangleFlatButton:
                text: 'Login'
                pos_hint: {'center_x':.5, 'center_y':.3}
                on_press: root.manager.current = 'profile'

<ProfileScreen>:
    name: 'profile'
    RelativeLayout:
        orientation: 'vertical'
        pos: self.pos
        Label:
            text: 'Speech to Text'
            pos_hint: {'center_x':0.5, 'center_y':0.905}
            font_size: (self.height/15)* 0.7
        Button:
            text:'Record'
            size_hint: 0.3,0.1
            pos_hint:{'center_x': 0.47, 'center_y': 0.705}
            on_press: root.record()
        Button:
            text:'Summarizer'
            size_hint: 0.3,0.1
            pos_hint:{'center_x': 0.47, 'center_y': 0.589}
            on_press: root.summarizer()
        TextInput:
            id: totext
            pos_hint:{'center_x': 0.47, 'center_y': 0.305}
            size_hint: 0.8,0.4
            font_size: '10dp'
            readonly: True



            
"""

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    def record(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Please say something")

            audio = r.listen(source)

            print("Recognizing Now .... ")

            try:
                recognized_text = r.recognize_google(audio)
                print("You have said \n" + recognized_text)
                print("Audio Recorded Successfully \n ")

                self.ids.totext.text = recognized_text  # Corrected line

            except Exception as e:
                print("Error :  " + str(e))

            with open("recorded.wav", "wb") as f:
                f.write(audio.get_wav_data())

    def summarizer(self):
        summarizer = pipeline("summarization", model="Falconsai/medical_summarization")

#         MEDICAL_DOCUMENT = """ 
#         PER --> John Smith
#         AGE --> 45-year-old
#         SEX --> male
#         CLINICAL_EVENT --> presents
#         SEVERITY --> severe
#         SIGN_SYMPTOM --> pain
#         SIGN_SYMPTOM --> swelling
#         LAB_VALUE --> limited
#         SIGN_SYMPTOM --> range of motion
#         DISEASE_DISORDER --> fracture
#         HISTORY --> significant medical history or allergies
#         MEDICATION --> analgesics
#         THERAPEUTIC_PROCEDURE --> immobilization    
#         THERAPEUTIC_PROCEDURE --> physical therapy
#         CLINICAL_EVENT --> Follow
#         AGE --> up
#         SIGN_SYMPTOM --> abnormalities
#         DIAGNOSTIC_PROCEDURE --> vital signs
#         DIAGNOSTIC_PROCEDURE --> systems
# """

        self.ids.totext.text =   """ 
        PER --> John Smith
        AGE --> 45-year-old
        SEX --> male
        CLINICAL_EVENT --> presents
        SEVERITY --> severe
        SIGN_SYMPTOM --> pain
        SIGN_SYMPTOM --> swelling
        LAB_VALUE --> limited
        SIGN_SYMPTOM --> range of motion
        DISEASE_DISORDER --> fracture
        HISTORY --> significant medical history or allergies
        MEDICATION --> analgesics
        THERAPEUTIC_PROCEDURE --> immobilization    
        THERAPEUTIC_PROCEDURE --> physical therapy
        CLINICAL_EVENT --> Follow
        AGE --> up
        SIGN_SYMPTOM --> abnormalities
        DIAGNOSTIC_PROCEDURE --> vital signs
        DIAGNOSTIC_PROCEDURE --> systems
        PER --> John Smith
        AGE --> 45-year-old
        SEX --> male
        CLINICAL_EVENT --> presents
        SEVERITY --> severe
        SIGN_SYMPTOM --> pain
        SIGN_SYMPTOM --> swelling
        LAB_VALUE --> limited
        SIGN_SYMPTOM --> range of motion
        DISEASE_DISORDER --> fracture
        HISTORY --> significant medical history or allergies
        MEDICATION --> analgesics
        THERAPEUTIC_PROCEDURE --> immobilization    
        THERAPEUTIC_PROCEDURE --> physical therapy
        CLINICAL_EVENT --> Follow
        AGE --> up
        SIGN_SYMPTOM --> abnormalities
        DIAGNOSTIC_PROCEDURE --> vital signs
        DIAGNOSTIC_PROCEDURE --> systems 
        """ 

        #summarizer(MEDICAL_DOCUMENT, max_length=73, min_length=30, do_sample=False)[0]['summary_text']


# class SummarizerApp(MDApp):
#     def build(self):
#         return MyLayout()



class RecorderApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen

if __name__ == '__main__':
    Window.size = (360, 640)
    RecorderApp().run()
    #SummarizerApp().run()
