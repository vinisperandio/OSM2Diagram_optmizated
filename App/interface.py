import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


GLADE_FILE = "OSM2BD.glade"

class interface():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(GLADE_FILE)
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("main_window")

        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show_all()

def main():
    interface()
    Gtk.main()
    exit(0)

main()