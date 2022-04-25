import wx
from wx.core import ID_ANY, SIGINT


class MyApp(wx.App):
    def __init__(self):
        super().__init__(True)
        self.InitFrame()

    def InitFrame(self):
        frame = MyFrame(None, title="Hello World!", pos=[100, 100])
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()

    def OnInit(self):
        panel = MyPanel(parent=self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        welcome_text = wx.StaticText(self, id=ID_ANY, label="Hello World!", pos= [100, 100])

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
