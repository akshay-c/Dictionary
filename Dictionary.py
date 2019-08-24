import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Dictionary')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE,size =(300,125), pos=(5, 5))
        my_btn = wx.Button(panel, label='Dictionary', pos=(5, 250))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        self.text_ctrl.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
        self.Show()

    def on_press(self, event):
        with wx.FileDialog(self, "Open File", wildcard="*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return 
            self.filename = fileDialog.GetPath()
        self.CreateDict()

    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_SPACE or keycode == wx.WXK_RETURN:
            word = self.text_ctrl.GetLineText(self.text_ctrl.GetNumberOfLines() - 1).split(" ")
            print(word)
            if word[-1] not in self.Dictionary:
                return
        event.Skip()

    def CreateDict(self):
        with open(self.filename, 'r') as f:
            Dictionary = f.read().split()
            self.Dictionary = set(Dictionary)
            print(self.Dictionary)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
