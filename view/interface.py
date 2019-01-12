import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

import time
import threading
from App import XMLSoup

GLADE_FILE = "view/OSM2BD.glade"

global flgt
flgt = True

class interface():


    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(GLADE_FILE)
        self.builder.connect_signals(self)

        self.arq = ""

        self.window = self.builder.get_object("main_window")
        self.val_search = self.builder.get_object("entry")
        self.progressBar = self.builder.get_object("progressBar")
        self.status = self.builder.get_object("status")
        self.bt_start = self.builder.get_object("bt_start")

        self.window.connect("delete-event", Gtk.main_quit)
        self.activity_mode = True
        self.window.show_all()


    def bt_search_clicked(self, widget):
        print("search")
        dialog = Gtk.FileChooserDialog("Please choose a file", None,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        dialog.set_modal(True)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.arq = dialog.get_filename()
            self.val_search.set_text(dialog.get_filename())
            self.bt_start.set_sensitive(True)

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def bt_start_clicked(self, wigdet):
        print("clicked")
        app_main(self)

def app_main(self):

    progress = self.progressBar
    status = self.status
    arq = self.arq

    def update_progress():
        progress.pulse()
        progress.set_text("Process...")
        return False

    def example_target():
        while flgt:
            GLib.idle_add(update_progress)
            time.sleep(0.3)

    def task():
        global flgt
        XMLSoup.start(arq)
        print("fim")
        flgt = False
        progress.set_fraction(1)
        progress.set_text("100% completed")
        status.push(1,"files were generated and stored in the Results directory.")

    thread1 = threading.Thread(target=example_target)
    thread1.daemon = True
    thread1.start()

    thread2 = threading.Thread(target=task)
    thread2.daemon = True
    thread2.start()


def main():
    interface()
    Gtk.main()
    exit(0)


main()
