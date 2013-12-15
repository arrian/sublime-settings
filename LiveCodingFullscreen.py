import sublime, sublime_plugin

class LiveCodingFullscreenCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command("toggle_full_screen")
		self.window.run_command("toggle_menu")
		self.window.run_command("toggle_tabs")
		self.window.run_command("toggle_minimap")