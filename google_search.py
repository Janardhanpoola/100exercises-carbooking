import webbrowser
     
query = input("Input your query: ")
webbrowser.open("http://google.com/search?q=%s" % query)