import sublime, sublime_plugin, subprocess


class HowdoiDirectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
                line = self.view.line(region)
                cont = self.view.substr(line)

                if (len(cont)<1):
                    pass
                else:

                    if sublime.platform() == 'windows':
                        path_prefix = ""
                    else:
                        path_prefix = "/usr/local/bin/" 


                    p = subprocess.Popen(path_prefix + "howdoi " + cont,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         shell=True)
                    output, errors = p.communicate()

                    # Python 3 returns binary data, hence we have to decode it.
                    # Python 2 won't be affected by this decoding.
                    output = output.decode('ascii')

                    # At least in Windows, output would contain carriage return
                    # characters (CR). We have to remove them in order to look
                    # properly.
                    output = output.replace('\r', '')

                    self.view.replace(edit, line, output)
