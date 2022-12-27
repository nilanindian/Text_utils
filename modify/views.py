from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(req):
    # return HttpResponse("hello")
    return render(req, "home.html")

# for analyze given text
def analyze(req):
    # text variable for store the user given text input
    text = req.POST.get('textbox','default')

    # variable for access  the mode of operation switches

    rmvpunc=req.POST.get("removepunc",'off')

    upper_case = req.POST.get("uppercase", 'off')

    newlinermv=req.POST.get("newlineremove", 'off')

    exspacermv=req.POST.get("spaceremove", 'off')

    # to store the operations
    operation=[]

    # print("text =",(text))
    # print(rmvpunc)
    # print(upper_case)
    # print(newlinermv)
    # print(exspacermv)



    if rmvpunc == 'on':
        operation.append("remove punction")
        analyze = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in (text):
            if char not in punc:
                analyze=analyze+char
        text=analyze

    if upper_case=='on':
        operation.append("full capitalize")

        text=text.upper()

    if newlinermv=='on':
        operation.append("new line remove")
        analyze = ""
        for char in text:
            if char!='\n' and char!='\r':
                analyze=analyze+char
        text=analyze

    if exspacermv=='on':
        operation.append("remove extra spaces")
        analyze = ""
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyze = analyze + char
        text=analyze

    params = {'purpose': operation, 'analyze_text': text}
    return render(req, "analyze.html", params)
