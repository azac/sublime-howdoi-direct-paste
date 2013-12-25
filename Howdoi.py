import sublime, sublime_plugin, subprocess


class HowdoiDirectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
                line = self.view.line(region)
                cont =self.view.substr(line)

                if (len(cont)<1):
                	pass
                else:        
	                p = subprocess.Popen("/usr/local/bin/howdoi "+cont,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	                output, errors = p.communicate()

	                self.view.replace(edit, line, output)







