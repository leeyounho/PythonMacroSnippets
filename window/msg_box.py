import traceback
import win32api
import win32con
from plyer import notification


class MsgBox:
    def __init__(self, handler):
        self.handler = handler

    def msgbox_yesno(self, title, body):  # yes : 6 / no : 7
        return True if win32api.MessageBox(self.handler, body, title, win32con.MB_YESNO) == 6 else False

    def msgbox_ok(self, title, body):  # ok : 1
        return True if win32api.MessageBox(self.handler, body, title, win32con.MB_OK) == 1 else False

    def msgbox_yesnocancel(self, title, body):  # yes : 6 / no : 7 / cancel : 2
        ret = win32api.MessageBox(self.handler, body, title, win32con.MB_YESNOCANCEL)
        if ret == 2:
            exit(0)
        return True if ret == 6 else False

    def msgbox_okcancel(self, title, body):  # ok : 1 / cancel : 2
        ret = win32api.MessageBox(self.handler, body, title, win32con.MB_OKCANCEL)
        if ret == 2:
            exit(0)
        return True

    def msgbox_error_stacktrace(self, title):  # ok : 1
        return True if win32api.MessageBox(self.handler, str(traceback.format_exc()), title,
                                           win32con.MB_ICONERROR) else False

    def msgbox_error_stacktrace_and_exit(self, title):  # ok : 1
        win32api.MessageBox(self.handler, str(traceback.format_exc()), title, win32con.MB_ICONERROR)
        exit(0)

    def msgbox_info(self, title, body):  # ok : 1
        return True if win32api.MessageBox(self.handler, body, title, win32con.MB_ICONINFORMATION) else False

    def msgbox_warning(self, title, body):  # ok : 1
        return True if win32api.MessageBox(self.handler, body, title, win32con.MB_ICONWARNING) else False

    def msgbox_retrycancel(self, title, body):  # retry : 4 / cancel : 2
        return True if win32api.MessageBox(self.handler, body, title, win32con.MB_RETRYCANCEL) == 4 else False

    # TODO app_name이 안나오네
    def toast_message(self, app_name, title, message, timeout):
        notification.notify(
            title=title,
            message=message,
            app_name=app_name,
            # app_icon='sample.ico',  # 'C:\\sample.ico'
            timeout=timeout,  # seconds
        )

if __name__ == '__main__':
    msg_box = MsgBox(0)
    # msgBox.msgbox_retrycancel('test', 'testestset')
    # msg_box.toast_message('test_app', 'title test', 'message test', 5)
    msg_box.toast_message2()
